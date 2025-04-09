import numpy as np
import pandas as pd

from data_processing.data_loading import load_data
from data_processing.paths import DATA_PATH


def compute_total_questions(exercise, level=None):
    if level is not None:
        data = load_data(exercise, level)
        total_questions = len(data)

    else:
        total_questions = 0
        for level in range(0, compute_highest_level(exercise) + 1):
            data = load_data(exercise, level)
            total_questions = total_questions + len(data)

    return total_questions


def compute_highest_level(exercise):
    data = pd.read_csv(DATA_PATH[exercise])
    highest_level = np.max(data[data["level"] < 100]["level"])
    return int(highest_level)
