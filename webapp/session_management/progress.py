from webapp.session_management.total_questions import compute_total_questions, compute_highest_exercise
from webapp.session_management.verification_session import is_key_in_exercise


def compute_answered_questions(session, unit, exercise=None):
    if exercise is not None:
        return compute_answered_questions_exercise(session, unit, exercise)

    elif exercise is None:
        return compute_answered_questions_unit(session, unit)

    else:
        return 0


def compute_answered_questions_unit(session, unit):
    answered_questions = 0
    for exercise in range(1, compute_highest_exercise(unit) + 1):
        answered_questions_exercise = compute_answered_questions_exercise(session, unit, exercise)
        answered_questions = answered_questions + answered_questions_exercise
    return int(answered_questions)


def compute_answered_questions_exercise(session, unit, exercise):
    if is_key_in_exercise(session, unit, exercise, 'result'):
        return compute_total_questions(unit, exercise=exercise)

    elif is_key_in_exercise(session, unit, exercise, 'progress'):
        return len(session[unit][str(exercise)]['progress'])

    else:
        return 0
