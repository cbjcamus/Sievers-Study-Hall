def is_unit_in_session(session, unit):
    """
    Checks whether a given unit exists in the session dictionary.

    Args:
        session (dict): The session dictionary tracking user data.
        unit (str): The unit identifier to look for.

    Returns:
        bool: True if the unit is present in the session, False otherwise.
    """
    return unit in session


def is_exercise_in_unit(session, unit, exercise):
    """
    Checks whether a specific exercise exists within a given unit in the session.

    First verifies that the unit exists in the session.
    Then checks if the exercise (converted to string) is present in that unit.

    Args:
        session (dict): The session dictionary tracking user data.
        unit (str): The unit identifier.
        exercise (str or int): The exercise identifier.

    Returns:
        bool: True if the exercise exists within the unit in the session, False otherwise.
    """
    if is_unit_in_session(session, unit):
        return str(exercise) in session[unit]
    else:
        return False


def is_key_in_exercise(session, unit, exercise, key):
    """
    Checks whether a specific key exists within a given exercise in a unit in the session.

    First confirms that the exercise exists within the unit.
    Then checks if the specified key is present in that exercise's session data.

    Args:
        session (dict): The session dictionary tracking user data.
        unit (str): The unit identifier.
        exercise (str or int): The exercise identifier.
        key (str): The key to check for in the exercise's session data.

    Returns:
        bool: True if the key is present, False otherwise.
    """
    if is_exercise_in_unit(session, unit, exercise):
        return key in session[unit][str(exercise)]
    else:
        return False


def init_session_key(session, unit, exercise, key):
    """
    Ensures that a specific key exists in the session for a given unit and exercise.

    If the unit or exercise is missing from the session, they are initialized.
    If the key does not exist under the exercise, it is created and initialized as an empty list.

    Args:
        session (dict): The session dictionary to update.
        unit (str): The unit identifier.
        exercise (str or int): The exercise identifier.
        key (str): The key to ensure within the exercise's data.

    Returns:
        None
    """
    if unit not in session:
        session[unit] = {}

    if str(exercise) not in session[unit]:
        session[unit][str(exercise)] = {}

    if key not in session[unit][str(exercise)]:
        session[unit][str(exercise)][key] = []

    return


def is_key_in_session(session, key):
    return key in session