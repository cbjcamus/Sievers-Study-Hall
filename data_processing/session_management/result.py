from data_processing.session_management.score import compute_score
from data_processing.session_management.session_ import result, progress, score


def register_result(exercise, level, session):
    score_level = compute_score(exercise, level, session)

    if result not in session:
        session[result] = {}

    if exercise not in session[result]:
        session[result][exercise] = {}

    if str(level) not in session[result][exercise]:
        session[result][exercise][str(level)] = {}

    session[result][exercise][str(level)] = round(score_level, 2)

    if exercise in session[progress] and str(level) in session[progress][exercise]:
        del session[progress][exercise][str(level)]

    if exercise in session[score] and str(level) in session[score][exercise]:
        del session[score][exercise][str(level)]

    session.modified = True
    return

