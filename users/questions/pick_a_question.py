import random

from flask_login import current_user

from data.data_processing.data_loading import (load_data_exercise, load_data_level, load_data_question)
from data.data_processing.exercises import is_exercise_multiple_choice, get_answer_column, \
    is_exercise_multiple_choice_foreign, get_question_column

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
    ex_str = str(ex_int)

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


def get_options_for_multiple_choice_exercises(unit, exercise, question_ID, language):
    if is_exercise_multiple_choice(unit, exercise) is False:
        return None

    question_data = load_data_question(unit, exercise, question_ID)
    answer_column = get_answer_column(unit, exercise, language)
    correct_answer = question_data[answer_column]

    other_options = pick_other_options(unit, exercise, question_data)
    other_answers = [str(option[answer_column]) for option in other_options]

    options_text = shuffle_options(str(correct_answer), other_answers)

    return options_text


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
