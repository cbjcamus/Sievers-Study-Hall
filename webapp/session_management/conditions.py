from data.data_processing.data_loading import load_data

from webapp.session_management.session_ import progress, result
from webapp.session_management.pick_a_question import pick_a_question
from webapp.session_management.session_ import print_exercise_level_completed


def level_finished(session, exercise, level):
    if progress in session and exercise in session[progress] and str(level) in session[progress][exercise]:
        data = load_data(exercise, level)

        answered_nrs = set(session[progress][exercise][str(level)].keys())

        if set(data["Nr"].astype(str)) == answered_nrs:
            print_exercise_level_completed(exercise, level)
            return True

    if pick_a_question(session, exercise, level) is None:
        print_exercise_level_completed(exercise, level)
        return True

    if result in session and exercise in session[result] and str(level) in session[result][exercise]:
        print_exercise_level_completed(exercise, level)
        return True

    else:
        return False