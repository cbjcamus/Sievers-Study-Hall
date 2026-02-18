from flask import render_template, session, request, redirect, url_for, flash, jsonify
from flask_login import current_user
from typing import cast

from . import routes_bp

from data.data_processing.levels import get_level_from_exercise
from data.data_processing.proverbs import get_text_proverb
from data.data_processing.data_loading import load_data_exercise
from data.data_processing.exercise_type import is_exercise_multiple_choice
from data.data_processing.total_questions import total_question_exercises, highest_exercise

from users.users.models import db, is_feedback_enabled, Bookmark, get_filename_full_bookmark, \
    get_filename_empty_bookmark
from users.progress.models import UserExerciseState

from users.progress.score import write_score
from users.progress.progress import compute_answered_questions, update_progress_in_session, get_next_exercise
from users.progress.register_update import register_progress, register_result, register_incorrect_answer
from users.progress.feedback_exercise_completed import get_feedback_exercise, get_incorrect_answers

from users.questions.normalization import get_correct_answer, get_list_of_correct_answers, is_user_answer_correct, \
    get_first_correct_answer
from users.questions.pick_a_question import (pick_a_question, is_exercise_finished, get_question_from_incorrect_answer,
                                             get_options_for_multiple_choice_exercises)
from users.session_management.logging import log_question_flagged
from users.session_management.verification_session import init_session_key, is_key_in_session

from webapp.i18n import get_language

from webapp.content.application.buttons import (BACK_TO, NEXT, NEXT_QUESTION, SUBMIT, REFRESH, NEXT_EXERCISE)
from webapp.content.application.text import YOUR_ANSWER, YOUR_INCORRECT_ANSWERS, FEEDBACK_LAST_QUESTION, \
    YOUR_SCORE_FOR_THIS_EXERCISE, ALL_QUESTIONS_SUCCESSFULLY_ANSWERED, EXERCISE_TITLE, ENTER_ANSWER_HERE, \
    ADDITIONAL_HELP, CONSULT_FAQ, NOT_AUTHENTICATED
from webapp.content.application.popup import get_popup_title, get_popup_text

from ..content.unit.unit_content_by_language import GUIDANCE_UNIT
from webapp.content.unit.unit_page import UNIT_PAGE
from webapp.content.unit.title_page import TITLE_PAGE
from webapp.content.unit.back_button import BACK_BUTTON
from webapp.content.exercise.content_exercises import FEEDBACK, QUESTION, INSTRUCTION, GUIDANCE_EXERCISE

session = cast(dict, session)


@routes_bp.route('/guidance/unit/<unit>/exercise/<int:exercise>')
def guidance(unit, exercise):

    language = get_language(request, session)

    if is_exercise_finished(session, unit, exercise) is True:
        feedback = session.pop("feedback", None) or {}
        result = feedback.get("result")
        feedback_message = feedback.get("feedback_message")
        user_answer = feedback.get("user_answer")
        previous_question = feedback.get("previous_question")

        number_of_incorrect_answers = 0
        incorrect_answers = []
        feedbacks = []

        register_result(session, unit, exercise, feedback)

        if current_user.is_authenticated:
            update_progress_in_session(session, unit)

        next_exercise = get_next_exercise(unit, exercise, highest_exercise)
        next_exercise_text = NEXT_EXERCISE[language]

        current_user_not_authenticated = not current_user.is_authenticated

        return render_template("exercise/exercise_completed.html",
                               unit=unit,
                               exercise=exercise,
                               exercise_title=EXERCISE_TITLE[language],
                               score=write_score,
                               unit_page=UNIT_PAGE,
                               title_page=TITLE_PAGE,
                               back_page=BACK_BUTTON,
                               is_feedback_box=True,
                               result=result,
                               feedback_message=feedback_message,
                               user_answer=user_answer,
                               previous_question=previous_question,
                               number_of_incorrect_answers=number_of_incorrect_answers,
                               incorrect_answers=incorrect_answers,
                               feedbacks=feedbacks,
                               all_questions_successfully_answered=ALL_QUESTIONS_SUCCESSFULLY_ANSWERED[language],
                               your_score_for_this_exercise=YOUR_SCORE_FOR_THIS_EXERCISE[language],
                               feedback_last_question=FEEDBACK_LAST_QUESTION[language],
                               your_incorrect_answers=YOUR_INCORRECT_ANSWERS[language],
                               get_question_from_incorrect_answer=get_question_from_incorrect_answer,
                               your_answer=YOUR_ANSWER[language],
                               refresh=REFRESH[language],
                               back_to=BACK_TO[language],
                               icon_full=get_filename_full_bookmark(),
                               icon_empty=get_filename_empty_bookmark(),
                               next_exercise=next_exercise,
                               next_exercise_text=next_exercise_text,
                               current_user_not_authenticated=current_user_not_authenticated,
                               not_authenticated_text=NOT_AUTHENTICATED[language],
                               )

    elif unit in GUIDANCE_EXERCISE[language] and exercise in GUIDANCE_EXERCISE[language][unit]:
        guidance = GUIDANCE_EXERCISE[language][unit][exercise]
        return render_template("exercise/guidance.html",
                               unit=unit,
                               exercise=exercise,
                               exercise_title=EXERCISE_TITLE[language],
                               guidance=guidance,
                               additional_help=ADDITIONAL_HELP[language],
                               consult_faq=CONSULT_FAQ[language],
                               unit_page=UNIT_PAGE,
                               title_page=TITLE_PAGE,
                               back_page=BACK_BUTTON,
                               answered_questions=compute_answered_questions(session, unit, exercise=exercise),
                               total_questions=total_question_exercises[unit][exercise],
                               next=NEXT[language],
                               back_to=BACK_TO[language],
                               )

    elif unit in GUIDANCE_UNIT[language]:
        guidance = GUIDANCE_UNIT[language][unit]
        return render_template("exercise/guidance.html",
                               unit=unit,
                               exercise=exercise,
                               exercise_title=EXERCISE_TITLE[language],
                               guidance=guidance,
                               additional_help=ADDITIONAL_HELP[language],
                               consult_faq=CONSULT_FAQ[language],
                               unit_page=UNIT_PAGE,
                               title_page=TITLE_PAGE,
                               back_page=BACK_BUTTON,
                               answered_questions=compute_answered_questions(session, unit, exercise=exercise),
                               total_questions=total_question_exercises[unit][exercise],
                               next=NEXT[language],
                               back_to=BACK_TO[language],
                               )

    else:
        return redirect(url_for('routes.exercise',
                                unit=unit,
                                exercise=exercise))


@routes_bp.route('/unit/<unit>/exercise/<int:exercise>')
def exercise(unit, exercise):

    language = get_language(request, session)

    if is_exercise_finished(session, unit, exercise) is True:
        feedback = session.pop("feedback", None) or {}
        result = feedback.get("result")
        feedback_message = feedback.get("feedback_message")
        user_answer = feedback.get("user_answer")
        previous_question = feedback.get("previous_question")

        if current_user.is_authenticated:
            incorrect_answers, number_of_incorrect_answers = get_incorrect_answers(session, unit, exercise)
            feedbacks = get_feedback_exercise(session, unit, exercise)
            incorrect_questions = [get_question_from_incorrect_answer(unit, exercise, 'incorrect', incorrect_answer, "")
                                   for incorrect_answer in incorrect_answers]
        else:
            number_of_incorrect_answers = 0
            incorrect_answers = []
            feedbacks = []
            incorrect_questions = []

        register_result(session, unit, exercise, feedback)

        if current_user.is_authenticated:
            update_progress_in_session(session, unit)

        next_exercise = get_next_exercise(unit, exercise, highest_exercise)
        next_exercise_text = NEXT_EXERCISE[language]

        current_user_not_authenticated = not current_user.is_authenticated

        return render_template("exercise/exercise_completed.html",
                               unit=unit,
                               exercise=exercise,
                               exercise_title=EXERCISE_TITLE[language],
                               score=write_score,
                               unit_page=UNIT_PAGE,
                               title_page=TITLE_PAGE,
                               back_page=BACK_BUTTON,
                               is_feedback_box=True,
                               result=result,
                               feedback_message=feedback_message,
                               user_answer=user_answer,
                               previous_question=previous_question,
                               number_of_incorrect_answers=number_of_incorrect_answers,
                               incorrect_answers=incorrect_answers,
                               feedbacks=feedbacks,
                               all_questions_successfully_answered=ALL_QUESTIONS_SUCCESSFULLY_ANSWERED[language],
                               your_score_for_this_exercise=YOUR_SCORE_FOR_THIS_EXERCISE[language],
                               feedback_last_question=FEEDBACK_LAST_QUESTION[language],
                               your_incorrect_answers=YOUR_INCORRECT_ANSWERS[language],
                               get_question_from_incorrect_answer=get_question_from_incorrect_answer,
                               your_answer=YOUR_ANSWER[language],
                               incorrect_questions=incorrect_questions,
                               refresh=REFRESH[language],
                               back_to=BACK_TO[language],
                               icon_full=get_filename_full_bookmark(),
                               icon_empty=get_filename_empty_bookmark(),
                               next_exercise=next_exercise,
                               next_exercise_text=next_exercise_text,
                               current_user_not_authenticated=current_user_not_authenticated,
                               not_authenticated_text=NOT_AUTHENTICATED[language],
                               )

    question_data = pick_a_question(session, unit, exercise)

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

    instruction = INSTRUCTION[language].get(unit, {}).get(exercise, "Translate the following word:")

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

    feedback = session.pop("feedback", None) or {}
    result = feedback.get("result")
    feedback_message = feedback.get("feedback_message")
    user_answer = feedback.get("user_answer")
    previous_question = feedback.get("previous_question")

    proverb = get_text_proverb()

    is_feedback_box = not is_feedback_enabled()

    incorrect_question = get_question_from_incorrect_answer(unit, exercise, result, user_answer, previous_question)

    gender = gender_english if get_language(request, session) == 'english' else gender_french

    if unit in GUIDANCE_EXERCISE[language] and exercise in GUIDANCE_EXERCISE[language][unit]:
        guidance_popup = GUIDANCE_EXERCISE[language][unit][exercise]
    elif unit in GUIDANCE_UNIT[language]:
        guidance_popup = GUIDANCE_UNIT[language][unit]
    else:
        guidance_popup = ""

    if is_key_in_session(session, 'popup') and not current_user.is_authenticated:
        clearance_popup_title = get_popup_title(session['popup']['unit'], session['popup']['exercise'])
        clearance_popup_text = get_popup_text(session['popup']['unit'], session['popup']['exercise'])
    else:
        clearance_popup_title = None
        clearance_popup_text = None

    if is_exercise_multiple_choice(unit, exercise) is True:

        options_text = get_options_for_multiple_choice_exercises(unit, exercise, question_data)

        return render_template("exercise/exercise_multiple_choice.html",
                               unit=unit,
                               exercise=exercise,
                               exercise_title=EXERCISE_TITLE[language],
                               question_text=formatted_question,
                               instruction_text=instruction,
                               nr=question_data["Nr"],
                               result=result,
                               feedback_message=feedback_message,
                               user_answer=user_answer,
                               unit_page=UNIT_PAGE,
                               title_page=TITLE_PAGE,
                               back_page=BACK_BUTTON,
                               answered_questions=compute_answered_questions(session, unit, exercise=exercise),
                               total_questions=total_question_exercises[unit][exercise],
                               proverb=proverb,
                               is_feedback_box=is_feedback_box,
                               gender=gender,
                               guidance=guidance_popup,
                               additional_help=ADDITIONAL_HELP[language],
                               consult_faq=CONSULT_FAQ[language],
                               options=options_text,
                               your_answer=YOUR_ANSWER[language],
                               incorrect_question=incorrect_question,
                               back_to=BACK_TO[language],
                               current_user=current_user,
                               icon_full=get_filename_full_bookmark(),
                               icon_empty=get_filename_empty_bookmark(),
                               clearance_popup_title=clearance_popup_title,
                               clearance_popup_text=clearance_popup_text,
                               )

    return render_template("exercise/exercise_input.html",
                           unit=unit,
                           exercise=exercise,
                           exercise_title=EXERCISE_TITLE[language],
                           question_text=formatted_question,
                           instruction_text=instruction,
                           nr=question_data["Nr"],
                           result=result,
                           feedback_message=feedback_message,
                           user_answer=user_answer,
                           unit_page=UNIT_PAGE,
                           title_page=TITLE_PAGE,
                           back_page=BACK_BUTTON,
                           answered_questions=compute_answered_questions(session, unit, exercise=exercise),
                           total_questions=total_question_exercises[unit][exercise],
                           proverb=proverb,
                           is_feedback_box=is_feedback_box,
                           gender=gender,
                           guidance=guidance_popup,
                           additional_help=ADDITIONAL_HELP[language],
                           consult_faq=CONSULT_FAQ[language],
                           your_answer=YOUR_ANSWER[language],
                           incorrect_question=incorrect_question,
                           submit=SUBMIT[language],
                           enter_answer_here=ENTER_ANSWER_HERE[language],
                           back_to=BACK_TO[language],
                           current_user=current_user,
                           icon_full=get_filename_full_bookmark(),
                           icon_empty=get_filename_empty_bookmark(),
                           clearance_popup_title=clearance_popup_title,
                           clearance_popup_text=clearance_popup_text,
                           )


@routes_bp.route('/check/<unit>/exercise/<int:exercise>', methods=['POST', 'GET'])
def check_answer(unit, exercise):

    language = get_language(request, session)

    init_session_key(session, unit, exercise, 'progress')
    init_session_key(session, unit, exercise, 'falses')

    if request.method == 'GET':
        return redirect(url_for('routes.exercise', unit=unit, exercise=exercise))

    user_answer = request.form.get('answer', '')
    nr = request.form.get('nr')

    data = load_data_exercise(unit, exercise)

    question_data = data[data["Nr"] == int(nr)].iloc[0]# .fillna("")
    correct_answer = get_correct_answer(unit, exercise, question_data)
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
        user_answer=user_answer,
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

    is_answer_correct = is_user_answer_correct(user_answer, correct_answer, question_text, unit, exercise)

    if is_answer_correct:
        register_progress(session, unit, exercise, nr)
    elif nr not in session[unit][str(exercise)]['falses']:
        register_incorrect_answer(session, unit, exercise, nr, user_answer)

    session.modified = True

    session["feedback"] = {
        "result": "correct" if is_answer_correct else "incorrect",
        "feedback_message": feedback_message,
        "user_answer": user_answer,
        "previous_question": question_text,
    }

    session[f"question_data"] = question_data.to_dict()

    if is_feedback_enabled():
        return redirect(url_for('routes.exercise_feedback',
                                unit=unit,
                                exercise=exercise))
    else:
        return redirect(url_for('routes.exercise',
                                unit=unit,
                                exercise=exercise))


@routes_bp.route('/feedback/unit/<unit>/exercise/<int:exercise>')
def exercise_feedback(unit, exercise):

    language = get_language(request, session)

    if is_exercise_finished(session, unit, exercise) is True:
        feedback = session.pop("feedback", None) or {}
        result = feedback.get("result")
        feedback_message = feedback.get("feedback_message")
        user_answer = feedback.get("user_answer")
        previous_question = feedback.get("previous_question")

        if current_user.is_authenticated:
            incorrect_answers, number_of_incorrect_answers = get_incorrect_answers(session, unit, exercise)
            feedbacks = get_feedback_exercise(session, unit, exercise)
            incorrect_questions = [get_question_from_incorrect_answer(unit, exercise, result, incorrect_answer, "")
                                   for incorrect_answer in incorrect_answers]
        else:
            number_of_incorrect_answers = 0
            incorrect_answers = []
            feedbacks = []
            incorrect_questions = []

        register_result(session, unit, exercise, feedback)

        if current_user.is_authenticated:
            update_progress_in_session(session, unit)

        next_exercise = get_next_exercise(unit, exercise, highest_exercise)
        next_exercise_text = NEXT_EXERCISE[language]

        current_user_not_authenticated = not current_user.is_authenticated

        return render_template("exercise/exercise_completed.html",
                               unit=unit,
                               exercise=exercise,
                               exercise_title=EXERCISE_TITLE[language],
                               score=write_score,
                               unit_page=UNIT_PAGE,
                               title_page=TITLE_PAGE,
                               back_page=BACK_BUTTON,
                               is_feedback_box=True,
                               result=result,
                               feedback_message=feedback_message,
                               user_answer=user_answer,
                               previous_question=previous_question,
                               number_of_incorrect_answers=number_of_incorrect_answers,
                               your_answer=YOUR_ANSWER[language],
                               incorrect_answers=incorrect_answers,
                               feedbacks=feedbacks,
                               all_questions_successfully_answered=ALL_QUESTIONS_SUCCESSFULLY_ANSWERED[language],
                               your_score_for_this_exercise=YOUR_SCORE_FOR_THIS_EXERCISE[language],
                               feedback_last_question=FEEDBACK_LAST_QUESTION[language],
                               get_question_from_incorrect_answer=get_question_from_incorrect_answer,
                               your_incorrect_answers=YOUR_INCORRECT_ANSWERS[language],
                               incorrect_questions=incorrect_questions,
                               refresh=REFRESH[language],
                               back_to=BACK_TO[language],
                               icon_full=get_filename_full_bookmark(),
                               icon_empty=get_filename_empty_bookmark(),
                               next_exercise=next_exercise,
                               next_exercise_text=next_exercise_text,
                               current_user_not_authenticated=current_user_not_authenticated,
                               not_authenticated_text=NOT_AUTHENTICATED[language],
                               )

    question_data = session.get(f"question_data", {})

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

    instruction = INSTRUCTION[language].get(unit, {}).get(exercise, "Translate the following word:")

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

    feedback = session.pop("feedback", None) or {}
    result = feedback.get("result")
    feedback_message = feedback.get("feedback_message")
    user_answer = feedback.get("user_answer")
    previous_question = feedback.get("previous_question")

    proverb = get_text_proverb()

    is_feedback_box = True

    incorrect_question = get_question_from_incorrect_answer(unit, exercise, result, user_answer, previous_question)

    if unit in GUIDANCE_EXERCISE[language] and exercise in GUIDANCE_EXERCISE[language][unit]:
        guidance_popup = GUIDANCE_EXERCISE[language][unit][exercise]
    elif unit in GUIDANCE_UNIT[language]:
        guidance_popup = GUIDANCE_UNIT[language][unit]
    else:
        guidance_popup = ""

    if is_key_in_session(session, 'popup') and not current_user.is_authenticated:
        clearance_popup_title = get_popup_title(session['popup']['unit'], session['popup']['exercise'])
        clearance_popup_text = get_popup_text(session['popup']['unit'], session['popup']['exercise'])
    else:
        clearance_popup_title = None
        clearance_popup_text = None

    if is_exercise_multiple_choice(unit, exercise) is True:

        return render_template("exercise/feedback_multiple_choice.html",
                               unit=unit,
                               exercise=exercise,
                               exercise_title=EXERCISE_TITLE[language],
                               question_text=formatted_question,
                               instruction_text=instruction,
                               nr=question_data["Nr"],
                               result=result,
                               feedback_message=feedback_message,
                               user_answer=user_answer,
                               unit_page=UNIT_PAGE,
                               title_page=TITLE_PAGE,
                               back_page=BACK_BUTTON,
                               answered_questions=compute_answered_questions(session, unit, exercise=exercise),
                               total_questions=total_question_exercises[unit][exercise],
                               proverb=proverb,
                               guidance=guidance_popup,
                               additional_help=ADDITIONAL_HELP[language],
                               consult_faq=CONSULT_FAQ[language],
                               is_feedback_box=is_feedback_box,
                               your_answer=YOUR_ANSWER[language],
                               incorrect_question=incorrect_question,
                               next_question=NEXT_QUESTION[language],
                               back_to=BACK_TO[language],
                               icon_full=get_filename_full_bookmark(),
                               icon_empty=get_filename_empty_bookmark(),
                               clearance_popup_title=clearance_popup_title,
                               clearance_popup_text=clearance_popup_text,
                               )

    return render_template("exercise/feedback_input.html",
                           unit=unit,
                           exercise=exercise,
                           exercise_title=EXERCISE_TITLE[language],
                           question_text=formatted_question,
                           instruction_text=instruction,
                           nr=question_data["Nr"],
                           result=result,
                           feedback_message=feedback_message,
                           user_answer=user_answer,
                           unit_page=UNIT_PAGE,
                           title_page=TITLE_PAGE,
                           back_page=BACK_BUTTON,
                           answered_questions=compute_answered_questions(session, unit, exercise=exercise),
                           total_questions=total_question_exercises[unit][exercise],
                           proverb=proverb,
                           guidance=guidance_popup,
                           additional_help=ADDITIONAL_HELP[language],
                           consult_faq=CONSULT_FAQ[language],
                           is_feedback_box=is_feedback_box,
                           your_answer=YOUR_ANSWER[language],
                           incorrect_question=incorrect_question,
                           next_question=NEXT_QUESTION[language],
                           back_to=BACK_TO[language],
                           icon_full=get_filename_full_bookmark(),
                           icon_empty=get_filename_empty_bookmark(),
                           clearance_popup_title=clearance_popup_title,
                           clearance_popup_text=clearance_popup_text,
                           )


@routes_bp.route('/reset/<unit>/exercise/<int:exercise>', methods=['POST'])
def reset_exercise(unit, exercise):
    """Clears progress for a specific unit exercise and removes any stored feedback."""

    if current_user.is_authenticated:
        row = UserExerciseState.query.filter_by(
            user_id=current_user.id, unit=unit, exercise=int(exercise)
        ).first()
        if row:
            # Remove any stored result and JSON state by deleting the row
            db.session.delete(row)
            db.session.commit()

        update_progress_in_session(session, unit)

    else:
        unit_dict = session.get(unit, {})
        unit_dict.pop(str(exercise), None)
        session[unit] = unit_dict

        if (unit, exercise) in session['unfinished_exercise']:
            session['unfinished_exercise'].remove((unit, exercise))

        session.pop(f"feedback", None)
        session.modified = True

    guidance = request.form.get('guidance') == 'true'

    if guidance is True:
        return redirect(url_for('routes.guidance', unit=unit, exercise=exercise))
    else:
        return redirect(url_for('routes.exercise', unit=unit, exercise=exercise))


@routes_bp.route('/unit/<unit>/exercise/<int:exercise>', methods=['POST'])
def flag_question(unit, exercise):
    feedback_message = request.args.get('feedback_message') or request.form.get('feedback_message')
    user_answer = request.args.get('user_answer') or request.form.get('user_answer')
    result = request.args.get('result') or request.form.get('result')
    reason = request.form.get('reason')

    if current_user.is_authenticated:
        log_question_flagged(unit, exercise, feedback_message, user_answer, result, reason, email=current_user.email)
    else:
        log_question_flagged(unit, exercise, feedback_message, user_answer, result, reason)

    flash("This answer has been flagged for review."
          "<br><br>Thank you!", "info")

    return redirect(request.referrer)


@routes_bp.route('/set-feedback-toggle', methods=['POST'])
def set_feedback_toggle():
    data = request.get_json()
    session['feedback_enabled'] = data.get('feedback_enabled', False)
    return '', 204


@routes_bp.route('/get-feedback-toggle')
def get_feedback_toggle():
    enabled = session.get('feedback_enabled', False)
    return jsonify({'feedback_enabled': enabled})


@routes_bp.route("/bookmark/toggle", methods=["POST"])
def toggle_bookmark():
    from flask import request, redirect, url_for, jsonify
    from users.users.models import Bookmark, db

    bookmark_id = request.form.get("bookmark_id")

    # Case 1: coming from the bookmarks page -> delete by ID
    if bookmark_id:
        bookmark = Bookmark.query.filter_by(
            id=int(bookmark_id),
            user_id=current_user.id
        ).first()

        if bookmark:
            db.session.delete(bookmark)
            db.session.commit()

            if request.headers.get("X-Requested-With") == "XMLHttpRequest":
                return jsonify({"bookmarked": False, "deleted": True})

        # if not found, just fall back to redirect/JSON
        if request.headers.get("X-Requested-With") == "XMLHttpRequest":
            return jsonify({"bookmarked": False})

        return redirect(request.referrer or url_for("routes.home"))

    # Case 2: coming from an exercise page -> use full data (your existing logic)
    unit = request.form["unit"]
    exercise = int(request.form["exercise"])
    level = request.form["level"]
    result = request.form["result"]
    user_answer = request.form.get("user_answer") or ""
    feedback_message = request.form["feedback_message"]

    bookmark = Bookmark.query.filter_by(
        user_id=current_user.id,
        unit=unit,
        exercise=exercise,
        level=level,
        result=result,
        user_answer=user_answer,
        feedback_message=feedback_message,
    ).first()

    bookmarked = False

    if bookmark:
        db.session.delete(bookmark)
    else:
        db.session.add(Bookmark(
            user_id=current_user.id,
            unit=unit,
            exercise=exercise,
            level=level,
            result=result,
            user_answer=user_answer,
            feedback_message=feedback_message,
        ))
        bookmarked = True

    db.session.commit()

    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return jsonify({"bookmarked": bookmarked})

    next_url = request.form.get("next") or request.referrer or url_for("routes.home")
    return redirect(next_url)
