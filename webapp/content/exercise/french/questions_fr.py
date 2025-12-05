from data.data_processing.units import (
    praepositionen_grammatik, praepositionen_verben, praepositionen_adjektive, praepositionen_nomen,
    praepositionen_artikel, praepositionen_adverbien,
    artikel, artikel_genus, pronomen, konnektoren, fragen, adverbien, wortstellung,
    adjektive, adjektivdeklinationen,
    verben, trennbare_verben, nomen_verben_verbindungen,
    praesens, imperativ, partizip_II, praeteritum, praeteritum_partizip_II, konjunktiv_II, konjunktiv_I, partizip_I,
)

# bullet point \u25CF
# arrow &#8594

QUESTION_FR = {

    praepositionen_grammatik: {
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
        19: "{french}",
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
        27: "{question}"
            "<br><br><i>\"{german}\"</i>",
        28: "{german}",
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
        9: "{question}"
           "<br><br><i>{french}</i>",
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
        41: "{french} = {question}",
        42: "{question}"
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
    },

    praepositionen_artikel: {
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
    },

    praepositionen_adverbien: {
        1: "Something"
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
        11: "{german} \u25CF {gender_french}, {case_french}",
        12: "{question}"
           "<br><br><i>{french}</i>",
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
        20: "{german} \u25CF {gender_french}, {case_french}",
        21: "{question}"
            "<br><br><i>{french}</i>",
        22: "{german} \u25CF {gender_french}, {case_french}",
        23: "{question}"
            "<br><br><i>{french}</i>",
        24: "{german} \u25CF {gender_french}, {case_french}",
        25: "{question}"
            "<br><br><i>{french}</i>",

        26: "{german} \u25CF {gender_french}, {case_french}",
        27: "{question}"
            "<br><br><i>{french}</i>",
        28: "{german} \u25CF {gender_french}, {case_french}",
        29: "{question}"
            "<br><br><i>{french}</i>",
        30: "{question}"
            "<br><br><i>{french}</i>",
        31: "{question}"
            "<br><br><i>{french}</i>",
        32: "{french}",
        33: "{question}"
            "<br><br><i>{french}</i>",

        34: "{german} \u25CF {gender_french}, {case_french}",
        35: "{question}"
            "<br><br><i>{french}</i>",
        36: "{german} \u25CF {gender_french}, {case_french}",
        37: "{question}"
            "<br><br><i>{french}</i>",
        38: "{german} \u25CF {gender_french}, {case_french}",
        39: "{question} \u25CF {person}" 
            "<br><br><i>{french}</i>",

        40: "{german} \u25CF {gender_french}, {case_french}",
        41: "{question}"
            "<br><br><i>{french}</i>",

        42: "{german} \u25CF {gender_french}, {case_french}",
        43: "{question}"
            "<br><br><i>{french}</i>",
        44: "{question}"
            "<br><br><i>{french}</i>"
            "<br><br>Article : {person}",
        45: "{question}"
            "<br><br><i>{french}</i>"
            "<br><br>Article : {person}",
    },

    artikel_genus: {
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
        11: "{question}"
           "<br><br><i>{french}</i>",
        12: "{question}"
           "<br><br><i>{french}</i>",
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

        21: "{question}"
           "<br><br><i>{french}</i>",
        22: "{question}"
           "<br><br><i>{french}</i>",
        23: "{question}"
           "<br><br><i>{french}</i>",
        24: "{question}"
           "<br><br><i>{french}</i>",
        25: "{question}"
           "<br><br><i>{french}</i>",
        26: "{question}"
           "<br><br><i>{french}</i>",
        27: "{question}"
           "<br><br><i>{french}</i>",
        28: "{question}"
           "<br><br><i>{french}</i>",
        29: "{question}"
           "<br><br><i>{french}</i>",
        30: "{question}"
            "<br><br><i>{french}</i>",
        31: "{question}"
           "<br><br><i>{french}</i>",
        32: "{question}"
           "<br><br><i>{french}</i>",
        33: "{question}"
           "<br><br><i>{french}</i>",
        34: "{question}"
           "<br><br><i>{french}</i>",
        35: "{question}"
           "<br><br><i>{french}</i>",

        36: "{question}"
           "<br><br><i>{french}</i>",
        37: "{question}"
           "<br><br><i>{french}</i>",
        38: "{question}"
           "<br><br><i>{french}</i>",
        39: "{question}"
           "<br><br><i>{french}</i>",
        40: "{question}"
            "<br><br><i>{french}</i>",
        41: "{question}"
            "<br><br><i>{french}</i>",
        42: "{question}"
            "<br><br><i>{french}</i>",
        43: "{question}"
            "<br><br><i>{french}</i>",
        44: "{question}"
            "<br><br><i>{french}</i>",
        45: "{question}"
            "<br><br><i>{french}</i>",
        46: "{question}"
            "<br><br><i>{french}</i>",
        47: "{question}"
            "<br><br><i>{french}</i>",
        48: "{question}"
            "<br><br><i>{french}</i>",
        49: "{question}"
            "<br><br><i>{french}</i>",
        50: "{question}"
            "<br><br><i>{french}</i>",
        51: "{question}"
            "<br><br><i>{french}</i>",
        52: "{question}"
            "<br><br><i>{french}</i>",
        53: "{question}"
            "<br><br><i>{french}</i>",
        54: "{question}"
            "<br><br><i>{french}</i>",
        55: "{question}"
            "<br><br><i>{french}</i>",
        56: "{question}"
            "<br><br><i>{french}</i>",
        57: "{question}"
            "<br><br><i>{french}</i>",
        58: "{question}"
            "<br><br><i>{french}</i>",
        59: "{question}"
            "<br><br><i>{french}</i>",
        60: "{question}"
            "<br><br><i>{french}</i>",
        61: "{question}"
            "<br><br><i>{french}</i>",
        62: "{question}"
            "<br><br><i>{french}</i>",
        63: "{question}"
            "<br><br><i>{french}</i>",
        64: "{question}"
            "<br><br><i>{french}</i>",
        65: "{question}"
            "<br><br><i>{french}</i>",
        66: "{question}"
            "<br><br><i>{french}</i>",
        67: "{question}"
            "<br><br><i>{french}</i>",
        68: "{question}"
            "<br><br><i>{french}</i>",
        69: "{question}"
            "<br><br><i>{french}</i>",
        70: "{question}"
            "<br><br><i>{french}</i>",
        71: "{question}"
            "<br><br><i>{french}</i>",
        72: "{question}"
            "<br><br><i>{french}</i>",
        73: "{question}"
            "<br><br><i>{french}</i>",
        74: "{question}"
            "<br><br><i>{french}</i>",
        75: "{question}"
            "<br><br><i>{french}</i>",
        76: "{question}"
            "<br><br><i>{french}</i>",
        77: "{question}"
            "<br><br><i>{french}</i>",
        78: "{question}"
            "<br><br><i>{french}</i>",
        79: "{question}"
            "<br><br><i>{french}</i>",
        80: "{question}"
            "<br><br><i>{french}</i>",
        81: "{question}"
            "<br><br><i>{french}</i>",
        82: "{question}"
            "<br><br><i>{french}</i>",
        83: "{question}"
            "<br><br><i>{french}</i>",
        84: "{question}"
            "<br><br><i>{french}</i>",
        85: "{question}"
            "<br><br><i>{french}</i>",
        86: "{question}"
            "<br><br><i>{french}</i>",
        87: "{question}"
            "<br><br><i>{french}</i>",
    },

    pronomen: {
        1: "{french} \u25CF {case_french}",
        2: "{question}"
            "<br><br><i>{french}</i>",
        3: "{french} \u25CF {case_french}",
        4: "{question}"
            "<br><br><i>{french}</i>",
        5: "{french} \u25CF {case_french}",
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
        15: "{german} \u25CF {gender_french}, {case_french}",
        16: "{question}"
            "<br><br><i>{french}</i>",
        17: "{german} \u25CF {gender_french}, {case_french}",
        18: "{question}"
            "<br><br><i>{french}</i>",

        19: "{french}",
        20: "{question}"
            "<br><br><i>{french}</i>",
        21: "{question}"
            "<br><br><i>{french}</i>",
        22: "{question}"
            "<br><br><i>{french}</i>",
        23: "{question}"
            "<br><br><i>{french}</i>",
        24: "{question}"
            "<br><br><i>{french}</i>",
        25: "{question}"
            "<br><br><i>{french}</i>",
        26: "{question}"
            "<br><br><i>{french}</i>",

        27: "{question}"
            "<br><br><i>{french}</i>",
        28: "{question}"
            "<br><br><i>{french}</i>",
        29: "{question}"
            "<br><br><i>{french}</i>",
        30: "{question}"
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
        25: "{question}"
            "<br><br><i>\"{german}\"</i>",
        26: "{question}"
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
    },

    wortstellung: {
        1: "Placeholder",
    },

    adjektive: {
        1: "{french}",
        2: "{french}",
        3: "{french}",
        4: "{question}",
        5: "{question}",
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
        12: "{question}"
            "<br><br><i>{french}</i>",

        13: "{french}",
        14: "{french}",
        15: "{french}",
        16: "{question}",
        17: "{question}",
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
        25: "{french}",
        26: "{french}",
        27: "{question}",
        28: "{question}",
        29: "{question}",

        30: "{french}",
        31: "{french}",
        32: "{french}",
        33: "{question}",
        34: "{question}",
        35: "{question}",
    },

    adjektivdeklinationen: {
        1: "{question} \u25CF {case_french} \u25CF {adjective}",
        2: "{question} \u25CF {adjective}",
        3: "{question} \u25CF {case_french} \u25CF {adjective}",
        4: "{question} \u25CF {adjective}",
        5: "{question} \u25CF {case_french} \u25CF {adjective}",
        6: "{question} \u25CF {adjective}",
        7: "{question} \u25CF {case_french} \u25CF {adjective}",
        8: "{question} \u25CF {adjective}",
        9: "{question} \u25CF {case_french} \u25CF {adjective}",
        10: "{question} \u25CF {adjective}",
        11: "{question} \u25CF {adjective}",
        12: "{question} \u25CF {adjective}",

        13: "{question} \u25CF {case_french} \u25CF {adjective}",
        14: "{question} \u25CF {adjective}",
        15: "{question} \u25CF {case_french} \u25CF {adjective}",
        16: "{question} \u25CF {adjective}",
        17: "{question} \u25CF {case_french} \u25CF {adjective}",
        18: "{question} \u25CF {adjective}",

        19: "{question} \u25CF {case_french} \u25CF {adjective}",
        20: "{question} \u25CF {adjective}",
        21: "{question} \u25CF {case_french} \u25CF {adjective}",
        22: "{question} \u25CF {adjective}",

        23: "{question} \u25CF {case_french} \u25CF {adjective}",
        24: "{question} \u25CF {adjective}",
        25: "{question} \u25CF {case_french} \u25CF {adjective}",
        26: "{question} \u25CF {adjective}",
        27: "{question} \u25CF {case_french} \u25CF {adjective}",
        28: "{question} \u25CF {adjective}",
        29: "{question} \u25CF {case_french} \u25CF {adjective}",
        30: "{question} \u25CF {adjective}",
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
           "<br><br>{french} → _____ ",
        2: "{french} \u25CF {prefix}",
        3: "{french}",

        4: "{root_french} → {root_german}"
           "<br><br>{french} → _____ ",
        5: "{french} \u25CF {prefix}",
        6: "{french}",

        7: "{root_french} → {root_german}"
           "<br><br>{french} → _____ ",
        8: "{root_french} → {root_german}"
           "<br><br>{french} → _____ ",
        9: "{root_french} → {root_german}"
           "<br><br>{french} → _____ ",
        10: "{root_french} → {root_german}"
            "<br><br>{french} → _____ ",
        11: "{french} \u25CF {prefix}",
        12: "{french} \u25CF {prefix}",
        14: "{french} \u25CF {prefix}",
        13: "{french} \u25CF {prefix}",
        15: "{french}",
        16: "{french}",
        17: "{french}",
        18: "{french}",

        19: "{root_french} → {root_german}"
            "<br><br>{french} → _____ ",
        20: "{root_french} → {root_german}"
            "<br><br>{french} → _____ ",
        21: "{root_french} → {root_german}"
            "<br><br>{french} → _____ ",
        22: "{root_french} → {root_german}"
            "<br><br>{french} → _____ ",
        23: "{french} \u25CF {prefix}",
        24: "{french} \u25CF {prefix}",
        25: "{french} \u25CF {prefix}",
        26: "{french} \u25CF {prefix}",
        27: "{french}",
        28: "{french}",
        29: "{french}",
        30: "{french}",
    },

    nomen_verben_verbindungen: {
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
        11: "{question}"
           "<br><br><i>{french}</i>",
        12: "{question}"
           "<br><br><i>{french}</i>",

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
        21: "{question}"
            "<br><br><i>{french}</i>",
        22: "{question}"
            "<br><br><i>{french}</i>",
        23: "{question}"
            "<br><br><i>{french}</i>",
        24: "{question}"
            "<br><br><i>{french}</i>",
    },

    praesens: {
        1: "{question} \u25CF {person} _____"
           "<br><br><i>{french}</i>",
        2: "{question} \u25CF {person} _____"
            "<br><br><i>{french}</i>",
        3: "{question} \u25CF {person} _____"
            "<br><br><i>{french}</i>",
        4: "{question} \u25CF {person} _____"
            "<br><br><i>{french}</i>",
        5: "{question} \u25CF {person} _____"
           "<br><br><i>{french}</i>",
        6: "{question} \u25CF {person} _____"
           "<br><br><i>{french}</i>",
        7: "{question} \u25CF {person} _____"
           "<br><br><i>{french}</i>",
        8: "{question} \u25CF {person} _____"
           "<br><br><i>{french}</i>",
        9: "{question} \u25CF {person} _____"
           "<br><br><i>{french}</i>",
        10: "{question} \u25CF {person} _____"
            "<br><br><i>{french}</i>",
        11: "{question} \u25CF {person} _____"
            "<br><br><i>{french}</i>",
        12: "{question} \u25CF {person} _____"
            "<br><br><i>{french}</i>",
        13: "{question} \u25CF {person} _____"
            "<br><br><i>{french}</i>",
        14: "{question} \u25CF {person} _____"
            "<br><br><i>{french}</i>",
        15: "{question} \u25CF {person} _____"
            "<br><br><i>{french}</i>",
        16: "{question} \u25CF {person} _____"
            "<br><br><i>{french}</i>",
        17: "{question} \u25CF {person} _____"
            "<br><br><i>{french}</i>",
        18: "{question} \u25CF {person} _____"
            "<br><br><i>{french}</i>",
        19: "{question} \u25CF {person} _____"
            "<br><br><i>{french}</i>",
        20: "{question} \u25CF {person} _____"
            "<br><br><i>{french}</i>",

        21: "{question} \u25CF {person} _____"
            "<br><br><i>{french}</i>",
        22: "{question} \u25CF {person} _____"
            "<br><br><i>{french}</i>",
        23: "{question} \u25CF {person} _____"
            "<br><br><i>{french}</i>",
        24: "{question} \u25CF {person} _____"
            "<br><br><i>{french}</i>",
        25: "{question} \u25CF {person} _____"
            "<br><br><i>{french}</i>",
        26: "{question} \u25CF {person} _____"
            "<br><br><i>{french}</i>",
        27: "{question} \u25CF {person} _____"
            "<br><br><i>{french}</i>",
        28: "{question} \u25CF {person} _____"
            "<br><br><i>{french}</i>",
        29: "{question} \u25CF {person} _____"
            "<br><br><i>{french}</i>",
        30: "{question} \u25CF {person} _____"
            "<br><br><i>{french}</i>",
        31: "{question} \u25CF {person} _____"
            "<br><br><i>{french}</i>",
        32: "{question} \u25CF {person} _____"
            "<br><br><i>{french}</i>",
        33: "{question} \u25CF {person} _____"
            "<br><br><i>{french}</i>",
        34: "{question} \u25CF {person} _____"
            "<br><br><i>{french}</i>",
        35: "{question} \u25CF {person} _____"
            "<br><br><i>{french}</i>",
        36: "{question} \u25CF {person} _____"
            "<br><br><i>{french}</i>",
        37: "{question} \u25CF {person} _____"
            "<br><br><i>{french}</i>",
        38: "{question} \u25CF {person} _____"
            "<br><br><i>{french}</i>",
        39: "{question} \u25CF {person} _____"
            "<br><br><i>{french}</i>",
        40: "{question} \u25CF {person} _____"
            "<br><br><i>{french}</i>",
    },

    partizip_II: {
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

        11: "{question}"
            "<br><br><i>{french}</i>",
        12: "{question}"
            "<br><br><i>{french}</i>",
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

        21: "{question}"
            "<br><br><i>{french}</i>",
        22: "{question}"
            "<br><br><i>{french}</i>",
        23: "{question}"
            "<br><br><i>{french}</i>",
        24: "{question}"
            "<br><br><i>{french}</i>",
        25: "{question}"
            "<br><br><i>{french}</i>",
        26: "{question}"
            "<br><br><i>{french}</i>",
        27: "{question}"
            "<br><br><i>{french}</i>",
        28: "{question}"
            "<br><br><i>{french}</i>",
        29: "{question}"
            "<br><br><i>{french}</i>",
        30: "{question}"
            "<br><br><i>{french}</i>",

        31: "{question}"
            "<br><br><i>{french}</i>",
        32: "{question}"
            "<br><br><i>{french}</i>",
        33: "{question}"
            "<br><br><i>{french}</i>",
        34: "{question}"
            "<br><br><i>{french}</i>",
        35: "{question}"
            "<br><br><i>{french}</i>",
        36: "{question}"
            "<br><br><i>{french}</i>",
        37: "{question}"
            "<br><br><i>{french}</i>",
        38: "{question}"
            "<br><br><i>{french}</i>",
        39: "{question}"
            "<br><br><i>{french}</i>",
        40: "{question}"
            "<br><br><i>{french}</i>",
        41: "{question}"
            "<br><br><i>{french}</i>",
        42: "{question}"
            "<br><br><i>{french}</i>",
        43: "{question}"
            "<br><br><i>{french}</i>",
        44: "{question}"
            "<br><br><i>{french}</i>",
        45: "{question}"
            "<br><br><i>{french}</i>",
        46: "{question}"
            "<br><br><i>{french}</i>",
        47: "{question}"
            "<br><br><i>{french}</i>",
        48: "{question}"
            "<br><br><i>{french}</i>",
        49: "{question}"
            "<br><br><i>{french}</i>",
        50: "{question}"
            "<br><br><i>{french}</i>",
    },

    praeteritum: {
        1: "{question} \u25CF {person} _____"
            "<br><br><i>{french}</i>",

        2: "{question} \u25CF er/sie/es _____"
            "<br><br><i>{french}</i>",
        3: "{question} \u25CF er/sie/es _____"
            "<br><br><i>{french}</i>",
        4: "{question} \u25CF er/sie/es _____"
            "<br><br><i>{french}</i>",
        5: "{question} \u25CF er/sie/es _____"
            "<br><br><i>{french}</i>",
        6: "{question} \u25CF er/sie/es _____"
            "<br><br><i>{french}</i>",
        7: "{question} \u25CF er/sie/es _____"
            "<br><br><i>{french}</i>",
        8: "{question} \u25CF er/sie/es _____"
            "<br><br><i>{french}</i>",
        9: "{question} \u25CF er/sie/es _____"
            "<br><br><i>{french}</i>",
        10: "{question} \u25CF er/sie/es _____"
            "<br><br><i>{french}</i>",
        11: "{question} \u25CF er/sie/es _____"
            "<br><br><i>{french}</i>",

        12: "{question} \u25CF er/sie/es _____"
            "<br><br><i>{french}</i>",
        13: "{question} \u25CF er/sie/es _____"
            "<br><br><i>{french}</i>",
        14: "{question} \u25CF er/sie/es _____"
            "<br><br><i>{french}</i>",
        15: "{question} \u25CF er/sie/es _____"
            "<br><br><i>{french}</i>",
        16: "{question} \u25CF er/sie/es _____"
            "<br><br><i>{french}</i>",
        17: "{question} \u25CF er/sie/es _____"
            "<br><br><i>{french}</i>",
        18: "{question} \u25CF er/sie/es _____"
            "<br><br><i>{french}</i>",
        19: "{question} \u25CF er/sie/es _____"
            "<br><br><i>{french}</i>",
        20: "{question} \u25CF er/sie/es _____"
            "<br><br><i>{french}</i>",
        21: "{question} \u25CF er/sie/es _____"
            "<br><br><i>{french}</i>",

        22: "{question} \u25CF er/sie/es _____"
            "<br><br><i>{french}</i>",
        23: "{question} \u25CF er/sie/es _____"
            "<br><br><i>{french}</i>",
        24: "{question} \u25CF er/sie/es _____"
            "<br><br><i>{french}</i>",
        25: "{question} \u25CF er/sie/es _____"
            "<br><br><i>{french}</i>",
        26: "{question} \u25CF er/sie/es _____"
            "<br><br><i>{french}</i>",
        27: "{question} \u25CF er/sie/es _____"
            "<br><br><i>{french}</i>",
        28: "{question} \u25CF er/sie/es _____"
            "<br><br><i>{french}</i>",
        29: "{question} \u25CF er/sie/es _____"
            "<br><br><i>{french}</i>",
        30: "{question} \u25CF er/sie/es _____"
            "<br><br><i>{french}</i>",
        31: "{question} \u25CF er/sie/es _____"
            "<br><br><i>{french}</i>",

        32: "{question} \u25CF er/sie/es _____"
            "<br><br><i>{french}</i>",
        33: "{question} \u25CF er/sie/es _____"
            "<br><br><i>{french}</i>",
        34: "{question} \u25CF er/sie/es _____"
            "<br><br><i>{french}</i>",
        35: "{question} \u25CF er/sie/es _____"
            "<br><br><i>{french}</i>",
        36: "{question} \u25CF er/sie/es _____"
            "<br><br><i>{french}</i>",
        37: "{question} \u25CF er/sie/es _____"
            "<br><br><i>{french}</i>",
        38: "{question} \u25CF er/sie/es _____"
            "<br><br><i>{french}</i>",
        39: "{question} \u25CF er/sie/es _____"
            "<br><br><i>{french}</i>",
        40: "{question} \u25CF er/sie/es _____"
            "<br><br><i>{french}</i>",
        41: "{question} \u25CF er/sie/es _____"
            "<br><br><i>{french}</i>",
        42: "{question} \u25CF er/sie/es _____"
            "<br><br><i>{french}</i>",
        43: "{question} \u25CF er/sie/es _____"
            "<br><br><i>{french}</i>",
        44: "{question} \u25CF er/sie/es _____"
            "<br><br><i>{french}</i>",
        45: "{question} \u25CF er/sie/es _____"
            "<br><br><i>{french}</i>",
        46: "{question} \u25CF er/sie/es _____"
            "<br><br><i>{french}</i>",
        47: "{question} \u25CF er/sie/es _____"
            "<br><br><i>{french}</i>",
        48: "{question} \u25CF er/sie/es _____"
            "<br><br><i>{french}</i>",
        49: "{question} \u25CF er/sie/es _____"
            "<br><br><i>{french}</i>",
        50: "{question} \u25CF er/sie/es _____"
            "<br><br><i>{french}</i>",
        51: "{question} \u25CF er/sie/es _____"
            "<br><br><i>{french}</i>",
    },

    praeteritum_partizip_II: {
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
        11: "{question}"
            "<br><br><i>{french}</i>",

        12: "{question}"
            "<br><br><i>{french}</i>",
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
        21: "{question}"
            "<br><br><i>{french}</i>",

        22: "{question}"
            "<br><br><i>{french}</i>",
        23: "{question}"
            "<br><br><i>{french}</i>",
        24: "{question}"
            "<br><br><i>{french}</i>",
        25: "{question}"
            "<br><br><i>{french}</i>",
        26: "{question}"
            "<br><br><i>{french}</i>",
        27: "{question}"
            "<br><br><i>{french}</i>",
        28: "{question}"
            "<br><br><i>{french}</i>",
        29: "{question}"
            "<br><br><i>{french}</i>",
        30: "{question}"
            "<br><br><i>{french}</i>",
        31: "{question}"
            "<br><br><i>{french}</i>",

        32: "{question}"
            "<br><br><i>{french}</i>",
        33: "{question}"
            "<br><br><i>{french}</i>",
        34: "{question}"
            "<br><br><i>{french}</i>",
        35: "{question}"
            "<br><br><i>{french}</i>",
        36: "{question}"
            "<br><br><i>{french}</i>",
        37: "{question}"
            "<br><br><i>{french}</i>",
        38: "{question}"
            "<br><br><i>{french}</i>",
        39: "{question}"
            "<br><br><i>{french}</i>",
        40: "{question}"
            "<br><br><i>{french}</i>",
        41: "{question}"
            "<br><br><i>{french}</i>",
        42: "{question}"
            "<br><br><i>{french}</i>",
        43: "{question}"
            "<br><br><i>{french}</i>",
        44: "{question}"
            "<br><br><i>{french}</i>",
        45: "{question}"
            "<br><br><i>{french}</i>",
        46: "{question}"
            "<br><br><i>{french}</i>",
        47: "{question}"
            "<br><br><i>{french}</i>",
        48: "{question}"
            "<br><br><i>{french}</i>",
        49: "{question}"
            "<br><br><i>{french}</i>",
        50: "{question}"
            "<br><br><i>{french}</i>",
        51: "{question}"
            "<br><br><i>{french}</i>",
    },

    imperativ: {
        1: "{question} \u25CF {person} \u25CF _____"
            "<br><br><i>{french}</i>",
        2: "{question} \u25CF {person} \u25CF _____"
            "<br><br><i>{french}</i>",
        3: "{question} \u25CF {person} \u25CF _____"
            "<br><br><i>{french}</i>",
        4: "{question} \u25CF {person} \u25CF _____"
            "<br><br><i>{french}</i>",
        5: "{question} \u25CF {person} \u25CF _____"
            "<br><br><i>{french}</i>",
        6: "{question} \u25CF {person} \u25CF _____"
            "<br><br><i>{french}</i>",

        7: "{question} \u25CF {person} \u25CF _____"
            "<br><br><i>{french}</i>",
        8: "{question} \u25CF {person} \u25CF _____"
            "<br><br><i>{french}</i>",
        9: "{question} \u25CF {person} \u25CF _____"
            "<br><br><i>{french}</i>",
        10: "{question} \u25CF {person} \u25CF _____"
            "<br><br><i>{french}</i>",
        11: "{question} \u25CF {person} \u25CF _____"
            "<br><br><i>{french}</i>",
        12: "{question} \u25CF {person} \u25CF _____"
            "<br><br><i>{french}</i>",
    },

    konjunktiv_II: {
        1: "{question} \u25CF {person} _____"
            "<br><br><i>{french}</i>",
    },

    konjunktiv_I: {
        1: "{question} \u25CF {person} _____"
            "<br><br><i>{french}</i>",
        2: "{question} \u25CF {person} _____"
            "<br><br><i>{french}</i>",
        3: "{question} \u25CF {person} _____"
            "<br><br><i>{french}</i>",
        4: "{question} \u25CF {person} _____"
            "<br><br><i>{french}</i>",
        5: "{question} \u25CF {person} _____"
            "<br><br><i>{french}</i>",
        6: "{question} \u25CF {person} _____"
            "<br><br><i>{french}</i>",
    },

    partizip_I: {
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
    },

}
