from data.content.exercise.templates import FEEDBACK, QUESTION, INSTRUCTION, GUIDANCE, DESCRIPTION

from data.data_processing.units import konnektoren, adverbien, fragen, verben, trennbare_verben, adjektive, \
    adjektive_nomen_wortstaemme, adjektive_verben_wortstaemme, nomen_verben_wortstaemme, praepositionen_verben, \
    praepositionen_adjektive, praepositionen_nomen
from data.data_processing.exercises import is_exercise_multiple_choice, get_question_column, get_answer_column
from data.data_processing.data_loading import load_data_question, load_data_level, load_data_unit

from users.questions.normalization import get_correct_answer, get_list_of_correct_answers, get_first_correct_answer


def get_template(unit, exercise, language, template):
    if unit in template[language]['exercise'] and exercise in template[language]['exercise'][unit]:
        template = template[language]['exercise'][unit][exercise]
    elif unit in template[language]['unit']:
        template = template[language]['unit'][unit]
    else:
        template = None
    return template


def format_description(unit, exercise, language):
    description = get_template(unit, exercise, language, DESCRIPTION)
    return description


def format_guidance(unit, exercise, language):
    guidance = get_template(unit, exercise, language, GUIDANCE)
    return guidance


def format_instruction(unit, exercise, language):
    instruction = get_template(unit, exercise, language, INSTRUCTION)
    return instruction


def format_question(unit, exercise, language, question_id):
    if question_id is None:
        return None

    question_data = load_data_question(unit, exercise, question_id)

    question_text = str(question_data["question"])
    german = str(question_data.get("german", ""))
    english = str(question_data.get("english", ""))
    french = str(question_data.get("french", ""))
    gender_english = question_data.get("gender_english", "")
    gender_french = question_data.get("gender_french", "")
    case_english = question_data.get("case_english", "")
    case_french = question_data.get("case_french", "")
    article_english = question_data.get("article_english", "")
    article_french = question_data.get("article_french", "")
    person = question_data.get("person", "")
    prefix = question_data.get("prefix", "")
    article = question_data.get("article", "")
    adjective = question_data.get("adjective", "")
    preposition = question_data.get("preposition", "")
    explanation_english = question_data.get("explanation_english", "")
    explanation_french = question_data.get("explanation_french", "")
    root_german = question_data.get("root_german", "")
    root_english = question_data.get("root_english", "")
    root_french = question_data.get("root_french", "")

    question_template = get_template(unit, exercise, language, QUESTION)

    formatted_question = question_template.format(
        question=question_text,
        german=german,
        english=english,
        french=french,
        gender_english=gender_english,
        gender_french=gender_french,
        case_english=case_english,
        case_french=case_french,
        article_english=article_english,
        article_french=article_french,
        person=person,
        prefix=prefix,
        article=article,
        adjective=adjective,
        preposition=preposition,
        explanation_english=explanation_english,
        explanation_french=explanation_french,
        root_german=root_german,
        root_english=root_english,
        root_french=root_french,
        type=type,
    )

    formatted_question = formatted_question.replace("\u25CF ", "\u25CF&nbsp;")

    return formatted_question


def format_feedback(unit, exercise, language, question_id):
    if question_id is None:
        return None

    question_data = load_data_question(unit, exercise, question_id)

    correct_answer = get_correct_answer(unit, exercise, question_id, language)
    correct_answers = get_list_of_correct_answers(correct_answer, unit)
    first_correct_answer = get_first_correct_answer(correct_answer)
    question_text = question_data["question"]
    german = question_data.get("german", "")
    english = question_data.get("english", "")
    french = question_data.get("french", "")
    gender_english = question_data.get("gender_english", "")
    gender_french = question_data.get("gender_french", "")
    case_english = question_data.get("case_english", "")
    case_french = question_data.get("case_french", "")
    article_english = question_data.get("article_english", "")
    article_french = question_data.get("article_french", "")
    person = question_data.get("person", "")
    prefix = question_data.get("prefix", "")
    article = question_data.get("article", "")
    adjective = question_data.get("adjective", "")
    preposition = question_data.get("preposition", "")
    explanation_english = question_data.get("explanation_english", "")
    explanation_french = question_data.get("explanation_french", "")
    root_german = question_data.get("root_german", "")
    root_english = question_data.get("root_english", "")
    root_french = question_data.get("root_french", "")

    feedback_template = get_template(unit, exercise, language, FEEDBACK)

    feedback_message = feedback_template.format(
        previous_question=question_text,
        correct_answer=correct_answer,
        correct_answers=correct_answers,
        first_correct_answer=first_correct_answer,
        # user_answer=user_answer,
        german=german,
        english=english,
        french=french,
        gender_english=gender_english,
        gender_french=gender_french,
        case_english=case_english,
        case_french=case_french,
        article_english=article_english,
        article_french=article_french,
        person=person,
        prefix=prefix,
        article=article,
        adjective=adjective,
        preposition=preposition,
        explanation_english=explanation_english,
        explanation_french=explanation_french,
        root_german=root_german,
        root_english=root_english,
        root_french=root_french,
        type=type,
    )

    feedback_message = feedback_message.replace("→ ", "→&nbsp;")
    feedback_message = feedback_message.replace("= ", "=&nbsp;")
    feedback_message = feedback_message.replace("+ ", "+&nbsp;")
    feedback_message = feedback_message.replace("\u25CF ", "\u25CF&nbsp;")

    return feedback_message


def format_gender(unit, exercise, language, question_id):
    question_data = load_data_question(unit, exercise, question_id)
    gender_english = question_data.get("gender_english", "")
    gender_french = question_data.get("gender_french", "")

    gender = gender_english if language == 'english' else gender_french
    return gender


def format_correction(unit, exercise, language, result, incorrect_answer, question_text):
    if result != "incorrect":
        return ""

    if is_exercise_multiple_choice(unit, exercise) is True:
        data = load_data_level(unit, exercise)

        question_column = get_question_column(unit, exercise, language)
        answer_column = get_answer_column(unit, exercise, language)

        match = data.loc[data[answer_column] == incorrect_answer, question_column]

        if not match.empty:
            question = match.iloc[0]
            return f"<br><br>{incorrect_answer} = {question}"
        else:
            return None

    elif unit == konnektoren:
        data = load_data_unit(unit)
        match = data.loc[data['konnektor'] == incorrect_answer, f"explanation_{language}"]

        if not match.empty:
            return f"<br><br>{match.iloc[0]}"
        else:
            return ""

    elif unit == fragen:
        data = load_data_unit(unit)
        match = data.loc[data['fragen'] == incorrect_answer, f"explanation_{language}"]

        if not match.empty:
            return f"<br><br>{match.iloc[0]}"
        else:
            return ""

    elif unit in [adverbien, verben, trennbare_verben, adjektive,
                  adjektive_nomen_wortstaemme, adjektive_verben_wortstaemme, nomen_verben_wortstaemme]:

        data = load_data_unit(unit)
        match = data.loc[data['answer'] == incorrect_answer, language]

        if not match.empty:
            question = match.iloc[0]
            return f"<br><br>{incorrect_answer} = {question}"
        else:
            return ""


    else:
        return ""

'''
    elif unit in [praepositionen_verben, praepositionen_adjektive, praepositionen_nomen]:
        if question_text == "":
            return ""

        data = load_data_unit(unit)
        combination = get_combination_from_question_text(unit, question_text, incorrect_answer)

        match_explanation = data.loc[data["combination"] == combination, f"explanation_{language}"]
        if match_explanation.empty:
            return ""

        else:
            match_explanation = match_explanation.iloc[0]
            return f"<br><br><i>{match_explanation}</i>"
'''

def get_combination_from_question_text(unit, question_text, incorrect_answer):
    if not question_text:
        return None

    data = load_data_unit(unit)

    matches = data.loc[data["question"] == question_text, "combination"]

    if matches.empty:
        return ""

    correct_combination = matches.iloc[0]

    correct_question_text = data.loc[data["combination"] == correct_combination, f"question"].iloc[0]
    combination = correct_question_text.replace("_____", incorrect_answer)

    return combination
