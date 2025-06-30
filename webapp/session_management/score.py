from webapp.session_management.total_questions import compute_highest_exercise, compute_total_questions
from webapp.session_management.verification_session import is_key_in_exercise, create_key_in_session


def write_score(session, unit, exercise=None):
    score_ = compute_score(session, unit, exercise=exercise)

    if score_ is None:
        return ""

    else:
        return f'{int(100 * score_)}%'


def compute_score(session, unit, exercise=None):
    if exercise is not None:
        return compute_score_exercise(session, unit, exercise)

    elif exercise is None:
        return compute_score_unit(session, unit)

    else:
        return None


def compute_score_unit(session, unit):
    trues_unit = 0
    falses_unit = 0
    for exercise in range(1, compute_highest_exercise(unit) + 1):
        trues_exercise, falses_exercise = compute_trues_and_falses(session, unit, exercise)
        trues_unit = trues_unit + trues_exercise
        falses_unit = falses_unit + falses_exercise
    return compute_fraction(trues_unit, falses_unit)


def compute_score_exercise(session, unit, exercise):
    if is_key_in_exercise(session, unit, exercise, 'result'):
        return session[unit][str(exercise)]['result']

    elif is_key_in_exercise(session, unit, exercise, 'progress'):
        trues, falses = compute_trues_and_falses(session, unit, exercise)
        return compute_fraction(trues, falses)
    else:
        return None


def compute_fraction(trues, falses):
    if trues + falses == 0:
        return None
    else:
        return trues / (trues + falses)


def compute_trues_and_falses(session, unit, exercise):
    if is_key_in_exercise(session, unit, exercise, 'result'):
        result_exercise = session[unit][str(exercise)]['result']
        trues = result_exercise * compute_total_questions(unit, exercise=exercise)
        falses = (1 - result_exercise) * compute_total_questions(unit, exercise=exercise)

    elif is_key_in_exercise(session, unit, exercise, 'progress'):
        create_key_in_session(session, unit, exercise, 'falses')
        trues = len( set(session[unit][str(exercise)]['progress']) - set(session[unit][str(exercise)]['falses']) )
        falses = len(session[unit][str(exercise)]['falses'])

    else:
        trues = 0
        falses = 0
    return trues, falses

