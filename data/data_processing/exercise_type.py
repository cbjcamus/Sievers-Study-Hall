import os
import re

import pandas as pd

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
EXERCISE_TYPE_PATH = os.path.join(BASE_DIR, "datasets/other", "exercise_type.csv")
df_exercise_type = pd.read_csv(EXERCISE_TYPE_PATH)


def get_extent(unit, exercise):
    """
    Reads the mapping/levels CSV (with columns: unit, exercise, extent)
    and returns the list of exercise IDs to include.
    """
    df = df_exercise_type[df_exercise_type['type'] == 'multiple_choice']

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


def get_answer_column(unit, exercise):
    """
    Reads the mapping/levels CSV (with columns: unit, exercise, extent)
    and returns the list of exercise IDs to include.
    """
    df = df_exercise_type[df_exercise_type['type'] == 'multiple_choice']

    row = df.loc[(df['unit'] == unit) & (df['exercise'] == exercise)]
    if row.empty:
        raise ValueError(f"No mapping row for unit={unit} exercise={exercise}")

    answer_column = row.iloc[0]["answer_column"]

    return answer_column


def get_question_column(unit, exercise):
    """
    Reads the mapping/levels CSV (with columns: unit, exercise, extent)
    and returns the list of exercise IDs to include.
    """
    df = df_exercise_type[df_exercise_type['type'] == 'multiple_choice']

    row = df.loc[(df['unit'] == unit) & (df['exercise'] == exercise)]
    if row.empty:
        raise ValueError(f"No mapping row for unit={unit} exercise={exercise}")

    question_column = row.iloc[0]["question_column"]

    return question_column


def is_exercise_multiple_choice(unit, exercise):
    df = df_exercise_type
    return not df[
        (df['unit'] == unit) &
        (df['exercise'] == exercise) &
        (df['type'] == 'multiple_choice')
    ].empty


def is_exercise_synonym(unit, exercise):
    df = df_exercise_type
    return not df[
        (df['unit'] == unit) &
        (df['exercise'] == exercise) &
        (df['type'] == 'synonym')
    ].empty
