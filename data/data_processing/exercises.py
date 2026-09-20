import os

import pandas as pd

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
EXERCISES_PATH = os.path.join(BASE_DIR, "datasets/other", "exercises.csv")
df_exercises = pd.read_csv(EXERCISES_PATH)

levels = ["A1", "A2", "B1", "B2", "C1", "C2",]

isolation = 'isolation'
context = 'context'
synonym = 'synonym'
antonym = 'antonym'

multiple_choice = 'multiple_choice'
multiple_choice_native = 'multiple_choice_native'
multiple_choice_target = 'multiple_choice_target'

word_order = 'word_order'
prompt = 'prompt'


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


def is_exercise_input(unit, exercise):
    df = df_exercises
    return not df[
        (df['unit'] == unit) &
        (df['exercise'] == exercise) &
        (df['category'] == 'input')
    ].empty


def is_exercise_synonym(unit, exercise):
    df = df_exercises
    return not df[
        (df['unit'] == unit) &
        (df['exercise'] == exercise) &
        (df['subcategory'] == 'synonym')
    ].empty


def is_exercise_multiple_choice(unit, exercise):
    df = df_exercises
    return not df[
        (df['unit'] == unit) &
        (df['exercise'] == exercise) &
        (df['category'] == 'multiple_choice')
        ].empty


def is_exercise_multiple_choice_native(unit, exercise):
    df = df_exercises
    return not df[
        (df['unit'] == unit) &
        (df['exercise'] == exercise) &
        (df['subcategory'] == 'multiple_choice_native')
        ].empty


def is_exercise_multiple_choice_target(unit, exercise):
    df = df_exercises
    return not df[
        (df['unit'] == unit) &
        (df['exercise'] == exercise) &
        (df['subcategory'] == 'multiple_choice_target')
        ].empty


def is_exercise_word_order(unit, exercise):
    df = df_exercises
    return not df[
        (df['unit'] == unit) &
        (df['exercise'] == exercise) &
        (df['category'] == 'word_order')
    ].empty


def is_exercise_prompt(unit, exercise):
    df = df_exercises
    return not df[
        (df['unit'] == unit) &
        (df['exercise'] == exercise) &
        (df['category'] == 'prompt')
    ].empty


def get_answer_column(unit, exercise, language):
    """
    Reads the mapping/levels CSV (with columns: unit, exercise, extent)
    and returns the list of exercise IDs to include.
    """

    if is_exercise_multiple_choice_native(unit, exercise):
        return language

    else:
        return 'answer'


def get_question_column(unit, exercise, language):
    """
    Reads the mapping/levels CSV (with columns: unit, exercise, extent)
    and returns the list of exercise IDs to include.
    """

    if is_exercise_multiple_choice_native(unit, exercise):
        return 'german'

    else:
        return language


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

    exercise_subcategory = row["subcategory"].iloc[0]

    if exercise_subcategory not in ["multiple_choice_target", "multiple_choice_native"]:
        return ''

    exercises = df[
        (df["unit"] == unit) &
        (df["level"] == level) &
        (df["subcategory"] == exercise_subcategory)
    ]["exercise"].tolist()

    return exercises


def does_unit_exercise_exist(unit, exercise, df=df_exercises):
    """
    Returns True if (unit, exercise) exists in df_exercises.
    """
    return (
        ((df["unit"] == unit) &
         (df["exercise"] == int(exercise)))
        .any()
    )


def get_category_from_exercise(unit, exercise, df=df_exercises):
    result = df[(df['unit'] == unit) & (df['exercise'] == exercise)]
    if not result.empty:
        return result.iloc[0]['category']
    return "N/A"


def get_subcategory_from_exercise(unit, exercise, df=df_exercises):
    result = df[(df['unit'] == unit) & (df['exercise'] == exercise)]
    if not result.empty:
        return result.iloc[0]['subcategory']
    return "N/A"