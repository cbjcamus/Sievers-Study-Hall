import numpy as np
import pandas as pd

from data.data_processing.paths import DATA_PATH, df_units
from data.data_processing.data_loading import load_data_exercise


def compute_total_questions(unit, exercise=None):
    """
    Computes the total number of questions for a specific exercise or for the entire unit.

    If an exercise is specified, loads the data for that exercise and returns the number of rows.
    If no exercise is provided, iterates over all exercises in the unit (from 0 to the highest one)
    and sums the number of questions across all exercises.

    Args:
        unit (str): The unit identifier.
        exercise (int or None): Optional exercise number. If None, totals all exercises in the unit.

    Returns:
        int: The total number of questions.
    """
    if exercise is not None:
        data = load_data_exercise(unit, exercise)
        total_questions = len(data)

    else:
        total_questions = 0
        for exercise in range(0, compute_highest_exercise(unit) + 1):
            data = load_data_exercise(unit, exercise)
            total_questions = total_questions + len(data)

    return total_questions


def compute_highest_exercise(unit):
    """
    Determines the highest exercise number for a given unit, excluding special exercises (>= 100).

    Loads the data for the specified unit from the corresponding CSV file in DATA_PATH.
    Filters out exercises with a number 100 or greater, then returns the maximum exercise number found.

    Args:
        unit (str): The unit identifier used to access the correct data source.

    Returns:
        int: The highest valid exercise number for the unit.
    """
    # data = pd.read_csv(DATA_PATH[unit])
    data = df_units[unit]
    highest_exercise = np.max(data[data["exercise"] < 100]["exercise"])
    return int(highest_exercise)
