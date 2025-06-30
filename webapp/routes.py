from flask import Blueprint, render_template, session, request, redirect, url_for, flash, jsonify

from data.data_processing.units import units
from data.data_processing.proverbs import get_text_proverb
from data.data_processing.data_loading import load_data

from webapp.session_management.score import write_score
from webapp.session_management.progress import compute_answered_questions
from webapp.session_management.statistics import print_question_flagged
from webapp.session_management.print_session import session_size, print_complete_session
from webapp.session_management.normalization import get_list_of_correct_answers, is_user_answer_correct
from webapp.session_management.total_questions import compute_total_questions
from webapp.session_management.pick_a_question import pick_a_question, is_exercise_finished
from webapp.session_management.register_update import register_progress, register_false, register_result
from webapp.session_management.verification_session import create_key_in_session

from webapp.content.unit.unit_page import UNIT_PAGE
from webapp.content.unit.title_page import TITLE_PAGE
from webapp.content.unit.back_button import BACK_BUTTON
from webapp.content.unit.introduction import INTRODUCTION
from webapp.content.unit.template_path import TEMPLATE_PATH
from webapp.content.exercise.feedbacks import FEEDBACK
from webapp.content.exercise.questions import QUESTION
from webapp.content.exercise.instructions import INSTRUCTION
from webapp.content.exercise.descriptions import DESCRIPTION

routes = Blueprint("routes", __name__)


@routes.before_request
def ensure_session_keys_exist_and_make_session_permanent():
    session.permanent = True

    if 'unfinished_exercise' not in session:
        session['unfinished_exercise'] = []

    # print_complete_session(session)
    print(f"Session size: {session_size(session)} bytes")
    # session.clear()


@routes.before_request
def convert_result():
    if 'result' in session:
        for unit in session['result']:
            if unit not in session:
                session[unit] = {}
            for exercise in session['result'][unit]:
                if str(exercise) not in session[unit]:
                    session[unit][str(exercise)] = {}
                session[unit][str(exercise)]['result'] = session['result'][unit][str(exercise)]
        del session['result']


@routes.before_request
def delete_old_unfinished_exercise():
    if session_size(session) > 3500:
        unit, exercise = session['unfinished_exercise'][0]
        if unit in session and str(exercise) in session[unit]:
            del session[unit][str(exercise)]
        session['unfinished_exercise'].remove((unit, exercise))


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
    if is_exercise_finished(session, unit, exercise) is True:
        register_result(session, unit, exercise)
        feedback = session.pop(f"feedback", None)
        result = feedback["result"] if feedback else None
        feedback_message = feedback["feedback_message"] if feedback else None
        user_answer = feedback["user_answer"] if feedback else None
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

    feedback = session.pop(f"feedback", None)
    result = feedback["result"] if feedback else None
    feedback_message = feedback["feedback_message"] if feedback else None
    user_answer = feedback["user_answer"] if feedback else None

    proverb = get_text_proverb()

    is_feedback_box = not session.get('feedback_enabled')

    return render_template("exercise/exercise.html",
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
                           )


@routes.route('/check/<unit>/exercise/<int:exercise>', methods=['POST', 'GET'])
def check_answer(unit, exercise):

    create_key_in_session(session, unit, exercise, 'progress')
    create_key_in_session(session, unit, exercise, 'falses')

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

    is_answer_correct = is_user_answer_correct(user_answer, correct_answer, question_text, unit)

    if is_answer_correct:
        register_progress(session, unit, exercise, nr)
    elif nr not in session[unit][str(exercise)]['falses']:
        register_false(session, unit, exercise, nr)

    session.modified = True

    session[f"feedback"] = {
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
        register_result(session, unit, exercise)
        feedback = session.pop(f"feedback", None)
        result = feedback["result"] if feedback else None
        feedback_message = feedback["feedback_message"] if feedback else None
        user_answer = feedback["user_answer"] if feedback else None
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

    feedback = session.pop(f"feedback", None)
    result = feedback["result"] if feedback else None
    feedback_message = feedback["feedback_message"] if feedback else None
    user_answer = feedback["user_answer"] if feedback else None

    proverb = get_text_proverb()

    is_feedback_box = True

    return render_template("exercise/feedback.html",
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
                           )


@routes.route('/reset/<unit>/exercise/<int:exercise>', methods=['POST'])
def reset_exercise(unit, exercise):
    """Clears progress for a specific unit exercise and removes any stored feedback."""
    '''if is_key_in_exercise(session, unit, exercise, 'progress'):
        del session[unit][str(exercise)]['progress']

    if is_key_in_exercise(session, unit, exercise, 'falses'):
        del session[unit][str(exercise)]['falses']

    if is_key_in_exercise(session, unit, exercise, 'result'):
        del session[unit][str(exercise)]['result']'''

    del session[unit][str(exercise)]

    if (unit, exercise) in session['unfinished_exercise']:
        session['unfinished_exercise'].remove((unit, exercise))

    session.pop(f"feedback", None)
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
    return '', 204


@routes.route('/get-feedback-toggle')
def get_feedback_toggle():
    enabled = session.get('feedback_enabled', False)
    return jsonify({'feedback_enabled': enabled})
