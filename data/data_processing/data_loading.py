import pandas as pd

from data.data_processing.paths import DATA_PATH
from data.data_processing.pre_processing import pre_processing


def load_data(unit, exercise):
    """
    Loads and preprocesses exercise data for a given unit and exercise.

    Reads the CSV file corresponding to the specified unit from the DATA_PATH dictionary,
    filters the rows to keep only those matching the given exercise,
    applies preprocessing specific to the unit and exercise,
    and fills any missing values with empty strings.

    Args:
        unit (str): The unit name used to locate the CSV file in DATA_PATH.
        exercise (str): The specific exercise to filter and preprocess.

    Returns:
        pandas.DataFrame: The cleaned and preprocessed data for the specified exercise.
    """
    data = pd.read_csv(DATA_PATH[unit])
    data = data[data['exercise'] == exercise]
    data = pre_processing(data, unit, exercise)
    data = data.fillna("")
    return data
