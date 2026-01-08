from flask_login import current_user

from users.progress.models import UserExerciseState
from users.questions.pick_a_question import is_exercise_finished

from data.data_processing.total_questions import total_question_exercises, highest_exercise
from users.session_management.verification_session import is_key_in_exercise


def compute_completed_exercises(session, unit, highest_exercise):
    highest_exercise_unit = highest_exercise[unit]

    finished_exercises = 0
    for exercise in range(1, highest_exercise_unit + 1):
        if is_exercise_finished(session, unit, exercise):
            finished_exercises = finished_exercises + 1

    return finished_exercises


def get_next_exercise(unit, current_exercise, highest_exercise):
    highest_exercise_unit = highest_exercise[unit]

    if current_exercise == highest_exercise_unit:
        return None

    else:
        return current_exercise + 1


def update_progress_in_session(session, unit):
    progress = session.setdefault('progress', {})

    progress[unit] = compute_completed_exercises(session, unit, highest_exercise)

    session.modified = True
    return


def compute_answered_questions(session, unit, exercise=None):
    """
    Computes the number of answered questions for a given unit or a specific exercise.

    If an exercise is provided, delegates to compute_answered_questions_exercise().
    If not, delegates to compute_answered_questions_unit() to count all answered questions across the unit.
    Returns 0 by default if neither condition is met (defensive fallback).

    Args:
        session (dict): The session dictionary tracking user progress.
        unit (str): The unit identifier.
        exercise (str or None): Optional exercise identifier.

    Returns:
        int: The number of answered questions.
    """
    if exercise is not None:
        return compute_answered_questions_exercise(session, unit, exercise)

    elif exercise is None:
        return compute_answered_questions_unit(session, unit)

    else:
        return 0


def compute_answered_questions_unit(session, unit):
    """
    Computes the total number of answered questions across all exercises within a unit.

    Iterates through all exercises from 1 up to the highest exercise number (inclusive),
    and sums the number of answered questions for each using compute_answered_questions_exercise().

    Args:
        session (dict): The session dictionary tracking user progress.
        unit (str): The unit identifier.

    Returns:
        int: The total number of answered questions in the unit.
    """
    answered_questions = 0
    for exercise in range(1, highest_exercise[unit] + 1):
        answered_questions_exercise = compute_answered_questions_exercise(session, unit, exercise)
        answered_questions = answered_questions + answered_questions_exercise
    return int(answered_questions)


def compute_answered_questions_exercise(session, unit, exercise):
    """
    Computes the number of answered questions for a specific exercise in a unit.

    If the session contains a 'result' key for the exercise, the exercise is considered fully completed,
    and the total number of questions is returned.

    If only a 'progress' key is present, returns the number of questions tracked in progress.

    If neither key is found, returns 0.

    Args:
        session (dict): The session dictionary tracking user progress.
        unit (str): The unit identifier.
        exercise (str or int): The exercise identifier.

    Returns:
        int: The number of answered questions for the exercise.
    """

    ex_int = int(exercise) if not isinstance(exercise, int) else exercise
    ex_str = str(ex_int)

    # DB-first path for authenticated users
    if current_user.is_authenticated:
        row = UserExerciseState.query.filter_by(
            user_id=current_user.id, unit=unit, exercise=ex_int
        ).first()
        if not row or not row.state:
            return 0

        s = row.state or {}
        finished = ("score" in s) or ("result" in s) or (row.completed_at is not None)

        if finished:
            total = total_question_exercises[unit][ex_int]
            return int(total or 0)

        # Not finished → number of correct so far
        if "correct_nrs" in s:
            return len(s["correct_nrs"])
        elif "correct_ids" in s:  # backward compat
            return len(s["correct_ids"])
        elif "answered" in s:
            return int((s["answered"] or {}).get("correct", 0))
        return 0

    if is_key_in_exercise(session, unit, exercise, 'result'):
        # return compute_total_questions(unit, exercise=exercise)
        return total_question_exercises[unit][ex_int]

    elif is_key_in_exercise(session, unit, exercise, 'progress'):
        return len(session[unit][str(exercise)]['progress'])

    else:
        return 0
