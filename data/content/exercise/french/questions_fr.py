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

QUESTION_UNIT_FR = {
    pronominaladverbien:
        "{question}"
        "<br><br><i>{french}</i>",


    praepositionen_artikel:
        "{question} \u25CF {preposition} \u25CF {person}"
        "<br><br><i>{french}</i>",

    verben_artikel:
        "{question} \u25CF {person}"
        "<br><br><i>{french}</i>",

    wortstellung:
        "Placeholder",

    komparativ_superlativ:
        "{german}"
        "<br><br><i>{french}</i>",

    adjektive_konjunktionen:
        "{question}"
        "<br><br><i>{french}</i>",


    nomen_verben_verbindungen:
        "{question}"
        "<br><br><i>{french}</i>",

    praesens:
        "{german} \u25CF {person} _____"
        "<br><br><i>{french}</i>",

    partizip_II:
        "{german}"
        "<br><br><i>{french}</i>",

    praeteritum:
        "{german} \u25CF {person} _____"
        "<br><br><i>{french}</i>",

    imperativ:
        "{german} \u25CF {person} \u25CF _____"
        "<br><br><i>{french}</i>",

    konjunktiv_II:
        "{german} \u25CF {person} _____"
        "<br><br><i>{french}</i>",

    konjunktiv_I:
        "{german} \u25CF {person} _____"
        "<br><br><i>{french}</i>",

    partizip_I:
        "{german}"
        "<br><br><i>{french}</i>",

    adjektive_verben_wortstaemme:
        "{root_french} → {question}"
        "<br><br>{french} → _____",

    adjektive_nomen_wortstaemme:
        "{root_french} → {question}"
        "<br><br>{french} → _____",

    nomen_verben_wortstaemme:
        "{root_french} → {question}"
        "<br><br>{french} → _____",

    genus_regeln:
        "{question}"
        "<br><br><i>{french}</i>",

    genus:
        "{question}"
        "<br><br><i>{french}</i>",

    plural:
        "Singulier : {question}"
        "<br><br>Pluriel : die _____"
        "<br><br><i>{french}</i>",
}


QUESTION_EXERCISE_FR = {
    praepositionen: {
        1: "{question}"
           "<br><br><i>{french}</i>",
        2: "{question}"
           "<br><br><i>{french}</i>",
        3: "{question}"
           "<br><br><i>{french}</i>",
        4: "{question}"
           "<br><br><i>{french}</i>",

        5: "{question}"
           "<br><br><i>{french}</i>",
        6: "{question}"
           "<br><br><i>{french}</i>",
        7: "{question}"
           "<br><br><i>{french}</i>",
        8: "{question}"
           "<br><br><i>{french}</i>",

        9: "{question}"
           "<br><br><i>{french}</i>",
        10: "{question}"
            "<br><br><i>{french}</i>",
        11: "{french}",
        12: "{question}"
            "<br><br><i>{french}</i>",

        13: "{question}"
            "<br><br><i>{french}</i>",
        14: "{question}"
            "<br><br><i>{french}</i>",
        15: "{french}",
        16: "{question}"
            "<br><br><i>{french}</i>",

        17: "{question}"
            "<br><br><i>{french}</i>",
        18: "{question}"
            "<br><br><i>{french}</i>",
        19: "{question}"
            "<br><br><i>{french}</i>",
        20: "{question}"
            "<br><br><i>{french}</i>",
        21: "{french}",
        22: "{question}"
            "<br><br><i>{french}</i>",
        23: "{french}",
        24: "{question}"
            "<br><br><i>{french}</i>",
        25: "{french}",
        26: "{question}"
            "<br><br><i>{french}</i>",
        27: "{french}",
        28: "{question}"
            "<br><br><i>{french}</i>",
        29: "{question}"
            "<br><br><i>\"{german}\"</i>",
        30: "{german}",
    },

    praepositionen_verben: {
        1: "{french} = {question}",
        2: "{question}"
           "<br><br><i>{french}</i>",
        3: "{french} = {question}",
        4: "{question}"
           "<br><br><i>{french}</i>",

        5: "{french} = {question}",
        6: "{question}"
           "<br><br><i>{french}</i>",
        7: "{french} = {question}",
        8: "{question}"
           "<br><br><i>{french}</i>",

        9: "{french} = {question}",
        10: "{question}"
            "<br><br><i>{french}</i>",
        11: "{french} = {question}",
        12: "{question}"
            "<br><br><i>{french}</i>",
        13: "{french} = {question}",
        14: "{question}"
            "<br><br><i>{french}</i>",
        15: "{french} = {question}",
        16: "{question}"
            "<br><br><i>{french}</i>",

        17: "{french} = {question}",
        18: "{question}"
            "<br><br><i>{french}</i>",
        19: "{french} = {question}",
        20: "{question}"
            "<br><br><i>{french}</i>",
        21: "{french} = {question}",
        22: "{question}"
            "<br><br><i>{french}</i>",
        23: "{french} = {question}",
        24: "{question}"
            "<br><br><i>{french}</i>",

        25: "{french} = {question}",
        26: "{question}"
            "<br><br><i>{french}</i>",
        27: "{french} = {question}",
        28: "{question}"
            "<br><br><i>{french}</i>",
        29: "{french} = {question}",
        30: "{question}"
            "<br><br><i>{french}</i>",
        31: "{french} = {question}",
        32: "{question}"
            "<br><br><i>{french}</i>",

        33: "{french} = {question}",
        34: "{question}"
            "<br><br><i>{french}</i>",
        35: "{french} = {question}",
        36: "{question}"
            "<br><br><i>{french}</i>",
        37: "{french} = {question}",
        38: "{question}"
            "<br><br><i>{french}</i>",
        39: "{french} = {question}",
        40: "{question}"
            "<br><br><i>{french}</i>",
    },

    praepositionen_adjektive: {
        1: "{french} = {question}",
        2: "{question}"
           "<br><br><i>{french}</i>",
        3: "{french} = {question}",
        4: "{question}"
           "<br><br><i>{french}</i>",

        5: "{french} = {question}",
        6: "{question}"
           "<br><br><i>{french}</i>",
        7: "{french} = {question}",
        8: "{question}"
           "<br><br><i>{french}</i>",
        9: "{french} = {question}",
        10: "{question}"
            "<br><br><i>{french}</i>",

        11: "{french} = {question}",
        12: "{question}"
            "<br><br><i>{french}</i>",
        13: "{french} = {question}",
        14: "{question}"
            "<br><br><i>{french}</i>",
        15: "{french} = {question}",
        16: "{question}"
            "<br><br><i>{french}</i>",

        17: "{french} = {question}",
        18: "{question}"
            "<br><br><i>{french}</i>",
        19: "{french} = {question}",
        20: "{question}"
            "<br><br><i>{french}</i>",
        21: "{french} = {question}",
        22: "{question}"
            "<br><br><i>{french}</i>",
    },

    praepositionen_nomen: {
        1: "{french} = {question}",
        2: "{question}"
           "<br><br><i>{french}</i>",
        3: "{french} = {question}",
        4: "{question}"
           "<br><br><i>{french}</i>",

        5: "{french} = {question}",
        6: "{question}"
           "<br><br><i>{french}</i>",
        7: "{french} = {question}",
        8: "{question}"
           "<br><br><i>{french}</i>",
        9: "{french} = {question}",
        10: "{question}"
            "<br><br><i>{french}</i>",
        11: "{french} = {question}",
        12: "{question}"
            "<br><br><i>{french}</i>",

        13: "{french} = {question}",
        14: "{question}"
            "<br><br><i>{french}</i>",
        15: "{french} = {question}",
        16: "{question}"
            "<br><br><i>{french}</i>",
        17: "{french} = {question}",
        18: "{question}"
            "<br><br><i>{french}</i>",
        19: "{french} = {question}",
        20: "{question}"
            "<br><br><i>{french}</i>",
        21: "{french} = {question}",
        22: "{question}"
            "<br><br><i>{french}</i>",
        23: "{french} = {question}",
        24: "{question}"
            "<br><br><i>{french}</i>",
        25: "{french} = {question}",
        26: "{question}"
            "<br><br><i>{french}</i>",
        27: "{french} = {question}",
        28: "{question}"
            "<br><br><i>{french}</i>",

        29: "{french} = {question}",
        30: "{question}"
            "<br><br><i>{french}</i>",
    },


    artikel: {
        1: "{german} \u25CF {gender_french}, {case_french}",
        2: "{question}"
           "<br><br><i>{french}</i>",
        3: "{question}"
           "<br><br><i>{french}</i>",
        4: "{question}"
           "<br><br><i>{french}</i>",
        5: "{question}"
           "<br><br><i>{french}</i>",
        6: "{question}"
           "<br><br><i>{french}</i>",
        7: "{question}"
           "<br><br><i>{french}</i>",
        8: "{question}"
           "<br><br><i>{french}</i>",
        9: "{question}"
           "<br><br><i>{french}</i>",
        10: "{question}"
            "<br><br><i>{french}</i>",
        11: "{question}"
            "<br><br><i>{french}</i>",
        12: "{german} \u25CF {gender_french}, {case_french}",
        13: "{question}"
            "<br><br><i>{french}</i>",
        14: "{question}"
            "<br><br><i>{french}</i>",
        15: "{question}"
            "<br><br><i>{french}</i>",
        16: "{question}"
            "<br><br><i>{french}</i>",
        17: "{question}"
            "<br><br><i>{french}</i>",
        18: "{question}"
            "<br><br><i>{french}</i>",
        19: "{question}"
            "<br><br><i>{french}</i>",
        20: "{question}"
            "<br><br><i>{french}</i>",
        21: "{german} \u25CF {gender_french}, {case_french}",
        22: "{question}"
            "<br><br><i>{french}</i>",
        23: "{german} \u25CF {gender_french}, {case_french}",
        24: "{question}"
            "<br><br><i>{french}</i>",
        25: "{german} \u25CF {gender_french}, {case_french}",
        26: "{question}"
            "<br><br><i>{french}</i>",

        27: "{german} \u25CF {gender_french}, {case_french}",
        28: "{question}"
            "<br><br><i>{french}</i>",
        29: "{german} \u25CF {gender_french}, {case_french}",
        30: "{question}"
            "<br><br><i>{french}</i>",
        31: "{french}",
        32: "{question}"
            "<br><br><i>{french}</i>",

        33: "{german} \u25CF {gender_french}, {case_french}",
        34: "{question}"
            "<br><br><i>{french}</i>",
        35: "{german} \u25CF {gender_french}, {case_french}",
        36: "{question}"
            "<br><br><i>{french}</i>",
        37: "{german} \u25CF {gender_french}, {case_french}",
        38: "{question} \u25CF {person}" 
            "<br><br><i>{french}</i>",

        39: "{german} \u25CF {gender_french}, {case_french}",
        40: "{question}"
            "<br><br><i>{french}</i>",

        41: "{german} \u25CF {gender_french}, {case_french}",
        42: "{question}"
            "<br><br><i>{french}</i>",
        43: "{question}"
            "<br><br><i>{french}</i>"
            "<br><br>Article : {person}",
        44: "{question}"
            "<br><br><i>{french}</i>"
            "<br><br>Article : {person}",
    },

    pronomen: {
        1: "{french}",
        2: "{question}"
           "<br><br><i>{french}</i>",
        3: "{french}",
        4: "{question}"
           "<br><br><i>{french}</i>",
        5: "{french}",
        6: "{question}"
           "<br><br><i>{french}</i>",
        7: "{question}"
           "<br><br><i>{french}</i>",
        8: "{question}"
           "<br><br><i>{french}</i>",
        9: "{question} \u25CF {person}"
           "<br><br><i>{french}</i>",
        10: "{question} \u25CF {person}"
            "<br><br><i>{french}</i>",

        11: "{french} \u25CF {case_french}",
        12: "{question}"
            "<br><br><i>{french}</i>",
        13: "{question}"
            "<br><br><i>{french}</i>",
        14: "{question}"
            "<br><br><i>{french}</i>",

        15: "{french}",
        16: "{question}"
            "<br><br><i>{french}</i>",
        17: "{gender_french} \u25CF {case_french}",
        18: "{question}"
            "<br><br><i>{french}</i>",
        19: "{question}"
            "<br><br><i>{french}</i>",
        20: "{question}"
            "<br><br><i>{french}</i>",
        21: "{question}"
            "<br><br><i>{french}</i>",
        22: "{question}"
            "<br><br><i>{french}</i>",
        23: "{question}"
            "<br><br><i>{french}</i>",

        24: "{french}",
        25: "{question}"
            "<br><br><i>{french}</i>",
        26: "{french} \u25CF {case_french}",
        27: "{question}"
            "<br><br><i>{french}</i>",
        28: "{question}"
            "<br><br><i>{french}</i>",
        29: "{question}"
            "<br><br><i>{french}</i>",
        30: "{question}"
            "<br><br><i>{french}</i>",
        31: "{german} \u25CF {gender_french}, {case_french}",
        32: "{question}"
            "<br><br><i>{french}</i>",
        33: "{german} \u25CF {gender_french}, {case_french}",
        34: "{question}"
            "<br><br><i>{french}</i>",

        35: "{french}",
        36: "{question}"
            "<br><br><i>{french}</i>",
        37: "{french}",
        38: "{question}"
            "<br><br><i>{french}</i>",
        39: "{question}"
            "<br><br><i>{french}</i>",

        40: "{french}, {gender_french}, {case_french}",
        41: "{question} \u25CF {gender_french}"
            "<br><br><i>{french}</i>",
        42: "{french}, {gender_french}, {case_french}",
        43: "{question} \u25CF {gender_french}"
            "<br><br><i>{french}</i>",
    },

    konnektoren: {
        1: "{french} \u25CF {case_french}",
        2: "{question}"
           "<br><br><i>{french}</i>",

        3: "{french} \u25CF {case_french}",
        4: "{question}"
           "<br><br><i>{french}</i>",

        5: "{french} \u25CF {case_french}",
        6: "{question}"
           "<br><br><i>{french}</i>",
        7: "{french} \u25CF {case_french}",
        8: "{question}"
           "<br><br><i>{french}</i>",
        9: "{french} \u25CF {case_french}",
        10: "{question}"
            "<br><br><i>{french}</i>",
        11: "{question}"
            "<br><br><i>\"{german}\"</i>",

        12: "{french} \u25CF {case_french}",
        13: "{question}"
            "<br><br><i>{french}</i>",
        14: "{french} \u25CF {case_french}",
        15: "{question}"
            "<br><br><i>{french}</i>",
        16: "{french} \u25CF {case_french}",
        17: "{question}"
            "<br><br><i>{french}</i>",
        18: "{question}"
            "<br><br><i>\"{german}\"</i>",

        19: "{french} \u25CF {case_french}",
        20: "{question}"
            "<br><br><i>{french}</i>",
        21: "{french} \u25CF {case_french}",
        22: "{question}"
            "<br><br><i>{french}</i>",
        23: "{french} \u25CF {case_french}",
        24: "{question}"
            "<br><br><i>{french}</i>",
        25: "{french} \u25CF {case_french}",
        26: "{question}"
            "<br><br><i>{french}</i>",
        27: "{french} \u25CF {case_french}",
        28: "{question}"
            "<br><br><i>{french}</i>",
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
        1: "{french}",
        2: "{question}"
           "<br><br><i>{french}</i>",

        3: "{french}",
        4: "{question}"
           "<br><br><i>{french}</i>",

        5: "{french}",
        6: "{question}"
           "<br><br><i>{french}</i>",

        7: "{french}",
        8: "{question}"
           "<br><br><i>{french}</i>",
        9: "{french}",
        10: "{question}"
           "<br><br><i>{french}</i>",

        11: "{french}",
        12: "{question}"
            "<br><br><i>{french}</i>",
        13: "{french}",
        14: "{question}"
            "<br><br><i>{french}</i>",

        15: "{french}",
        16: "{question}"
            "<br><br><i>{french}</i>",
    },

    adverbien: {
        1: "{french}",
        2: "{question}"
           "<br><br><i>{french}</i>",
        3: "{french}",
        4: "{question}"
           "<br><br><i>{french}</i>",

        5: "{french}",
        6: "{question}"
           "<br><br><i>{french}</i>",
        7: "{french}",
        8: "{question}"
           "<br><br><i>{french}</i>",
        9: "{question}"
            "<br><br><i>\"{german}\"</i>",
        10: "{german}",

        11: "{french}",
        12: "{question}"
            "<br><br><i>{french}</i>",
        13: "{french}",
        14: "{question}"
            "<br><br><i>{french}</i>",
        15: "{french}",
        16: "{question}"
            "<br><br><i>{french}</i>",
        17: "{french}",
        18: "{question}"
            "<br><br><i>{french}</i>",
        19: "{question}"
            "<br><br><i>\"{german}\"</i>",
        20: "{german}",

        21: "{french}",
        22: "{question}"
            "<br><br><i>{french}</i>",
        23: "{french}",
        24: "{question}"
            "<br><br><i>{french}</i>",
        25: "{french}",
        26: "{question}"
            "<br><br><i>{french}</i>",
        27: "{french}",
        28: "{question}"
            "<br><br><i>{french}</i>",
        29: "{question}"
            "<br><br><i>\"{german}\"</i>",
        30: "{german}",

        31: "{french}",
        32: "{question}"
            "<br><br><i>{french}</i>",
        33: "{french}",
        34: "{question}"
            "<br><br><i>{french}</i>",
        35: "{french}",
        36: "{question}"
            "<br><br><i>{french}</i>",
        37: "{french}",
        38: "{question}"
            "<br><br><i>{french}</i>",
        39: "{question}"
            "<br><br><i>\"{german}\"</i>",
        40: "{german}",

        41: "{french}",
        42: "{question}"
            "<br><br><i>{french}</i>",
        43: "{french}",
        44: "{question}"
            "<br><br><i>{french}</i>",
        45: "{french}",
        46: "{question}"
            "<br><br><i>{french}</i>",
        47: "{french}",
        48: "{question}"
            "<br><br><i>{french}</i>",
        49: "{question}"
            "<br><br><i>\"{german}\"</i>",
        50: "{german}",

        51: "{french}",
        52: "{question}"
            "<br><br><i>{french}</i>",
        53: "{french}",
        54: "{question}"
            "<br><br><i>{french}</i>",
        55: "{french}",
        56: "{question}"
            "<br><br><i>{french}</i>",
        57: "{french}",
        58: "{question}"
            "<br><br><i>{french}</i>",
        59: "{question}"
            "<br><br><i>\"{german}\"</i>",
        60: "{german}",

        61: "{french}",
        62: "{question}"
            "<br><br><i>{french}</i>",
        63: "{french}",
        64: "{question}"
            "<br><br><i>{french}</i>",
        65: "{french}",
        66: "{question}"
            "<br><br><i>{french}</i>",
        67: "{french}",
        68: "{question}"
            "<br><br><i>{french}</i>",
        69: "{question}"
            "<br><br><i>\"{german}\"</i>",
        70: "{german}",

        71: "{french}",
        72: "{question}"
            "<br><br><i>{french}</i>",
        73: "{french}",
        74: "{question}"
            "<br><br><i>{french}</i>",
        75: "{french}",
        76: "{question}"
            "<br><br><i>{french}</i>",
        77: "{french}",
        78: "{question}"
            "<br><br><i>{french}</i>",
        79: "{question}"
            "<br><br><i>\"{german}\"</i>",
        80: "{german}",
    },

    adjektive: {
        1: "{french}",
        2: "{french}",
        3: "{french}",

        4: "{french}",
        5: "{french}",
        6: "{french}",

        7: "{french}",
        8: "{french}",
        9: "{french}",
        10: "{french}",
        11: "{french}",
        12: "{german}",

        13: "{french}",
        14: "{french}",
        15: "{french}",
        16: "{french}",
        17: "{french}",
        18: "{french}",
        19: "{french}",
        20: "{french}",
        21: "{french}",
        22: "{german}",
        23: "{german}",
        24: "{german}",
    },

    adjektivdeklinationen: {
        1: "{question} \u25CF {case_french} \u25CF {adjective}",
        2: "{question} \u25CF {adjective}"
           "<br><br><i>{french}</i>",
        3: "{question} \u25CF {case_french} \u25CF {adjective}",
        4: "{question} \u25CF {adjective}"
           "<br><br><i>{french}</i>",
        5: "{question} \u25CF {case_french} \u25CF {adjective}",
        6: "{question} \u25CF {adjective}"
           "<br><br><i>{french}</i>",
        7: "{question} \u25CF {case_french} \u25CF {adjective}",
        8: "{question} \u25CF {adjective}"
           "<br><br><i>{french}</i>",
        9: "{question} \u25CF {case_french} \u25CF {adjective}",
        10: "{question} \u25CF {adjective}"
            "<br><br><i>{french}</i>",
        11: "{question} \u25CF {adjective}"
            "<br><br><i>{french}</i>",
        12: "{question} \u25CF {adjective}"
            "<br><br><i>{french}</i>",
        13: "{question} \u25CF {case_french} \u25CF {adjective}",
        14: "{question} \u25CF {adjective}"
            "<br><br><i>{french}</i>",

        15: "{question} \u25CF {case_french} \u25CF {adjective}",
        16: "{question} \u25CF {adjective}"
            "<br><br><i>{french}</i>",
        17: "{question} \u25CF {case_french} \u25CF {adjective}",
        18: "{question} \u25CF {adjective}"
            "<br><br><i>{french}</i>",
        19: "{question} \u25CF {case_french} \u25CF {adjective}",
        20: "{question} \u25CF {adjective}"
            "<br><br><i>{french}</i>",
        21: "{question} \u25CF {case_french} \u25CF {adjective}",
        22: "{question} \u25CF {adjective}"
            "<br><br><i>{french}</i>",

        23: "{question} \u25CF {case_french} \u25CF {adjective}",
        24: "{question} \u25CF {adjective}"
            "<br><br><i>{french}</i>",
        25: "{question} \u25CF {case_french} \u25CF {adjective}",
        26: "{question} \u25CF {adjective}"
            "<br><br><i>{french}</i>",
        27: "{question} \u25CF {case_french} \u25CF {adjective}",
        28: "{question} \u25CF {adjective}"
            "<br><br><i>{french}</i>",

        29: "{question} \u25CF {case_french} \u25CF {adjective}",
        30: "{question} \u25CF {adjective}"
            "<br><br><i>{french}</i>",
        31: "{question} \u25CF {case_french} \u25CF {adjective}",
        32: "{question} \u25CF {adjective}"
            "<br><br><i>{french}</i>",
    },

    verben: {
        1: "{french}",
        2: "{french}",
        3: "{french}",
        4: "{french}",
        5: "{french}",

        6: "{french}",
        7: "{french}",
        8: "{french}",
        9: "{french}",
        10: "{french}",

        11: "{french}",
        12: "{french}",
        13: "{french}",
        14: "{french}",
        15: "{french}",
        16: "{question}",
        17: "{question}",
        18: "{question}",
        19: "{question}",
        20: "{question}",

        21: "{french}",
        22: "{french}",
        23: "{french}",
        24: "{french}",
        25: "{french}",
        26: "{question}",
        27: "{question}",
        28: "{question}",
        29: "{question}",
        30: "{question}",

        31: "{french}",
        32: "{french}",
        33: "{french}",
        34: "{french}",
        35: "{french}",
        36: "{french}",
        37: "{french}",
        38: "{french}",
        39: "{french}",
        40: "{french}",
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
        1: "{root_french} → {root_german}"
           "<br><br>{french} → _____",
        2: "{french} \u25CF {prefix}",
        3: "{french}",

        4: "{root_french} → {root_german}"
           "<br><br>{french} → _____",
        5: "{french} \u25CF {prefix}",
        6: "{french}",

        7: "{root_french} → {root_german}"
           "<br><br>{french} → _____",
        8: "{root_french} → {root_german}"
           "<br><br>{french} → _____",
        9: "{root_french} → {root_german}"
           "<br><br>{french} → _____",
        10: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        11: "{french} \u25CF {prefix}",
        12: "{french} \u25CF {prefix}",
        14: "{french} \u25CF {prefix}",
        13: "{french} \u25CF {prefix}",
        15: "{french}",
        16: "{french}",
        17: "{french}",
        18: "{french}",

        19: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        20: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        21: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        22: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        23: "{french} \u25CF {prefix}",
        24: "{french} \u25CF {prefix}",
        25: "{french} \u25CF {prefix}",
        26: "{french} \u25CF {prefix}",
        27: "{french}",
        28: "{french}",
        29: "{french}",
        30: "{french}",

        31: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        32: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        33: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        34: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        35: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        36: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        37: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        38: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        39: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        40: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        41: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        42: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        43: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        44: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        45: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        46: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        47: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        48: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        49: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        50: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        51: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        52: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        53: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        54: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        55: "{french} \u25CF {prefix}",
        56: "{french} \u25CF {prefix}",
        57: "{french} \u25CF {prefix}",
        58: "{french} \u25CF {prefix}",
        59: "{french} \u25CF {prefix}",
        60: "{french} \u25CF {prefix}",
        61: "{french} \u25CF {prefix}",
        62: "{french} \u25CF {prefix}",
        63: "{french}",
        64: "{french}",
        65: "{french}",
        66: "{french}",
        67: "{french}",
        68: "{french}",
        69: "{french}",
        70: "{french}",
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
        13: "{french}",
        14: "{french}",
        15: "{french}",
        16: "{question}"
            "<br><br><i>{french}</i>",

        17: "{french}",
        18: "{question}"
            "<br><br><i>{french}</i>",
        19: "{french}",
        20: "{question}"
            "<br><br><i>{french}</i>",

        21: "{french}",
        22: "{question}"
            "<br><br><i>{french}</i>",

        23: "{question}",
        24: "{question}"
            "<br><br><i>{french}</i>",
    },
}
