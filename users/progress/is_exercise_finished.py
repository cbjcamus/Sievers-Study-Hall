from flask_login import current_user

from data.data_processing.data_loading import load_data_exercise

from users.users.models import UserExerciseState
from users.questions.pick_a_question import pick_a_question

from users.session_management.verification_session import is_key_in_exercise


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
    ex_int = int(exercise) if not isinstance(exercise, int) else exercise
    ex_str = str(ex_int)

    if current_user.is_authenticated:
        row = UserExerciseState.query.filter_by(
            user_id=current_user.id, unit=unit, exercise=ex_int
        ).first()
        if row and row.completed_at:
            return True

    if is_key_in_exercise(session, unit, exercise, 'progress'):
        data = load_data_exercise(unit, exercise)

        answered_nrs = set(session[unit][str(exercise)]['progress'])

        if set(data["Nr"].astype(str)) == answered_nrs:
            return True

    if is_key_in_exercise(session, unit, exercise, 'result'):
        return True

    if pick_a_question(session, unit, exercise) is None:
        return True

    else:
        return False
