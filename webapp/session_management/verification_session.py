def is_unit_in_session(session, unit):
    return unit in session


def is_exercise_in_unit(session, unit, exercise):
    if is_unit_in_session(session, unit):
        return str(exercise) in session[unit]
    else:
        return False


def is_key_in_exercise(session, unit, exercise, key):
    if is_exercise_in_unit(session, unit, exercise):
        return key in session[unit][str(exercise)]
    else:
        return False


def create_key_in_session(session, unit, exercise, key):
    if unit not in session:
        session[unit] = {}

    if str(exercise) not in session[unit]:
        session[unit][str(exercise)] = {}

    if key not in session[unit][str(exercise)]:
        session[unit][str(exercise)][key] = []

    return
