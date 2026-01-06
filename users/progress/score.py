from flask_login import current_user

from users.progress.models import UserExerciseState
from data.data_processing.total_questions import highest_exercise, total_question_exercises
from users.session_management.verification_session import is_key_in_exercise, init_session_key


def update_score_in_session(session, unit):
    score = session.setdefault('score', {})

    score[unit] = compute_score_unit(session, unit)

    session.modified = True
    return


def write_score(session, unit, exercise=None):
    """
    Computes and returns the score as a percentage string for a given unit or exercise.

    Delegates the score calculation to compute_score(). If no score is available (None),
    returns an empty string. Otherwise, formats the score as a whole-number percentage string.

    Args:
        session (dict): The session dictionary tracking user performance.
        unit (str): The unit identifier.
        exercise (str or None): Optional exercise identifier. If None, computes the total unit score.

    Returns:
        str: The score as a percentage string (e.g., "85%"), or an empty string if no score is available.
    """
    score = compute_score(session, unit, exercise=exercise)

    if score is None:
        return ""

    else:
        return f'{int(100 * score)}%'


def compute_score(session, unit, exercise=None):
    """
    Computes the score for a specific exercise or for the entire unit.

    If an exercise is specified, delegates to compute_score_exercise().
    If no exercise is given, computes the overall score across all exercises in the unit
    using compute_score_unit(). Returns None if neither condition is met (defensive fallback).

    Args:
        session (dict): The session dictionary tracking user results.
        unit (str): The unit identifier.
        exercise (str or None): Optional exercise identifier.

    Returns:
        float or None: The score as a float between 0 and 1, or None if no data is available.
    """
    if exercise is not None:
        return compute_score_exercise(session, unit, exercise)

    elif exercise is None:
        return compute_score_unit(session, unit)

    else:
        return None


def compute_score_unit(session, unit):
    """
    Computes the overall score for a unit by aggregating correct and incorrect answers across all exercises.

    Iterates through all exercises in the unit, summing the number of correct (trues) and incorrect (falses)
    answers using compute_trues_and_falses(). Then calculates the final score as a fraction of correct answers
    over the total using compute_fraction().

    Args:
        session (dict): The session dictionary tracking user results.
        unit (str): The unit identifier.

    Returns:
        float: The unit score as a float between 0 and 1.
    """
    trues_unit = 0
    falses_unit = 0
    for exercise in range(1, highest_exercise[unit] + 1):
        trues_exercise, falses_exercise = compute_trues_and_falses(session, unit, exercise)
        trues_unit = trues_unit + trues_exercise
        falses_unit = falses_unit + falses_exercise
    return compute_ratio_correct_answers(trues_unit, falses_unit)


def compute_score_exercise(session, unit, exercise):
    """
    Computes the score for a specific exercise within a unit.

    If the 'result' key exists in the session for the given exercise, returns the stored score.
    Otherwise, if 'progress' exists, calculates the score by counting correct and incorrect answers
    using compute_trues_and_falses(), and computes the score as a fraction.
    If neither key is present, returns None.

    Args:
        session (dict): The session dictionary tracking user progress.
        unit (str): The unit identifier.
        exercise (str or int): The exercise identifier.

    Returns:
        float or None: The score as a float between 0 and 1, or None if no data is available.
    """
    ex_int = int(exercise) if not isinstance(exercise, int) else exercise
    ex_str = str(ex_int)

    if current_user.is_authenticated:
        row = UserExerciseState.query.filter_by(
            user_id=current_user.id, unit=unit, exercise=ex_int
        ).first()
        if not row or not (row.state or {}):
            return None

        s = row.state or {}
        finished = ("score" in s) or ("result" in s) or (row.completed_at is not None)

        # If finished and score is stored, return it directly.
        if finished and ("score" in s or "result" in s):
            try:
                return float(s.get("score", s.get("result")))
            except (TypeError, ValueError):
                # fall through to recompute from counts
                pass

        # Otherwise compute from trues/falses (mirrors anonymous logic)
        trues, falses = compute_trues_and_falses(session, unit, ex_int)
        denom = trues + falses
        if denom <= 0:
            # If finished but no stored score and counts are empty, try total-based fallback.
            if finished:
                total = s.get("total_questions")
                if total is None:
                    # total = compute_total_questions(unit, ex_int)
                    total = total_question_exercises[unit][ex_int]
                total = int(total or 0)
                if total > 0:
                    # With no counts we can't infer split → return None rather than 0.
                    return None
            return None
        return compute_ratio_correct_answers(trues, falses)

    else:
        if is_key_in_exercise(session, unit, exercise, 'result'):
            return session[unit][str(exercise)]['result']

        elif is_key_in_exercise(session, unit, exercise, 'progress'):
            trues, falses = compute_trues_and_falses(session, unit, exercise)
            return compute_ratio_correct_answers(trues, falses)
        else:
            return None


def compute_ratio_correct_answers(trues, falses):
    """
    Computes the fraction of correct answers over the total number of answers.

    If both trues and falses are zero, returns None to indicate that no score can be computed.

    Args:
        trues (int): Number of correct answers.
        falses (int): Number of incorrect answers.

    Returns:
        float or None: The score as a float between 0 and 1, or None if no answers were given.
    """
    if trues + falses == 0:
        return None
    else:
        return round(trues / (trues + falses), 2)


def compute_trues_and_falses(session, unit, exercise):
    """
    Calculates the number of correct (trues) and incorrect (falses) answers for a specific exercise.

    - If a final score ('result') is recorded in the session, computes trues and falses proportionally
      based on the total number of questions.
    - If only progress is recorded, compares the list of answered question IDs with the list of incorrect ones.
    - If neither is available, assumes 0 trues and 0 falses.

    Args:
        session (dict): The session dictionary tracking user progress.
        unit (str): The unit identifier.
        exercise (str or int): The exercise identifier.

    Returns:
        tuple: A pair (trues, falses) representing the number of correct and incorrect answers.
    """

    ex_int = int(exercise) if not isinstance(exercise, int) else exercise
    ex_str = str(ex_int)

    if current_user.is_authenticated:
        row = UserExerciseState.query.filter_by(
            user_id=current_user.id, unit=unit, exercise=ex_int
        ).first()
        if not row or not row.state:
            return 0, 0

        state = row.state or {}
        total = state.get("total_questions")
        if total is None:
            # total = compute_total_questions(unit, ex_int)
            total = total_question_exercises[unit][ex_int]
        total = int(total or 0)

        # Finished path: DB has score/result or completed_at set
        if "score" in state or "result" in state or row.completed_at:
            try:
                score = float(state.get("score", state.get("result", 0.0)) or 0.0)
            except (TypeError, ValueError):
                score = 0.0
            trues = int(round(score * total))
            falses = max(total - trues, 0)
            return trues, falses

        # Unfinished path: use sets of Nrs like session logic
        correct_nrs = set(int(n) for n in (state.get("correct_nrs") or state.get("correct_ids") or []))
        incorrect_nrs = set(int(k) for k in (state.get("incorrect") or {}).keys())
        trues = len(correct_nrs - incorrect_nrs)
        falses = len(incorrect_nrs)
        return trues, falses

    else:
        if is_key_in_exercise(session, unit, exercise, 'result'):
            result_exercise = session[unit][str(exercise)]['result']
            # trues = result_exercise * compute_total_questions(unit, exercise=exercise)
            trues = result_exercise * total_question_exercises[unit][ex_int]
            # falses = (1 - result_exercise) * compute_total_questions(unit, exercise=exercise)
            falses = (1 - result_exercise) * total_question_exercises[unit][ex_int]

        elif is_key_in_exercise(session, unit, exercise, 'progress'):
            init_session_key(session, unit, exercise, 'falses')
            trues = len( set(session[unit][str(exercise)]['progress']) - set(session[unit][str(exercise)]['falses']) )
            falses = len(session[unit][str(exercise)]['falses'])

        else:
            trues = 0
            falses = 0
        return trues, falses
