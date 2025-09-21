from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime, timedelta
from hashlib import sha1
from typing import Dict, List, Tuple

from users.users.models import db
from users.progress.models import UserExerciseState

# ---------- IDs / hashing ----------

def make_qid(unit: str, exercise: int, question_text: str, answer_text: str, qtype: str = "") -> str:
    """
    Stable id for a question based on its *content*, not Nr.
    Changing Nr won't change qid; editing text/answer will.
    """
    payload = f"{unit}|{exercise}|{qtype}|{question_text}|{answer_text}"
    return sha1(payload.encode("utf-8")).hexdigest()

# ---------- CRUD helpers ----------

@dataclass
class State:
    correct_ids: List[str]
    incorrect: Dict[str, str]  # qid -> first incorrect answer

    @classmethod
    def empty(cls) -> "State":
        return cls(correct_ids=[], incorrect={})

def _get_or_create_row(user_id: int, unit: str, exercise: int) -> UserExerciseState:
    row = UserExerciseState.query.filter_by(user_id=user_id, unit=unit, exercise=exercise).first()
    if not row:
        row = UserExerciseState(user_id=user_id, unit=unit, exercise=exercise, state={})
        db.session.add(row)
    return row

def load_state(user_id: int, unit: str, exercise: int) -> State:
    row = UserExerciseState.query.filter_by(user_id=user_id, unit=unit, exercise=exercise).first()
    if not row or not row.state:
        return State.empty()
    s = row.state
    return State(correct_ids=s.get("correct_ids", []), incorrect=s.get("incorrect", {}))

def save_correct(user_id: int, unit: str, exercise: int, qid: str, total_questions: int | None = None) -> None:
    row = _get_or_create_row(user_id, unit, exercise)
    s = load_state(user_id, unit, exercise)
    if qid not in s.correct_ids:
        s.correct_ids.append(qid)
    s.incorrect.pop(qid, None)
    row.state = {"correct_ids": s.correct_ids, "incorrect": s.incorrect}
    now = datetime.utcnow()
    row.updated_at = now
    if total_questions is not None and len(s.correct_ids) >= total_questions:
        row.completed_at = now
    db.session.commit()

def save_incorrect(user_id: int, unit: str, exercise: int, qid: str, given_answer: str) -> None:
    """
    First wrong attempt is recorded; second wrong does nothing if already present.
    """
    row = _get_or_create_row(user_id, unit, exercise)
    s = load_state(user_id, unit, exercise)
    if (qid not in s.incorrect) and (qid not in s.correct_ids):
        s.incorrect[qid] = given_answer
        row.state = {"correct_ids": s.correct_ids, "incorrect": s.incorrect}
        row.updated_at = datetime.utcnow()
        db.session.commit()

def reset_state(user_id: int, unit: str, exercise: int) -> None:
    UserExerciseState.query.filter_by(user_id=user_id, unit=unit, exercise=exercise).delete()
    db.session.commit()

def compute_score(user_id: int, unit: str, exercise: int, total_questions: int) -> float:
    s = load_state(user_id, unit, exercise)
    if total_questions <= 0:
        return 0.0
    return min(len(s.correct_ids) / total_questions, 1.0)

# ---------- session merge on login ----------

def merge_session_into_db(
    *,
    user_id: int,
    unit: str,
    exercise: int,
    # session shapes you currently have:
    session_progress_nrs: List[int],
    session_falses_nrs: List[int],
    # mapping from current Nr -> (qid, question_text, answer_text, qtype)
    nr_to_qid: Dict[int, Tuple[str, str, str, str]],
) -> None:
    """
    Converts current session lists (by Nr) to qids using today's CSV mapping,
    then unions into DB state (first wrong only).
    """
    row = _get_or_create_row(user_id, unit, exercise)
    s = load_state(user_id, unit, exercise)

    # merge correct
    for nr in session_progress_nrs:
        meta = nr_to_qid.get(nr)
        if not meta:
            continue
        qid, *_ = meta
        if qid not in s.correct_ids:
            s.correct_ids.append(qid)
        s.incorrect.pop(qid, None)

    # merge incorrect (only if not already correct or incorrect)
    for nr in session_falses_nrs:
        meta = nr_to_qid.get(nr)
        if not meta:
            continue
        qid, _qt, _ans, _type = meta
        if (qid not in s.correct_ids) and (qid not in s.incorrect):
            # You said keep the entire incorrect answer; session dict may have it:
            # If you keep only ids for anonymous users, you can store a placeholder or skip.
            s.incorrect[qid] = ""  # or a session_provided_text if you have it

    row.state = {"correct_ids": s.correct_ids, "incorrect": s.incorrect}
    row.updated_at = datetime.utcnow()
    db.session.commit()

# ---------- housekeeping (TTL for unfinished) ----------

def prune_abandoned_unfinished(days: int = 10) -> int:
    """
    Delete rows not completed and not updated recently to save space.
    Returns number of rows deleted.
    """
    cutoff = datetime.utcnow() - timedelta(days=days)
    q = UserExerciseState.__table__.delete().where(
        (UserExerciseState.completed_at.is_(None)) & (UserExerciseState.updated_at < cutoff)
    )
    res = db.session.execute(q)
    db.session.commit()
    return res.rowcount
