import random

from flask_login import current_user

from data.data_processing.data_loading import load_data_exercise, load_data_level, is_exercise_multiple_choice

from users.progress.models import UserExerciseState
from users.session_management.verification_session import is_key_in_exercise, init_session_key


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
    ex_str = str(ex_int)

    # ------------------------------------------------------------------
    # Logged-in: filter with DB state
    # ------------------------------------------------------------------
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
    return random_question


def pick_other_options(unit, exercise, question):
    data = load_data_level(unit, exercise)

    other_questions = []
    if len(data) > 1:
        sampled_df = data[data["Nr"] != question["Nr"]].sample(
            min(4, len(data) - 1), replace=False
        )
        other_questions = sampled_df.to_dict(orient="records")

    return other_questions


def shuffle_options(correct_answer, other_answers):
    """
    Returns a list of 5 options in random order.

    Args:
        correct_answer (str): The correct answer.
        other_answers (list): List of 4 other answers.

    Returns:
        list: 5 options shuffled randomly.
    """
    options = [correct_answer] + other_answers
    random.shuffle(options)
    return options


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

    if pick_a_question(session, unit, exercise) is None:
        return True

    if is_key_in_exercise(session, unit, exercise, 'result'):
        return True

    else:
        return False


def get_question_from_incorrect_answer(unit, exercise, result, incorrect_answer):

    if result != "incorrect":
        return ""

    elif is_exercise_multiple_choice(unit, exercise) is False:
        return ""

    else:
        data = load_data_level(unit, exercise)

        match = data.loc[data['answer'] == incorrect_answer, 'question']

        if not match.empty:
            question = match.iloc[0]
            return f"({question})"
        else:
            return None