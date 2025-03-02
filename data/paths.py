import os

from data.exercises import (artikel, pronomen, konnektoren, praepositionen_grammatik, adjektivDeklinationen,
                            praesens, praepositionen_konjugation, imperativ, perfekt, praeteritum, konjunktiv,
                            verben, adjektive, adverbien)

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_PATH = {artikel: os.path.join(BASE_DIR, "questions", "artikel.csv"),
             pronomen: os.path.join(BASE_DIR, "questions", "pronomen.csv"),
             konnektoren: os.path.join(BASE_DIR, "questions", "konnektoren.csv"),
             praepositionen_grammatik: os.path.join(BASE_DIR, "questions", "praepositionen_grammatik.csv"),
             adjektivDeklinationen: os.path.join(BASE_DIR, "questions", "adjektivdeklinationen.csv"),

             praesens: os.path.join(BASE_DIR, "questions", "praesens.csv"),
             praepositionen_konjugation: os.path.join(BASE_DIR, "questions", "praepositionen_konjugation.csv"),
             imperativ: os.path.join(BASE_DIR, "questions", "imperativ.csv"),
             perfekt: os.path.join(BASE_DIR, "questions", "perfekt.csv"),
             praeteritum: os.path.join(BASE_DIR, "questions", "praeteritum.csv"),
             konjunktiv: os.path.join(BASE_DIR, "questions", "konjunktiv.csv"),

             verben: os.path.join(BASE_DIR, "questions", "verben.csv"),
             adjektive: os.path.join(BASE_DIR, "questions", "adjektive.csv"),
             adverbien: os.path.join(BASE_DIR, "questions", "adverbien.csv"),
             }

SCORE_PATH = {artikel: os.path.join(BASE_DIR, "scores/artikel", ""),
              pronomen: os.path.join(BASE_DIR, "scores/pronomen", ""),
              konnektoren: os.path.join(BASE_DIR, "scores/konnektoren", ""),
              praepositionen_grammatik: os.path.join(BASE_DIR, "scores/praepositionen_grammatik", ""),
              adjektivDeklinationen: os.path.join(BASE_DIR, "scores/adjektivdeklinationen", ""),

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

EXERCISE_PAGES = {
    konnektoren: "/konnektoren",
    artikel: "/artikel",
    pronomen: "/pronomen",
    praepositionen_grammatik: "/praepositionen_grammatik",
    adjektivDeklinationen: "/adjektivdeklinationen",

    praesens: "/praesens",
    praepositionen_konjugation: "/praepositionen_konjugation",
    imperativ: "/imperativ",
    perfekt: "/perfekt",
    praeteritum: "/praeteritum",
    konjunktiv: "/konjunktiv",

    verben: "/verben",
    adjektive: "/adjektive",
    adverbien: "/adverbien",
}
