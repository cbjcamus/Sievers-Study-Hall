import os

from data.data_processing.units import (praepositionen_grammatik, praepositionen_verben, praepositionen_adjektive,
                                        praepositionen_nomen, praepositionen_adverbien, praepositionen_artikel,
                                        artikel, pronomen, konnektoren, fragen, adverbien, adjektivdeklinationen,
                                        praesens, imperativ, partizip_II, praeteritum, praeteritum_partizip_II,
                                        konjunktiv_II, konjunktiv_I, partizip_I,
                                        verben, trennbare_verben, adjektive, deverbale_nomen,
                                        )

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

    adjektive: os.path.join(BASE_DIR, "datasets/adjektive", "adjektive.csv"),
    adjektivdeklinationen: os.path.join(BASE_DIR, "datasets/adjektive", "adjektivdeklinationen.csv"),

    trennbare_verben: os.path.join(BASE_DIR, "datasets/konjugation", "trennbare_verben.csv"),
    verben: os.path.join(BASE_DIR, "datasets/konjugation", "verben.csv"),

    praesens: os.path.join(BASE_DIR, "datasets/konjugation", "praesens.csv"),
    imperativ: os.path.join(BASE_DIR, "datasets/konjugation", "imperativ.csv"),
    partizip_II: os.path.join(BASE_DIR, "datasets/konjugation", "partizip_II.csv"),
    praeteritum: os.path.join(BASE_DIR, "datasets/konjugation", "praeteritum.csv"),
    praeteritum_partizip_II: os.path.join(BASE_DIR, "datasets/konjugation", "praeteritum_partizip_II.csv"),
    konjunktiv_II: os.path.join(BASE_DIR, "datasets/konjugation", "konjunktiv_II.csv"),
    konjunktiv_I: os.path.join(BASE_DIR, "datasets/konjugation", "konjunktiv_I.csv"),
    partizip_I: os.path.join(BASE_DIR, "datasets/konjugation", "partizip_I.csv"),

    deverbale_nomen: os.path.join(BASE_DIR, "datasets/wortschatz", "deverbale_substantive.csv"),
             }
