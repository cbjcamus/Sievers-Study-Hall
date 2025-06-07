import os
from datetime import datetime
from flask import request

from data.data_processing.units import units

progress = 'progress'
score = 'score'
result = 'result'

def print_unit_exercise_question_flagged(unit, exercise, feedback_message, user_answer):
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    EXERCISE_COMPLETED_PATH = os.path.join(BASE_DIR, "../statistics", "unit_exercise_question_flagged.txt")
    NOW = datetime.now()

    forwarded_for = request.headers.get('X-Forwarded-For', request.remote_addr)
    user_ip = forwarded_for.split(',')[0].strip()

    with open(EXERCISE_COMPLETED_PATH, "a", encoding="utf-8") as file:
        file.write(f"\n{user_ip}, {NOW}, {unit}, {exercise}, {feedback_message}, {user_answer}")
    return


def print_unit_exercise_completed(unit, exercise):
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    EXERCISE_COMPLETED_PATH = os.path.join(BASE_DIR, "../statistics", "unit_exercise_completed.txt")
    NOW = datetime.now()

    forwarded_for = request.headers.get('X-Forwarded-For', request.remote_addr)
    user_ip = forwarded_for.split(',')[0].strip()  # Take the first IP if there are multiple

    with open(EXERCISE_COMPLETED_PATH, "a", encoding="utf-8") as file:
        file.write(f"\n{user_ip}, {NOW}, {unit}, {exercise}")
    return


def print_unit_exercise_checked(unit, exercise):
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    EXERCISE_CHECKED_PATH = os.path.join(BASE_DIR, "../statistics", "unit_exercise_check.txt")
    NOW = datetime.now()
    with open(EXERCISE_CHECKED_PATH, "a", encoding="utf-8") as file:
        file.write(f"\n{NOW}, {unit}, {exercise}")
    return


def print_session(session):
    print_session_dictionary(session, progress)
    print_session_dictionary(session, score)
    print_session_dictionary(session, result)
    print_session_feedbacks(session)
    return


def print_session_dictionary(session, dictionary):
    if dictionary in session:
        for x, y in session[dictionary].items():
            print(dictionary, x, y)
    else:
        print(f'{dictionary} empty')
    return


def print_session_feedbacks(session):
    for unit in units:
        feedback = f"{units}_result"
        if feedback in session:
            for x, y in session[feedback].items():
                print(feedback, x, y)
        else:
            print(f'{feedback} empty')
    return