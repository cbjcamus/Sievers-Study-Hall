from data.data_processing.units import units


def print_complete_session(session):
    print_session_dictionary(session, 'progress')
    print_session_dictionary(session, 'score')
    print_session_dictionary(session, 'result')
    print_session_feedbacks(session)
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
