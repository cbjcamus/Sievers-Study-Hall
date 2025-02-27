import os
import pandas as pd
from flask import render_template, Flask, session, request, redirect, url_for
from utils.paths import DATA_PATH
from utils.exercises import konnektoren
from utils.statistics import (answered_questions_by_exercise_and_level, total_questions_by_exercise_and_level,
                              answered_questions_by_exercise, total_questions_by_exercise)

app = Flask(__name__,
            static_url_path='/webapp/static',
            static_folder='webapp/static',
            template_folder='webapp/templates')
app.secret_key = 'this_is_a_bad_secret_key_but_I_believe_it_works'

EXERCISE_PAGES = {
    "konnektoren": "/konnektoren",
    "artikeln": "/artikeln",
    "verben": "/verben"
}

QUESTION_TEMPLATES = {
    "konnektoren": {
        1: "Find the translation of the following connector:<br><br><strong>{question}</strong>",
        2: "Find the missing connector in the following sentence:<br><br>{question}<br><br>{english}",
        3: "Find the translation of the following connector:<br><br><strong>{question}</strong>",
        4: "Find the missing connector in the following sentence:<br><br>{question}<br><br>{english}",
        5: "Find the translation of the following connector:<br><br><strong>{question}</strong>",
        6: "Find the missing connector in the following sentence:<br><br>{question}<br><br>{english}",
        7: "Find the translation of the following connector:<br><br><strong>{question}</strong>",
        8: "Find the missing connector in the following sentence:<br><br>{question}<br><br>{english}",
    },
}

FEEDBACK_TEMPLATES = {
    "konnektoren": {
        1: "{previous_question} = {correct_answer}",
        2: "{english_text} = {german_text}",
        3: "{previous_question} = {correct_answer}",
        4: "{english_text} = {german_text}",
        5: "{previous_question} = {correct_answer}",
        6: "{english_text} = {german_text}",
        7: "{previous_question} = {correct_answer}",
        8: "{english_text} = {german_text}",
    },
}

def load_data(exercise, level):
    data = pd.read_csv(DATA_PATH[exercise])
    data = data[data["level"] == level]
    if exercise not in session:
        session[exercise] = {}
    if str(level) not in session[exercise]:
        session[exercise][str(level)] = {}
    answered_nrs = session[exercise][str(level)].keys()
    filtered_data = data[~data["Nr"].astype(str).isin(answered_nrs)]
    if filtered_data.empty:
        return None  # All questions answered
    return filtered_data.sample(1).iloc[0]


@app.route('/')
def home():
    return render_template('home.html',
                           answered_questions_by_exercise=answered_questions_by_exercise,
                           total_questions_by_exercise=total_questions_by_exercise)


@app.route('/konnektoren')
def konnektoren():
    print(session)
    print(answered_questions_by_exercise_and_level(konnektoren, 1, session))
    return render_template('konnektoren.html',
                           answered_questions_by_exercise_and_level=answered_questions_by_exercise_and_level,
                           total_questions_by_exercise_and_level=total_questions_by_exercise_and_level)


@app.route('/exercise/<exercise>/level/<int:level>')
def exercise(exercise, level):
    if exercise in session and str(level) in session[exercise]:
        data = pd.read_csv(DATA_PATH[exercise])
        data = data.fillna("")  # Ensure NaN values don't interfere
        data = data[data["level"] == level]
        answered_nrs = set(session[exercise][str(level)].keys())

        if set(data["Nr"].astype(str)) == answered_nrs:
            return render_template("exercise_completed.html", exercise=exercise, level=level, exercise_pages=EXERCISE_PAGES)

    question_data = load_data(exercise, level)
    if question_data is None:
        return render_template("exercise_completed.html", exercise=exercise, level=level, exercise_pages=EXERCISE_PAGES)

    # Ensure values are strings and handle NaN safely
    question_text = str(question_data["question"]).strip()
    english_text = str(question_data.get("english", "")).strip()
    german_text = str(question_data.get("german", "")).strip()

    formatted_question = QUESTION_TEMPLATES.get(exercise, {}).get(level, "{question}").format(
        question=question_text,
        english=english_text
    )

    print("Final Rendered Question:", formatted_question)  # Debugging to check the question output

    result_data = session.pop(f"{exercise}_result", None)

    return render_template("exercise.html",
                           exercise=exercise,
                           level=level,
                           question_text=formatted_question,
                           nr=question_data["Nr"],
                           result=result_data["result"] if result_data else None,
                           feedback_message=result_data["feedback_message"] if result_data else None,
                           user_answer=result_data["user_answer"] if result_data else None,
                           exercise_pages=EXERCISE_PAGES)


@app.route('/check/<exercise>/level/<int:level>', methods=['POST'])
def check_answer(exercise, level):
    user_answer = request.form['answer'].strip().lower()
    nr = request.form['nr']
    data = pd.read_csv(DATA_PATH[exercise])
    data = data.fillna("")
    data = data[data["level"] == level]
    question_data = data[data["Nr"] == int(nr)].iloc[0]
    correct_answer = question_data["answer"].strip().lower()
    question_text = question_data["question"]
    english_text = question_data.get("english", "")
    german_text = question_data.get("german", "")
    feedback_template = FEEDBACK_TEMPLATES.get(exercise, {}).get(level, "{previous_question} = {correct_answer}")
    feedback_message = feedback_template.format(
        previous_question=question_text,
        correct_answer=correct_answer,
        user_answer=user_answer,
        english_text=english_text,
        german_text=german_text,
    )
    session[f"{exercise}_result"] = {
        "result": "correct" if user_answer == correct_answer else "incorrect",
        "feedback_message": feedback_message,
        "user_answer": user_answer,
        "question": question_text,
        "answer": correct_answer,
        "german": german_text,
        "english": english_text
    }
    if user_answer == correct_answer:
        session_data = session.get(exercise, {})
        session_data.setdefault(str(level), {})
        session_data[str(level)][nr] = 1
        session[exercise] = session_data
        session.modified = True
    return redirect(url_for('exercise', exercise=exercise, level=level))


@app.route('/reset/<exercise>/level/<int:level>', methods=['POST'])
def reset_exercise(exercise, level):
    if exercise in session:
        session[exercise][str(level)] = {}  # Reset progress for this exercise & level
        session.modified = True
    return redirect(url_for('exercise', exercise=exercise, level=level))



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # Default to 8080 if PORT is not set
    app.run(host="0.0.0.0", port=port)
