from data.data_processing.exercise_type import get_extent
from data.data_processing.paths import df_units
from data.data_processing.pre_processing import pre_processing


def load_data_unit(unit):
    data = df_units[unit].fillna("")
    data = data[data["exercise"] < 100].copy()
    return data


def load_data_exercise(unit, exercise):
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
    data = df_units[unit]
    data = data[data['exercise'] == exercise].copy()
    data = pre_processing(data, unit, exercise)
    data = data.fillna("")
    return data


def load_data_level(unit, exercise):
    """
    Loads and preprocesses exercise data for a given unit and exercise,
    filtering using the 'extent' list from the mapping CSV.
    """
    data = df_units[unit]

    extent = get_extent(unit, int(exercise))

    data['exercise'] = data['exercise'].astype(int)
    data = data[data['exercise'].isin(extent)]

    data = pre_processing(data, unit, exercise)
    return data.fillna("")

