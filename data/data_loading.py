import pandas as pd

from data.paths import DATA_PATH
from data.pre_processing import pre_processing


def load_data(exercise, level):
    data = pd.read_csv(DATA_PATH[exercise])
    data = data[data["level"] == level]
    data = pre_processing(data, exercise, level)
    return data


def pick_a_question(session, exercise, level):
    data = load_data(exercise, level)

    if "progress" not in session:
        session["progress"] = {}

    if exercise not in session["progress"]:
        session["progress"][exercise] = {}

    if str(level) not in session["progress"][exercise]:
        session["progress"][exercise][str(level)] = {}

    answered_nrs = session["progress"][exercise][str(level)].keys()
    filtered_data = data[~data["Nr"].astype(str).isin(answered_nrs)]

    if filtered_data.empty:
        return None  # All datasets answered
    return filtered_data.sample(1).iloc[0]
