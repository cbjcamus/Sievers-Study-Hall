import numpy as np
import pandas as pd

from data.data_loading import load_data
from data.paths import DATA_PATH, SCORE_PATH


def compute_total_questions(exercise, level=None):
    if level is None:
        total_questions = 0
        for level in range(0, compute_highest_level(exercise) + 1):
            data = load_data(exercise, level)
            total_questions = total_questions + len(data)

    else:
        data = load_data(exercise, level)
        total_questions = len(data)

    return total_questions


def compute_answered_questions(exercise, level=None, session=None):
    if level is None:
        answered_questions = 0
        if session is None:
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
        else:
            for level in range(1, compute_highest_level(exercise) + 1):
                answered_questions = answered_questions + 0 # answered_questions(exercise, level, session=session)
            return int(answered_questions)

    else:
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


def compute_highest_level(exercise):
    data = pd.read_csv(DATA_PATH[exercise])
    highest_level = np.max(data["level"])
    return int(highest_level)

