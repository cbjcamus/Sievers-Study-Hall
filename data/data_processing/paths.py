import os
import pandas as pd

from data.data_processing.units import (praepositionen_grammatik, praepositionen_verben, praepositionen_adjektive,
                                        praepositionen_nomen, praepositionen_adverbien, praepositionen_artikel,
                                        artikel, pronomen, konnektoren, fragen, adverbien, wortstellung,
                                        adjektive, adjektivdeklinationen,
                                        verben, trennbare_verben, nomen_verben_verbindungen,
                                        praesens, imperativ, partizip_II, praeteritum, praeteritum_partizip_II,
                                        konjunktiv_II, konjunktiv_I, partizip_I,
                                        artikel_genus, genus_routledge,
                                        units)

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


DATA_PATH = {
    praepositionen_grammatik: os.path.join(BASE_DIR, "datasets/praepositionen", "praepositionen_grammatik.csv"),
    praepositionen_verben: os.path.join(BASE_DIR, "datasets/praepositionen", "praepositionen_verben.csv"),
    praepositionen_adjektive: os.path.join(BASE_DIR, "datasets/praepositionen", "praepositionen_adjektive.csv"),
    praepositionen_nomen: os.path.join(BASE_DIR, "datasets/praepositionen", "praepositionen_nomen.csv"),
    praepositionen_adverbien: os.path.join(BASE_DIR, "datasets/praepositionen", "praepositionen_adverbien.csv"),
    praepositionen_artikel: os.path.join(BASE_DIR, "datasets/praepositionen", "praepositionen_artikel.csv"),

    artikel: os.path.join(BASE_DIR, "datasets/grammatik", "artikel.csv"),
    pronomen: os.path.join(BASE_DIR, "datasets/grammatik", "pronomen.csv"),
    konnektoren: os.path.join(BASE_DIR, "datasets/grammatik", "konnektoren.csv"),
    fragen: os.path.join(BASE_DIR, "datasets/grammatik", "fragen.csv"),
    adverbien: os.path.join(BASE_DIR, "datasets/grammatik", "adverbien.csv"),
    wortstellung: os.path.join(BASE_DIR, "datasets/grammatik", "wortstellung.csv"),

    adjektive: os.path.join(BASE_DIR, "datasets/adjektive", "adjektive.csv"),
    adjektivdeklinationen: os.path.join(BASE_DIR, "datasets/adjektive", "adjektivdeklinationen.csv"),

    verben: os.path.join(BASE_DIR, "datasets/verben", "verben.csv"),
    trennbare_verben: os.path.join(BASE_DIR, "datasets/verben", "trennbare_verben.csv"),
    nomen_verben_verbindungen: os.path.join(BASE_DIR, "datasets/verben", "nomen_verben_verbindungen.csv"),

    praesens: os.path.join(BASE_DIR, "datasets/konjugation", "praesens.csv"),
    imperativ: os.path.join(BASE_DIR, "datasets/konjugation", "imperativ.csv"),
    partizip_II: os.path.join(BASE_DIR, "datasets/konjugation", "partizip_II.csv"),
    praeteritum: os.path.join(BASE_DIR, "datasets/konjugation", "praeteritum.csv"),
    praeteritum_partizip_II: os.path.join(BASE_DIR, "datasets/konjugation", "praeteritum_partizip_II.csv"),
    konjunktiv_II: os.path.join(BASE_DIR, "datasets/konjugation", "konjunktiv_II.csv"),
    konjunktiv_I: os.path.join(BASE_DIR, "datasets/konjugation", "konjunktiv_I.csv"),
    partizip_I: os.path.join(BASE_DIR, "datasets/konjugation", "partizip_I.csv"),

    artikel_genus: os.path.join(BASE_DIR, "datasets/grammatik", "artikel_genus.csv"),
    genus_routledge: os.path.join(BASE_DIR, "datasets/genus", "genus_routledge.csv"),
}

df_units = {unit: pd.read_csv(DATA_PATH[unit]) for unit in units}
