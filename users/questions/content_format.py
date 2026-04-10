from flask import request, session

from data.data_processing.data_loading import load_data_question, load_data_level, load_data_unit
from data.content.exercise.content_exercises import FEEDBACK, QUESTION, INSTRUCTION, GUIDANCE_EXERCISE
from data.content.unit.unit_content_by_language import GUIDANCE_UNIT
from data.data_processing.exercise_type import is_exercise_multiple_choice, get_question_column
from data.data_processing.units import konnektoren, adverbien, fragen, verben, trennbare_verben, adjektive, \
    adjektive_nomen_wortstaemme, adjektive_verben_wortstaemme, nomen_verben_wortstaemme, praepositionen_verben, \
    praepositionen_adjektive, praepositionen_nomen

from users.questions.normalization import get_correct_answer, get_list_of_correct_answers, get_first_correct_answer
from webapp.i18n import get_language


def get_guidance(unit, exercise, language):
    if unit in GUIDANCE_EXERCISE[language] and exercise in GUIDANCE_EXERCISE[language][unit]:
        guidance = GUIDANCE_EXERCISE[language][unit][exercise]
    elif unit in GUIDANCE_UNIT[language]:
        guidance = GUIDANCE_UNIT[language][unit]
    else:
        guidance = None
    return guidance


def format_instruction(unit, exercise, language):
    instruction = INSTRUCTION[language].get(unit, {}).get(exercise, "Translate the following word:")
    return instruction


def format_question(unit, exercise, language, question_ID):
    if question_ID is None:
        return None

    question_data = load_data_question(unit, exercise, question_ID)

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
    type = question_data.get("type", "")

    formatted_question = QUESTION[language].get(unit, {}).get(exercise, "{question}").format(
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


def format_feedback(unit, exercise, language, question_ID):
    if question_ID is None:
        return None

    question_data = load_data_question(unit, exercise, question_ID)

    correct_answer = get_correct_answer(unit, exercise, question_ID, language)
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
    type = question_data.get("type", "")

    feedback_template = FEEDBACK[language].get(unit, {}).get(exercise, "{previous_question} = {correct_answer}")
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


def get_gender(unit, exercise, language, question_ID):
    question_data = load_data_question(unit, exercise, question_ID)
    gender_english = question_data.get("gender_english", "")
    gender_french = question_data.get("gender_french", "")

    gender = gender_english if language == 'english' else gender_french
    return gender


def get_question_from_incorrect_answer(unit, exercise, result, incorrect_answer, question_text):

    if result != "incorrect":
        return ""

    elif is_exercise_multiple_choice(unit, exercise) is True:
        data = load_data_level(unit, exercise)
        language = get_language(request, session)

        if get_question_column(unit, exercise) == "foreign":
            match = data.loc[data['answer'] == incorrect_answer, language]

        else:
            match = data.loc[data[language] == incorrect_answer, 'question']

        if not match.empty:
            question = match.iloc[0]
            return f"<br><br>{incorrect_answer} = {question}"
        else:
            return None

    elif unit in [konnektoren, adverbien, fragen, verben, trennbare_verben, adjektive,
                  adjektive_nomen_wortstaemme, adjektive_verben_wortstaemme, nomen_verben_wortstaemme]:
        data = load_data_unit(unit)
        language = get_language(request, session)

        match = data.loc[data['answer'] == incorrect_answer, language]

        if not match.empty:
            question = match.iloc[0]
            return f"<br><br>{incorrect_answer} = {question}"
        else:
            return ""

    elif unit in [praepositionen_verben, praepositionen_adjektive, praepositionen_nomen]:
        if question_text == "":
            return ""

        data = load_data_unit(unit)
        language = get_language(request, session)

        combination = get_combination_from_question_text(unit, question_text, incorrect_answer)

        match_explanation = data.loc[data["combination"] == combination, f"explanation_{language}"]
        if match_explanation.empty:
            return ""

        else:
            match_explanation = match_explanation.iloc[0]
            return f"<br><br><i>{match_explanation}</i>"

    else:
        return ""


def get_combination_from_question_text(unit, question_text, incorrect_answer):
    data = load_data_unit(unit)

    print('question_text', question_text)
    print('incorrect_answer', incorrect_answer)

    correct_combination = data.loc[data["question"] == question_text, f"combination"].iloc[0]
    correct_question_text = data.loc[data["combination"] == correct_combination, f"question"].iloc[0]
    combination = correct_question_text.replace("_____", incorrect_answer)

    return combination
