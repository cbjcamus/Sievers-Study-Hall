from data.data_processing.data_loading import load_data

from webapp.session_management.statistics import print_exercise_completed
from webapp.session_management.verification_session import is_key_in_exercise, create_key_in_session


def pick_a_question(session, unit, exercise):
    data = load_data(unit, exercise)

    create_key_in_session(session, unit, exercise, 'progress')
    answered_nrs = session[unit][str(exercise)]['progress']
    filtered_data = data[~data["Nr"].astype(str).isin(answered_nrs)]

    if filtered_data.empty:
        return None

    random_question = filtered_data.sample(1).iloc[0]# .fillna("")
    return random_question


def is_exercise_finished(session, unit, exercise):
    if is_key_in_exercise(session, unit, exercise, 'progress'):
        data = load_data(unit, exercise)

        answered_nrs = set(session[unit][str(exercise)]['progress'])

        if set(data["Nr"].astype(str)) == answered_nrs:
            return True

    if pick_a_question(session, unit, exercise) is None:
        return True

    if is_key_in_exercise(session, unit, exercise, 'result'):
        return True

    else:
        return False
