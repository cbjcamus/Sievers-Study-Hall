import os
from flask import request
from datetime import datetime


def log_exercise_completed(unit, exercise):
    """
    Logs the completion of an exercise by writing an entry to a CSV file with metadata.

    Constructs the path to the statistics directory and the 'exercise_completed.csv' file.
    Ensures the directory and file exist. Determines the next available record number.
    Retrieves the user's IP address from the request headers (or falls back to remote address).
    Appends a new line to the CSV file with the current timestamp, IP, unit, and exercise.

    Args:
        unit (str): The unit identifier of the completed exercise.
        exercise (str or int): The exercise identifier.

    Returns:
        None
    """
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    STATISTICS_DIR = os.path.join(BASE_DIR, "../statistics")
    EXERCISE_COMPLETED_PATH = os.path.join(BASE_DIR, "../statistics", "exercise_completed.csv")
    now = datetime.now()

    create_folder(STATISTICS_DIR)
    create_file(EXERCISE_COMPLETED_PATH, "Nr; IP; date; unit; exercise")

    next_nr = get_next_number(EXERCISE_COMPLETED_PATH)

    forwarded_for = request.headers.get('X-Forwarded-For', request.remote_addr)
    user_ip = forwarded_for.split(',')[0].strip()  # Take the first IP if there are multiple

    with open(EXERCISE_COMPLETED_PATH, "a", encoding="utf-8") as file:
        file.write(f"\n{next_nr}; {user_ip}; {now}; {unit}; {exercise}")
    return


def log_question_flagged(unit, exercise, feedback_message, user_answer, result):
    """
    Logs a flagged question to a CSV file with relevant metadata for review.

    Creates the statistics folder and the 'question_flagged.csv' file if they do not exist.
    Determines the next available entry number. Retrieves the user's IP address from the request headers.
    Records the current timestamp, unit, exercise, evaluation result, feedback message, and user answer.

    Args:
        unit (str): The unit in which the question was flagged.
        exercise (str or int): The exercise identifier.
        feedback_message (str): The feedback message explaining the issue.
        user_answer (str): The user's submitted answer.
        result (str): The evaluation result (e.g., "correct", "incorrect").

    Returns:
        None
    """
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    STATISTICS_DIR = os.path.join(BASE_DIR, "../statistics")
    QUESTION_FLAGGED_PATH = os.path.join(STATISTICS_DIR, "question_flagged.csv")
    now = datetime.now()

    create_folder(STATISTICS_DIR)
    create_file(QUESTION_FLAGGED_PATH, "Nr; IP; date; unit; exercise; result; feedback_message; user_answer")

    next_nr = get_next_number(QUESTION_FLAGGED_PATH)

    forwarded_for = request.headers.get('X-Forwarded-For', request.remote_addr)
    user_ip = forwarded_for.split(',')[0].strip()

    with open(QUESTION_FLAGGED_PATH, "a", encoding="utf-8") as filepath:
        filepath.write(f"\n{next_nr}; {user_ip}; {now}; {unit}; {exercise}; {result}; {feedback_message}; {user_answer}")
    return


def log_progress_deleted_from_session(unit, exercise):
    """
    Logs the deletion of progress data from the session to a CSV file for auditing purposes.

    Ensures the statistics folder and 'progress_deleted_from_session.csv' file exist.
    Retrieves the current timestamp, determines the next record number, and extracts the user's IP address.
    Writes a new entry to the file with the unit, exercise, and metadata.

    Args:
        unit (str): The unit identifier where progress was deleted.
        exercise (str or int): The exercise identifier.

    Returns:
        None
    """
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    STATISTICS_DIR = os.path.join(BASE_DIR, "../statistics")
    PROGRESS_DELETED_PATH = os.path.join(STATISTICS_DIR, "progress_deleted_from_session.csv")
    now = datetime.now()

    create_folder(STATISTICS_DIR)
    create_file(PROGRESS_DELETED_PATH, "Nr; IP; date; unit; exercise")

    next_nr = get_next_number(PROGRESS_DELETED_PATH)

    forwarded_for = request.headers.get('X-Forwarded-For', request.remote_addr)
    user_ip = forwarded_for.split(',')[0].strip()

    with open(PROGRESS_DELETED_PATH, "a", encoding="utf-8") as filepath:
        filepath.write(f"\n{next_nr}; {user_ip}; {now}; {unit}; {exercise}")
    return


def create_folder(folder):
    """
    Creates a folder if it does not already exist.

    Uses os.makedirs with exist_ok=True to avoid raising an error if the folder exists.

    Args:
        folder (str): The path of the folder to create.

    Returns:
        None
    """
    os.makedirs(folder, exist_ok=True)
    return


def create_file(file, first_line):
    """
    Creates a new file with a specified header line if the file does not already exist.

    Checks whether the file exists using os.path.isfile. If not, creates it and writes
    the provided first line (typically a header) using UTF-8 encoding.

    Args:
        file (str): The full path to the file to create.
        first_line (str): The header or initial content to write to the new file.

    Returns:
        None
    """
    if not os.path.isfile(file):
        with open(file, 'w', encoding='utf-8') as file:
            file.write(first_line)
    return


def get_next_number(file):
    """
    Determines the next available sequential number for a CSV file entry.

    Opens the given file and reads all non-empty lines. If the file has at least
    one data line (besides the header), extracts the number from the first column
    of the last line and increments it. Returns 1 if the file is empty or the number
    cannot be parsed.

    Args:
        file (str): The path to the CSV file.

    Returns:
        int: The next available entry number.
    """
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