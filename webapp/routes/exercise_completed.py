from flask import render_template
from flask_login import current_user

from data.content.unit.unit_page import UNIT_PAGE
from data.content.unit.title_page import TITLE_PAGE
from data.content.unit.back_button import BACK_BUTTON
from data.content.application.text import EXERCISE_TITLE, ALL_QUESTIONS_SUCCESSFULLY_ANSWERED, \
    YOUR_SCORE_FOR_THIS_EXERCISE, FEEDBACK_LAST_QUESTION, YOUR_INCORRECT_ANSWERS, YOUR_ANSWER, NOT_AUTHENTICATED
from data.content.application.buttons import NEXT_EXERCISE, REFRESH, BACK_TO
from data.data_processing.total_questions import highest_exercise_per_unit

from users.users.settings import get_filename_empty_bookmark, get_filename_full_bookmark, get_filename_flag
from users.progress.score import write_score
from users.progress.progress import update_progress_in_home_page, get_next_exercise
from users.progress.register_update import register_result
from users.progress.feedback_exercise_completed import get_incorrect_answers, get_feedback_exercise
from users.questions.content_format import format_correction, format_question, format_feedback


def render_exercise_completed_template(session, unit, exercise, language):
    feedback = session.pop("feedback", None) or {}
    result = feedback.get("result")
    user_answer = feedback.get("user_answer")
    previous_question_id = feedback.get("previous_question_id")

    previous_question = format_question(unit, exercise, language, previous_question_id)
    feedback_message = format_feedback(unit, exercise, language, previous_question_id)

    if current_user.is_authenticated:
        incorrect_answers, number_of_incorrect_answers = get_incorrect_answers(session, unit, exercise)
        feedbacks = get_feedback_exercise(session, unit, exercise, language)
        corrections = [format_correction(unit, exercise, language, 'incorrect', incorrect_answer, "")
                               for incorrect_answer in incorrect_answers]
    else:
        number_of_incorrect_answers = 0
        incorrect_answers = []
        feedbacks = []
        corrections = []

    register_result(session, unit, exercise, feedback)

    update_progress_in_home_page(session, unit)

    next_exercise = get_next_exercise(unit, exercise, highest_exercise_per_unit)
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
                           format_correction=format_correction,
                           your_answer=YOUR_ANSWER[language],
                           corrections=corrections,
                           refresh=REFRESH[language],
                           back_to=BACK_TO[language],
                           icon_full=get_filename_full_bookmark(),
                           icon_empty=get_filename_empty_bookmark(),
                           icon_flag=get_filename_flag(),
                           next_exercise=next_exercise,
                           next_exercise_text=next_exercise_text,
                           current_user_not_authenticated=current_user_not_authenticated,
                           not_authenticated_text=NOT_AUTHENTICATED[language],
                           )
