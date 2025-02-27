import numpy as np
import pandas as pd

from utils.paths import DATA_PATH, SCORE_PATH


def total_questions_by_exercise_and_level(exercise, level):
    data = pd.read_csv(DATA_PATH[exercise])
    data = data[data["level"] == level]
    total_questions = len(data)
    return total_questions


def answered_questions_by_exercise_and_level(exercise, level, session=None):
    if session is None:
        try:
            path = f"{SCORE_PATH[exercise]}/level{level}.csv"
            scores = pd.read_csv(path)
            answered_questions = (scores["score"] == 1).sum()
        except FileNotFoundError:
            answered_questions = 0
        except pd.errors.EmptyDataError:
            answered_questions = 0
        return int(answered_questions)

    else:
        level = str(level)
        if exercise in session:
            if level in session[exercise]:
                return sum(session[exercise][level].values())
            else:
                return 0
        else:
            return 0



def total_questions_by_exercise(exercise):
    data = pd.read_csv(DATA_PATH[exercise])
    # data = data[data["level"] != "NaN"]
    data = data.dropna(subset="level")
    total_questions = len(data)
    return total_questions


def answered_questions_by_exercise(exercise, session=None):
    answered_questions = 0
    if session is None:
        for level in range(1, highest_level_exercise(exercise)+1):
            try:
                path = f"{SCORE_PATH[exercise]}/level{level}.csv"
                scores = pd.read_csv(path)
                answered_questions = answered_questions + (scores["score"] == 1).sum()
            except FileNotFoundError:
                pass
            except pd.errors.EmptyDataError:
                pass
        return int(answered_questions)
    else:
        for level in range(1, highest_level_exercise(exercise) + 1):
            answered_questions = answered_questions + answered_questions_by_exercise_and_level(exercise, level, session=session)
        return int(answered_questions)


def highest_level_exercise(exercise):
    data = pd.read_csv(DATA_PATH[exercise])
    highest_level = np.max(data["level"])
    return int(highest_level)
