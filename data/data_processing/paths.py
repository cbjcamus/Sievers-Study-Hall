import os

from data.data_processing.exercises import (praepositionen_grammatik, praepositionen_verben, praepositionen_adjektive,
                                            praepositionen_nomen,
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

    artikel: os.path.join(BASE_DIR, "datasets/grammatik", "artikel.csv"),
    pronomen: os.path.join(BASE_DIR, "datasets/grammatik", "pronomen.csv"),
    konnektoren: os.path.join(BASE_DIR, "datasets/grammatik", "konnektoren.csv"),
    fragen: os.path.join(BASE_DIR, "datasets/grammatik", "fragen.csv"),
    adverbien: os.path.join(BASE_DIR, "datasets/grammatik", "adverbien.csv"),
    adjektivdeklinationen: os.path.join(BASE_DIR, "datasets/grammatik", "adjektivdeklinationen.csv"),

    praesens: os.path.join(BASE_DIR, "datasets/konjugation", "praesens.csv"),
    imperativ: os.path.join(BASE_DIR, "datasets/konjugation", "imperativ.csv"),
    partizip_II: os.path.join(BASE_DIR, "datasets/konjugation", "partizip_II.csv"),
    praeteritum: os.path.join(BASE_DIR, "datasets/konjugation", "praeteritum.csv"),
    praeteritum_partizip_II: os.path.join(BASE_DIR, "datasets/konjugation", "praeteritum_partizip_II.csv"),
    konjunktiv_II: os.path.join(BASE_DIR, "datasets/konjugation", "konjunktiv_II.csv"),
    konjunktiv_I: os.path.join(BASE_DIR, "datasets/konjugation", "konjunktiv_I.csv"),
    partizip_I: os.path.join(BASE_DIR, "datasets/konjugation", "partizip_I.csv"),

    verben: os.path.join(BASE_DIR, "datasets/konjugation", "verben.csv"),
    trennbare_verben: os.path.join(BASE_DIR, "datasets/konjugation", "trennbare_verben.csv"),
    adjektive: os.path.join(BASE_DIR, "datasets/wortschatz", "adjektive.csv"),
    deverbale_nomen: os.path.join(BASE_DIR, "datasets/wortschatz", "deverbale_substantive.csv"),
             }

SCORE_PATH = {artikel: os.path.join(BASE_DIR, "scores/artikel", ""),
              pronomen: os.path.join(BASE_DIR, "scores/pronomen", ""),
              konnektoren: os.path.join(BASE_DIR, "scores/konnektoren", ""),
              praepositionen_grammatik: os.path.join(BASE_DIR, "scores/praepositionen_grammatik", ""),
              adjektivdeklinationen: os.path.join(BASE_DIR, "scores/adjektivdeklinationen", ""),

              praesens: os.path.join(BASE_DIR, "scores/praesens", ""),
              praepositionen_verben: os.path.join(BASE_DIR, "scores/praepositionen_konjugation", ""),
              imperativ: os.path.join(BASE_DIR, "scores/imperativ", ""),
              partizip_II: os.path.join(BASE_DIR, "scores/partizip_II", ""),
              praeteritum: os.path.join(BASE_DIR, "scores/praeteritum", ""),
              konjunktiv_II: os.path.join(BASE_DIR, "scores/konjunktiv", ""),

              verben: os.path.join(BASE_DIR, "scores/verben", ""),
              adjektive: os.path.join(BASE_DIR, "scores/adjektive", ""),
              adverbien: os.path.join(BASE_DIR, "scores/adverbien", ""),
              }
