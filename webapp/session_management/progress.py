import pandas as pd

from webapp.session_management.total_questions import compute_total_questions, compute_highest_level
from data_processing.paths import SCORE_PATH
from webapp.session_management.session_ import progress, result


def compute_answered_questions(exercise, level=None, session=None):
    if level is not None and session is not None:
        return compute_answered_questions_level_session(exercise, level, session)

    elif level is None and session is not None:
        return compute_answered_questions_exercise_session(exercise, session)

    elif level is None and session is None:
        return compute_answered_question_exercise_local(exercise)

    elif level is not None and session is None:
        return compute_answered_questions_level_local(exercise, level)

    else:
        return 0


def compute_answered_questions_exercise_session(exercise, session):
    answered_questions = 0
    for level in range(1, compute_highest_level(exercise) + 1):
        answered_questions_level = compute_answered_questions_level_session(exercise, level, session)
        answered_questions = answered_questions + answered_questions_level
    return int(answered_questions)


def compute_answered_questions_level_session(exercise, level, session):
    if result in session and exercise in session[result] and str(level) in session[result][exercise]:
        return compute_total_questions(exercise, level=level)

    elif progress in session and exercise in session[progress]:
        if str(level) in session[progress][exercise]:
            return sum(session[progress][exercise][str(level)].values())
        else:
            return 0

    else:
        return 0


def compute_answered_questions_level_local(exercise, level):
    try:
        path = f"{SCORE_PATH[exercise]}/level{level}.csv"
        scores = pd.read_csv(path)
        answered_questions = (scores["score"] == 1).sum()
    except FileNotFoundError:
        answered_questions = 0
    except pd.errors.EmptyDataError:
        answered_questions = 0
    return int(answered_questions)


def compute_answered_question_exercise_local(exercise):
    answered_questions = 0
    for level in range(1, compute_highest_level(exercise) + 1):
        try:
            path = f"{SCORE_PATH[exercise]}/level{level}.csv"
            scores = pd.read_csv(path)
            answered_questions = answered_questions + (scores["score"] == 1).sum()
        except FileNotFoundError:
            pass
        except pd.errors.EmptyDataError:
            pass
    return int(answered_questions)


