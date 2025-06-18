from data.data_processing.data_loading import load_data


def pick_a_question(session, unit, exercise):
    data = load_data(unit, exercise)

    if 'progress' not in session:
        session['progress'] = {}

    if unit not in session['progress']:
        session['progress'][unit] = {}

    if str(exercise) not in session['progress'][unit]:
        session['progress'][unit][str(exercise)] = {}

    answered_nrs = session['progress'][unit][str(exercise)].keys()
    filtered_data = data[~data["Nr"].astype(str).isin(answered_nrs)]

    if filtered_data.empty:
        return None
    return filtered_data.sample(1).iloc[0]
