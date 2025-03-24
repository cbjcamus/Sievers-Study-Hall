import pandas as pd
import os
import random


BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PROVERBS_PATH = os.path.join(BASE_DIR, "datasets", "proverbs.csv")

proverbs = pd.read_csv(PROVERBS_PATH)


def get_random_proverb():
    proverb = proverbs.sample(1).iloc[0]
    return proverb


def get_text_proverb():
    proverb = get_random_proverb()
    random_number = random.random()
    if random_number > 0.9:
        text = (f"<b>{change_color(text='Proverb', color='#DAA520')}</b>"
                f"<br><br>{proverb['german']}"
                f"<br><br><i>{proverb['english']}</i>")
    else:
        text = ""
    return text


def change_color(text, color="#AEEEEE"):
    return f'<span style="color: {color};">{text}</span>'