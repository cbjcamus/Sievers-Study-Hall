from data.data_processing.data_loading import load_data

from webapp.session_management.session_ import progress, result
from webapp.session_management.pick_a_question import pick_a_question
from webapp.session_management.session_ import print_unit_exercise_completed


def exercise_finished(session, unit, exercise):
    if progress in session and unit in session[progress] and str(exercise) in session[progress][unit]:
        data = load_data(unit, exercise)

        answered_nrs = set(session[progress][unit][str(exercise)].keys())

        if set(data["Nr"].astype(str)) == answered_nrs:
            print_unit_exercise_completed(unit, exercise)
            return True

    if pick_a_question(session, unit, exercise) is None:
        print_unit_exercise_completed(unit, exercise)
        return True

    if result in session and unit in session[result] and str(exercise) in session[result][unit]:
        print_unit_exercise_completed(unit, exercise)
        return True

    else:
        return False