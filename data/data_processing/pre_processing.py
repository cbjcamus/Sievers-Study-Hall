import pandas as pd
from data.data_processing.exercises import praesens, praeteritum, imperativ, konjunktiv_II, konjunktiv_I


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

    elif exercise == konjunktiv_II:
        return pre_processing_konjunktiv_ii(data)

    elif exercise == konjunktiv_I:
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


'''
def pre_processing(data, exercise, level):
    if exercise == praeteritum and level > 1:
        data['answer'] = data['er/sie/es']
        return data

    processors = {
        praesens: pre_processing_praesens,
        (praeteritum, 1): pre_processing_praeteritum,
        imperativ: pre_processing_imperativ,
        konjunktiv_II: pre_processing_konjunktiv_ii,
        konjunktiv_I: pre_processing_konjunktiv_i,
    }

    processor = processors.get((exercise, level)) or processors.get(exercise)
    return processor(data) if processor else data
'''