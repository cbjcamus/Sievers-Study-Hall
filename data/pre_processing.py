import numpy as np
import pandas as pd
from data.exercises import praesens, praeteritum, imperativ, konjunktiv


def pre_processing(data, exercise, level):
    if exercise == praesens:
        return pre_processing_praesens(data)

    elif exercise == praeteritum and level == 1:
        return pre_processing_praeteritum(data)

    elif exercise == praeteritum and level > 1:
        data['answer'] = data['er/sie/es']
        return data

    elif exercise == imperativ:
        return pre_processing_imperativ(data)

    elif exercise == konjunktiv:
        return pre_processing_konjunktiv(data)

    else:
        return data


def pre_processing_praesens(data):
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


def pre_processing_praeteritum(data):
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


def pre_processing_imperativ(data):
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


def pre_processing_konjunktiv(data):
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
