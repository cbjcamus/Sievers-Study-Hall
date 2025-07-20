from webapp.session_management.score import compute_score
from webapp.session_management.verification_session import is_key_in_exercise, create_key_in_session
from webapp.session_management.statistics import print_exercise_completed


def register_progress(session, unit, exercise, nr):
    if (unit, exercise) not in session['unfinished_exercise']:
        session['unfinished_exercise'].append((unit, exercise))

    create_key_in_session(session, unit, exercise, 'progress')
    session[unit][str(exercise)]['progress'].append(nr)
    return


def register_false(session, unit, exercise, nr):
    create_key_in_session(session, unit, exercise, 'falses')
    session[unit][str(exercise)]['falses'].append(nr)
    return


def register_user_incorrect_answer(session, unit, exercise, incorrect_answer):
    create_key_in_session(session, unit, exercise, 'incorrect_answer')
    session[unit][str(exercise)]['incorrect_answer'].append(incorrect_answer)
    return


def register_result(session, unit, exercise, feedback):
    if feedback is not None:
        print_exercise_completed(unit, exercise)

    create_key_in_session(session, unit, exercise, 'progress')
    create_key_in_session(session, unit, exercise, 'falses')

    score_exercise = compute_score(session, unit, exercise)
    session[unit][str(exercise)]['result'] = round(score_exercise, 2)

    if is_key_in_exercise(session, unit, exercise, 'progress'):
        del session[unit][str(exercise)]['progress']

    if is_key_in_exercise(session, unit, exercise, 'falses'):
        del session[unit][str(exercise)]['falses']

    if is_key_in_exercise(session, unit, exercise, 'incorrect_answer'):
        del session[unit][str(exercise)]['incorrect_answer']

    if (unit, exercise) in session['unfinished_exercise']:
        session['unfinished_exercise'].remove((unit, exercise))

    session.modified = True
    return
