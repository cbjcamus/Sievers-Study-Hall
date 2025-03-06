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
                level = str(level)
                if "progress" in session and exercise in session["progress"]:
                    if level in session["progress"][exercise]:
                        answered_questions = answered_questions + sum(session["progress"][exercise][level].values())
                    else:
                        answered_questions = answered_questions + 0
                else:
                    answered_questions = answered_questions + 0
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
            if "progress" in session and exercise in session["progress"]:
                if level in session["progress"][exercise]:
                    return sum(session["progress"][exercise][level].values())
                else:
                    return 0
            else:
                return 0


def compute_score(exercise, level=None, session=None):
    if level is None:
        if session is None:
            return "0%"
        else:
            trues = 0
            falses = 0
            if "score" in session and exercise in session['score']:
                for level in range(1, compute_highest_level(exercise) + 1):
                    if str(level) in session["score"][exercise]:
                        trues = trues + compute_trues(exercise, level, session)
                        falses = falses + compute_falses(exercise, level, session)

                return compute_fraction(trues, falses)
            else:
                return "0%"

    else:
        if session is None:
            return "0%"
        else:
            if "score" in session and exercise in session["score"] and str(level) in session["score"][exercise]:
                trues = compute_trues(exercise, level, session)
                falses = compute_falses(exercise, level, session)
                return compute_fraction(trues, falses)
            else:
                return "0%"


def compute_fraction(trues, falses):
    if trues + falses == 0:
        return "0%"

    else:
        return f"{int(100 * trues / (trues + falses))}%"


def compute_trues(exercise, level, session):
    return sum(1 for val in session["score"][exercise][str(level)].values() if val is True)


def compute_falses(exercise, level, session):
    return sum(1 for val in session["score"][exercise][str(level)].values() if val is False)


def compute_highest_level(exercise):
    data = pd.read_csv(DATA_PATH[exercise])
    highest_level = np.max(data["level"])
    return int(highest_level)

