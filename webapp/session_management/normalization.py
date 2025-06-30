import unicodedata

from data.data_processing.units import konnektoren
from data.data_processing.synonyms import search_for_main_synonym, SYNONYMS_PATH, get_list_of_synonyms


def is_user_answer_correct(user_answer, correct_answer, question, unit):
    synonym_units = [konnektoren]

    if user_answer == question and unit in synonym_units:
        return False

    user_answer = normalization(user_answer, unit)

    if "/" in correct_answer:
        correct_answers = correct_answer.split("/")
        correct_answers = [normalization(answer, unit) for answer in correct_answers]
        return user_answer in correct_answers
    else:
        correct_answer = normalization(correct_answer, unit)
        return user_answer == correct_answer


def normalization(input_str, unit):
    output = input_str.strip().lower()
    output = remove_comma(output)
    output = normalize_umlaut(output)
    output = search_for_main_synonym(output, unit)
    output = replace_sharp_s(output)
    return output


def replace_sharp_s(input_str):
    return input_str.replace("ß", "ss")


def remove_comma(input_str):
    return input_str.replace(",", "")


def normalize_umlaut(input_str):
    return unicodedata.normalize('NFC', input_str)


def get_list_of_correct_answers(answer, unit, file_path=SYNONYMS_PATH):

    if "/" in answer:
        answers = answer.split("/")
        answers = [normalization(answer, unit) for answer in answers]
        return ', '.join(answers)

    else:
        answer = lowercase_first_letter(answer)
        synonyms = get_list_of_synonyms(answer, unit, file_path=file_path)
        if not synonyms:
            return answer
        else:
            return f"{answer}, {synonyms}"


def lowercase_first_letter(s):
    if not s:
        return s
    return s[0].lower() + s[1:]