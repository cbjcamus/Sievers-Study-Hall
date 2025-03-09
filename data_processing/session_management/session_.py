progress = 'progress'
score = 'score'
result = 'result'


def print_session(session):
    print_session_dictionary(session, progress)
    print_session_dictionary(session, score)
    print_session_dictionary(session, result)
    return

def print_session_dictionary(session, dictionary):
    if dictionary in session:
        for x, y in session[dictionary].items():
            print(dictionary, x, y)
    else:
        print(f'{dictionary} empty')
    return