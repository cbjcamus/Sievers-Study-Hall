import os
from flask import request
from datetime import datetime


def print_exercise_completed(unit, exercise):
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    STATISTICS_DIR = os.path.join(BASE_DIR, "../statistics")
    EXERCISE_COMPLETED_PATH = os.path.join(BASE_DIR, "../statistics", "exercise_completed.csv")
    NOW = datetime.now()

    create_folder(STATISTICS_DIR)
    create_file(EXERCISE_COMPLETED_PATH, "Nr; IP; date; unit; exercise")

    next_nr = get_next_number(EXERCISE_COMPLETED_PATH)

    forwarded_for = request.headers.get('X-Forwarded-For', request.remote_addr)
    user_ip = forwarded_for.split(',')[0].strip()  # Take the first IP if there are multiple

    with open(EXERCISE_COMPLETED_PATH, "a", encoding="utf-8") as file:
        file.write(f"\n{next_nr}; {user_ip}; {NOW}; {unit}; {exercise}")
    return


def print_question_flagged(unit, exercise, feedback_message, user_answer, result):
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    STATISTICS_DIR = os.path.join(BASE_DIR, "../statistics")
    QUESTION_FLAGGED_PATH = os.path.join(STATISTICS_DIR, "question_flagged.csv")
    NOW = datetime.now()

    create_folder(STATISTICS_DIR)
    create_file(QUESTION_FLAGGED_PATH, "Nr; IP; date; unit; exercise; result; feedback_message; user_answer")

    next_nr = get_next_number(QUESTION_FLAGGED_PATH)

    forwarded_for = request.headers.get('X-Forwarded-For', request.remote_addr)
    user_ip = forwarded_for.split(',')[0].strip()

    with open(QUESTION_FLAGGED_PATH, "a", encoding="utf-8") as file:
        file.write(f"\n{next_nr}; {user_ip}; {NOW}; {unit}; {exercise}; {result}; {feedback_message}; {user_answer}")
    return


def print_progress_deleted_from_session(unit, exercise):
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    STATISTICS_DIR = os.path.join(BASE_DIR, "../statistics")
    PROGRESS_DELETED_PATH = os.path.join(STATISTICS_DIR, "progress_deleted_from_session.csv")
    NOW = datetime.now()

    create_folder(STATISTICS_DIR)
    create_file(PROGRESS_DELETED_PATH, "Nr; IP; date; unit; exercise")

    next_nr = get_next_number(PROGRESS_DELETED_PATH)

    forwarded_for = request.headers.get('X-Forwarded-For', request.remote_addr)
    user_ip = forwarded_for.split(',')[0].strip()

    with open(PROGRESS_DELETED_PATH, "a", encoding="utf-8") as file:
        file.write(f"\n{next_nr}; {user_ip}; {NOW}; {unit}; {exercise}")
    return


def create_folder(folder):
    os.makedirs(folder, exist_ok=True)
    return


def create_file(file, first_line):
    if not os.path.isfile(file):
        with open(file, 'w', encoding='utf-8') as file:
            file.write(first_line)
    return


def get_next_number(file):
    next_nr = 1
    if os.path.exists(file):
        with open(file, "r", encoding="utf-8") as file:
            lines = [line for line in file if line.strip()]
            if len(lines) > 1:
                last_line = lines[-1]
                try:
                    last_nr = int(last_line.split(";")[0])
                    next_nr = last_nr + 1
                except ValueError:
                    pass

    return next_nr