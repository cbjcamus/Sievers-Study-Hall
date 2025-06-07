import pandas as pd

from data.data_processing.paths import DATA_PATH
from data.data_processing.pre_processing import pre_processing


def load_data(unit, exercise):
    data = pd.read_csv(DATA_PATH[unit])
    data = data[data['exercise'] == exercise]
    data = pre_processing(data, unit, exercise)
    return data
