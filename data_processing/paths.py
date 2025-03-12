import os

from data_processing.exercises import (artikel, pronomen, konnektoren, praepositionen_grammatik, adjektivdeklinationen,
                                       praesens, praepositionen_konjugation, imperativ, perfekt, praeteritum, konjunktiv,
                                       partizip_I,
                                       adverbien, verben, trennbare_verben, adjektive, deverbale_substantive)

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

DATA_PATH = {artikel: os.path.join(BASE_DIR, "datasets", "artikel.csv"),
             pronomen: os.path.join(BASE_DIR, "datasets", "pronomen.csv"),
             konnektoren: os.path.join(BASE_DIR, "datasets", "konnektoren.csv"),
             praepositionen_grammatik: os.path.join(BASE_DIR, "datasets", "praepositionen_grammatik.csv"),
             adjektivdeklinationen: os.path.join(BASE_DIR, "datasets", "adjektivdeklinationen.csv"),

             praesens: os.path.join(BASE_DIR, "datasets", "praesens.csv"),
             praepositionen_konjugation: os.path.join(BASE_DIR, "datasets", "praepositionen_konjugation.csv"),
             imperativ: os.path.join(BASE_DIR, "datasets", "imperativ.csv"),
             perfekt: os.path.join(BASE_DIR, "datasets", "perfekt.csv"),
             praeteritum: os.path.join(BASE_DIR, "datasets", "praeteritum.csv"),
             konjunktiv: os.path.join(BASE_DIR, "datasets", "konjunktiv.csv"),
             partizip_I: os.path.join(BASE_DIR, "datasets", "partizip_I.csv"),

             adverbien: os.path.join(BASE_DIR, "datasets", "adverbien.csv"),
             verben: os.path.join(BASE_DIR, "datasets", "verben.csv"),
             trennbare_verben: os.path.join(BASE_DIR, "datasets", "trennbare_verben.csv"),
             adjektive: os.path.join(BASE_DIR, "datasets", "adjektive.csv"),
             deverbale_substantive: os.path.join(BASE_DIR, "datasets", "deverbale_substantive.csv"),
             }

EXERCISE_PAGES = {
    konnektoren: "/konnektoren",
    artikel: "/artikel",
    pronomen: "/pronomen",
    praepositionen_grammatik: "/praepositionen_grammatik",
    adjektivdeklinationen: "/adjektivdeklinationen",

    praesens: "/praesens",
    praepositionen_konjugation: "/praepositionen_konjugation",
    imperativ: "/imperativ",
    perfekt: "/perfekt",
    praeteritum: "/praeteritum",
    konjunktiv: "/konjunktiv",
    partizip_I: "/partizip_I",

    adverbien: "/adverbien",
    verben: "/verben",
    trennbare_verben: "/trennbare_verben",
    adjektive: "/adjektive",
    deverbale_substantive: "/deverbale_substantive",
}

SCORE_PATH = {artikel: os.path.join(BASE_DIR, "scores/artikel", ""),
              pronomen: os.path.join(BASE_DIR, "scores/pronomen", ""),
              konnektoren: os.path.join(BASE_DIR, "scores/konnektoren", ""),
              praepositionen_grammatik: os.path.join(BASE_DIR, "scores/praepositionen_grammatik", ""),
              adjektivdeklinationen: os.path.join(BASE_DIR, "scores/adjektivdeklinationen", ""),

              praesens: os.path.join(BASE_DIR, "scores/praesens", ""),
              praepositionen_konjugation: os.path.join(BASE_DIR, "scores/praepositionen_konjugation", ""),
              imperativ: os.path.join(BASE_DIR, "scores/imperativ", ""),
              perfekt: os.path.join(BASE_DIR, "scores/perfekt", ""),
              praeteritum: os.path.join(BASE_DIR, "scores/praeteritum", ""),
              konjunktiv: os.path.join(BASE_DIR, "scores/konjunktiv", ""),

              verben: os.path.join(BASE_DIR, "scores/verben", ""),
              adjektive: os.path.join(BASE_DIR, "scores/adjektive", ""),
              adverbien: os.path.join(BASE_DIR, "scores/adverbien", ""),
              }