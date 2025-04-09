from data_processing.exercises import exercises

progress = 'progress'
score = 'score'
result = 'result'


def print_session(session):
    print_session_dictionary(session, progress)
    print_session_dictionary(session, score)
    print_session_dictionary(session, result)
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
    for exercise in exercises:
        feedback = f"{exercise}_result"
        if feedback in session:
            for x, y in session[feedback].items():
                print(feedback, x, y)
        else:
            print(f'{feedback} empty')
    return