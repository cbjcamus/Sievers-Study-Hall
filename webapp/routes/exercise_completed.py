from flask import render_template
from flask_login import current_user

from data.content.application.buttons import BACK_TO, NEXT_EXERCISE, REFRESH
from data.content.application.text import (
    ALL_QUESTIONS_SUCCESSFULLY_ANSWERED,
    EXERCISE_TITLE,
    FEEDBACK_LAST_QUESTION,
    NOT_AUTHENTICATED,
    YOUR_ANSWER,
    YOUR_INCORRECT_ANSWERS,
    YOUR_SCORE_FOR_THIS_EXERCISE,
)
from data.content.unit.unit_content_by_language import UNIT_NAME
from data.content.unit.unit_url_path import UNIT_URL_PATH
from data.data_processing.exercises import get_level_from_exercise
from data.data_processing.total_questions import highest_exercise_per_unit
from users.progress.feedback_exercise_completed import (
    get_feedback_exercise,
    get_incorrect_answers,
)
from users.progress.progress import get_next_exercise, update_progress_in_home_page
from users.progress.register_update import register_result
from users.progress.score import write_score
from users.questions.content_format import (
    format_correction,
    format_feedback,
    format_question,
)
from users.users.settings import (
    get_filename_empty_bookmark,
    get_filename_flag,
    get_filename_full_bookmark,
)


def render_exercise_completed_template(session, unit, exercise, language):
    feedback = session.pop("feedback", None) or {}
    result = feedback.get("result")
    user_answer = feedback.get("user_answer")
    previous_question_id = feedback.get("previous_question_id")
    translation = feedback.get("translation")
    cefr_level = feedback.get("cefr_level")
    commentary = feedback.get("commentary")

    previous_question = format_question(unit, exercise, language, previous_question_id)
    feedback_message = format_feedback(
        unit,
        exercise,
        language,
        previous_question_id,
        user_answer,
        translation,
        cefr_level,
        commentary,
    )

    if current_user.is_authenticated:
        incorrect = get_incorrect_answers(session, unit, exercise)
        number_of_incorrect_answers = len(incorrect)
        incorrect_answers = [x["answer"] for x in incorrect.values()]

        feedbacks = get_feedback_exercise(session, unit, exercise, language, incorrect)
        corrections = [
            format_correction(
                unit, exercise, language, "incorrect", incorrect_answer, ""
            )
            for incorrect_answer in incorrect_answers
        ]
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

    level_exercise = get_level_from_exercise(unit, exercise)

    return render_template(
        "exercise/exercise_completed.html",
        unit=unit,
        exercise=exercise,
        exercise_title=EXERCISE_TITLE[language],
        score=write_score,
        unit_url_path=UNIT_URL_PATH,
        unit_name=UNIT_NAME[language][unit],
        is_feedback_box=True,
        result=result,
        feedback_message=feedback_message,
        user_answer=user_answer,
        previous_question=previous_question,
        number_of_incorrect_answers=number_of_incorrect_answers,
        incorrect_answers=incorrect_answers,
        feedbacks=feedbacks,
        all_questions_successfully_answered=ALL_QUESTIONS_SUCCESSFULLY_ANSWERED[
            language
        ],
        your_score_for_this_exercise=YOUR_SCORE_FOR_THIS_EXERCISE[language],
        feedback_last_question=FEEDBACK_LAST_QUESTION[language],
        your_incorrect_answers=YOUR_INCORRECT_ANSWERS[language],
        format_correction=format_correction,
        your_answer=YOUR_ANSWER[language],
        corrections=corrections,
        refresh=REFRESH[language],
        back_to=BACK_TO[language],
        level_exercise=level_exercise,
        icon_full=get_filename_full_bookmark(),
        icon_empty=get_filename_empty_bookmark(),
        icon_flag=get_filename_flag(),
        next_exercise=next_exercise,
        next_exercise_text=next_exercise_text,
        current_user_not_authenticated=current_user_not_authenticated,
        not_authenticated_text=NOT_AUTHENTICATED[language],
    )
