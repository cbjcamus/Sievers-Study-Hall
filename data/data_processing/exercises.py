import os

import pandas as pd

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
EXERCISES_PATH = os.path.join(BASE_DIR, "datasets/other", "exercises.csv")
df_exercises = pd.read_csv(EXERCISES_PATH)

levels = ["A1", "A2", "B1", "B2", "C1", "C2",]


def get_level_from_exercise(unit, exercise, df=df_exercises):
    result = df[(df['unit'] == unit) & (df['exercise'] == exercise)]
    if not result.empty:
        return result.iloc[0]['level']
    return "N/A"


def get_exercises_by_level(level, df_level=df_exercises):
    """
    Returns a dataframe filtered by unit and level.
    If no rows match, returns None.
    """

    df_filtered = df_level[(df_level["level"] == level)]

    if df_filtered.empty:
        return None

    return df_filtered


def get_exercises_by_unit_and_level(unit, level, df_level=df_exercises):
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


def is_exercise_multiple_choice(unit, exercise):
    df = df_exercises
    return not df[
        (df['unit'] == unit) &
        (df['exercise'] == exercise) &
        (df['type'].isin(['multiple_choice', 'multiple_choice_foreign']))
    ].empty


def is_exercise_multiple_choice_foreign(unit, exercise):
    df = df_exercises
    return not df[
        (df['unit'] == unit) &
        (df['exercise'] == exercise) &
        (df['type'] == 'multiple_choice_foreign')
    ].empty


def is_exercise_synonym(unit, exercise):
    df = df_exercises
    return not df[
        (df['unit'] == unit) &
        (df['exercise'] == exercise) &
        (df['type'] == 'synonym')
    ].empty


def is_exercise_input(unit, exercise):
    df = df_exercises
    return not df[
        (df['unit'] == unit) &
        (df['exercise'] == exercise) &
        (df['type'].isin(['input', 'synonym']))
    ].empty


def is_exercise_word_order(unit, exercise):
    df = df_exercises
    return not df[
        (df['unit'] == unit) &
        (df['exercise'] == exercise) &
        (df['type'] == 'word_order')
    ].empty


def get_answer_column(unit, exercise, language):
    """
    Reads the mapping/levels CSV (with columns: unit, exercise, extent)
    and returns the list of exercise IDs to include.
    """

    if is_exercise_multiple_choice_foreign(unit, exercise):
        return language

    else:
        return 'answer'

'''
    df = df_exercise_type[df_exercise_type['type'] == 'multiple_choice']

    row = df.loc[(df['unit'] == unit) & (df['exercise'] == exercise)]
    if row.empty:
        raise ValueError(f"No mapping row for unit={unit} exercise={exercise}")

    answer_column = row.iloc[0]["answer_column"]

    return answer_column
'''


def get_question_column(unit, exercise, language):
    """
    Reads the mapping/levels CSV (with columns: unit, exercise, extent)
    and returns the list of exercise IDs to include.
    """

    if is_exercise_multiple_choice_foreign(unit, exercise):
        return language

    else:
        return 'question'

'''

    df = df_exercise_type[df_exercise_type['type'] == 'multiple_choice']

    row = df.loc[(df['unit'] == unit) & (df['exercise'] == exercise)]
    if row.empty:
        raise ValueError(f"No mapping row for unit={unit} exercise={exercise}")

    question_column = row.iloc[0]["question_column"]

    return question_column
'''


def get_multiple_choice_extent(unit, exercise):
    """
    Reads the mapping/levels CSV (with columns: unit, exercise, extent)
    and returns the list of exercise IDs to include.
    """
    df = df_exercises

    level = get_level_from_exercise(unit, exercise, df=df)

    row = df[
        (df["unit"] == unit) &
        (df["exercise"] == exercise)
    ]

    if row.empty:
        return ''

    exercise_type = row["type"].iloc[0]

    if exercise_type not in ["multiple_choice", "multiple_choice_foreign"]:
        return ''

    exercises = df[
        (df["unit"] == unit) &
        (df["level"] == level) &
        (df["type"] == exercise_type)
    ]["exercise"].tolist()

    return exercises

'''
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

'''