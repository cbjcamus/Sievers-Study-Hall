from data_processing.session_management.total_questions import compute_highest_level, compute_total_questions
from data_processing.session_management.session_ import score, result


def write_score(exercise, level=None, session=None):
    score_ = compute_score(exercise, level=level, session=session)

    if score_ == 0:
        return ""

    else:
        return f'{int(100 * score_)}%'


def compute_score(exercise, level=None, session=None):
    if level is not None and session is not None:
        return compute_score_level_session(exercise, level, session)

    elif level is None and session is not None:
        return compute_score_exercise_session(exercise, session)

    elif level is None and session is None:
        return 0

    elif level is not None and session is None:
        return 0

    else:
        return 0


def compute_score_level_session(exercise, level, session):
    if result in session and exercise in session[result] and str(level) in session[result][exercise]:
        return session[result][exercise][str(level)]

    elif score in session and exercise in session[score] and str(level) in session[score][exercise]:
        trues = compute_trues(exercise, level, session)
        falses = compute_falses(exercise, level, session)
        return compute_fraction(trues, falses)
    else:
        return 0


def compute_score_exercise_session(exercise, session):
    trues = 0
    falses = 0
    for level in range(1, compute_highest_level(exercise) + 1):
        trues = trues + compute_trues(exercise, level, session)
        falses = falses + compute_falses(exercise, level, session)
    return compute_fraction(trues, falses)


def compute_fraction(trues, falses):
    if trues + falses == 0:
        return 0

    else:
        return trues / (trues + falses)


def compute_trues(exercise, level, session):
    if result in session and exercise in session[result] and str(level) in session[result][exercise]:
        result_level = session[result][exercise][str(level)]
        trues = result_level * compute_total_questions(exercise, level=level)

    elif score in session and exercise in session[score] and str(level) in session[score][exercise]:
        trues = sum(1 for val in session[score][exercise][str(level)].values() if val is True)

    else:
        trues = 0
    return trues


def compute_falses(exercise, level, session):
    if result in session and exercise in session[result] and str(level) in session[result][exercise]:
        result_level = session[result][exercise][str(level)]
        falses = (1 - result_level) * compute_total_questions(exercise, level=level)

    elif score in session and exercise in session[score] and str(level) in session[score][exercise]:
        falses = sum(1 for val in session[score][exercise][str(level)].values() if val is False)

    else:
        falses = 0
    return falses
