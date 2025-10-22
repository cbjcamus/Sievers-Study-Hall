import os
import re
import pandas as pd

from data.data_processing.paths import DATA_PATH
from data.data_processing.pre_processing import pre_processing


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
    data = pd.read_csv(DATA_PATH[unit])
    data = data[data['exercise'] == exercise]
    data = pre_processing(data, unit, exercise)
    data = data.fillna("")
    return data


def load_data_level(unit, exercise):
    """
    Loads and preprocesses exercise data for a given unit and exercise,
    filtering using the 'extent' list from the mapping CSV.
    """
    data = pd.read_csv(DATA_PATH[unit])

    extent = get_extent(unit, int(exercise))

    data['exercise'] = data['exercise'].astype(int)
    data = data[data['exercise'].isin(extent)]

    data = pre_processing(data, unit, exercise)
    return data.fillna("")


BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
MULTIPLE_CHOICE_PATH = os.path.join(BASE_DIR, "datasets/other", "multiple_choice_exercises.csv")


def get_extent(unit, exercise, csv_file=MULTIPLE_CHOICE_PATH):
    """
    Reads the mapping/levels CSV (with columns: unit, exercise, extent)
    and returns the list of exercise IDs to include.
    """
    df = pd.read_csv(csv_file)

    row = df.loc[(df['unit'] == unit) & (df['exercise'] == exercise)]
    if row.empty:
        raise ValueError(f"No mapping row for unit={unit} exercise={exercise}")

    row0 = row.iloc[0]

    if 'extent' not in df.columns or pd.isna(row0['extent']):
        raise KeyError("'extent' column missing or empty in mapping CSV.")

    # Extract numbers robustly: handles "11, 12, 13" or "11 12 13"
    vals = [int(x) for x in re.findall(r'\d+', str(row0['extent']))]
    if not vals:
        raise ValueError(f"No valid exercise numbers found in extent for unit={unit}, exercise={exercise}")

    return vals


def get_answer_column(unit, exercise, csv_file=MULTIPLE_CHOICE_PATH):
    """
    Reads the mapping/levels CSV (with columns: unit, exercise, extent)
    and returns the list of exercise IDs to include.
    """
    df = pd.read_csv(csv_file)

    row = df.loc[(df['unit'] == unit) & (df['exercise'] == exercise)]
    if row.empty:
        raise ValueError(f"No mapping row for unit={unit} exercise={exercise}")

    answer_column = row.iloc[0]["answer_column"]

    return answer_column


def get_question_column(unit, exercise, csv_file=MULTIPLE_CHOICE_PATH):
    """
    Reads the mapping/levels CSV (with columns: unit, exercise, extent)
    and returns the list of exercise IDs to include.
    """
    df = pd.read_csv(csv_file)

    row = df.loc[(df['unit'] == unit) & (df['exercise'] == exercise)]
    if row.empty:
        raise ValueError(f"No mapping row for unit={unit} exercise={exercise}")

    question_column = row.iloc[0]["question_column"]

    return question_column


def is_exercise_multiple_choice(unit, exercise, csv_file=MULTIPLE_CHOICE_PATH):
    df = pd.read_csv(csv_file)
    return not df[(df['unit'] == unit) & (df['exercise'] == exercise)].empty