import unicodedata

from flask import session, request

from data.data_processing.units import konnektoren
from data.data_processing.synonyms import search_for_main_synonym, SYNONYMS_PATH, get_list_of_synonyms_for_feedback
from data.data_processing.data_loading import load_data_exercise, is_exercise_multiple_choice, get_answer_column

from webapp.i18n import get_language


def get_correct_answer(unit, exercise, question_data):
    language = get_language(request, session)

    if is_exercise_multiple_choice(unit, exercise) and get_answer_column(unit, exercise) == "foreign":
        return question_data.get(language, "")
    else:
        return question_data.get("answer", "")


def is_user_answer_correct(user_answer, correct_answer, question, unit):
    """
    Determines whether the user's answer is correct, with optional support for multiple correct answers
    and unit-specific normalization and synonym handling.

    If the user's answer exactly matches the question text and the unit is in 'synonym_units',
    it is automatically marked incorrect (to avoid echoing the prompt as an answer).

    The user's answer and correct answer(s) are normalized using a unit-specific function.
    If multiple correct answers are provided (separated by '/'), the function checks if
    the normalized user answer matches any of them.

    Args:
        user_answer (str): The answer submitted by the user.
        correct_answer (str): The correct answer string, possibly with multiple options separated by '/'.
        question (str): The original question prompt, used to detect echoing.
        unit (str): The unit name, used for normalization and synonym-specific logic.

    Returns:
        bool: True if the answer is correct, False otherwise.
    """
    synonym_units = [konnektoren]

    if user_answer == question and unit in synonym_units:
        return False

    user_answer = normalize_answer(user_answer, unit)

    if "/" in correct_answer:
        correct_answers = correct_answer.split("/")
        correct_answers = [normalize_answer(answer, unit) for answer in correct_answers]
        return user_answer in correct_answers
    else:
        correct_answer = normalize_answer(correct_answer, unit)
        return user_answer == correct_answer


def normalize_answer(input_str, unit):
    """
    Normalizes the input string for comparison by applying a series of standard transformations.

    The process includes:
    - Stripping whitespace and converting to lowercase.
    - Removing commas.
    - Converting German umlauts to their normalized forms.
    - Replacing synonyms with their main form based on the unit.
    - Replacing the German sharp 'ß' with 'ss'.

    Args:
        input_str (str): The raw input string to normalize.
        unit (str): The unit name used to select the appropriate synonym mapping.

    Returns:
        str: The fully normalized version of the input string.
    """
    normalized_str = input_str.strip().lower()
    normalized_str = remove_comma(normalized_str)
    normalized_str = normalize_umlaut(normalized_str)
    normalized_str = search_for_main_synonym(normalized_str, unit)
    normalized_str = replace_sharp_s(normalized_str)
    return normalized_str


def replace_sharp_s(input_str):
    """
    Replaces the German sharp 'ß' character with 'ss' in the input string.

    Args:
        input_str (str): The string in which to replace 'ß'.

    Returns:
        str: The string with all 'ß' characters replaced by 'ss'.
    """
    return input_str.replace("ß", "ss")


def remove_comma(input_str):
    """
    Removes all commas from the input string.

    Args:
        input_str (str): The string to clean.

    Returns:
        str: The string without any commas.
    """
    return input_str.replace(",", "")


def normalize_umlaut(input_str):
    """
    Applies Unicode normalization (NFC) to the input string to standardize characters,
    including composed forms of umlauts (e.g., 'ä', 'ö', 'ü').

    This ensures consistent representation of accented characters for accurate comparison.

    Args:
        input_str (str): The string to normalize.

    Returns:
        str: The normalized string.
    """
    return unicodedata.normalize('NFC', input_str)


def get_list_of_correct_answers(correct_answer, unit, file_path=SYNONYMS_PATH):
    """
    Returns a comma-separated list of all valid correct answers for a given input.

    If multiple correct answers are provided (separated by '/'), each is normalized
    and returned as a comma-separated string.

    If there's a single correct answer, it is cleaned by lowercasing the first letter,
    and any synonyms for it (based on the unit) are appended to the string.

    Args:
        correct_answer (str): The expected answer or list of acceptable answers separated by '/'.
        unit (str): The unit used to retrieve the appropriate synonym mappings.
        file_path (str): Path to the synonyms CSV file (default is SYNONYMS_PATH).

    Returns:
        str: A comma-separated list of valid correct answers and synonyms.
    """
    if "/" in correct_answer:
        answers = correct_answer.split("/")
        answers = [normalize_answer(answer, unit) for answer in answers]
        return ', '.join(answers)

    else:
        correct_answer = lowercase_first_letter(correct_answer)
        synonyms = get_list_of_synonyms_for_feedback(correct_answer, unit, file_path=file_path)
        if not synonyms:
            return correct_answer
        else:
            return f"{correct_answer}, {synonyms}"


def lowercase_first_letter(s):
    """
    Converts the first character of the string to lowercase, if the string is not empty.

    Args:
        s (str): The input string.

    Returns:
        str: The string with its first letter lowercased, or the original string if empty.
    """
    if not s:
        return s
    return s[0].lower() + s[1:]