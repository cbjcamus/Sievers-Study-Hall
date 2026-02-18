import pandas as pd

from flask import session, request
from flask_login import current_user

from data.data_processing.data_loading import load_data_exercise
from data.data_processing.exercise_type import is_exercise_multiple_choice

from users.progress.models import UserExerciseState
from users.questions.normalization import get_list_of_correct_answers

from webapp.i18n import get_language
from webapp.content.exercise.content_exercises import FEEDBACK


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
    ex_str = str(ex_int)

    # ----------------------------------------------------------
    # Logged-in: get from DB state
    # ----------------------------------------------------------
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

    else:
        if 'incorrect_answer' in session[unit][str(exercise)]:
            incorrect_answers = session[unit][str(exercise)]['incorrect_answer']
            number_of_incorrect_answers = len(incorrect_answers)
        else:
            incorrect_answers = []
            number_of_incorrect_answers = 0

        return incorrect_answers, number_of_incorrect_answers


def get_feedback_exercise(session, unit, exercise):
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

    Returns:
        list: A list of formatted feedback strings for each incorrect answer.
    """

    ex_int = int(exercise) if not isinstance(exercise, int) else exercise
    ex_str = str(ex_int)

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

    data = load_data_exercise(unit, exercise)
    data = data[data["Nr"].isin(incorrect_ids)]
    data["Nr"] = pd.Categorical(data["Nr"], categories=incorrect_ids, ordered=True)
    data = data.sort_values("Nr")

    feedbacks = format_feedback(data, unit, exercise)
    return feedbacks


def format_feedback(df, unit, exercise):
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

    Returns:
        list: A list of formatted feedback strings, one for each row in the DataFrame.
    """
    language = get_language(request, session)
    template = FEEDBACK[language][unit][exercise]
    result = []

    for _, row in df.iterrows():

        if is_exercise_multiple_choice(unit, exercise) is True:
            correct_answers = row.get(language, "")
        else:
            correct_answers = get_list_of_correct_answers(row.get("answer", ""), unit)

        formatted = template.format(
            previous_question=row.get("question", ""),
            correct_answer=row.get("answer", ""),
            correct_answers=correct_answers,
            german=row.get("german", ""),
            english=row.get("english", ""),
            french=row.get("french", ""),
            gender_english=row.get("gender_english", ""),
            gender_french=row.get("gender_french", ""),
            case_english=row.get("case_english", ""),
            case_french=row.get("case_french", ""),
            article_english=row.get("article_english", ""),
            article_french=row.get("article_french", ""),
            person=row.get("person", ""),
            prefix=row.get("prefix", ""),
            article=row.get("article", ""),
            adjective=row.get("adjective", ""),
            preposition=row.get("preposition", ""),
            explanation_english=row.get("explanation_english", ""),
            explanation_french=row.get("explanation_french", ""),
            root_german=row.get("root_german", ""),
            root_english=row.get("root_english", ""),
            root_french=row.get("root_french", ""),
        )
        result.append(formatted)
    return result
