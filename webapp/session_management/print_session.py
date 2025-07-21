import json

from data.data_processing.units import units


def print_complete_session(session):
    """
    Prints the entire session dictionary, displaying progress and data for each unit and exercise.

    For each key in the session:
    - If the key corresponds to a known unit (as listed in the global 'units'),
      it prints each exercise and its associated values.
    - Otherwise, it prints the key and its value directly.

    Args:
        session (dict): The session dictionary to inspect.

    Returns:
        None
    """
    for key in session:
        if key in units:
            for exercise, value in session[key].items():
                print(key, exercise, value)
        else:
            print(key, session[key])
    return


def session_size(session):
    """
    Calculates the size of the session data in bytes.

    Converts the session dictionary to a JSON string and encodes it in UTF-8,
    then returns the length of the resulting byte string.

    Args:
        session (dict): The session dictionary to measure.

    Returns:
        int: The size of the session in bytes.
    """
    session_data = dict(session)
    session_json = json.dumps(session_data)
    size_in_bytes = len(session_json.encode('utf-8'))
    return size_in_bytes