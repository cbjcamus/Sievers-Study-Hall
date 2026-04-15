import pandas as pd
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LEVELS_PATH = os.path.join(BASE_DIR, "datasets/other", "levels.csv")
df_level = pd.read_csv(LEVELS_PATH)

levels = ["A1", "A2", "B1", "B2", "C1", "C2",]


def get_level_from_exercise(unit, exercise, df=df_level):
    result = df[(df['unit'] == unit) & (df['exercise'] == exercise)]
    if not result.empty:
        return result.iloc[0]['level']
    return "N/A"


def get_exercises_by_level(level, df_level=df_level):
    """
    Returns a dataframe filtered by unit and level.
    If no rows match, returns None.
    """

    df_filtered = df_level[(df_level["level"] == level)]

    if df_filtered.empty:
        return None

    return df_filtered


def get_exercises_by_unit_and_level(unit, level, df_level=df_level):
    """
    Returns a dataframe filtered by unit and level.
    If no rows match, returns None.
    """

    df_filtered = df_level[
        (df_level["unit"] == unit) &
        (df_level["level"] == level)
    ]

    if df_filtered.empty:
        return None

    return df_filtered