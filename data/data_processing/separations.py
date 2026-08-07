import os
import pandas as pd

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SEPARATIONS_PATH = os.path.join(BASE_DIR, "datasets/other", "separations.csv")
df_separations = pd.read_csv(SEPARATIONS_PATH)

separations = set(
    zip(df_separations["unit"], df_separations["exercise"])
)