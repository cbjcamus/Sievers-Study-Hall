from flask_login import current_user

from data.data_processing.data_loading import load_data_exercise

from users.users.models import UserExerciseState
from users.session_management.verification_session import init_session_key


def pick_a_question(session, unit, exercise):
    """
    Selects a random unanswered question from the specified unit and exercise.

    Loads the relevant data and retrieves the list of already answered question IDs
    from the session (stored under 'progress'). Filters out the answered questions,
    and randomly selects one from the remaining pool. If all questions have been answered,
    returns None.

    Args:
        session (dict): The session dictionary tracking user progress.
        unit (str): The unit identifier.
        exercise (str or int): The exercise identifier (converted to string for session lookup).

    Returns:
        pandas.Series or None: A single unanswered question row, or None if all have been answered.
    """
    data = load_data_exercise(unit, exercise)

    ex_int = int(exercise) if not isinstance(exercise, int) else exercise

    if current_user.is_authenticated:
        row = UserExerciseState.query.filter_by(
            user_id=current_user.id, unit=unit, exercise=ex_int
        ).first()

        correct_nrs = set()
        if row and row.state:
            # prefer "correct_nrs" (Nr-based); fallback to empty
            correct_nrs = set(map(int, row.state.get("correct_nrs", [])))

        filtered_data = data[~data["Nr"].astype(int).isin(correct_nrs)]

    else:
        init_session_key(session, unit, exercise, 'progress')
        answered_nrs = session[unit][str(exercise)]['progress']
        filtered_data = data[~data["Nr"].astype(str).isin(answered_nrs)]

    if filtered_data.empty:
        return None

    random_question = filtered_data.sample(1).iloc[0]
    return random_question["Nr"]
