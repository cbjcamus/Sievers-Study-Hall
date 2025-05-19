import pandas as pd
import os
import random

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PROVERBS_PATH = os.path.join(BASE_DIR, "datasets/other", "proverbs.csv")

proverbs = pd.read_csv(PROVERBS_PATH)


def get_text_proverb():
    proverb = get_random_proverb()
    random_number = random.random()
    if random_number > 0.9:
        text = (f"<b>{change_color(text='Proverb', color='#850fbf')}</b>" # #DAA520
                f"<br><br>{proverb['german']}"
                f"<br><br><i>{proverb['english']}</i>")
        return text
    else:
        return None


def get_random_proverb():
    proverb = proverbs.sample(1).iloc[0]
    return proverb


def change_color(text, color="#AEEEEE"):
    return f'<span style="color: {color};">{text}</span>'