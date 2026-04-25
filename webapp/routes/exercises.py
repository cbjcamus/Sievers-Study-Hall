from flask import render_template, session, request, redirect, url_for, flash, jsonify
from flask_login import current_user
from typing import cast

from data.content.unit.unit_page import UNIT_PAGE
from data.content.unit.title_page import TITLE_PAGE
from data.content.unit.back_button import BACK_BUTTON
from data.content.application.text import YOUR_ANSWER, EXERCISE_TITLE, ENTER_ANSWER_HERE, ADDITIONAL_HELP, CONSULT_FAQ
from data.content.application.popup import get_popup_title, get_popup_text
from data.content.application.buttons import BACK_TO, NEXT, NEXT_QUESTION, SUBMIT

from data.data_processing.proverbs import get_text_proverb
from data.data_processing.data_loading import load_question_text
from data.data_processing.exercises import is_exercise_multiple_choice
from data.data_processing.total_questions import total_question_exercises

from users.users.models import db, is_feedback_enabled, get_filename_full_bookmark, \
    get_filename_empty_bookmark, get_filename_flag, UserExerciseState, is_instruction_page_enabled

from users.progress.progress import compute_answered_questions, update_progress_in_session
from users.progress.register_update import register_progress, register_incorrect_answer
from users.progress.is_exercise_finished import is_exercise_finished

from users.questions.normalization import is_user_answer_correct
from users.questions.content_format import format_instruction, format_question, format_gender, format_guidance, \
    format_feedback, format_correction
from users.questions.pick_a_question import (pick_a_question, get_options_for_multiple_choice_exercises)

from users.session_management.logging import log_question_flagged
from users.session_management.session_update import update_session_dictionary, read_feedback
from users.session_management.verification_session import init_session_key, is_key_in_session

from . import routes_bp
from .exercise_completed import render_exercise_completed_template

from webapp.i18n import get_language


session = cast(dict, session)


@routes_bp.route('/guidance/unit/<unit>/exercise/<int:exercise>')
def guidance(unit, exercise):

    language = get_language(request, session)

    if is_exercise_finished(session, unit, exercise) is True:
        return render_exercise_completed_template(session, unit, exercise, language)

    update_session_dictionary(session, "current_exercise", "unit", unit)
    update_session_dictionary(session, "current_exercise", "exercise", exercise)

    guidance = format_guidance(unit, exercise, language)

    if guidance and is_instruction_page_enabled():
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
        return render_exercise_completed_template(session, unit, exercise, language)

    formated_instruction = format_instruction(unit, exercise, language)

    question_id = pick_a_question(session, unit, exercise)
    formated_question_text = format_question(unit, exercise, language, question_id)

    result, user_answer, previous_question_id = read_feedback(session)

    feedback_message = format_feedback(unit, exercise, language, previous_question_id)
    previous_question = load_question_text(unit, exercise, previous_question_id)
    correction = format_correction(unit, exercise, language, result, user_answer, previous_question)

    gender = format_gender(unit, exercise, language, question_id)

    guidance_popup = format_guidance(unit, exercise, language)

    proverb = get_text_proverb(language)

    is_feedback_box = not is_feedback_enabled()

    if is_key_in_session(session, 'popup') and not current_user.is_authenticated:
        clearance_popup_title = get_popup_title(session['popup']['unit'], session['popup']['exercise'], language)
        clearance_popup_text = get_popup_text(session['popup']['unit'], session['popup']['exercise'], language)
    else:
        clearance_popup_title = None
        clearance_popup_text = None

    options_text = get_options_for_multiple_choice_exercises(unit, exercise, question_id, language)

    exercise_is_input = not is_exercise_multiple_choice(unit, exercise)
    exercise_is_multiple_choice = is_exercise_multiple_choice(unit, exercise)

    return render_template("exercise/exercise.html",
                           unit=unit,
                           exercise=exercise,
                           exercise_title=EXERCISE_TITLE[language],
                           instruction_text=formated_instruction,
                           question_text=formated_question_text,
                           exercise_is_input=exercise_is_input,
                           exercise_is_multiple_choice=exercise_is_multiple_choice,
                           nr=question_id,
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
                           correction=correction,
                           submit=SUBMIT[language],
                           enter_answer_here=ENTER_ANSWER_HERE[language],
                           back_to=BACK_TO[language],
                           current_user=current_user,
                           icon_full=get_filename_full_bookmark(),
                           icon_empty=get_filename_empty_bookmark(),
                           icon_flag=get_filename_flag(),
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
    question_id = request.form.get('nr')

    is_answer_correct = is_user_answer_correct(unit, exercise, question_id, user_answer, language)
    result = "correct" if is_answer_correct else "incorrect"

    if is_answer_correct:
        register_progress(session, unit, exercise, question_id)
    elif question_id not in session[unit][str(exercise)]['falses']:
        register_incorrect_answer(session, unit, exercise, question_id, user_answer)

    session.modified = True

    update_session_dictionary(session, "feedback", "result", result)
    update_session_dictionary(session, "feedback", "user_answer", user_answer)
    update_session_dictionary(session, "feedback", "previous_question_id", question_id)

    update_session_dictionary(session, "current_exercise", "question_id", question_id)

    if is_feedback_enabled():
        route = 'routes.exercise_feedback'
    else:
        route = 'routes.exercise'

    return redirect(url_for(route,
                            unit=unit,
                            exercise=exercise))


@routes_bp.route('/feedback/unit/<unit>/exercise/<int:exercise>')
def exercise_feedback(unit, exercise):

    language = get_language(request, session)

    if is_exercise_finished(session, unit, exercise) is True:
        return render_exercise_completed_template(session, unit, exercise, language)

    question_id = session.get("current_exercise").get("question_id")

    formated_instruction = format_instruction(unit, exercise, language)
    formated_question_text = format_question(unit, exercise, language, question_id)

    result, user_answer, previous_question_id = read_feedback(session)

    feedback_message = format_feedback(unit, exercise, language, question_id)
    previous_question = format_question(unit, exercise, language, question_id)
    correction = format_correction(unit, exercise, language, result, user_answer, previous_question)

    guidance_popup = format_guidance(unit, exercise, language)

    proverb = get_text_proverb(language)

    is_feedback_box = True

    if is_key_in_session(session, 'popup') and not current_user.is_authenticated:
        clearance_popup_title = get_popup_title(session['popup']['unit'], session['popup']['exercise'], language)
        clearance_popup_text = get_popup_text(session['popup']['unit'], session['popup']['exercise'], language)
    else:
        clearance_popup_title = None
        clearance_popup_text = None

    return render_template("exercise/feedback.html",
                           unit=unit,
                           exercise=exercise,
                           exercise_title=EXERCISE_TITLE[language],
                           question_text=formated_question_text,
                           instruction_text=formated_instruction,
                           nr=question_id,
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
                           correction=correction,
                           next_question=NEXT_QUESTION[language],
                           back_to=BACK_TO[language],
                           icon_full=get_filename_full_bookmark(),
                           icon_empty=get_filename_empty_bookmark(),
                           icon_flag=get_filename_flag(),
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

    next_url = request.form.get("next")
    guidance = request.form.get('guidance') == 'true'

    if next_url:
        return redirect(next_url)

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
