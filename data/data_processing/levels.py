import pandas as pd
import os

from data.data_processing.paths import df_units

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LEVELS_PATH = os.path.join(BASE_DIR, "datasets/other", "levels.csv")
df_level = pd.read_csv(LEVELS_PATH)


def get_level_from_exercise(unit, exercise, df=df_level):
    result = df[(df['unit'] == unit) & (df['exercise'] == exercise)]
    if not result.empty:
        return result.iloc[0]['level']
    return "N/A"