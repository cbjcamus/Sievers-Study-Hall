from flask import session
from typing import cast

from flask_login import current_user

from . import routes_bp

from data.data_processing.units import units
from data.data_processing.total_questions import highest_exercise

from users.session_management.logging import log_progress_deleted_from_session
from users.session_management.print_session import session_size, print_session_size, print_complete_session
from users.session_management.verification_session import is_key_in_exercise, is_key_in_session

session = cast(dict, session)


@routes_bp.before_request
def ensure_session_keys_exist_and_make_session_permanent():
    session.permanent = True

    if 'unfinished_exercise' not in session:
        session['unfinished_exercise'] = []

    # print_complete_session(session)
    # print_session_size(session)
    # print_user_info_from_db()
    # session.clear()


@routes_bp.before_request
def clear_progress_for_unconnected_users():
    if not current_user.is_authenticated:
        if session_size(session) > 3000:
            if is_key_in_session(session, 'progress'):
                session.pop('progress')


@routes_bp.before_request
def delete_old_unfinished_exercise():
    if session_size(session) > 3000:
        if not session['unfinished_exercise']:
            session.clear()
        else:
            unit, exercise = session['unfinished_exercise'][0]
            if unit in session and str(exercise) in session[unit]:
                log_progress_deleted_from_session(unit, exercise)
                del session[unit][str(exercise)]

            session['unfinished_exercise'].remove((unit, exercise))
            session['popup'] = {'unit': unit, 'exercise': exercise}

        # print(f"Progress deleted for {unit} {exercise}")


@routes_bp.app_context_processor
def inject_popup():
    return {"popup": session.pop("popup", None)}


@routes_bp.after_request
def clear_empty_unit_dictionary(response):
    if session_size(session) > 3000:
        for unit in units:
            for exercise in range(100):
                if is_key_in_exercise(session, unit, exercise, 'progress'):
                    if (len(session[unit][str(exercise)]['progress']) == 0
                            and is_key_in_exercise(session, unit, exercise, 'result') is False):
                        unit_dict = session.get(unit, {})
                        unit_dict.pop(str(exercise), None)
                        session[unit] = unit_dict
    return response