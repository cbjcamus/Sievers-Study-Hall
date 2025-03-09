from data_processing.session_management.session_ import progress, score, result
from data_processing.data_loading import load_data, pick_a_question


def level_finished(exercise, level, session):
    if progress in session and exercise in session[progress] and str(level) in session[progress][exercise]:
        data = load_data(exercise, level)

        answered_nrs = set(session[progress][exercise][str(level)].keys())

        if set(data["Nr"].astype(str)) == answered_nrs:
            return True

    if pick_a_question(session, exercise, level) is None:
        return True

    if result in session and exercise in session[result] and str(level) in session[result][exercise]:
        return True

    else:
        return False