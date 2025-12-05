import os
import pandas as pd

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SYNONYMS_PATH = os.path.join(BASE_DIR, "datasets/other", "synonyms.csv")
df_synonyms = pd.read_csv(SYNONYMS_PATH)


def get_list_of_synonyms_for_feedback(correct_answer, unit):
    """
    Retrieves a comma-separated list of synonyms corresponding to a given main answer.

    Loads a CSV file containing synonym mappings, filters rows where the 'unit' matches
    and the 'output' (main synonym) equals the given answer. Then joins all matching
    'input' entries (the synonyms) into a single comma-separated string.

    Args:
        correct_answer (str): The main synonym to find associated variants for.
        unit (str): The unit used to filter the relevant entries.
        file_path (str): Path to the synonyms CSV file (default is SYNONYMS_PATH).

    Returns:
        str: A comma-separated string of synonyms for the given answer.
    """
    filtered = df_synonyms[(df_synonyms['unit'] == unit) & (df_synonyms['output'] == correct_answer)]
    synonyms = ', '.join(filtered['input'])
    return synonyms
