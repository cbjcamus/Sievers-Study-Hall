import pandas as pd

from data.data_processing.data_loading import load_data

from webapp.content.exercise.feedbacks import FEEDBACK
from webapp.session_management.normalization import get_list_of_correct_answers

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
    if 'falses' in session[unit][str(exercise)]:
        incorrect_ids = session[unit][str(exercise)]['falses']
        incorrect_ids = [int(i) for i in incorrect_ids]
    else:
        incorrect_ids = []

    data = load_data(unit, exercise)
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
    template = FEEDBACK[unit][exercise]
    result = []
    for _, row in df.iterrows():
        formatted = template.format(
            previous_question=row.get("question", ""),
            correct_answers=get_list_of_correct_answers(row.get("answer", ""), unit),
            english=row.get("english", ""),
            german=row.get("german", ""),
            adjective=row.get("adjective", ""),
            gender=row.get("gender", ""),
            case=row.get("case", ""),
            article=row.get("article", ""),
            person=row.get("person", ""),
            prefix=row.get("prefix", ""),
            explanation=row.get("explanation", "")
        )
        result.append(formatted)
    return result
