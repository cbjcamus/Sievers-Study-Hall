import json

from data.data_processing.units import units


def print_complete_session(session):
    for key in session:
        if key in units:
            for exercise, value in session[key].items():
                print(key, exercise, value)
        else:
            print(key, session[key])
    return


def print_session_dictionary(session, dictionary):
    if dictionary in session:
        for x, y in session[dictionary].items():
            print(dictionary, x, y)
    else:
        print(f'{dictionary} empty')
    return


def print_session_feedbacks(session):
    for unit in units:
        feedback = f"{units}_result"
        if feedback in session:
            for x, y in session[feedback].items():
                print(feedback, x, y)
        else:
            print(f'{feedback} empty')
    return


def session_size(session):
    session_data = dict(session)
    session_json = json.dumps(session_data)
    size_in_bytes = len(session_json.encode('utf-8'))
    return size_in_bytes