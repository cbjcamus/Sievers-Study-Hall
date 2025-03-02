import numpy as np
import pandas as pd

from data.paths import DATA_PATH, SCORE_PATH
from data.exercises import praesens, praeteritum, imperativ, konjunktiv


def total_questions_by_exercise_and_level(exercise, level):
    data = pd.read_csv(DATA_PATH[exercise])
    data = data[data["level"] == level]
    total_questions = len(data)

    if exercise == praesens:
        total_questions = total_questions * 6

    return total_questions


def answered_questions_by_exercise_and_level(exercise, level, session=None):
    if session is None:
        try:
            path = f"{SCORE_PATH[exercise]}/level{level}.csv"
            scores = pd.read_csv(path)
            answered_questions = (scores["score"] == 1).sum()
        except FileNotFoundError:
            answered_questions = 0
        except pd.errors.EmptyDataError:
            answered_questions = 0
        return int(answered_questions)

    else:
        level = str(level)
        if exercise in session:
            if level in session[exercise]:
                return sum(session[exercise][level].values())
            else:
                return 0
        else:
            return 0


def total_questions_by_exercise(exercise):
    data = pd.read_csv(DATA_PATH[exercise])
    data = data.dropna(subset="level")
    total_questions = len(data)

    if exercise == praesens:
        total_questions = total_questions * 6

    return total_questions


def answered_questions_by_exercise(exercise, session=None):
    answered_questions = 0
    if session is None:
        for level in range(1, highest_level_exercise(exercise)+1):
            try:
                path = f"{SCORE_PATH[exercise]}/level{level}.csv"
                scores = pd.read_csv(path)
                answered_questions = answered_questions + (scores["score"] == 1).sum()
            except FileNotFoundError:
                pass
            except pd.errors.EmptyDataError:
                pass
        return int(answered_questions)
    else:
        for level in range(1, highest_level_exercise(exercise) + 1):
            answered_questions = answered_questions + answered_questions_by_exercise_and_level(exercise, level, session=session)
        return int(answered_questions)


def highest_level_exercise(exercise):
    data = pd.read_csv(DATA_PATH[exercise])
    highest_level = np.max(data["level"])
    return int(highest_level)


'''
def load_data(exercise, level):
    data = pd.read_csv(DATA_PATH[exercise])
    data = data[data["level"] == level]
    data = pre_processing(data, exercise)
    if exercise not in session:
        session[exercise] = {}
    if str(level) not in session[exercise]:
        session[exercise][str(level)] = {}
    answered_nrs = session[exercise][str(level)].keys()
    filtered_data = data[~data["Nr"].astype(str).isin(answered_nrs)]
    if filtered_data.empty:
        return None  # All questions answered
    return filtered_data.sample(1).iloc[0]
'''

def load_data(exercise, level):
    data = pd.read_csv(DATA_PATH[exercise])
    data = data[data["level"] == level]
    data = pre_processing(data, exercise, level)
    return data


def pick_a_question(session, exercise, level):
    data = load_data(exercise, level)
    if exercise not in session:
        session[exercise] = {}
    if str(level) not in session[exercise]:
        session[exercise][str(level)] = {}
    answered_nrs = session[exercise][str(level)].keys()
    filtered_data = data[~data["Nr"].astype(str).isin(answered_nrs)]
    if filtered_data.empty:
        return None  # All questions answered
    return filtered_data.sample(1).iloc[0]


def pre_processing(data, exercise, level):
    if exercise == praesens:
        persons = ['ich', 'du', 'er/sie/es', 'wir', 'ihr', 'Sie']
        new_rows = []

        for index, row in data.iterrows():
            for person in persons:
                new_row = row.drop(persons).to_dict()
                new_row['person'] = person
                new_row['answer'] = row[person]
                new_rows.append(new_row)

        data = pd.DataFrame(new_rows)
        data['Nr'] = range(1, len(data) + 1)

        return data

    elif exercise == praeteritum and level == 1:
        persons = ['ich', 'du', 'er/sie/es', 'wir', 'ihr', 'Sie']
        new_rows = []

        for index, row in data.iterrows():
            for person in persons:
                new_row = row.drop(persons).to_dict()
                new_row['person'] = person
                new_row['answer'] = row[person]
                new_rows.append(new_row)

        data = pd.DataFrame(new_rows)
        data['Nr'] = range(1, len(data) + 1)
        return data

    elif exercise == praeteritum and level > 1:
        data['answer'] = data['er/sie/es']
        return data

    elif exercise == imperativ:
        persons = ['du', 'ihr', 'Sie']
        new_rows = []

        for index, row in data.iterrows():
            for person in persons:
                new_row = row.drop(persons).to_dict()
                new_row['person'] = person
                new_row['answer'] = row[person]
                new_rows.append(new_row)

        data = pd.DataFrame(new_rows)
        data['Nr'] = range(1, len(data) + 1)
        return data

    elif exercise == konjunktiv:
        persons = ['ich', 'du', 'er/sie/es', 'wir', 'ihr', 'Sie']
        new_rows = []

        for index, row in data.iterrows():
            for person in persons:
                new_row = row.drop(persons).to_dict()
                new_row['person'] = person
                new_row['answer'] = row[person]
                new_rows.append(new_row)

        data = pd.DataFrame(new_rows)
        data['Nr'] = range(1, len(data) + 1)
        return data

    else:
        return data

