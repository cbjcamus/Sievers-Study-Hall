from data.data_processing.data_loading import load_data

from webapp.session_management.verification_session import is_key_in_exercise, init_session_key


def pick_a_question(session, unit, exercise):
    """
    Selects a random unanswered question from the specified unit and exercise.

    Loads the relevant data and retrieves the list of already answered question IDs
    from the session (stored under 'progress'). Filters out the answered questions,
    and randomly selects one from the remaining pool. If all questions have been answered,
    returns None.

    Args:
        session (dict): The session dictionary tracking user progress.
        unit (str): The unit identifier.
        exercise (str or int): The exercise identifier (converted to string for session lookup).

    Returns:
        pandas.Series or None: A single unanswered question row, or None if all have been answered.
    """
    data = load_data(unit, exercise)

    init_session_key(session, unit, exercise, 'progress')
    answered_nrs = session[unit][str(exercise)]['progress']
    filtered_data = data[~data["Nr"].astype(str).isin(answered_nrs)]

    if filtered_data.empty:
        return None

    random_question = filtered_data.sample(1).iloc[0]# .fillna("")
    return random_question


def is_exercise_finished(session, unit, exercise):
    """
    Determines whether a given exercise has been completed by the user.

    The exercise is considered finished if:
    - All question IDs in the data match those stored in session['progress'].
    - OR no more questions are available to pick.
    - OR a 'result' key exists in the session for that unit and exercise.

    Args:
        session (dict): The session dictionary tracking user progress.
        unit (str): The unit identifier.
        exercise (str or int): The exercise identifier (converted to string for lookup).

    Returns:
        bool: True if the exercise is complete, False otherwise.
    """
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
