import os

import pandas as pd

from data.data_processing.units import (
    praepositionen, praepositionen_verben, praepositionen_adjektive, praepositionen_nomen, pronominaladverbien,
    artikel, pronomen, praepositionen_artikel, verben_artikel,
    konnektoren, fragen, adverbien, wortstellung,
    genus_regeln, genus, plural,
    adjektive, komparativ_superlativ, adjektivdeklinationen, adjektive_konjunktionen,
    verben, trennbare_verben, nomen_verben_verbindungen,
    praesens, imperativ, partizip_II, praeteritum, konjunktiv_II, konjunktiv_I, partizip_I,
    nomen_verben_wortstaemme, adjektive_verben_wortstaemme, adjektive_nomen_wortstaemme,
    zahlen,
    units,
)

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


DATA_PATH = {
    praepositionen: os.path.join(BASE_DIR, "datasets/praepositionen", "praepositionen.csv"),
    praepositionen_verben: os.path.join(BASE_DIR, "datasets/praepositionen", "praepositionen_verben.csv"),
    praepositionen_adjektive: os.path.join(BASE_DIR, "datasets/praepositionen", "praepositionen_adjektive.csv"),
    praepositionen_nomen: os.path.join(BASE_DIR, "datasets/praepositionen", "praepositionen_nomen.csv"),
    pronominaladverbien: os.path.join(BASE_DIR, "datasets/praepositionen", "pronominaladverbien.csv"),

    artikel: os.path.join(BASE_DIR, "datasets/artikel_pronomen_kasus", "artikel.csv"),
    pronomen: os.path.join(BASE_DIR, "datasets/artikel_pronomen_kasus", "pronomen.csv"),
    praepositionen_artikel: os.path.join(BASE_DIR, "datasets/artikel_pronomen_kasus", "praepositionen_artikel.csv"),
    verben_artikel: os.path.join(BASE_DIR, "datasets/artikel_pronomen_kasus", "verben_artikel.csv"),

    konnektoren: os.path.join(BASE_DIR, "datasets/satzbildung", "konnektoren.csv"),
    fragen: os.path.join(BASE_DIR, "datasets/satzbildung", "fragen.csv"),
    adverbien: os.path.join(BASE_DIR, "datasets/satzbildung", "adverbien.csv"),
    wortstellung: os.path.join(BASE_DIR, "datasets/satzbildung", "wortstellung.csv"),

    genus_regeln: os.path.join(BASE_DIR, "datasets/genus", "genus_regeln.csv"),
    genus: os.path.join(BASE_DIR, "datasets/genus", "genus.csv"),
    plural: os.path.join(BASE_DIR, "datasets/genus", "plural.csv"),

    adjektive: os.path.join(BASE_DIR, "datasets/adjektive", "adjektive.csv"),
    komparativ_superlativ: os.path.join(BASE_DIR, "datasets/adjektive", "komparativ_superlativ.csv"),
    adjektivdeklinationen: os.path.join(BASE_DIR, "datasets/adjektive", "adjektivdeklinationen.csv"),
    adjektive_konjunktionen: os.path.join(BASE_DIR, "datasets/adjektive", "adjektive_konjunktionen.csv"),

    verben: os.path.join(BASE_DIR, "datasets/verben", "verben.csv"),
    trennbare_verben: os.path.join(BASE_DIR, "datasets/verben", "trennbare_verben.csv"),
    nomen_verben_verbindungen: os.path.join(BASE_DIR, "datasets/verben", "nomen_verben_verbindungen.csv"),

    praesens: os.path.join(BASE_DIR, "datasets/konjugation", "praesens.csv"),
    imperativ: os.path.join(BASE_DIR, "datasets/konjugation", "imperativ.csv"),
    partizip_II: os.path.join(BASE_DIR, "datasets/konjugation", "partizip_II.csv"),
    praeteritum: os.path.join(BASE_DIR, "datasets/konjugation", "praeteritum.csv"),
    konjunktiv_II: os.path.join(BASE_DIR, "datasets/konjugation", "konjunktiv_II.csv"),
    konjunktiv_I: os.path.join(BASE_DIR, "datasets/konjugation", "konjunktiv_I.csv"),
    partizip_I: os.path.join(BASE_DIR, "datasets/konjugation", "partizip_I.csv"),

    nomen_verben_wortstaemme: os.path.join(BASE_DIR, "datasets/wortstaemme", "nomen_verben_wortstaemme.csv"),
    adjektive_verben_wortstaemme: os.path.join(BASE_DIR, "datasets/wortstaemme", "adjektive_verben_wortstaemme.csv"),
    adjektive_nomen_wortstaemme: os.path.join(BASE_DIR, "datasets/wortstaemme", "adjektive_nomen_wortstaemme.csv"),

    zahlen: os.path.join(BASE_DIR, "datasets/sonstige", "zahlen.csv"),
}

df_units = {unit: pd.read_csv(DATA_PATH[unit]) for unit in units}
