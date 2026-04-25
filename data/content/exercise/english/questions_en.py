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
)

# bullet point \u25CF
# arrow &#8594

QUESTION_UNIT_EN = {
    pronominaladverbien:
        "{question}"
        "<br><br><i>{english}</i>",

    praepositionen_artikel:
        "{question} \u25CF {preposition} \u25CF {person}"
        "<br><br><i>{english}</i>",

    verben_artikel:
        "{question} \u25CF {person}"
        "<br><br><i>{english}</i>",

    wortstellung:
        "Placeholder",

    komparativ_superlativ:
        "{german}"
        "<br><br><i>{english}</i>",

    adjektive_konjunktionen:
        "{question}"
        "<br><br><i>{english}</i>",

    nomen_verben_verbindungen:
        "{question}"
        "<br><br><i>{english}</i>",

    praesens:
        "{german} \u25CF {person} _____"
        "<br><br><i>{english}</i>",

    partizip_II:
        "{german}"
        "<br><br><i>{english}</i>",

    praeteritum:
        "{german} \u25CF {person} _____"
        "<br><br><i>{english}</i>",

    imperativ:
        "{german} \u25CF {person} \u25CF _____"
        "<br><br><i>{english}</i>",

    konjunktiv_II:
        "{german} \u25CF {person} _____"
        "<br><br><i>{english}</i>",

    konjunktiv_I:
        "{german} \u25CF {person} _____"
        "<br><br><i>{english}</i>",

    partizip_I:
        "{german}"
        "<br><br><i>{english}</i>",

    adjektive_verben_wortstaemme:
        "{root_english} → {question}"
        "<br><br>{english} → _____",

    adjektive_nomen_wortstaemme:
        "{root_english} → {question}"
        "<br><br>{english} → _____",

    nomen_verben_wortstaemme:
        "{root_english} → {question}"
        "<br><br>{english} → _____",

    genus_regeln:
        "{question}"
        "<br><br><i>{english}</i>",

    genus:
        "{question}"
        "<br><br><i>{english}</i>",

    plural:
        "Singular: {question}"
        "<br><br>Plural: die _____"
        "<br><br><i>{english}</i>",
}


QUESTION_EXERCISE_EN = {
    praepositionen: {
        1: "{question}"
           "<br><br><i>{english}</i>",
        2: "{question}"
           "<br><br><i>{english}</i>",
        3: "{question}"
           "<br><br><i>{english}</i>",
        4: "{question}"
           "<br><br><i>{english}</i>",

        5: "{question}"
           "<br><br><i>{english}</i>",
        6: "{question}"
           "<br><br><i>{english}</i>",
        7: "{question}"
           "<br><br><i>{english}</i>",
        8: "{question}"
           "<br><br><i>{english}</i>",

        9: "{question}"
           "<br><br><i>{english}</i>",
        10: "{question}"
            "<br><br><i>{english}</i>",
        11: "{english}",
        12: "{question}"
            "<br><br><i>{english}</i>",

        13: "{question}"
            "<br><br><i>{english}</i>",
        14: "{question}"
            "<br><br><i>{english}</i>",
        15: "{english}",
        16: "{question}"
            "<br><br><i>{english}</i>",

        17: "{question}"
            "<br><br><i>{english}</i>",
        18: "{question}"
            "<br><br><i>{english}</i>",
        19: "{question}"
            "<br><br><i>{english}</i>",
        20: "{question}"
            "<br><br><i>{english}</i>",
        21: "{english}",
        22: "{question}"
            "<br><br><i>{english}</i>",
        23: "{english}",
        24: "{question}"
            "<br><br><i>{english}</i>",
        25: "{english}",
        26: "{question}"
            "<br><br><i>{english}</i>",
        27: "{english}",
        28: "{question}"
            "<br><br><i>{english}</i>",
        29: "{question}"
            "<br><br><i>\"{german}\"</i>",
        30: "{german}",
    },

    praepositionen_verben: {
        1: "{english} = {question}",
        2: "{question}"
           "<br><br><i>{english}</i>",
        3: "{english} = {question}",
        4: "{question}"
           "<br><br><i>{english}</i>",

        5: "{english} = {question}",
        6: "{question}"
           "<br><br><i>{english}</i>",
        7: "{english} = {question}",
        8: "{question}"
           "<br><br><i>{english}</i>",

        9: "{english} = {question}",
        10: "{question}"
            "<br><br><i>{english}</i>",
        11: "{english} = {question}",
        12: "{question}"
            "<br><br><i>{english}</i>",
        13: "{english} = {question}",
        14: "{question}"
            "<br><br><i>{english}</i>",
        15: "{english} = {question}",
        16: "{question}"
            "<br><br><i>{english}</i>",

        17: "{english} = {question}",
        18: "{question}"
            "<br><br><i>{english}</i>",
        19: "{english} = {question}",
        20: "{question}"
            "<br><br><i>{english}</i>",
        21: "{english} = {question}",
        22: "{question}"
            "<br><br><i>{english}</i>",
        23: "{english} = {question}",
        24: "{question}"
            "<br><br><i>{english}</i>",

        25: "{english} = {question}",
        26: "{question}"
            "<br><br><i>{english}</i>",
        27: "{english} = {question}",
        28: "{question}"
            "<br><br><i>{english}</i>",
        29: "{english} = {question}",
        30: "{question}"
            "<br><br><i>{english}</i>",
        31: "{english} = {question}",
        32: "{question}"
            "<br><br><i>{english}</i>",

        33: "{english} = {question}",
        34: "{question}"
            "<br><br><i>{english}</i>",
        35: "{english} = {question}",
        36: "{question}"
            "<br><br><i>{english}</i>",
        37: "{english} = {question}",
        38: "{question}"
            "<br><br><i>{english}</i>",
        39: "{english} = {question}",
        40: "{question}"
            "<br><br><i>{english}</i>",
    },

    praepositionen_adjektive: {
        1: "{english} = {question}",
        2: "{question}"
           "<br><br><i>{english}</i>",
        3: "{english} = {question}",
        4: "{question}"
           "<br><br><i>{english}</i>",

        5: "{english} = {question}",
        6: "{question}"
           "<br><br><i>{english}</i>",
        7: "{english} = {question}",
        8: "{question}"
           "<br><br><i>{english}</i>",
        9: "{english} = {question}",
        10: "{question}"
            "<br><br><i>{english}</i>",

        11: "{english} = {question}",
        12: "{question}"
            "<br><br><i>{english}</i>",
        13: "{english} = {question}",
        14: "{question}"
            "<br><br><i>{english}</i>",
        15: "{english} = {question}",
        16: "{question}"
            "<br><br><i>{english}</i>",

        17: "{english} = {question}",
        18: "{question}"
            "<br><br><i>{english}</i>",
        19: "{english} = {question}",
        20: "{question}"
            "<br><br><i>{english}</i>",
        21: "{english} = {question}",
        22: "{question}"
            "<br><br><i>{english}</i>",
    },

    praepositionen_nomen: {
        1: "{english} = {question}",
        2: "{question}"
           "<br><br><i>{english}</i>",
        3: "{english} = {question}",
        4: "{question}"
           "<br><br><i>{english}</i>",

        5: "{english} = {question}",
        6: "{question}"
           "<br><br><i>{english}</i>",
        7: "{english} = {question}",
        8: "{question}"
           "<br><br><i>{english}</i>",
        9: "{english} = {question}",
        10: "{question}"
            "<br><br><i>{english}</i>",
        11: "{english} = {question}",
        12: "{question}"
            "<br><br><i>{english}</i>",

        13: "{english} = {question}",
        14: "{question}"
            "<br><br><i>{english}</i>",
        15: "{english} = {question}",
        16: "{question}"
            "<br><br><i>{english}</i>",
        17: "{english} = {question}",
        18: "{question}"
            "<br><br><i>{english}</i>",
        19: "{english} = {question}",
        20: "{question}"
            "<br><br><i>{english}</i>",
        21: "{english} = {question}",
        22: "{question}"
            "<br><br><i>{english}</i>",
        23: "{english} = {question}",
        24: "{question}"
            "<br><br><i>{english}</i>",
        25: "{english} = {question}",
        26: "{question}"
            "<br><br><i>{english}</i>",
        27: "{english} = {question}",
        28: "{question}"
            "<br><br><i>{english}</i>",

        29: "{english} = {question}",
        30: "{question}"
            "<br><br><i>{english}</i>",
    },

    artikel: {
        1: "{german} \u25CF {gender_english} \u25CF {case_english}",
        2: "{question} \u25CF {gender_english} \u25CF {case_english}"
           "<br><br><i>{english}</i>",
        3: "{question} \u25CF {gender_english} \u25CF {case_english}"
           "<br><br><i>{english}</i>",
        4: "{question} \u25CF {gender_english} \u25CF {case_english}"
           "<br><br><i>{english}</i>",
        5: "{question} \u25CF {gender_english} \u25CF {case_english}"
           "<br><br><i>{english}</i>",
        6: "{question} \u25CF {gender_english} \u25CF {case_english}"
           "<br><br><i>{english}</i>",
        7: "{question} \u25CF {gender_english} \u25CF {case_english}"
           "<br><br><i>{english}</i>",
        8: "{question} \u25CF {gender_english} \u25CF {case_english}"
           "<br><br><i>{english}</i>",
        9: "{question} \u25CF {gender_english} \u25CF {case_english}"
           "<br><br><i>{english}</i>",
        10: "{question} \u25CF {gender_english} \u25CF {case_english}"
            "<br><br><i>{english}</i>",
        11: "{question} \u25CF {gender_english} \u25CF {case_english}"
            "<br><br><i>{english}</i>",
        12: "{german} \u25CF {gender_english} \u25CF {case_english}",
        13: "{question} \u25CF {gender_english} \u25CF {case_english}"
            "<br><br><i>{english}</i>",
        14: "{question} \u25CF {gender_english} \u25CF {case_english}"
            "<br><br><i>{english}</i>",
        15: "{question} \u25CF {gender_english} \u25CF {case_english}"
            "<br><br><i>{english}</i>",
        16: "{question} \u25CF {gender_english} \u25CF {case_english}"
            "<br><br><i>{english}</i>",
        17: "{question} \u25CF {gender_english} \u25CF {case_english}"
            "<br><br><i>{english}</i>",
        18: "{question} \u25CF {gender_english} \u25CF {case_english}"
            "<br><br><i>{english}</i>",
        19: "{question} \u25CF {gender_english} \u25CF {case_english}"
            "<br><br><i>{english}</i>",
        20: "{question} \u25CF {gender_english} \u25CF {case_english}"
            "<br><br><i>{english}</i>",
        21: "{german} \u25CF {gender_english}, {case_english}",
        22: "{question}"
            "<br><br><i>{english}</i>",
        23: "{german} \u25CF {gender_english}, {case_english}",
        24: "{question}"
            "<br><br><i>{english}</i>",
        25: "{german} \u25CF {gender_english}, {case_english}",
        26: "{question}"
            "<br><br><i>{english}</i>",

        27: "{german} \u25CF {gender_english}, {case_english}",
        28: "{question}"
            "<br><br><i>{english}</i>",
        29: "{german} \u25CF {gender_english}, {case_english}",
        30: "{question}"
            "<br><br><i>{english}</i>",
        31: "{english}",
        32: "{question}"
            "<br><br><i>{english}</i>",

        33: "{german} \u25CF {gender_english}, {case_english}",
        34: "{question}"
            "<br><br><i>{english}</i>",
        35: "{german} \u25CF {gender_english}, {case_english}",
        36: "{question}"
            "<br><br><i>{english}</i>",
        37: "{german} \u25CF {gender_english}, {case_english}",
        38: "{question} \u25CF {person}" 
            "<br><br><i>{english}</i>",

        39: "{german} \u25CF {gender_english}, {case_english}",
        40: "{question}"
            "<br><br><i>{english}</i>",

        41: "{german} \u25CF {gender_english}, {case_english}",
        42: "{question}"
            "<br><br><i>{english}</i>",
        43: "{question}"
            "<br><br><i>{english}</i>"
            "<br><br>Article: {person}",
        44: "{question}"
            "<br><br><i>{english}</i>"
            "<br><br>Article: {person}",
    },

    pronomen: {
        1: "{english}",
        2: "{question}"
           "<br><br><i>{english}</i>",
        3: "{english}",
        4: "{question}"
           "<br><br><i>{english}</i>",
        5: "{english}",
        6: "{question}"
           "<br><br><i>{english}</i>",
        7: "{question}"
           "<br><br><i>{english}</i>",
        8: "{question}"
           "<br><br><i>{english}</i>",
        9: "{question} \u25CF {person}"
           "<br><br><i>{english}</i>",
        10: "{question} \u25CF {person}"
            "<br><br><i>{english}</i>",

        11: "{english} \u25CF {case_english}",
        12: "{question}"
            "<br><br><i>{english}</i>",
        13: "{question}"
            "<br><br><i>{english}</i>",
        14: "{question}"
            "<br><br><i>{english}</i>",

        15: "{english}",
        16: "{question}"
            "<br><br><i>{english}</i>",
        17: "{gender_english} \u25CF {case_english}",
        18: "{question}"
            "<br><br><i>{english}</i>",
        19: "{question}"
            "<br><br><i>{english}</i>",
        20: "{question}"
            "<br><br><i>{english}</i>",
        21: "{question}"
            "<br><br><i>{english}</i>",
        22: "{question}"
            "<br><br><i>{english}</i>",
        23: "{question}"
            "<br><br><i>{english}</i>",

        24: "{english}",
        25: "{question}"
            "<br><br><i>{english}</i>",
        26: "{english} \u25CF {case_english}",
        27: "{question}"
            "<br><br><i>{english}</i>",
        28: "{question}"
            "<br><br><i>{english}</i>",
        29: "{question}"
            "<br><br><i>{english}</i>",
        30: "{question}"
            "<br><br><i>{english}</i>",
        31: "{german} \u25CF {gender_english}, {case_english}",
        32: "{question}"
            "<br><br><i>{english}</i>",
        33: "{german} \u25CF {gender_english}, {case_english}",
        34: "{question}"
            "<br><br><i>{english}</i>",

        35: "{english}",
        36: "{question}"
            "<br><br><i>{english}</i>",
        37: "{english}",
        38: "{question}"
            "<br><br><i>{english}</i>",
        39: "{question}"
            "<br><br><i>{english}</i>",

        40: "{english}, {gender_english}, {case_english}",
        41: "{question} \u25CF {gender_english}"
            "<br><br><i>{english}</i>",
        42: "{english}, {gender_english}, {case_english}",
        43: "{question} \u25CF {gender_english}"
            "<br><br><i>{english}</i>",
    },

    konnektoren: {
        1: "{english} \u25CF {case_english}",
        2: "{question}"
           "<br><br><i>{english}</i>",

        3: "{english} \u25CF {case_english}",
        4: "{question}"
           "<br><br><i>{english}</i>",

        5: "{english} \u25CF {case_english}",
        6: "{question}"
           "<br><br><i>{english}</i>",
        7: "{english} \u25CF {case_english}",
        8: "{question}"
           "<br><br><i>{english}</i>",
        9: "{english} \u25CF {case_english}",
        10: "{question}"
            "<br><br><i>{english}</i>",
        11: "{question}"
            "<br><br><i>\"{german}\"</i>",

        12: "{english} \u25CF {case_english}",
        13: "{question}"
            "<br><br><i>{english}</i>",
        14: "{english} \u25CF {case_english}",
        15: "{question}"
            "<br><br><i>{english}</i>",
        16: "{english} \u25CF {case_english}",
        17: "{question}"
            "<br><br><i>{english}</i>",
        18: "{question}"
            "<br><br><i>\"{german}\"</i>",

        19: "{english} \u25CF {case_english}",
        20: "{question}"
            "<br><br><i>{english}</i>",
        21: "{english} \u25CF {case_english}",
        22: "{question}"
            "<br><br><i>{english}</i>",
        23: "{english} \u25CF {case_english}",
        24: "{question}"
            "<br><br><i>{english}</i>",
        25: "{english} \u25CF {case_english}",
        26: "{question}"
            "<br><br><i>{english}</i>",
        27: "{english} \u25CF {case_english}",
        28: "{question}"
            "<br><br><i>{english}</i>",
        29: "{question}"
            "<br><br><i>\"{german}\"</i>",
        30: "{question}"
            "<br><br><i>\"{german}\"</i>",
        31: "{question}"
            "<br><br><i>\"{german}\"</i>",
        32: "{question}"
            "<br><br><i>\"{german}\"</i>",
    },

    fragen: {
        1: "{english}",
        2: "{question}"
           "<br><br><i>{english}</i>",

        3: "{english}",
        4: "{question}"
           "<br><br><i>{english}</i>",

        5: "{english}",
        6: "{question}"
           "<br><br><i>{english}</i>",

        7: "{english}",
        8: "{question}"
           "<br><br><i>{english}</i>",
        9: "{english}",
        10: "{question}"
            "<br><br><i>{english}</i>",

        11: "{english}",
        12: "{question}"
            "<br><br><i>{english}</i>",
        13: "{english}",
        14: "{question}"
            "<br><br><i>{english}</i>",

        15: "{english}",
        16: "{question}"
            "<br><br><i>{english}</i>",
    },

    adverbien: {
        1: "{english}",
        2: "{question}"
           "<br><br><i>{english}</i>",
        3: "{english}",
        4: "{question}"
           "<br><br><i>{english}</i>",

        5: "{english}",
        6: "{question}"
           "<br><br><i>{english}</i>",
        7: "{english}",
        8: "{question}"
           "<br><br><i>{english}</i>",
        9: "{question}"
            "<br><br><i>\"{german}\"</i>",
        10: "{german}",

        11: "{english}",
        12: "{question}"
            "<br><br><i>{english}</i>",
        13: "{english}",
        14: "{question}"
            "<br><br><i>{english}</i>",
        15: "{english}",
        16: "{question}"
            "<br><br><i>{english}</i>",
        17: "{english}",
        18: "{question}"
            "<br><br><i>{english}</i>",
        19: "{question}"
            "<br><br><i>\"{german}\"</i>",
        20: "{german}",

        21: "{english}",
        22: "{question}"
            "<br><br><i>{english}</i>",
        23: "{english}",
        24: "{question}"
            "<br><br><i>{english}</i>",
        25: "{english}",
        26: "{question}"
            "<br><br><i>{english}</i>",
        27: "{english}",
        28: "{question}"
            "<br><br><i>{english}</i>",
        29: "{question}"
            "<br><br><i>\"{german}\"</i>",
        30: "{german}",

        31: "{english}",
        32: "{question}"
            "<br><br><i>{english}</i>",
        33: "{english}",
        34: "{question}"
            "<br><br><i>{english}</i>",
        35: "{english}",
        36: "{question}"
            "<br><br><i>{english}</i>",
        37: "{english}",
        38: "{question}"
            "<br><br><i>{english}</i>",
        39: "{question}"
            "<br><br><i>\"{german}\"</i>",
        40: "{german}",

        41: "{english}",
        42: "{question}"
            "<br><br><i>{english}</i>",
        43: "{english}",
        44: "{question}"
            "<br><br><i>{english}</i>",
        45: "{english}",
        46: "{question}"
            "<br><br><i>{english}</i>",
        47: "{english}",
        48: "{question}"
            "<br><br><i>{english}</i>",
        49: "{question}"
            "<br><br><i>\"{german}\"</i>",
        50: "{german}",

        51: "{english}",
        52: "{question}"
            "<br><br><i>{english}</i>",
        53: "{english}",
        54: "{question}"
            "<br><br><i>{english}</i>",
        55: "{english}",
        56: "{question}"
            "<br><br><i>{english}</i>",
        57: "{english}",
        58: "{question}"
            "<br><br><i>{english}</i>",
        59: "{question}"
            "<br><br><i>\"{german}\"</i>",
        60: "{german}",

        61: "{english}",
        62: "{question}"
            "<br><br><i>{english}</i>",
        63: "{english}",
        64: "{question}"
            "<br><br><i>{english}</i>",
        65: "{english}",
        66: "{question}"
            "<br><br><i>{english}</i>",
        67: "{english}",
        68: "{question}"
            "<br><br><i>{english}</i>",
        69: "{question}"
            "<br><br><i>\"{german}\"</i>",
        70: "{german}",

        71: "{english}",
        72: "{question}"
            "<br><br><i>{english}</i>",
        73: "{english}",
        74: "{question}"
            "<br><br><i>{english}</i>",
        75: "{english}",
        76: "{question}"
            "<br><br><i>{english}</i>",
        77: "{english}",
        78: "{question}"
            "<br><br><i>{english}</i>",
        79: "{question}"
            "<br><br><i>\"{german}\"</i>",
        80: "{german}",
    },


    adjektive: {
        1: "{english}",
        2: "{english}",
        3: "{english}",

        4: "{english}",
        5: "{english}",
        6: "{english}",

        7: "{english}",
        8: "{english}",
        9: "{english}",
        10: "{english}",
        11: "{english}",
        12: "{german}",

        13: "{english}",
        14: "{english}",
        15: "{english}",
        16: "{english}",
        17: "{english}",
        18: "{english}",
        19: "{english}",
        20: "{english}",
        21: "{english}",
        22: "{german}",
        23: "{german}",
        24: "{german}",
    },

    adjektivdeklinationen: {
        1: "{question} \u25CF {case_english} \u25CF {adjective}",
        2: "{question} \u25CF {adjective}"
           "<br><br><i>{english}</i>",
        3: "{question} \u25CF {case_english} \u25CF {adjective}",
        4: "{question} \u25CF {adjective}"
           "<br><br><i>{english}</i>",
        5: "{question} \u25CF {case_english} \u25CF {adjective}",
        6: "{question} \u25CF {adjective}"
           "<br><br><i>{english}</i>",
        7: "{question} \u25CF {case_english} \u25CF {adjective}",
        8: "{question} \u25CF {adjective}"
           "<br><br><i>{english}</i>",
        9: "{question} \u25CF {case_english} \u25CF {adjective}",
        10: "{question} \u25CF {adjective}"
            "<br><br><i>{english}</i>",
        11: "{question} \u25CF {adjective}"
            "<br><br><i>{english}</i>",
        12: "{question} \u25CF {adjective}"
            "<br><br><i>{english}</i>",
        13: "{question} \u25CF {case_english} \u25CF {adjective}",
        14: "{question} \u25CF {adjective}"
            "<br><br><i>{english}</i>",

        15: "{question} \u25CF {case_english} \u25CF {adjective}",
        16: "{question} \u25CF {adjective}"
            "<br><br><i>{english}</i>",
        17: "{question} \u25CF {case_english} \u25CF {adjective}",
        18: "{question} \u25CF {adjective}"
            "<br><br><i>{english}</i>",
        19: "{question} \u25CF {case_english} \u25CF {adjective}",
        20: "{question} \u25CF {adjective}"
            "<br><br><i>{english}</i>",
        21: "{question} \u25CF {case_english} \u25CF {adjective}",
        22: "{question} \u25CF {adjective}"
            "<br><br><i>{english}</i>",

        23: "{question} \u25CF {case_english} \u25CF {adjective}",
        24: "{question} \u25CF {adjective}"
            "<br><br><i>{english}</i>",
        25: "{question} \u25CF {case_english} \u25CF {adjective}",
        26: "{question} \u25CF {adjective}"
            "<br><br><i>{english}</i>",
        27: "{question} \u25CF {case_english} \u25CF {adjective}",
        28: "{question} \u25CF {adjective}"
            "<br><br><i>{english}</i>",

        29: "{question} \u25CF {case_english} \u25CF {adjective}",
        30: "{question} \u25CF {adjective}"
            "<br><br><i>{english}</i>",
        31: "{question} \u25CF {case_english} \u25CF {adjective}",
        32: "{question} \u25CF {adjective}"
            "<br><br><i>{english}</i>",
    },

    verben: {
        1: "{english}",
        2: "{english}",
        3: "{english}",
        4: "{english}",
        5: "{english}",

        6: "{english}",
        7: "{english}",
        8: "{english}",
        9: "{english}",
        10: "{english}",

        11: "{english}",
        12: "{english}",
        13: "{english}",
        14: "{english}",
        15: "{english}",
        16: "{question}",
        17: "{question}",
        18: "{question}",
        19: "{question}",
        20: "{question}",

        21: "{english}",
        22: "{english}",
        23: "{english}",
        24: "{english}",
        25: "{english}",
        26: "{question}",
        27: "{question}",
        28: "{question}",
        29: "{question}",
        30: "{question}",

        31: "{english}",
        32: "{english}",
        33: "{english}",
        34: "{english}",
        35: "{english}",
        36: "{english}",
        37: "{english}",
        38: "{english}",
        39: "{english}",
        40: "{english}",
        41: "{question}",
        42: "{question}",
        43: "{question}",
        44: "{question}",
        45: "{question}",
        46: "{question}",
        47: "{question}",
        48: "{question}",
        49: "{question}",
        50: "{question}",
    },

    trennbare_verben: {
        1: "{root_english} → {root_german}"
           "<br><br>{english} → _____",
        2: "{english} \u25CF {prefix}",
        3: "{english}",

        4: "{root_english} → {root_german}"
           "<br><br>{english} → _____",
        5: "{english} \u25CF {prefix}",
        6: "{english}",

        7: "{root_english} → {root_german}"
           "<br><br>{english} → _____",
        8: "{root_english} → {root_german}"
           "<br><br>{english} → _____",
        9: "{root_english} → {root_german}"
           "<br><br>{english} → _____",
        10: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        11: "{english} \u25CF {prefix}",
        12: "{english} \u25CF {prefix}",
        14: "{english} \u25CF {prefix}",
        13: "{english} \u25CF {prefix}",
        15: "{english}",
        16: "{english}",
        17: "{english}",
        18: "{english}",

        19: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        20: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        21: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        22: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        23: "{english} \u25CF {prefix}",
        24: "{english} \u25CF {prefix}",
        25: "{english} \u25CF {prefix}",
        26: "{english} \u25CF {prefix}",
        27: "{english}",
        28: "{english}",
        29: "{english}",
        30: "{english}",

        31: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        32: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        33: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        34: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        35: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        36: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        37: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        38: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        39: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        40: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        41: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        42: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        43: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        44: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        45: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        46: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        47: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        48: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        49: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        50: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        51: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        52: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        53: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        54: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        55: "{english} \u25CF {prefix}",
        56: "{english} \u25CF {prefix}",
        57: "{english} \u25CF {prefix}",
        58: "{english} \u25CF {prefix}",
        59: "{english} \u25CF {prefix}",
        60: "{english} \u25CF {prefix}",
        61: "{english} \u25CF {prefix}",
        62: "{english} \u25CF {prefix}",
        63: "{english}",
        64: "{english}",
        65: "{english}",
        66: "{english}",
        67: "{english}",
        68: "{english}",
        69: "{english}",
        70: "{english}",
    },

    zahlen: {
        1: "{question}",
        2: "{question}",
        3: "{question}",
        4: "{question}",
        5: "{question}",
        6: "{question}",
        7: "{question}",
        8: "{question}",
        9: "{question}",
        10: "{question}",

        11: "{question}",
        12: "{question}",
        13: "{english}",
        14: "{english}",
        15: "{english}",
        16: "{question}"
            "<br><br><i>{english}</i>",

        17: "{english}",
        18: "{question}"
            "<br><br><i>{english}</i>",
        19: "{english}",
        20: "{question}"
            "<br><br><i>{english}</i>",

        21: "{english}",
        22: "{question}"
            "<br><br><i>{english}</i>",

        23: "{question}",
        24: "{question}"
            "<br><br><i>{english}</i>",
    },

}
