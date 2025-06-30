import numpy as np
import pandas as pd

from data.data_processing.paths import DATA_PATH
from data.data_processing.data_loading import load_data


def compute_total_questions(unit, exercise=None):
    if exercise is not None:
        data = load_data(unit, exercise)
        total_questions = len(data)

    else:
        total_questions = 0
        for exercise in range(0, compute_highest_exercise(unit) + 1):
            data = load_data(unit, exercise)
            total_questions = total_questions + len(data)

    return total_questions


def compute_highest_exercise(unit):
    data = pd.read_csv(DATA_PATH[unit])
    highest_exercise = np.max(data[data["exercise"] < 100]["exercise"])
    return int(highest_exercise)
