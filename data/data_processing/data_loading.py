import pandas as pd

from data.data_processing.paths import DATA_PATH
from data.data_processing.pre_processing import pre_processing


def load_data(exercise, level):
    data = pd.read_csv(DATA_PATH[exercise])
    data = data[data["level"] == level]
    data = pre_processing(data, exercise, level)
    return data
