import os
import pandas as pd

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SYNONYMS_PATH = os.path.join(BASE_DIR, "datasets/other", "synonyms.csv")


def search_for_main_synonym(input_str, exercise, csv_file=SYNONYMS_PATH):
    df = pd.read_csv(csv_file)
    df = df[df['exercise'] == exercise]
    mapping = dict(zip(df["input"], df["output"]))
    return mapping.get(input_str, input_str)


def get_list_of_synonyms(answer, exercise, file_path=SYNONYMS_PATH):
    df = pd.read_csv(file_path)
    filtered = df[(df['exercise'] == exercise) & (df['output'] == answer)]
    synonyms = ', '.join(filtered['input'])
    return synonyms
