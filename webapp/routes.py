from flask import Blueprint, render_template, session, request, redirect, url_for, flash, jsonify

from data.data_processing.data_loading import load_data
from data.data_processing.proverbs import get_text_proverb
from data.data_processing.units import units

from webapp.session_management.progress import compute_answered_questions
from webapp.session_management.total_questions import compute_total_questions
from webapp.session_management.score import write_score
from webapp.session_management.pick_a_question import pick_a_question
from webapp.session_management.statistics import print_question_flagged
from webapp.session_management.result import register_result
from webapp.session_management.conditions import exercise_finished
from webapp.session_management.normalization import get_list_of_correct_answers, is_equal

from webapp.content.unit.title_page import TITLE_PAGE
from webapp.content.unit.back_button import BACK_BUTTON
from webapp.content.unit.introduction import INTRODUCTION
from webapp.content.unit.unit_page import UNIT_PAGE
from webapp.content.unit.template_path import TEMPLATE_PATH
from webapp.content.exercise.feedbacks import FEEDBACK
from webapp.content.exercise.questions import QUESTION
from webapp.content.exercise.instructions import INSTRUCTION
from webapp.content.exercise.descriptions import DESCRIPTION


routes = Blueprint("routes", __name__)


@routes.before_request
def ensure_session_keys_exist_and_make_session_permanent():
    """Ensure that progress, score, and result exist in the session before handling any request."""
    if 'progress' not in session:
        session['progress'] = {}
    if 'score' not in session:
        session['score'] = {}
    if 'result' not in session:
        session['result'] = {}

    session.permanent = True
    # session.clear()


@routes.route('/')
def home():
    return render_template('home.html',
                           answered_questions=compute_answered_questions,
                           total_questions=compute_total_questions,
                           score=write_score,
                           explanation=INTRODUCTION,
                           title_page=TITLE_PAGE,
                           unit_page=UNIT_PAGE,
                           )


@routes.route('/settings')
def settings():
    return render_template('menu/settings.html',
                           )


@routes.route('/contact')
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


@routes.route('/unit/<unit>/exercise/<int:exercise>')
def exercise(unit, exercise):
    if exercise_finished(session, unit, exercise) is True:
        register_result(session, unit, exercise)
        result_data = session.pop(f"{unit}_result", None)
        return render_template("exercise/exercise_completed.html",
                               unit=unit,
                               exercise=exercise,
                               score=write_score,
                               unit_page=UNIT_PAGE,
                               title_page=TITLE_PAGE,
                               back_page=BACK_BUTTON,
                               is_feedback_box=True,
                               result=result_data["result"] if result_data else None,
                               feedback_message=result_data["feedback_message"] if result_data else None,
                               user_answer=result_data["user_answer"] if result_data else None,
                               )

    question_data = pick_a_question(session, unit, exercise)

    # Ensure values are strings and handle NaN safely
    question_text = str(question_data["question"])
    english = str(question_data.get("english", ""))
    german = str(question_data.get("german", ""))
    adjective = question_data.get("adjective", "")
    gender = question_data.get("gender", "")
    case = question_data.get("case", "")
    article = question_data.get("article", "")
    person = question_data.get("person", "")
    prefix = question_data.get("prefix", "")

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
    )

    result_data = session.pop(f"{unit}_result", None)

    proverb = get_text_proverb()

    is_feedback_box = not session.get('feedback_enabled')

    return render_template("exercise/exercise.html",
                           unit=unit,
                           exercise=exercise,
                           question_text=formatted_question,
                           instruction_text=instruction,
                           nr=question_data["Nr"],
                           result=result_data["result"] if result_data else None,
                           feedback_message=result_data["feedback_message"] if result_data else None,
                           user_answer=result_data["user_answer"] if result_data else None,
                           unit_page=UNIT_PAGE,
                           title_page=TITLE_PAGE,
                           back_page=BACK_BUTTON,
                           answered_questions=compute_answered_questions(session, unit, exercise=exercise),
                           total_questions=compute_total_questions(unit, exercise=exercise),
                           proverb=proverb,
                           is_feedback_box=is_feedback_box,
                           )


@routes.route('/check/<unit>/exercise/<int:exercise>', methods=['POST', 'GET'])
def check_answer(unit, exercise):

    if request.method == 'GET':
        return redirect(url_for('routes.exercise', unit=unit, exercise=exercise))

    user_answer = request.form.get('answer', '')
    nr = request.form.get('nr')

    data = load_data(unit, exercise)

    question_data = data[data["Nr"] == int(nr)].iloc[0]
    correct_answer = question_data["answer"]
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
    )

    correct_answer_condition = is_equal(user_answer, correct_answer, question_text, unit)

    session[f"{unit}_result"] = {
        "result": "correct" if correct_answer_condition else "incorrect",
        "feedback_message": feedback_message,
        "user_answer": user_answer,
    }

    # Initialize score storage if missing
    if unit not in session['score']:
        session['score'][unit] = {}
    if str(exercise) not in session['score'][unit]:
        session['score'][unit][str(exercise)] = {}

    if correct_answer_condition:
        session_data = session['progress'].get(unit, {})
        session_data.setdefault(str(exercise), {})
        session_data[str(exercise)][nr] = 1
        session['progress'][unit] = session_data
        session['progress'].setdefault(unit, {}).setdefault(str(exercise), {})[nr] = 1

    if not correct_answer_condition:
        session['score'][unit][str(exercise)][nr] = False
    elif nr not in session['score'][unit][str(exercise)]:
        session['score'][unit][str(exercise)][nr] = True

    session.modified = True

    session[f"{unit}_question_data"] = question_data.to_dict()

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
    if exercise_finished(session, unit, exercise) is True:
        register_result(session, unit, exercise)
        result_data = session.pop(f"{unit}_result", None)
        return render_template("exercise/exercise_completed.html",
                               unit=unit,
                               exercise=exercise,
                               score=write_score,
                               unit_page=UNIT_PAGE,
                               title_page=TITLE_PAGE,
                               back_page=BACK_BUTTON,
                               is_feedback_box=True,
                               result=result_data["result"] if result_data else None,
                               feedback_message=result_data["feedback_message"] if result_data else None,
                               user_answer=result_data["user_answer"] if result_data else None,
                               )

    question_data = session.get(f"{unit}_question_data", {})

    # Ensure values are strings and handle NaN safely
    question_text = str(question_data["question"])
    english = str(question_data.get("english", ""))
    german = str(question_data.get("german", ""))
    adjective = question_data.get("adjective", "")
    gender = question_data.get("gender", "")
    case = question_data.get("case", "")
    article = question_data.get("article", "")
    person = question_data.get("person", "")
    prefix = question_data.get("prefix", "")

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
    )

    result_data = session.pop(f"{unit}_result", None)

    proverb = get_text_proverb()

    is_feedback_box = True

    return render_template("exercise/feedback.html",
                           unit=unit,
                           exercise=exercise,
                           question_text=formatted_question,
                           instruction_text=instruction,
                           nr=question_data["Nr"],
                           result=result_data["result"] if result_data else None,
                           feedback_message=result_data["feedback_message"] if result_data else None,
                           user_answer=result_data["user_answer"] if result_data else None,
                           unit_page=UNIT_PAGE,
                           title_page=TITLE_PAGE,
                           back_page=BACK_BUTTON,
                           answered_questions=compute_answered_questions(session, unit, exercise=exercise),
                           total_questions=compute_total_questions(unit, exercise=exercise),
                           proverb=proverb,
                           is_feedback_box=is_feedback_box,
                           )


@routes.route('/reset/<unit>/exercise/<int:exercise>', methods=['POST'])
def reset_exercise(unit, exercise):
    """Clears progress for a specific unit exercise and removes any stored feedback."""
    if 'progress' in session and unit in session['progress'] and str(exercise) in session['progress'][unit]:
        del session['progress'][unit][str(exercise)]

    if 'score' in session and unit in session['score'] and str(exercise) in session['score'][unit]:
        del session['score'][unit][str(exercise)]

    if 'result' in session and unit in session['result'] and str(exercise) in session['result'][unit]:
        del session['result'][unit][str(exercise)]

    session.pop(f"{unit}_result", None)  # Clear any stored feedback
    session.modified = True
    return redirect(url_for('routes.exercise', unit=unit, exercise=exercise))


@routes.route('/unit/<unit>/exercise/<int:exercise>', methods=['POST'])
def flag_question(unit, exercise):
    feedback_message = request.args.get('feedback_message') or request.form.get('feedback_message')
    user_answer = request.args.get('user_answer') or request.form.get('user_answer')

    print_question_flagged(unit, exercise, feedback_message, user_answer)

    flash("This answer has been flagged for review."
          "<br><br>Thank you!", "info")

    return redirect(request.referrer)


@routes.route('/set-feedback-toggle', methods=['POST'])
def set_feedback_toggle():
    data = request.get_json()
    session['feedback_enabled'] = data.get('feedback_enabled', False)
    return '', 204  # No content


@routes.route('/get-feedback-toggle')
def get_feedback_toggle():
    enabled = session.get('feedback_enabled', False)
    return jsonify({'feedback_enabled': enabled})
