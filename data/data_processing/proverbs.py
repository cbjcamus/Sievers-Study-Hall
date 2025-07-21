import pandas as pd
import os
import random

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PROVERBS_PATH = os.path.join(BASE_DIR, "datasets/other", "proverbs.csv")

proverbs = pd.read_csv(PROVERBS_PATH)


def get_text_proverb():
    """
    Returns a formatted proverb formatted_proverb with a 10% probability.

    Randomly selects a German proverb and its English translation using get_random_proverb().
    With a 10% chance (random number > 0.9), returns an HTML-formatted string:
    - "Proverb" label in bold and gold color.
    - German proverb.
    - English translation in italics.

    With 90% probability, returns None (i.e., no proverb shown).

    Returns:
        str or None: HTML-formatted proverb formatted_proverb or None.
    """
    proverb = get_random_proverb()
    random_number = random.random()
    if random_number > 0.9:
        formatted_proverb = (f"<b>{change_color(text='Proverb', color='#DAA520')}</b>" # #DAA520
                f"<br><br>{proverb['german']}"
                f"<br><br><i>{proverb['english']}</i>")
        return formatted_proverb
    else:
        return None


def get_random_proverb():
    """
    Randomly selects and returns a single proverb from the global 'proverbs' DataFrame.

    Returns:
        pandas.Series: A single row representing a proverb with its associated data.
    """
    proverb = proverbs.sample(1).iloc[0]
    return proverb


def change_color(text, color="#AEEEEE"):
    """
    Wraps the given text in a HTML <span> tag with a specified text color.

    Args:
        text (str): The text to be styled.
        color (str): A hex color code to apply to the text (default is light blue "#AEEEEE").

    Returns:
        str: HTML-formatted string with the specified color.
    """
    return f'<span style="color: {color};">{text}</span>'