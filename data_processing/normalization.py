import os
import pandas as pd

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SYNONYMS_PATH = os.path.join(BASE_DIR, "datasets/other", "synonyms.csv")


def is_equal(user_answer, correct_answer, question, exercise):
    if user_answer == question:
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
    output = search_for_synonyms(output, exercise)
    return output


def replace_sharp_s(input_str):
    return input_str.replace("ß", "ss")


def search_for_synonyms(input_str, exercise, csv_file=SYNONYMS_PATH):
    df = pd.read_csv(csv_file)
    df = df[df['exercise'] == exercise]  # Filter by exercise
    mapping = dict(zip(df["input"], df["output"]))
    return mapping.get(input_str, input_str)


def get_answers(answer, exercise, file_path=SYNONYMS_PATH):

    if "/" in answer:
        answers = answer.split("/")
        answers = [normalization(answer, exercise) for answer in answers]
        return ', '.join(answers)

    else:
        answer = lowercase_first_letter(answer)
        synonyms = get_synonyms(answer, exercise, file_path=file_path)
        if not synonyms:
            return answer
        else:
            return f"{answer}, {synonyms}"


def get_synonyms(answer, exercise, file_path=SYNONYMS_PATH):
    df = pd.read_csv(file_path)
    filtered = df[(df['exercise'] == exercise) & (df['output'] == answer)]
    synonyms = ', '.join(filtered['input'])
    return synonyms


def lowercase_first_letter(s):
    if not s:
        return s
    return s[0].lower() + s[1:]