from flask_login import current_user

from datetime import datetime

from users.users.models import db
from users.progress.models import UserExerciseState

from users.progress.score import compute_score
from users.session_management.logging import log_exercise_completed
from users.session_management.verification_session import is_key_in_exercise, init_session_key
from users.questions.total_questions import compute_total_questions

def register_progress(session, unit, exercise, nr):
    """
    Registers progress for a specific question number in a given unit and exercise.

    If the (unit, exercise) pair is not already listed in 'unfinished_exercise',
    it is added to that list.

    Ensures the 'progress' key exists in the session for the exercise, then appends
    the question number to the tracked progress list.

    Args:
        session (dict): The session dictionary tracking user progress.
        unit (str): The unit identifier.
        exercise (str or int): The exercise identifier.
        nr (int or str): The question number to register as answered.

    Returns:
        None
    """
    ex_int = int(exercise) if not isinstance(exercise, int) else exercise
    nr_int = int(nr) if not isinstance(nr, int) else nr

    if current_user.is_authenticated:
        row = UserExerciseState.query.filter_by(
            user_id=current_user.id, unit=unit, exercise=ex_int
        ).first()
        if not row:
            row = UserExerciseState(user_id=current_user.id, unit=unit, exercise=ex_int, state={})
            db.session.add(row)

        s = row.state or {}
        correct_nrs = set(int(n) for n in s.get("correct_nrs", []))
        incorrect   = {int(k): v for k, v in (s.get("incorrect") or {}).items()}

        correct_nrs.add(nr_int)          # mark this Nr as correct
        # incorrect.pop(nr_int, None)      # remove from incorrect if it was there

        # keep any existing finished fields if they exist (won’t in progress)
        next_state = {"correct_nrs": sorted(correct_nrs), "incorrect": {str(k): v for k, v in incorrect.items()}}
        if "score" in s: next_state["score"] = s["score"]
        if "total_questions" in s: next_state["total_questions"] = s["total_questions"]

        row.state = next_state
        row.updated_at = datetime.utcnow()
        db.session.commit()
        return

    else:
        if (unit, exercise) not in session['unfinished_exercise']:
            session['unfinished_exercise'].append((unit, exercise))

        init_session_key(session, unit, exercise, 'progress')
        session[unit][str(exercise)]['progress'].append(nr)
        return


'''
def register_false(session, unit, exercise, nr):
    """
    Records a question as incorrectly answered for a specific unit and exercise.

    Ensures the 'falses' key exists in the session for the given exercise, then appends
    the question number to the list of incorrect answers.

    Args:
        session (dict): The session dictionary tracking user progress.
        unit (str): The unit identifier.
        exercise (str or int): The exercise identifier.
        nr (int or str): The question number to mark as incorrect.

    Returns:
        None
    """
    if (unit, exercise) not in session['unfinished_exercise']:
        session['unfinished_exercise'].append((unit, exercise))

    init_session_key(session, unit, exercise, 'falses')
    session[unit][str(exercise)]['falses'].append(nr)
    return
'''


def register_incorrect_answer(session, unit, exercise, nr, incorrect_answer):
    """
    Stores the user's incorrect answer for a given unit and exercise.

    Ensures the 'incorrect_answer' key exists in the session for the specified exercise,
    then appends the user's incorrect response to the list.

    Args:
        session (dict): The session dictionary tracking user input.
        unit (str): The unit identifier.
        exercise (str or int): The exercise identifier.
        incorrect_answer (str): The user's incorrect answer to store.

    Returns:
        None
    """

    ex_int = int(exercise) if not isinstance(exercise, int) else exercise
    nr_int = int(nr) if not isinstance(nr, int) else nr

    if current_user.is_authenticated:
        row = UserExerciseState.query.filter_by(
            user_id=current_user.id, unit=unit, exercise=ex_int
        ).first()
        if not row:
            row = UserExerciseState(user_id=current_user.id, unit=unit, exercise=ex_int, state={})
            db.session.add(row)

        s = row.state or {}
        # Use Nrs for in-progress state
        correct_nrs = {int(n) for n in s.get("correct_nrs", [])}
        incorrect = {int(k): v for k, v in (s.get("incorrect") or {}).items()}

        # Only record an incorrect if this Nr isn’t already marked correct
        if nr_int not in correct_nrs:
            # Keep first wrong answer; don’t overwrite if already recorded
            if nr_int not in incorrect:
                incorrect[nr_int] = incorrect_answer or ""

        # Rebuild state; preserve any finished fields if present
        next_state = {
            "correct_nrs": sorted(correct_nrs),
            "incorrect": {str(k): v for k, v in incorrect.items()},
        }
        if "score" in s:
            next_state["score"] = s["score"]
        if "total_questions" in s:
            next_state["total_questions"] = s["total_questions"]

        row.state = next_state
        row.updated_at = datetime.utcnow()
        db.session.commit()
        return

    else:
        if (unit, exercise) not in session['unfinished_exercise']:
            session['unfinished_exercise'].append((unit, exercise))

        init_session_key(session, unit, exercise, 'falses')
        session[unit][str(exercise)]['falses'].append(nr)

        # init_session_key(session, unit, exercise, 'incorrect_answer')
        # session[unit][str(exercise)]['incorrect_answer'].append(incorrect_answer)
    return


def register_result(session, unit, exercise, feedback):
    """
    Finalizes and records the result of a completed exercise.

    If feedback is provided, prints a completion message.
    Ensures required session keys ('progress' and 'falses') exist before computing the score.
    Stores the computed score (rounded to two decimal places) under the 'result' key.

    Cleans up temporary progress data by removing:
    - 'progress' (answered questions),
    - 'falses' (incorrect question IDs),
    - 'incorrect_answer' (user's incorrect responses).

    Also removes the (unit, exercise) pair from the 'unfinished_exercise' list if present,
    and marks the session as modified to ensure the update is saved.

    Args:
        session (dict): The session dictionary tracking user data.
        unit (str): The unit identifier.
        exercise (str or int): The exercise identifier.
        feedback (any): Feedback data used to confirm completion.

    Returns:
        None
    """

    ex_int = int(exercise) if not isinstance(exercise, int) else exercise
    ex_str = str(ex_int)

    if current_user.is_authenticated:
        total_q = int(compute_total_questions(unit, ex_int) or 0)

        # Use the same scoring function your UI uses
        # If your project exposes compute_score_exercise(...), use that instead.
        score_val = compute_score(session, unit, ex_int)
        try:
            score_final = float(score_val) if score_val is not None else 0.0
        except (TypeError, ValueError):
            score_final = 0.0
        score_final = round(score_final, 2)

        row = UserExerciseState.query.filter_by(
            user_id=current_user.id, unit=unit, exercise=ex_int
        ).first()
        if not row:
            row = UserExerciseState(user_id=current_user.id, unit=unit, exercise=ex_int, state={})
            db.session.add(row)

        # Persist only canonical completion state; drop per-question JSON
        row.state = {
            "score": score_final,
            "total_questions": total_q,
        }
        row.completed_at = datetime.utcnow()
        row.updated_at = row.completed_at
        db.session.commit()

        # Optional: analytics/logging
        if feedback is not None:
            log_exercise_completed(unit, ex_int, score_final, email=current_user.email)

        # We don't need to touch session for logged-in users, but it's harmless to clean:
        if unit in session and ex_str in session[unit]:
            for key in ("progress", "falses", "incorrect_answer", "result"):
                session[unit][ex_str].pop(key, None)
        session.setdefault("unfinished_exercise", [])
        if (unit, ex_int) in session["unfinished_exercise"]:
            session["unfinished_exercise"].remove((unit, ex_int))
        session.modified = True
        return

    else:
        init_session_key(session, unit, exercise, 'progress')
        init_session_key(session, unit, exercise, 'falses')

        score_exercise = compute_score(session, unit, exercise)
        session[unit][str(exercise)]['result'] = round(score_exercise, 2)

        if feedback is not None:
            log_exercise_completed(unit, exercise, round(score_exercise, 2))

        if is_key_in_exercise(session, unit, exercise, 'progress'):
            del session[unit][str(exercise)]['progress']

        if is_key_in_exercise(session, unit, exercise, 'falses'):
            del session[unit][str(exercise)]['falses']

        if is_key_in_exercise(session, unit, exercise, 'incorrect_answer'):
            del session[unit][str(exercise)]['incorrect_answer']

        if (unit, exercise) in session['unfinished_exercise']:
            session['unfinished_exercise'].remove((unit, exercise))

        session.modified = True
    return
