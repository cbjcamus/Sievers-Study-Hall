import pandas as pd
from data.data_processing.units import praesens, praeteritum, imperativ, konjunktiv_II, konjunktiv_I


def pre_processing(data, unit, exercise):
    if unit == praesens:
        return pre_processing_praesens(data)

    elif unit == praeteritum:
        return pre_processing_praeteritum(data, exercise)

    elif unit == imperativ:
        return pre_processing_imperativ(data)

    elif unit == konjunktiv_II:
        return pre_processing_konjunktiv_ii(data)

    elif unit == konjunktiv_I:
        return pre_processing_konjunktiv_i(data)

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


def pre_processing_praeteritum(data, exercise):

    if exercise == 1:
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

    else:
        data['answer'] = data['er/sie/es'].copy()

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


def pre_processing_konjunktiv_ii(data):
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


def pre_processing_konjunktiv_i(data):
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
