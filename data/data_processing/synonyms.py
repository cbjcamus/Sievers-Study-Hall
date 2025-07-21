import os
import pandas as pd

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SYNONYMS_PATH = os.path.join(BASE_DIR, "datasets/other", "synonyms.csv")


def search_for_main_synonym(input_str, unit, csv_file=SYNONYMS_PATH):
    """
    Searches for the main synonym of a given input string based on a CSV mapping.

    Loads a CSV file containing synonym mappings, filters the entries for the specified unit,
    and creates a dictionary that maps lowercase input words to their main synonyms ("output").
    If the input string is found in the mapping, returns the corresponding synonym in lowercase.
    Otherwise, returns the original input string in lowercase.

    Args:
        input_str (str): The input string to look up.
        unit (str): The unit used to filter the relevant synonym entries.
        csv_file (str): Path to the synonyms CSV file (default is SYNONYMS_PATH).

    Returns:
        str: The main synonym for the input string, or the original string if no match is found.
    """
    df = pd.read_csv(csv_file)
    df = df[df['unit'] == unit]
    df['input'] = df['input'].str.lower()
    mapping = dict(zip(df["input"], df["output"]))
    return mapping.get(input_str, input_str).lower()


def get_list_of_synonyms_for_feedback(answer, unit, file_path=SYNONYMS_PATH):
    """
    Retrieves a comma-separated list of synonyms corresponding to a given main answer.

    Loads a CSV file containing synonym mappings, filters rows where the 'unit' matches
    and the 'output' (main synonym) equals the given answer. Then joins all matching
    'input' entries (the synonyms) into a single comma-separated string.

    Args:
        answer (str): The main synonym to find associated variants for.
        unit (str): The unit used to filter the relevant entries.
        file_path (str): Path to the synonyms CSV file (default is SYNONYMS_PATH).

    Returns:
        str: A comma-separated string of synonyms for the given answer.
    """
    df = pd.read_csv(file_path)
    filtered = df[(df['unit'] == unit) & (df['output'] == answer)]
    synonyms = ', '.join(filtered['input'])
    return synonyms
