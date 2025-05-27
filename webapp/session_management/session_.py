import os
from datetime import datetime

from data.data_processing.exercises import exercises

progress = 'progress'
score = 'score'
result = 'result'


def print_exercise_level_completed(exercise, level):
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    EXERCISE_COMPLETED_PATH = os.path.join(BASE_DIR, "../statistics", "exercise_level_completed.txt")
    NOW = datetime.now()
    print(f"{NOW}, {exercise}, {level}")
    with open(EXERCISE_COMPLETED_PATH, "a", encoding="utf-8") as file:
        file.write(f"{NOW}, {exercise}, {level}\n")
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
    for exercise in exercises:
        feedback = f"{exercise}_result"
        if feedback in session:
            for x, y in session[feedback].items():
                print(feedback, x, y)
        else:
            print(f'{feedback} empty')
    return