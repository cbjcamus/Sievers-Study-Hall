from flask import session
from typing import cast

from . import routes_bp

from data.data_processing.units import units

from users.session_management.logging import log_progress_deleted_from_session
from users.session_management.print_session import session_size
from users.session_management.print_session import print_complete_session, print_user_info_from_db, print_session_size
from users.questions.total_questions import compute_highest_exercise
from users.session_management.verification_session import is_key_in_exercise

session = cast(dict, session)


@routes_bp.before_request
def ensure_session_keys_exist_and_make_session_permanent():
    session.permanent = True

    if 'unfinished_exercise' not in session:
        session['unfinished_exercise'] = []

    # print_complete_session(session)
    # print_session_size(session)
    print_user_info_from_db()
    # session.clear()


@routes_bp.before_request
def delete_old_unfinished_exercise():
    if session_size(session) > 3500:
        unit, exercise = session['unfinished_exercise'][0]
        if unit in session and str(exercise) in session[unit]:
            log_progress_deleted_from_session(unit, exercise)
            del session[unit][str(exercise)]

        session['unfinished_exercise'].remove((unit, exercise))
        session['progress_deleted'] = {'unit': unit, 'exercise': exercise}
        # print(f"Progress deleted for {unit} {exercise}")


'''
@routes_bp.after_request
def clear_progress_deleted_flag(response):
    session.pop('progress_deleted', None)
    return response
'''


@routes_bp.after_request
def clear_empty_unit_dictionary(response):
    if session_size(session) > 2000:
        for unit in units:
            for exercise in range(compute_highest_exercise(unit)):
                if (is_key_in_exercise(session, unit, exercise, 'falses')
                        and is_key_in_exercise(session, unit, exercise, 'progress')):
                    if (len(session[unit][str(exercise)]['falses']) == 0
                            and len(session[unit][str(exercise)]['progress']) == 0):
                        unit_dict = session.get(unit, {})
                        unit_dict.pop(str(exercise), None)
                        session[unit] = unit_dict
    return response