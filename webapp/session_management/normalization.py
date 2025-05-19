from data.data_processing.exercises import konnektoren
from data.data_processing.synonyms import search_for_main_synonym, SYNONYMS_PATH, get_list_of_synonyms


def is_equal(user_answer, correct_answer, question, exercise):
    synonym_exercises = [konnektoren]

    if user_answer == question and exercise in synonym_exercises:
        return False

    user_answer = normalization(user_answer, exercise)

    if "/" in correct_answer:
        correct_answers = correct_answer.split("/")
        correct_answers = [normalization(answer, exercise) for answer in correct_answers]
        return user_answer in correct_answers
    else:
        correct_answer = normalization(correct_answer, exercise)
        return user_answer == correct_answer


def normalization(input_str, exercise):
    output = input_str.strip().lower()
    output = replace_sharp_s(output)
    output = remove_comma(output)
    output = search_for_main_synonym(output, exercise)
    return output


def replace_sharp_s(input_str):
    return input_str.replace("ß", "ss")


def remove_comma(input_str):
    return input_str.replace(",", "")


def get_answers(answer, exercise, file_path=SYNONYMS_PATH):

    if "/" in answer:
        answers = answer.split("/")
        answers = [normalization(answer, exercise) for answer in answers]
        return ', '.join(answers)

    else:
        answer = lowercase_first_letter(answer)
        synonyms = get_list_of_synonyms(answer, exercise, file_path=file_path)
        if not synonyms:
            return answer
        else:
            return f"{answer}, {synonyms}"


def lowercase_first_letter(s):
    if not s:
        return s
    return s[0].lower() + s[1:]