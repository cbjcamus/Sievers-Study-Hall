from flask import Blueprint, render_template, session, request, redirect, url_for

from data.normalization import normalization, get_answers
from data.paths import EXERCISE_PAGES
from data.statistics import (answered_questions_by_exercise, total_questions_by_exercise,
                             answered_questions_by_exercise_and_level, total_questions_by_exercise_and_level,
                             load_data, pick_a_question)
from webapp.feedback_templates import FEEDBACK_TEMPLATES
from webapp.question_templates import QUESTION_TEMPLATES
from webapp.description_templates import DESCRIPTION_TEMPLATES
from webapp.title_page import TITLE_PAGE

routes = Blueprint("routes", __name__)


@routes.route('/')
def home():
    return render_template('home.html',
                           answered_questions_by_exercise=answered_questions_by_exercise,
                           total_questions_by_exercise=total_questions_by_exercise)


@routes.route('/artikel')
def artikel():
    return render_template('artikel.html',
                           answered_questions_by_exercise_and_level=answered_questions_by_exercise_and_level,
                           total_questions_by_exercise_and_level=total_questions_by_exercise_and_level,
                           description_templates=DESCRIPTION_TEMPLATES)


@routes.route('/pronomen')
def pronomen():
    return render_template('pronomen.html',
                           answered_questions_by_exercise_and_level=answered_questions_by_exercise_and_level,
                           total_questions_by_exercise_and_level=total_questions_by_exercise_and_level,
                           description_templates=DESCRIPTION_TEMPLATES)


@routes.route('/konnektoren')
def konnektoren():
    return render_template('konnektoren.html',
                           answered_questions_by_exercise_and_level=answered_questions_by_exercise_and_level,
                           total_questions_by_exercise_and_level=total_questions_by_exercise_and_level,
                           description_templates=DESCRIPTION_TEMPLATES)


@routes.route('/praepositionen_grammatik')
def praepositionen_grammatik():
    return render_template('praepositionen_grammatik.html',
                           answered_questions_by_exercise_and_level=answered_questions_by_exercise_and_level,
                           total_questions_by_exercise_and_level=total_questions_by_exercise_and_level,
                           description_templates=DESCRIPTION_TEMPLATES)


@routes.route('/adjektivdeklinationen')
def adjektivdeklinationen():
    return render_template('adjektivdeklinationen.html',
                           answered_questions_by_exercise_and_level=answered_questions_by_exercise_and_level,
                           total_questions_by_exercise_and_level=total_questions_by_exercise_and_level,
                           description_templates=DESCRIPTION_TEMPLATES)


@routes.route('/praesens')
def praesens():
    return render_template('praesens.html',
                           answered_questions_by_exercise_and_level=answered_questions_by_exercise_and_level,
                           total_questions_by_exercise_and_level=total_questions_by_exercise_and_level,
                           description_templates=DESCRIPTION_TEMPLATES)


@routes.route('/praepositionen_konjugation')
def praepositionen_konjugation():
    return render_template('praepositionen_konjugation.html',
                           answered_questions_by_exercise_and_level=answered_questions_by_exercise_and_level,
                           total_questions_by_exercise_and_level=total_questions_by_exercise_and_level,
                           description_templates=DESCRIPTION_TEMPLATES)


@routes.route('/perfekt')
def perfekt():
    return render_template('perfekt.html',
                           answered_questions_by_exercise_and_level=answered_questions_by_exercise_and_level,
                           total_questions_by_exercise_and_level=total_questions_by_exercise_and_level,
                           description_templates=DESCRIPTION_TEMPLATES)


@routes.route('/praeteritum')
def praeteritum():
    return render_template('praeteritum.html',
                           answered_questions_by_exercise_and_level=answered_questions_by_exercise_and_level,
                           total_questions_by_exercise_and_level=total_questions_by_exercise_and_level,
                           description_templates=DESCRIPTION_TEMPLATES)


@routes.route('/imperativ')
def imperativ():
    return render_template('imperativ.html',
                           answered_questions_by_exercise_and_level=answered_questions_by_exercise_and_level,
                           total_questions_by_exercise_and_level=total_questions_by_exercise_and_level,
                           description_templates=DESCRIPTION_TEMPLATES)


@routes.route('/konjunktiv')
def konjunktiv():
    return render_template('konjunktiv.html',
                           answered_questions_by_exercise_and_level=answered_questions_by_exercise_and_level,
                           total_questions_by_exercise_and_level=total_questions_by_exercise_and_level,
                           description_templates=DESCRIPTION_TEMPLATES)


@routes.route('/adverbien')
def adverbien():
    return render_template('adverbien.html',
                           answered_questions_by_exercise_and_level=answered_questions_by_exercise_and_level,
                           total_questions_by_exercise_and_level=total_questions_by_exercise_and_level,
                           description_templates=DESCRIPTION_TEMPLATES)


@routes.route('/exercise/<exercise>/level/<int:level>')
def exercise(exercise, level):
    if exercise in session and str(level) in session[exercise]:
        data = load_data(exercise, level)

        answered_nrs = set(session[exercise][str(level)].keys())

        if set(data["Nr"].astype(str)) == answered_nrs:
            return render_template("exercise_completed.html",
                                   exercise=exercise,
                                   level=level,
                                   exercise_pages=EXERCISE_PAGES,
                                   title_page=TITLE_PAGE,)

    question_data = pick_a_question(session, exercise, level)

    if question_data is None:
        return render_template("exercise_completed.html",
                               exercise=exercise,
                               level=level,
                               exercise_pages=EXERCISE_PAGES,
                               title_page=TITLE_PAGE,)

    # Ensure values are strings and handle NaN safely
    question_text = str(question_data["question"])
    english_text = str(question_data.get("english", ""))
    german_text = str(question_data.get("german", ""))
    adjective = question_data.get("adjective", "")
    gender = question_data.get("gender", "")
    case = question_data.get("case", "")
    article = question_data.get("article", "")
    person = question_data.get("person", "")

    formatted_question = QUESTION_TEMPLATES.get(exercise, {}).get(level, "{question}").format(
        question=question_text,
        english_text=english_text,
        german=german_text,
        adjective=adjective,
        gender=gender,
        case=case,
        article=article,
        person=person,
    )

    result_data = session.pop(f"{exercise}_result", None)

    answered_questions = answered_questions_by_exercise_and_level(exercise, level, session)
    total_questions = total_questions_by_exercise_and_level(exercise, level)

    return render_template("exercise.html",
                           exercise=exercise,
                           level=level,
                           question_text=formatted_question,
                           nr=question_data["Nr"],
                           result=result_data["result"] if result_data else None,
                           feedback_message=result_data["feedback_message"] if result_data else None,
                           user_answer=result_data["user_answer"] if result_data else None,
                           exercise_pages=EXERCISE_PAGES,
                           title_page=TITLE_PAGE,
                           answered_questions=answered_questions,
                           total_questions=total_questions)


@routes.route('/check/<exercise>/level/<int:level>', methods=['POST'])
def check_answer(exercise, level):
    user_answer = normalization(request.form['answer'], exercise)
    nr = request.form['nr']

    data = load_data(exercise, level)

    question_data = data[data["Nr"] == int(nr)].iloc[0]
    correct_answer = normalization(question_data["answer"], exercise)
    correct_answers = get_answers(correct_answer, exercise)
    question_text = question_data["question"]
    english_text = question_data.get("english", "")
    german_text = question_data.get("german", "")
    adjective = question_data.get("adjective", "")
    gender = question_data.get("gender", "")
    case = question_data.get("case", "")
    article = question_data.get("article", "")
    person = question_data.get("person", "")
    feedback_template = FEEDBACK_TEMPLATES.get(exercise, {}).get(level, "{previous_question} = {correct_answer}")
    feedback_message = feedback_template.format(
        previous_question=question_text,
        correct_answer=correct_answer,
        correct_answers=correct_answers,
        user_answer=user_answer,
        english=english_text,
        german=german_text,
        adjective=adjective,
        gender=gender,
        case=case,
        article=article,
        person=person,
    )

    session[f"{exercise}_result"] = {
        "result": "correct" if user_answer == correct_answer else "incorrect",
        "feedback_message": feedback_message,
        "user_answer": user_answer,
        "question": question_text,
        "answer": correct_answers,
        "german": german_text,
        "english": english_text
    }
    if user_answer == correct_answer:
        session_data = session.get(exercise, {})
        session_data.setdefault(str(level), {})
        session_data[str(level)][nr] = 1
        session[exercise] = session_data
        session.modified = True
    return redirect(url_for('routes.exercise', exercise=exercise, level=level))


@routes.route('/reset/<exercise>/level/<int:level>', methods=['POST'])
def reset_exercise(exercise, level):
    if exercise in session:
        session[exercise][str(level)] = {}  # Reset progress for this exercise & level
        session.modified = True
    return redirect(url_for('routes.exercise', exercise=exercise, level=level))
