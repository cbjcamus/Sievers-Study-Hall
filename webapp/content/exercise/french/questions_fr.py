from data.data_processing.units import (
    praepositionen_grammatik, praepositionen_verben, praepositionen_adjektive, praepositionen_nomen,
    praepositionen_artikel,
    artikel, artikel_genus, pronomen, konnektoren, fragen, adverbien,
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

        17: "{french}",
        18: "{question}"
            "<br><br><i>{french}</i>",
        19: "{french}",
        20: "{question}"
            "<br><br><i>{french}</i>",
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
        1: "{french} = {german} _____",
        2: "{question}"
            "<br><br><i>{french}</i>",
        3: "{french} = {german} _____",
        4: "{question}"
           "<br><br><i>{french}</i>",

        5: "{french} = {german} _____",
        6: "{question}"
           "<br><br><i>{french}</i>",
        7: "{french} = {german} _____",
        8: "{question}"
           "<br><br><i>{french}</i>",
        9: "{french} = {german} _____",
        10: "{question}"
           "<br><br><i>{french}</i>",

        11: "{french} = {german} _____",
        12: "{question}"
           "<br><br><i>{french}</i>",
        13: "{french} = {german} _____",
        14: "{question}"
           "<br><br><i>{french}</i>",
        15: "{french} = {german} _____",
        16: "{question}"
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

    artikel: {
        1: "{question} \u25CF {gender_french}, {case_french}",
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
        11: "{question} \u25CF {gender_french}, {case_french}",
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
        20: "{question} \u25CF {gender_french}, {case_french}",
        21: "{question}"
            "<br><br><i>{french}</i>",
        22: "{question} \u25CF {gender_french}, {case_french}",
        23: "{question}"
            "<br><br><i>{french}</i>",
        24: "{question} \u25CF {gender_french}, {case_french}",
        25: "{question}"
            "<br><br><i>{french}</i>",

        26: "{question} \u25CF {gender_french}, {case_french}",
        27: "{question}"
            "<br><br><i>{french}</i>",
        28: "{question} \u25CF {gender_french}, {case_french}",
        29: "{question}"
            "<br><br><i>{french}</i>",
        30: "{question}"
            "<br><br><i>{french}</i>",
        31: "{question}"
            "<br><br><i>{french}</i>",
        32: "{french}",
        33: "{question}"
            "<br><br><i>{french}</i>",

        34: "{question} \u25CF {gender_french}, {case_french}",
        35: "{question}"
            "<br><br><i>{french}</i>",
        36: "{question} \u25CF {gender_french}, {case_french}",
        37: "{question}"
            "<br><br><i>{french}</i>",
        38: "{question} \u25CF {gender_french}, {case_french}",
        39: "{question} \u25CF {person}" 
            "<br><br><i>{french}</i>",

        40: "{question} \u25CF {gender_french}, {case_french}",
        41: "{question}"
            "<br><br><i>{french}</i>",

        42: "{question} \u25CF {gender_french}, {case_french}",
        43: "{question}"
            "<br><br><i>{french}</i>",
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
        3: "{question}"
            "<br><br><i>{french}</i>",
        4: "{question}"
            "<br><br><i>{french}</i>",
        5: "{question}"
            "<br><br><i>{french}</i>",
        6: "{question}"
            "<br><br><i>{french}</i>",

        7: "{french} \u25CF {case_french}",
        8: "{question}"
            "<br><br><i>{french}</i>",
        9: "{question}"
            "<br><br><i>{french}</i>",
        10: "{question}"
            "<br><br><i>{french}</i>",
        11: "{german} \u25CF {gender_french}, {case_french}",
        12: "{question}"
            "<br><br><i>{french}</i>",
        13: "{german} \u25CF {gender_french}, {case_french}",
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
        7: "{question}",

        8: "{french} \u25CF {case_french}",
        9: "{question}"
           "<br><br><i>{french}</i>",
        10: "{french} \u25CF {case_french}",
        11: "{question}"
           "<br><br><i>{french}</i>",
        12: "{question}",

        13: "{french} \u25CF {case_french}",
        14: "{question}"
           "<br><br><i>{french}</i>",
        15: "{question}",
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
        17: "{french}",
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
        27: "{french}",
        28: "{question}"
            "<br><br><i>{french}</i>",

        29: "{french}",
        30: "{question}"
            "<br><br><i>{french}</i>",
        31: "{french}",
        32: "{question}"
            "<br><br><i>{french}</i>",
        33: "{french}",
        34: "{question}",
        35: "{french}",
        36: "{question}",
        37: "{french}",
        38: "{question}",
        39: "{french}",
        40: "{question}",
        41: "{french}",
        42: "{question}",
        43: "{french}",
        44: "{question}",
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

        31: "{question}",
        32: "{question}",
        33: "{question}",
        34: "{question}",
        35: "{question}",
        36: "{question}",
        37: "{question}",
        38: "{question}",
        39: "{question}",
        40: "{question}",
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
    },

    praesens: {
        1: "{question} \u25CF {person} _____",
        2: "{question} \u25CF {person} _____",
        3: "{question} \u25CF {person} _____",
        4: "{question} \u25CF {person} _____",
        5: "{question} \u25CF {person} _____",
        6: "{question} \u25CF {person} _____",
        7: "{question} \u25CF {person} _____",
        8: "{question} \u25CF {person} _____",
        9: "{question} \u25CF {person} _____",
        10: "{question} \u25CF {person} _____",
        11: "{question} \u25CF {person} _____",
        12: "{question} \u25CF {person} _____",
        13: "{question} \u25CF {person} _____",
        14: "{question} \u25CF {person} _____",
        15: "{question} \u25CF {person} _____",
        16: "{question} \u25CF {person} _____",
        17: "{question} \u25CF {person} _____",
        18: "{question} \u25CF {person} _____",
        19: "{question} \u25CF {person} _____",
        20: "{question} \u25CF {person} _____",

        21: "{question} \u25CF {person} _____",
        22: "{question} \u25CF {person} _____",
        23: "{question} \u25CF {person} _____",
        24: "{question} \u25CF {person} _____",
        25: "{question} \u25CF {person} _____",
        26: "{question} \u25CF {person} _____",
        27: "{question} \u25CF {person} _____",
        28: "{question} \u25CF {person} _____",
        29: "{question} \u25CF {person} _____",
        30: "{question} \u25CF {person} _____",
        31: "{question} \u25CF {person} _____",
        32: "{question} \u25CF {person} _____",
        33: "{question} \u25CF {person} _____",
        34: "{question} \u25CF {person} _____",
        35: "{question} \u25CF {person} _____",
        36: "{question} \u25CF {person} _____",
        37: "{question} \u25CF {person} _____",
        38: "{question} \u25CF {person} _____",
        39: "{question} \u25CF {person} _____",
        40: "{question} \u25CF {person} _____",
    },

    partizip_II: {
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
        13: "{question}",
        14: "{question}",
        15: "{question}",
        16: "{question}",
        17: "{question}",
        18: "{question}",
        19: "{question}",
        20: "{question}",

        21: "{question}",
        22: "{question}",
        23: "{question}",
        24: "{question}",
        25: "{question}",
        26: "{question}",
        27: "{question}",
        28: "{question}",
        29: "{question}",
        30: "{question}",

        31: "{question}",
        32: "{question}",
        33: "{question}",
        34: "{question}",
        35: "{question}",
        36: "{question}",
        37: "{question}",
        38: "{question}",
        39: "{question}",
        40: "{question}",
    },

    praeteritum: {
        1: "{question} \u25CF {person} _____",

        2: "{question} \u25CF er/sie/es _____",
        3: "{question} \u25CF er/sie/es _____",
        4: "{question} \u25CF er/sie/es _____",
        5: "{question} \u25CF er/sie/es _____",
        6: "{question} \u25CF er/sie/es _____",
        7: "{question} \u25CF er/sie/es _____",
        8: "{question} \u25CF er/sie/es _____",
        9: "{question} \u25CF er/sie/es _____",
        10: "{question} \u25CF er/sie/es _____",
        11: "{question} \u25CF er/sie/es _____",

        12: "{question} \u25CF er/sie/es _____",
        13: "{question} \u25CF er/sie/es _____",
        14: "{question} \u25CF er/sie/es _____",
        15: "{question} \u25CF er/sie/es _____",
        16: "{question} \u25CF er/sie/es _____",
        17: "{question} \u25CF er/sie/es _____",
        18: "{question} \u25CF er/sie/es _____",
        19: "{question} \u25CF er/sie/es _____",
        20: "{question} \u25CF er/sie/es _____",
        21: "{question} \u25CF er/sie/es _____",

        22: "{question} \u25CF er/sie/es _____",
        23: "{question} \u25CF er/sie/es _____",
        24: "{question} \u25CF er/sie/es _____",
        25: "{question} \u25CF er/sie/es _____",
        26: "{question} \u25CF er/sie/es _____",
        27: "{question} \u25CF er/sie/es _____",
        28: "{question} \u25CF er/sie/es _____",
        29: "{question} \u25CF er/sie/es _____",
        30: "{question} \u25CF er/sie/es _____",
        31: "{question} \u25CF er/sie/es _____",

        32: "{question} \u25CF er/sie/es _____",
        33: "{question} \u25CF er/sie/es _____",
        34: "{question} \u25CF er/sie/es _____",
        35: "{question} \u25CF er/sie/es _____",
        36: "{question} \u25CF er/sie/es _____",
        37: "{question} \u25CF er/sie/es _____",
        38: "{question} \u25CF er/sie/es _____",
        39: "{question} \u25CF er/sie/es _____",
        40: "{question} \u25CF er/sie/es _____",
        41: "{question} \u25CF er/sie/es _____",
    },

    praeteritum_partizip_II: {
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
        13: "{question}",
        14: "{question}",
        15: "{question}",
        16: "{question}",
        17: "{question}",
        18: "{question}",
        19: "{question}",
        20: "{question}",
        21: "{question}",

        22: "{question}",
        23: "{question}",
        24: "{question}",
        25: "{question}",
        26: "{question}",
        27: "{question}",
        28: "{question}",
        29: "{question}",
        30: "{question}",
        31: "{question}",

        32: "{question}",
        33: "{question}",
        34: "{question}",
        35: "{question}",
        36: "{question}",
        37: "{question}",
        38: "{question}",
        39: "{question}",
        40: "{question}",
        41: "{question}",
    },

    imperativ: {
        1: "{question} \u25CF {person} \u25CF _____",
        2: "{question} \u25CF {person} \u25CF _____",
        3: "{question} \u25CF {person} \u25CF _____",
        4: "{question} \u25CF {person} \u25CF _____",
        5: "{question} \u25CF {person} \u25CF _____",
        6: "{question} \u25CF {person} \u25CF _____",

        7: "{question} \u25CF {person} \u25CF _____",
        8: "{question} \u25CF {person} \u25CF _____",
        9: "{question} \u25CF {person} \u25CF _____",
        10: "{question} \u25CF {person} \u25CF _____",
        11: "{question} \u25CF {person} \u25CF _____",
        12: "{question} \u25CF {person} \u25CF _____",
    },

    konjunktiv_II: {
        1: "{question} \u25CF {person} _____",
    },

    konjunktiv_I: {
        1: "{question} \u25CF {person} _____",
        2: "{question} \u25CF {person} _____",
        3: "{question} \u25CF {person} _____",
        4: "{question} \u25CF {person} _____",
        5: "{question} \u25CF {person} _____",
        6: "{question} \u25CF {person} _____",
    },

    partizip_I: {
        1: "{question}",
        2: "{question}",
        3: "{question}",
        4: "{question}",
        5: "{question}",
    },

}
