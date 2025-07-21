from webapp.session_management.total_questions import compute_total_questions, compute_highest_exercise
from webapp.session_management.verification_session import is_key_in_exercise


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
    for exercise in range(1, compute_highest_exercise(unit) + 1):
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
    if is_key_in_exercise(session, unit, exercise, 'result'):
        return compute_total_questions(unit, exercise=exercise)

    elif is_key_in_exercise(session, unit, exercise, 'progress'):
        return len(session[unit][str(exercise)]['progress'])

    else:
        return 0
