import pandas as pd

from flask_login import current_user

from data.data_processing.data_loading import load_data_exercise
from data.data_processing.exercises import is_exercise_prompt

from users.users.models import UserExerciseState
from users.questions.content_format import format_feedback


def get_incorrect_answers(session, unit, exercise):
    """
    Retrieves the list of incorrect answers and their count from the session data
    for a specific unit and exercise.

    Checks if 'incorrect_answer' exists in the session dictionary for the given unit
    and exercise. If found, returns the list and its length; otherwise, returns an
    empty list and count 0.

    Args:
        session (dict): The session dictionary storing user progress.
        unit (str): The unit identifier.
        exercise (str or int): The exercise identifier (converted to string for lookup).

    Returns:
        tuple: (list of incorrect answers, number of incorrect answers)
    """

    ex_int = int(exercise) if not isinstance(exercise, int) else exercise

    # ----------------------------------------------------------
    # Logged-in: get from DB state
    # ----------------------------------------------------------
    '''
    if current_user.is_authenticated:
        row = UserExerciseState.query.filter_by(
            user_id=current_user.id, unit=unit, exercise=ex_int
        ).first()
        if row and row.state:
            incorrect = row.state.get("incorrect", {})
            if incorrect:
                answers = list(incorrect.values())
                return answers, len(answers)
            return [], 0
        return [], 0
    '''

    '''
    else:
        if 'incorrect_answer' in session[unit][str(exercise)]:
            incorrect_answers = session[unit][str(exercise)]['incorrect_answer']
            number_of_incorrect_answers = len(incorrect_answers)
        else:
            incorrect_answers = []
            number_of_incorrect_answers = 0

        return incorrect_answers, number_of_incorrect_answers
    '''

    if current_user.is_authenticated:
        row = UserExerciseState.query.filter_by(
            user_id=current_user.id,
            unit=unit,
            exercise=ex_int
        ).first()

        if row and row.state:
            return row.state.get("incorrect") or {}

    else:
        exercise_state = session.get(unit, {}).get(str(exercise), {})

        ids = exercise_state.get("falses", [])
        answers = exercise_state.get("incorrect_answer", [])

        return {
            int(question_id): answer
            for question_id, answer in zip(ids, answers)
        }


def get_feedback_exercise(session, unit, exercise, language, incorrect):
    """
    Generates detailed feedback for all incorrect answers from a given exercise.

    Retrieves the list of incorrect question IDs ('falses') from the session data
    for the specified unit and exercise. Loads and filters the exercise data to
    include only the incorrect questions, preserves their original order, and passes
    the filtered data to a formatting function to generate feedback messages.

    Args:
        session (dict): The session dictionary storing user progress.
        unit (str): The unit identifier.
        exercise (str or int): The exercise identifier (converted to string for lookup).
        language (str): The User's language

    Returns:
        list: A list of formatted feedback strings for each incorrect answer.
    """

    '''
    ex_int = int(exercise) if not isinstance(exercise, int) else exercise

    # ---- collect incorrect Nrs ----
    incorrect_ids = []

    if current_user.is_authenticated:
        row = UserExerciseState.query.filter_by(
            user_id=current_user.id, unit=unit, exercise=ex_int
        ).first()
        if row and row.state:
            inc = row.state.get("incorrect") or {}
            # keys are Nrs (stored as str in JSON); coerce to int
            incorrect_ids = [int(k) for k in inc.keys()]
            # incorrect_ids.sort()  # deterministic order (ascending)

    else:
        if 'falses' in session[unit][str(exercise)]:
            incorrect_ids = session[unit][str(exercise)]['falses']
            incorrect_ids = [int(i) for i in incorrect_ids]
        else:
            incorrect_ids = []

    if not incorrect_ids:
        return []
    '''

    incorrect_ids = [int(k) for k in incorrect]

    data = load_data_exercise(unit, exercise)
    data = data[data["Nr"].isin(incorrect_ids)]

    data["Nr"] = pd.Categorical(
        data["Nr"],
        categories=incorrect_ids,
        ordered=True
    )

    data = data.sort_values("Nr")

    data["user_answer"] = data["Nr"].apply(
        lambda nr: incorrect[str(int(nr))]["answer"]
    )

    if is_exercise_prompt(unit, exercise):
        data["translation"] = data["Nr"].apply(
            lambda nr: incorrect[str(int(nr))]["translation"]
        )
        data["commentary"] = data["Nr"].apply(
            lambda nr: incorrect[str(int(nr))]["commentary"]
        )

    feedbacks = format_feedbacks(data, unit, exercise, language)
    return feedbacks


def format_feedbacks(df, unit, exercise, language):
    """
    Formats feedback messages for each row in a DataFrame using a predefined template.

    Retrieves the feedback template from the FEEDBACK dictionary for the specified unit
    and exercise. For each row in the DataFrame, fills in the template with values from
    specific columns (e.g., 'question', 'answer', 'english', etc.). Also formats the list
    of correct answers using get_list_of_correct_answers().

    Args:
        df (pandas.DataFrame): The filtered exercise data containing incorrect answers.
        unit (str): The unit identifier used to select the appropriate template.
        exercise (str): The exercise identifier used to select the appropriate template.
        language (str): The User's language

    Returns:
        list: A list of formatted feedback strings, one for each row in the DataFrame.
    """
    result = []

    for _, row in df.iterrows():

        question_id = row.get("Nr", "")

        user_answer = row.get("user_answer", None)
        translation = row.get("translation", None)
        commentary = row.get("commentary", None)

        formatted = format_feedback(unit, exercise, language, question_id,
                                    user_answer=user_answer, translation=translation, commentary=commentary)

        result.append(formatted)
    return result
