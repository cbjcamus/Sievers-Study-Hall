from flask import Blueprint, render_template, session, request, redirect, url_for

from data.data_processing.data_loading import load_data
from data.data_processing.proverbs import get_text_proverb

from webapp.session_management.progress import compute_answered_questions
from webapp.session_management.total_questions import compute_total_questions
from webapp.session_management.score import write_score
from webapp.session_management.pick_a_question import pick_a_question
from webapp.session_management.session_ import progress, score, result
from webapp.session_management.result import register_result
from webapp.session_management.conditions import level_finished
from webapp.session_management.normalization import get_list_of_correct_answers, is_equal

from webapp.content.exercise.title_page import TITLE_PAGE
from webapp.content.exercise.back_button import BACK_BUTTON
from webapp.content.exercise.explanation import EXPLANATION
from webapp.content.exercise.exercise_page import EXERCISE_PAGES
from webapp.content.level.feedbacks import FEEDBACK
from webapp.content.level.questions import QUESTION
from webapp.content.level.instructions import INSTRUCTION
from webapp.content.level.descriptions import DESCRIPTION


routes = Blueprint("routes", __name__)


@routes.before_request
def ensure_session_keys_exist():
    """Ensure that progress, score, and result exist in the session before handling any request."""
    if progress not in session:
        session[progress] = {}
    if score not in session:
        session[score] = {}
    if result not in session:
        session[result] = {}

    # session.clear()


@routes.route('/')
def home():
    return render_template('home.html',
                           answered_questions=compute_answered_questions,
                           total_questions=compute_total_questions,
                           score=write_score,
                           explanation=EXPLANATION,
                           title_page=TITLE_PAGE,
                           exercise_page=EXERCISE_PAGES
                           )


@routes.route('/about')
def about():
    return render_template('menu/about.html',
                           )


@routes.route('/faq')
def faq():
    return render_template('menu/faq.html',
                           )


@routes.route('/updates')
def updates():
    return render_template('menu/updates.html',
                           )


@routes.route('/praepositionen_grammatik')
def praepositionen_grammatik():
    return render_template('praepositionen/praepositionen_grammatik.html',
                           answered_questions=compute_answered_questions,
                           total_questions=compute_total_questions,
                           score=write_score,
                           description_templates=DESCRIPTION)


@routes.route('/praepositionen_verben')
def praepositionen_verben():
    return render_template('praepositionen/praepositionen_verben.html',
                           answered_questions=compute_answered_questions,
                           total_questions=compute_total_questions,
                           score=write_score,
                           description_templates=DESCRIPTION)


@routes.route('/praepositionen_adjektive')
def praepositionen_adjektive():
    return render_template('praepositionen/praepositionen_adjektive.html',
                           answered_questions=compute_answered_questions,
                           total_questions=compute_total_questions,
                           score=write_score,
                           description_templates=DESCRIPTION)


@routes.route('/praepositionen_nomen')
def praepositionen_nomen():
    return render_template('praepositionen/praepositionen_nomen.html',
                           answered_questions=compute_answered_questions,
                           total_questions=compute_total_questions,
                           score=write_score,
                           description_templates=DESCRIPTION)


@routes.route('/artikel')
def artikel():
    return render_template('grammatik/artikel.html',
                           answered_questions=compute_answered_questions,
                           total_questions=compute_total_questions,
                           score=write_score,
                           description_templates=DESCRIPTION)


@routes.route('/pronomen')
def pronomen():
    return render_template('grammatik/pronomen.html',
                           answered_questions=compute_answered_questions,
                           total_questions=compute_total_questions,
                           score=write_score,
                           description_templates=DESCRIPTION)


@routes.route('/konnektoren')
def konnektoren():
    return render_template('grammatik/konnektoren.html',
                           answered_questions=compute_answered_questions,
                           total_questions=compute_total_questions,
                           score=write_score,
                           description_templates=DESCRIPTION)


@routes.route('/fragen')
def fragen():
    return render_template('grammatik/fragen.html',
                           answered_questions=compute_answered_questions,
                           total_questions=compute_total_questions,
                           score=write_score,
                           description_templates=DESCRIPTION)


@routes.route('/adjektivdeklinationen')
def adjektivdeklinationen():
    return render_template('grammatik/adjektivdeklinationen.html',
                           answered_questions=compute_answered_questions,
                           total_questions=compute_total_questions,
                           score=write_score,
                           description_templates=DESCRIPTION)


@routes.route('/praesens')
def praesens():
    return render_template('konjugation/praesens.html',
                           answered_questions=compute_answered_questions,
                           total_questions=compute_total_questions,
                           score=write_score,
                           description_templates=DESCRIPTION)


@routes.route('/partizip_II')
def partizip_II():
    return render_template('konjugation/partizip_II.html',
                           answered_questions=compute_answered_questions,
                           total_questions=compute_total_questions,
                           score=write_score,
                           description_templates=DESCRIPTION)


@routes.route('/praeteritum')
def praeteritum():
    return render_template('konjugation/praeteritum.html',
                           answered_questions=compute_answered_questions,
                           total_questions=compute_total_questions,
                           score=write_score,
                           description_templates=DESCRIPTION)


@routes.route('/praeteritum_partizip_II')
def praeteritum_partizip_II():
    return render_template('konjugation/praeteritum_partizip_II.html',
                           answered_questions=compute_answered_questions,
                           total_questions=compute_total_questions,
                           score=write_score,
                           description_templates=DESCRIPTION)


@routes.route('/imperativ')
def imperativ():
    return render_template('konjugation/imperativ.html',
                           answered_questions=compute_answered_questions,
                           total_questions=compute_total_questions,
                           score=write_score,
                           description_templates=DESCRIPTION)


@routes.route('/konjunktiv_II')
def konjunktiv_II():
    return render_template('konjugation/konjunktiv_II.html',
                           answered_questions=compute_answered_questions,
                           total_questions=compute_total_questions,
                           score=write_score,
                           description_templates=DESCRIPTION)


@routes.route('/konjunktiv_I')
def konjunktiv_I():
    return render_template('konjugation/konjunktiv_I.html',
                           answered_questions=compute_answered_questions,
                           total_questions=compute_total_questions,
                           score=write_score,
                           description_templates=DESCRIPTION)


@routes.route('/partizip_I')
def partizip_I():
    return render_template('konjugation/partizip_I.html',
                           answered_questions=compute_answered_questions,
                           total_questions=compute_total_questions,
                           score=write_score,
                           description_templates=DESCRIPTION)


@routes.route('/adverbien')
def adverbien():
    return render_template('grammatik/adverbien.html',
                           answered_questions=compute_answered_questions,
                           total_questions=compute_total_questions,
                           score=write_score,
                           description_templates=DESCRIPTION)


@routes.route('/verben')
def verben():
    return render_template('verben/verben.html',
                           answered_questions=compute_answered_questions,
                           total_questions=compute_total_questions,
                           score=write_score,
                           description_templates=DESCRIPTION)


@routes.route('/trennbare_verben')
def trennbare_verben():
    return render_template('verben/trennbare_verben.html',
                           answered_questions=compute_answered_questions,
                           total_questions=compute_total_questions,
                           score=write_score,
                           description_templates=DESCRIPTION)


@routes.route('/deverbale_substantive')
def deverbale_substantive():
    return render_template('wortschatz/deverbale_substantive.html',
                           answered_questions=compute_answered_questions,
                           total_questions=compute_total_questions,
                           score=write_score,
                           description_templates=DESCRIPTION)


@routes.route('/exercise/<exercise>/level/<int:level>')
def exercise(exercise, level):
    if level_finished(session, exercise, level) is True:
        register_result(session, exercise, level)
        return render_template("exercise/exercise_completed.html",
                               exercise=exercise,
                               level=level,
                               exercise_pages=EXERCISE_PAGES,
                               title_page=TITLE_PAGE,
                               back_page=BACK_BUTTON,
                               )

    question_data = pick_a_question(session, exercise, level)

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

    instruction = INSTRUCTION.get(exercise, {}).get(level, "Translate the following word:")

    formatted_question = QUESTION.get(exercise, {}).get(level, "{question}").format(
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

    result_data = session.pop(f"{exercise}_result", None)

    proverb = get_text_proverb()

    return render_template("exercise/exercise.html",
                           exercise=exercise,
                           level=level,
                           question_text=formatted_question,
                           instruction_text=instruction,
                           nr=question_data["Nr"],
                           result=result_data["result"] if result_data else None,
                           feedback_message=result_data["feedback_message"] if result_data else None,
                           user_answer=result_data["user_answer"] if result_data else None,
                           exercise_pages=EXERCISE_PAGES,
                           title_page=TITLE_PAGE,
                           back_page=BACK_BUTTON,
                           answered_questions=compute_answered_questions(session, exercise, level=level),
                           total_questions=compute_total_questions(exercise, level=level),
                           proverb=proverb)


@routes.route('/check/<exercise>/level/<int:level>', methods=['POST', 'GET'])
def check_answer(exercise, level):

    if request.method == 'GET':
        return redirect(url_for('routes.exercise', exercise=exercise, level=level))

    user_answer = request.form['answer']
    nr = request.form['nr']

    data = load_data(exercise, level)

    question_data = data[data["Nr"] == int(nr)].iloc[0]
    correct_answer = question_data["answer"]
    correct_answers = get_list_of_correct_answers(correct_answer, exercise)
    question_text = question_data["question"]
    english = question_data.get("english", "")
    german = question_data.get("german", "")
    adjective = question_data.get("adjective", "")
    gender = question_data.get("gender", "")
    case = question_data.get("case", "")
    article = question_data.get("article", "")
    person = question_data.get("person", "")
    prefix = question_data.get("prefix", "")
    feedback_template = FEEDBACK.get(exercise, {}).get(level, "{previous_question} = {correct_answer}")
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

    correct_answer_condition = is_equal(user_answer, correct_answer, question_text, exercise)

    session[f"{exercise}_result"] = {
        "result": "correct" if correct_answer_condition else "incorrect",
        "feedback_message": feedback_message,
        "user_answer": user_answer,
    }

    # Initialize score storage if missing
    if exercise not in session[score]:
        session[score][exercise] = {}
    if str(level) not in session[score][exercise]:
        session[score][exercise][str(level)] = {}

    if correct_answer_condition:
        session_data = session[progress].get(exercise, {})
        session_data.setdefault(str(level), {})
        session_data[str(level)][nr] = 1
        session[progress][exercise] = session_data
        session[progress].setdefault(exercise, {}).setdefault(str(level), {})[nr] = 1

    if not correct_answer_condition:
        session[score][exercise][str(level)][nr] = False
    elif nr not in session[score][exercise][str(level)]:
        session[score][exercise][str(level)][nr] = True

    session.modified = True

    return redirect(url_for('routes.exercise', exercise=exercise, level=level))


@routes.route('/reset/<exercise>/level/<int:level>', methods=['POST'])
def reset_exercise(exercise, level):
    """Clears progress for a specific exercise level and removes any stored feedback."""
    if progress in session and exercise in session[progress] and str(level) in session[progress][exercise]:
        del session[progress][exercise][str(level)]

    if score in session and exercise in session[score] and str(level) in session[score][exercise]:
        del session[score][exercise][str(level)]

    if result in session and exercise in session[result] and str(level) in session[result][exercise]:
        del session[result][exercise][str(level)]

    session.pop(f"{exercise}_result", None)  # Clear any stored feedback
    session.modified = True
    return redirect(url_for('routes.exercise', exercise=exercise, level=level))

