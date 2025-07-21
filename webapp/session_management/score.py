from webapp.session_management.total_questions import compute_highest_exercise, compute_total_questions
from webapp.session_management.verification_session import is_key_in_exercise, init_session_key


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
    for exercise in range(1, compute_highest_exercise(unit) + 1):
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
        return trues / (trues + falses)


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
    if is_key_in_exercise(session, unit, exercise, 'result'):
        result_exercise = session[unit][str(exercise)]['result']
        trues = result_exercise * compute_total_questions(unit, exercise=exercise)
        falses = (1 - result_exercise) * compute_total_questions(unit, exercise=exercise)

    elif is_key_in_exercise(session, unit, exercise, 'progress'):
        init_session_key(session, unit, exercise, 'falses')
        trues = len( set(session[unit][str(exercise)]['progress']) - set(session[unit][str(exercise)]['falses']) )
        falses = len(session[unit][str(exercise)]['falses'])

    else:
        trues = 0
        falses = 0
    return trues, falses

