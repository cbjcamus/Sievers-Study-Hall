from webapp.session_management.total_questions import compute_highest_level, compute_total_questions
from webapp.session_management.session_ import score, result


def write_score(session, exercise, level=None):
    score_ = compute_score(session, exercise, level=level)

    if score_ is None:
        return ""

    else:
        return f'{int(100 * score_)}%'


def compute_score(session, exercise, level=None):
    if level is not None:
        return compute_score_level_session(session, exercise, level)

    elif level is None:
        return compute_score_exercise_session(session, exercise)

    else:
        return None


def compute_score_level_session(session, exercise, level):
    if result in session and exercise in session[result] and str(level) in session[result][exercise]:
        return session[result][exercise][str(level)]

    elif score in session and exercise in session[score] and str(level) in session[score][exercise]:
        trues = compute_trues(session, exercise, level)
        falses = compute_falses(session, exercise, level)
        return compute_fraction(trues, falses)
    else:
        return None


def compute_score_exercise_session(session, exercise):
    trues = 0
    falses = 0
    for level in range(1, compute_highest_level(exercise) + 1):
        trues = trues + compute_trues(session, exercise, level)
        falses = falses + compute_falses(session, exercise, level)
    return compute_fraction(trues, falses)


def compute_fraction(trues, falses):
    if trues + falses == 0:
        return 0

    else:
        return trues / (trues + falses)


def compute_trues(session, exercise, level):
    if result in session and exercise in session[result] and str(level) in session[result][exercise]:
        result_level = session[result][exercise][str(level)]
        trues = result_level * compute_total_questions(exercise, level=level)

    elif score in session and exercise in session[score] and str(level) in session[score][exercise]:
        trues = sum(1 for val in session[score][exercise][str(level)].values() if val is True)

    else:
        trues = 0
    return trues


def compute_falses(session, exercise, level):
    if result in session and exercise in session[result] and str(level) in session[result][exercise]:
        result_level = session[result][exercise][str(level)]
        falses = (1 - result_level) * compute_total_questions(exercise, level=level)

    elif score in session and exercise in session[score] and str(level) in session[score][exercise]:
        falses = sum(1 for val in session[score][exercise][str(level)].values() if val is False)

    else:
        falses = 0
    return falses
