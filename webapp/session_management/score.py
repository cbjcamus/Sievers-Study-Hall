from webapp.session_management.total_questions import compute_highest_exercise, compute_total_questions
from webapp.session_management.session_ import score, result


def write_score(session, unit, exercise=None):
    score_ = compute_score(session, unit, exercise=exercise)

    if score_ is None:
        return ""

    else:
        return f'{int(100 * score_)}%'


def compute_score(session, unit, exercise=None):
    if exercise is not None:
        return compute_score_exercise_session(session, unit, exercise)

    elif exercise is None:
        return compute_score_unit_session(session, unit)

    else:
        return None


def compute_score_exercise_session(session, unit, exercise):
    if result in session and unit in session[result] and str(exercise) in session[result][unit]:
        return session[result][unit][str(exercise)]

    elif score in session and unit in session[score] and str(exercise) in session[score][unit]:
        trues = compute_trues(session, unit, exercise)
        falses = compute_falses(session, unit, exercise)
        return compute_fraction(trues, falses)
    else:
        return None


def compute_score_unit_session(session, unit):
    trues = 0
    falses = 0
    for exercise in range(1, compute_highest_exercise(unit) + 1):
        trues = trues + compute_trues(session, unit, exercise)
        falses = falses + compute_falses(session, unit, exercise)
    return compute_fraction(trues, falses)


def compute_fraction(trues, falses):
    if trues + falses == 0:
        return 0

    else:
        return trues / (trues + falses)


def compute_trues(session, unit, exercise):
    if result in session and unit in session[result] and str(exercise) in session[result][unit]:
        result_exercise = session[result][unit][str(exercise)]
        trues = result_exercise * compute_total_questions(unit, exercise=exercise)

    elif score in session and unit in session[score] and str(exercise) in session[score][unit]:
        trues = sum(1 for val in session[score][unit][str(exercise)].values() if val is True)

    else:
        trues = 0
    return trues


def compute_falses(session, unit, exercise):
    if result in session and unit in session[result] and str(exercise) in session[result][unit]:
        result_exercise = session[result][unit][str(exercise)]
        falses = (1 - result_exercise) * compute_total_questions(unit, exercise=exercise)

    elif score in session and unit in session[score] and str(exercise) in session[score][unit]:
        falses = sum(1 for val in session[score][unit][str(exercise)].values() if val is False)

    else:
        falses = 0
    return falses
