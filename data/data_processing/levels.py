import pandas as pd
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LEVELS_PATH = os.path.join(BASE_DIR, "datasets/other", "levels.csv")


def get_level_from_exercise(unit, exercise, filepath=LEVELS_PATH):
    df = pd.read_csv(filepath)
    result = df[(df['unit'] == unit) & (df['exercise'] == exercise)]
    if not result.empty:
        return result.iloc[0]['level']
    return "N/A"