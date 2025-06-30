import os
import pandas as pd

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SYNONYMS_PATH = os.path.join(BASE_DIR, "datasets/other", "synonyms.csv")


def search_for_main_synonym(input_str, unit, csv_file=SYNONYMS_PATH):
    df = pd.read_csv(csv_file)
    df = df[df['unit'] == unit]
    df['input'] = df['input'].str.lower()
    mapping = dict(zip(df["input"], df["output"]))
    return mapping.get(input_str, input_str).lower()


def get_list_of_synonyms(answer, unit, file_path=SYNONYMS_PATH):
    df = pd.read_csv(file_path)
    filtered = df[(df['unit'] == unit) & (df['output'] == answer)]
    synonyms = ', '.join(filtered['input'])
    return synonyms
