from flask import Blueprint, render_template, session, request, redirect, url_for, flash, jsonify, Response
from typing import cast

session = cast(dict, session)

from data.data_processing.units import units
from data.data_processing.proverbs import get_text_proverb
from data.data_processing.data_loading import load_data_exercise, is_exercise_multiple_choice

from webapp.session_management.score import write_score
from webapp.session_management.logging import log_question_flagged, log_progress_deleted_from_session
from webapp.session_management.progress import compute_answered_questions
from webapp.session_management.print_session import session_size, print_complete_session
from webapp.session_management.normalization import get_list_of_correct_answers, is_user_answer_correct
from webapp.session_management.total_questions import compute_total_questions, compute_highest_exercise
from webapp.session_management.pick_a_question import (pick_a_question, is_exercise_finished, pick_other_options,
                                                       shuffle_options, get_question_from_incorrect_answer)
from webapp.session_management.register_update import (register_progress, register_false, register_result,
                                                       register_user_incorrect_answer)
from webapp.session_management.verification_session import init_session_key, is_key_in_exercise
from webapp.session_management.feedback_exercise_completed import get_feedback_exercise, get_incorrect_answers

from webapp.content.unit.stars import STARS
from webapp.content.unit.unit_page import UNIT_PAGE
from webapp.content.unit.title_page import TITLE_PAGE
from webapp.content.unit.back_button import BACK_BUTTON
from webapp.content.unit.introduction import INTRODUCTION
from webapp.content.unit.template_path import TEMPLATE_PATH
from webapp.content.unit.guidance_unit import GUIDANCE_UNIT
from webapp.content.exercise.feedbacks import FEEDBACK
from webapp.content.exercise.questions import QUESTION
from webapp.content.exercise.instructions import INSTRUCTION
from webapp.content.exercise.descriptions import DESCRIPTION
from webapp.content.exercise.guidance_exercise import GUIDANCE_EXERCISE

from webapp.style.icons import STAR_GOLD

routes = Blueprint("routes", __name__)


@routes.before_request
def ensure_session_keys_exist_and_make_session_permanent():
    session.permanent = True

    if 'unfinished_exercise' not in session:
        session['unfinished_exercise'] = []

    # print_complete_session(session)
    # print(f"Session size: {session_size(session)} bytes")
    # session.clear()


@routes.before_request
def delete_old_unfinished_exercise():
    if session_size(session) > 3500:
        unit, exercise = session['unfinished_exercise'][0]
        if unit in session and str(exercise) in session[unit]:
            log_progress_deleted_from_session(unit, exercise)
            del session[unit][str(exercise)]

        session['unfinished_exercise'].remove((unit, exercise))
        session['progress_deleted'] = {'unit': unit, 'exercise': exercise}
        print(f"Progress deleted for {unit} {exercise}")


@routes.after_request
def clear_progress_deleted_flag(response):
    session.pop('progress_deleted', None)
    return response


@routes.after_request
def clear_empty_unit_dictionary(response):
    if session_size(session) > 2000:
        for unit in units:
            for exercise in range(compute_highest_exercise(unit)):
                if (is_key_in_exercise(session, unit, exercise, 'falses')
                        and is_key_in_exercise(session, unit, exercise, 'progress')):
                    if (len(session[unit][str(exercise)]['falses']) == 0
                            and len(session[unit][str(exercise)]['progress']) == 0):
                        unit_dict = session.get(unit, {})
                        unit_dict.pop(str(exercise), None)
                        session[unit] = unit_dict
    return response


@routes.route('/', endpoint='home')
def home():
    return render_template('home.html',
                           answered_questions=compute_answered_questions,
                           total_questions=compute_total_questions,
                           score=write_score,
                           explanation=INTRODUCTION,
                           title_page=TITLE_PAGE,
                           button_unit=TITLE_PAGE,
                           unit_page=UNIT_PAGE,
                           unit_stars=STARS,
                           STAR_GOLD=STAR_GOLD,
                           )


@routes.route('/settings', endpoint='settings')
def settings():
    return render_template('menu/settings.html',
                           )


@routes.route('/contact', endpoint='contact')
def contact():
    return render_template('menu/contact.html',
                           )


for unit in units:
    route_path = UNIT_PAGE[unit]
    template = TEMPLATE_PATH[unit]

    def make_route(unit=unit, template=template):
        endpoint_name = f'dynamic_route_{unit}'
        @routes.route(route_path, endpoint=endpoint_name)
        def dynamic_route():
            introduction = INTRODUCTION.get(unit, {})
            return render_template(template,
                                   answered_questions=compute_answered_questions,
                                   total_questions=compute_total_questions,
                                   score=write_score,
                                   introduction=introduction,
                                   description_templates=DESCRIPTION,
                                   )
        return dynamic_route

    make_route()


@routes.route('/guidance/unit/<unit>/exercise/<int:exercise>')
def guidance(unit, exercise):
    if is_exercise_finished(session, unit, exercise) is True:
        feedback = session.pop(f"feedback", None)
        result = feedback["result"] if feedback else None
        feedback_message = feedback["feedback_message"] if feedback else None
        user_answer = feedback["user_answer"] if feedback else None

        incorrect_answers, number_of_incorrect_answers= get_incorrect_answers(session, unit, exercise)

        feedbacks = get_feedback_exercise(session, unit, exercise)

        register_result(session, unit, exercise, feedback)
        return render_template("exercise/exercise_completed.html",
                               unit=unit,
                               exercise=exercise,
                               score=write_score,
                               unit_page=UNIT_PAGE,
                               title_page=TITLE_PAGE,
                               back_page=BACK_BUTTON,
                               is_feedback_box=True,
                               result=result,
                               feedback_message=feedback_message,
                               user_answer=user_answer,
                               number_of_incorrect_answers=number_of_incorrect_answers,
                               incorrect_answers=incorrect_answers,
                               feedbacks=feedbacks,
                               )

    elif unit in GUIDANCE_EXERCISE and exercise in GUIDANCE_EXERCISE[unit]:
        guidance = GUIDANCE_EXERCISE[unit][exercise]
        return render_template("exercise/guidance.html",
                               unit=unit,
                               exercise=exercise,
                               guidance=guidance,
                               unit_page=UNIT_PAGE,
                               title_page=TITLE_PAGE,
                               back_page=BACK_BUTTON,
                               answered_questions=compute_answered_questions(session, unit, exercise=exercise),
                               total_questions=compute_total_questions(unit, exercise=exercise),
                               )

    elif unit in GUIDANCE_UNIT:
        guidance = GUIDANCE_UNIT[unit]
        return render_template("exercise/guidance.html",
                               unit=unit,
                               exercise=exercise,
                               guidance=guidance,
                               unit_page=UNIT_PAGE,
                               title_page=TITLE_PAGE,
                               back_page=BACK_BUTTON,
                               answered_questions=compute_answered_questions(session, unit, exercise=exercise),
                               total_questions=compute_total_questions(unit, exercise=exercise),
                               )

    else:
        return redirect(url_for('routes.exercise',
                                unit=unit,
                                exercise=exercise))


@routes.route('/unit/<unit>/exercise/<int:exercise>')
def exercise(unit, exercise):
    if is_exercise_finished(session, unit, exercise) is True:
        feedback = session.pop(f"feedback", None)
        result = feedback["result"] if feedback else None
        feedback_message = feedback["feedback_message"] if feedback else None
        user_answer = feedback["user_answer"] if feedback else None

        incorrect_answers, number_of_incorrect_answers = get_incorrect_answers(session, unit, exercise)

        feedbacks = get_feedback_exercise(session, unit, exercise)

        register_result(session, unit, exercise, feedback)
        return render_template("exercise/exercise_completed.html",
                               unit=unit,
                               exercise=exercise,
                               score=write_score,
                               unit_page=UNIT_PAGE,
                               title_page=TITLE_PAGE,
                               back_page=BACK_BUTTON,
                               is_feedback_box=True,
                               result=result,
                               feedback_message=feedback_message,
                               user_answer=user_answer,
                               number_of_incorrect_answers=number_of_incorrect_answers,
                               incorrect_answers=incorrect_answers,
                               feedbacks=feedbacks,
                               )

    question_data = pick_a_question(session, unit, exercise)

    question_text = str(question_data["question"])
    english = str(question_data.get("english", ""))
    german = str(question_data.get("german", ""))
    adjective = question_data.get("adjective", "")
    gender = question_data.get("gender", "")
    case = question_data.get("case", "")
    article = question_data.get("article", "")
    person = question_data.get("person", "")
    prefix = question_data.get("prefix", "")
    explanation = question_data.get("explanation", "")

    instruction = INSTRUCTION.get(unit, {}).get(exercise, "Translate the following word:")

    formatted_question = QUESTION.get(unit, {}).get(exercise, "{question}").format(
        question=question_text,
        english=english,
        german=german,
        adjective=adjective,
        gender=gender,
        case=case,
        article=article,
        person=person,
        prefix=prefix,
        explanation=explanation,
    )

    feedback = session.pop(f"feedback", None)
    result = feedback["result"] if feedback else None
    feedback_message = feedback["feedback_message"] if feedback else None
    user_answer = feedback["user_answer"] if feedback else None

    proverb = get_text_proverb()

    is_feedback_box = not session.get('feedback_enabled')

    incorrect_question = get_question_from_incorrect_answer(unit, exercise, result, user_answer)

    if is_exercise_multiple_choice(unit, exercise) is True:
        other_options = pick_other_options(unit, exercise, question_data)

        other_question_text = [str(option["answer"]) for option in other_options]

        options_text = shuffle_options(str(question_data["answer"]), other_question_text)

        return render_template("exercise/exercise_multiple_choice.html",
                               unit=unit,
                               exercise=exercise,
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
                               total_questions=compute_total_questions(unit, exercise=exercise),
                               proverb=proverb,
                               is_feedback_box=is_feedback_box,
                               gender=gender,
                               options=options_text,
                               incorrect_question=incorrect_question,
                               )

    return render_template("exercise/exercise_input.html",
                           unit=unit,
                           exercise=exercise,
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
                           total_questions=compute_total_questions(unit, exercise=exercise),
                           proverb=proverb,
                           is_feedback_box=is_feedback_box,
                           gender=gender,
                           incorrect_question=incorrect_question,
                           )


@routes.route('/check/<unit>/exercise/<int:exercise>', methods=['POST', 'GET'])
def check_answer(unit, exercise):

    init_session_key(session, unit, exercise, 'progress')
    init_session_key(session, unit, exercise, 'falses')

    if request.method == 'GET':
        return redirect(url_for('routes.exercise', unit=unit, exercise=exercise))

    user_answer = request.form.get('answer', '')
    nr = request.form.get('nr')

    data = load_data_exercise(unit, exercise)

    question_data = data[data["Nr"] == int(nr)].iloc[0]# .fillna("")
    correct_answer = question_data.get("answer", "")
    correct_answers = get_list_of_correct_answers(correct_answer, unit)
    question_text = question_data["question"]
    english = question_data.get("english", "")
    german = question_data.get("german", "")
    adjective = question_data.get("adjective", "")
    gender = question_data.get("gender", "")
    case = question_data.get("case", "")
    article = question_data.get("article", "")
    person = question_data.get("person", "")
    prefix = question_data.get("prefix", "")
    explanation = question_data.get("explanation", "")

    feedback_template = FEEDBACK.get(unit, {}).get(exercise, "{previous_question} = {correct_answer}")
    feedback_message = feedback_template.format(
        previous_question=question_text,
        correct_answer=correct_answer,
        correct_answers=correct_answers,
        user_answer=user_answer,
        english=english,
        german=german,
        adjective=adjective,
        gender=gender,
        case=case,
        article=article,
        person=person,
        prefix=prefix,
        explanation=explanation,
    )

    is_answer_correct = is_user_answer_correct(user_answer, correct_answer, question_text, unit)

    if is_answer_correct:
        register_progress(session, unit, exercise, nr)
    elif nr not in session[unit][str(exercise)]['falses']:
        register_false(session, unit, exercise, nr)
        register_user_incorrect_answer(session, unit, exercise, user_answer)

    session.modified = True

    session["feedback"] = {
        "result": "correct" if is_answer_correct else "incorrect",
        "feedback_message": feedback_message,
        "user_answer": user_answer,
    }

    session[f"question_data"] = question_data.to_dict()

    if session.get('feedback_enabled') is True:
        return redirect(url_for('routes.exercise_feedback',
                                unit=unit,
                                exercise=exercise))
    else:
        return redirect(url_for('routes.exercise',
                                unit=unit,
                                exercise=exercise))


@routes.route('/feedback/unit/<unit>/exercise/<int:exercise>')
def exercise_feedback(unit, exercise):
    if is_exercise_finished(session, unit, exercise) is True:
        feedback = session.pop(f"feedback", None)
        result = feedback["result"] if feedback else None
        feedback_message = feedback["feedback_message"] if feedback else None
        user_answer = feedback["user_answer"] if feedback else None

        incorrect_answers, number_of_incorrect_answers = get_incorrect_answers(session, unit, exercise)

        feedbacks = get_feedback_exercise(session, unit, exercise)

        register_result(session, unit, exercise, feedback)

        return render_template("exercise/exercise_completed.html",
                               unit=unit,
                               exercise=exercise,
                               score=write_score,
                               unit_page=UNIT_PAGE,
                               title_page=TITLE_PAGE,
                               back_page=BACK_BUTTON,
                               is_feedback_box=True,
                               result=result,
                               feedback_message=feedback_message,
                               user_answer=user_answer,
                               number_of_incorrect_answers=number_of_incorrect_answers,
                               incorrect_answers=incorrect_answers,
                               feedbacks=feedbacks,
                               )

    question_data = session.get(f"question_data", {})

    question_text = str(question_data["question"])
    english = str(question_data.get("english", ""))
    german = str(question_data.get("german", ""))
    adjective = question_data.get("adjective", "")
    gender = question_data.get("gender", "")
    case = question_data.get("case", "")
    article = question_data.get("article", "")
    person = question_data.get("person", "")
    prefix = question_data.get("prefix", "")
    explanation = question_data.get("explanation", "")

    instruction = INSTRUCTION.get(unit, {}).get(exercise, "Translate the following word:")

    formatted_question = QUESTION.get(unit, {}).get(exercise, "{question}").format(
        question=question_text,
        english=english,
        german=german,
        adjective=adjective,
        gender=gender,
        case=case,
        article=article,
        person=person,
        prefix=prefix,
        explanation=explanation,
    )

    feedback = session.pop(f"feedback", None)
    result = feedback["result"] if feedback else None
    feedback_message = feedback["feedback_message"] if feedback else None
    user_answer = feedback["user_answer"] if feedback else None

    proverb = get_text_proverb()

    is_feedback_box = True

    incorrect_question = get_question_from_incorrect_answer(unit, exercise, result, user_answer)

    if is_exercise_multiple_choice(unit, exercise) is True:

        return render_template("exercise/feedback_multiple_choice.html",
                               unit=unit,
                               exercise=exercise,
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
                               total_questions=compute_total_questions(unit, exercise=exercise),
                               proverb=proverb,
                               is_feedback_box=is_feedback_box,
                               incorrect_question=incorrect_question,
                               )

    return render_template("exercise/feedback_input.html",
                           unit=unit,
                           exercise=exercise,
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
                           total_questions=compute_total_questions(unit, exercise=exercise),
                           proverb=proverb,
                           is_feedback_box=is_feedback_box,
                           incorrect_question=incorrect_question,
                           )


@routes.route('/reset/<unit>/exercise/<int:exercise>', methods=['POST'])
def reset_exercise(unit, exercise):
    """Clears progress for a specific unit exercise and removes any stored feedback."""
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


@routes.route('/unit/<unit>/exercise/<int:exercise>', methods=['POST'])
def flag_question(unit, exercise):
    feedback_message = request.args.get('feedback_message') or request.form.get('feedback_message')
    user_answer = request.args.get('user_answer') or request.form.get('user_answer')
    result = request.args.get('result') or request.form.get('result')

    log_question_flagged(unit, exercise, feedback_message, user_answer, result)

    flash("This answer has been flagged for review."
          "<br><br>Thank you!", "info")

    return redirect(request.referrer)


@routes.route('/set-feedback-toggle', methods=['POST'])
def set_feedback_toggle():
    data = request.get_json()
    session['feedback_enabled'] = data.get('feedback_enabled', False)
    return '', 204


@routes.route('/get-feedback-toggle')
def get_feedback_toggle():
    enabled = session.get('feedback_enabled', False)
    return jsonify({'feedback_enabled': enabled})


@routes.route('/robots.txt')
def robots_txt():
    return Response(
        "User-agent: *\nDisallow:\nSitemap: https://www.sieversstudyhall.com/sitemap.xml",
        mimetype='text/plain'
    )


@routes.route('/sitemap.xml')
def sitemap():
    from flask import Response, url_for
    import datetime

    pages = []
    today = datetime.date.today().isoformat()

    # Static routes
    pages.append({'loc': url_for('home', _external=True), 'lastmod': today})
    pages.append({'loc': url_for('settings', _external=True), 'lastmod': today})
    pages.append({'loc': url_for('contact', _external=True), 'lastmod': today})

    # Dynamic unit routes
    for unit in units:
        endpoint = f'dynamic_route_{unit}'
        try:
            loc = url_for(endpoint, _external=True)
            pages.append({'loc': loc, 'lastmod': today})
        except:
            pass  # In case the endpoint wasn't properly registered

    sitemap_xml = render_template('sitemap_template.xml', pages=pages)
    return Response(sitemap_xml, mimetype='application/xml')