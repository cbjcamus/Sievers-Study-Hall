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

QUESTION_EN = {

    praepositionen_grammatik: {
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

        17: "{english}",
        18: "{question}"
            "<br><br><i>{english}</i>",
        19: "{english}",
        20: "{question}"
            "<br><br><i>{english}</i>",
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
        9: "{question}"
           "<br><br><i>{english}</i>",
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
    },

    praepositionen_nomen: {
        1: "{question} = {german} _____",
        2: "{question}"
            "<br><br><i>{english}</i>",
        3: "{question} = {german} _____",
        4: "{question}"
           "<br><br><i>{english}</i>",

        5: "{question} = {german} _____",
        6: "{question}"
           "<br><br><i>{english}</i>",
        7: "{question} = {german} _____",
        8: "{question}"
           "<br><br><i>{english}</i>",
        9: "{question} = {german} _____",
        10: "{question}"
           "<br><br><i>{english}</i>",

        11: "{question} = {german} _____",
        12: "{question}"
           "<br><br><i>{english}</i>",
        13: "{question} = {german} _____",
        14: "{question}"
           "<br><br><i>{english}</i>",
        15: "{question} = {german} _____",
        16: "{question}"
            "<br><br><i>{english}</i>",
    },

    praepositionen_artikel: {
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
    },

    artikel: {
        1: "{question} \u25CF {gender_english}, {case_english}",
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
        11: "{question} \u25CF {gender_english}, {case_english}",
        12: "{question}"
           "<br><br><i>{english}</i>",
        13: "{question}"
           "<br><br><i>{english}</i>",
        14: "{question}"
           "<br><br><i>{english}</i>",
        15: "{question}"
           "<br><br><i>{english}</i>",
        16: "{question}"
            "<br><br><i>{english}</i>",
        17: "{question}"
            "<br><br><i>{english}</i>",
        18: "{question}"
            "<br><br><i>{english}</i>",
        19: "{question}"
            "<br><br><i>{english}</i>",
        20: "{question} \u25CF {gender_english}, {case_english}",
        21: "{question}"
            "<br><br><i>{english}</i>",
        22: "{question} \u25CF {gender_english}, {case_english}",
        23: "{question}"
            "<br><br><i>{english}</i>",
        24: "{question} \u25CF {gender_english}, {case_english}",
        25: "{question}"
            "<br><br><i>{english}</i>",

        26: "{question} \u25CF {gender_english}, {case_english}",
        27: "{question}"
            "<br><br><i>{english}</i>",
        28: "{question} \u25CF {gender_english}, {case_english}",
        29: "{question}"
            "<br><br><i>{english}</i>",
        30: "{question}"
            "<br><br><i>{english}</i>",
        31: "{question}"
            "<br><br><i>{english}</i>",
        32: "{english}",
        33: "{question}"
            "<br><br><i>{english}</i>",

        34: "{question} \u25CF {gender_english}, {case_english}",
        35: "{question}"
            "<br><br><i>{english}</i>",
        36: "{question} \u25CF {gender_english}, {case_english}",
        37: "{question}"
            "<br><br><i>{english}</i>",
        38: "{question} \u25CF {gender_english}, {case_english}",
        39: "{question} \u25CF {person}" 
            "<br><br><i>{english}</i>",

        40: "{question} \u25CF {gender_english}, {case_english}",
        41: "{question}"
            "<br><br><i>{english}</i>",

        42: "{question} \u25CF {gender_english}, {case_english}",
        43: "{question}"
            "<br><br><i>{english}</i>",
    },

    artikel_genus: {
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
        11: "{question}"
           "<br><br><i>{english}</i>",
        12: "{question}"
           "<br><br><i>{english}</i>",
        13: "{question}"
           "<br><br><i>{english}</i>",
        14: "{question}"
           "<br><br><i>{english}</i>",
        15: "{question}"
           "<br><br><i>{english}</i>",
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

        21: "{question}"
           "<br><br><i>{english}</i>",
        22: "{question}"
           "<br><br><i>{english}</i>",
        23: "{question}"
           "<br><br><i>{english}</i>",
        24: "{question}"
           "<br><br><i>{english}</i>",
        25: "{question}"
           "<br><br><i>{english}</i>",
        26: "{question}"
           "<br><br><i>{english}</i>",
        27: "{question}"
           "<br><br><i>{english}</i>",
        28: "{question}"
           "<br><br><i>{english}</i>",
        29: "{question}"
           "<br><br><i>{english}</i>",
        30: "{question}"
            "<br><br><i>{english}</i>",
        31: "{question}"
           "<br><br><i>{english}</i>",
        32: "{question}"
           "<br><br><i>{english}</i>",
        33: "{question}"
           "<br><br><i>{english}</i>",
        34: "{question}"
           "<br><br><i>{english}</i>",
        35: "{question}"
           "<br><br><i>{english}</i>",

        36: "{question}"
           "<br><br><i>{english}</i>",
        37: "{question}"
           "<br><br><i>{english}</i>",
        38: "{question}"
           "<br><br><i>{english}</i>",
        39: "{question}"
           "<br><br><i>{english}</i>",
        40: "{question}"
            "<br><br><i>{english}</i>",
        41: "{question}"
            "<br><br><i>{english}</i>",
        42: "{question}"
            "<br><br><i>{english}</i>",
        43: "{question}"
            "<br><br><i>{english}</i>",
        44: "{question}"
            "<br><br><i>{english}</i>",
        45: "{question}"
            "<br><br><i>{english}</i>",
        46: "{question}"
            "<br><br><i>{english}</i>",
        47: "{question}"
            "<br><br><i>{english}</i>",
        48: "{question}"
            "<br><br><i>{english}</i>",
        49: "{question}"
            "<br><br><i>{english}</i>",
        50: "{question}"
            "<br><br><i>{english}</i>",
        51: "{question}"
            "<br><br><i>{english}</i>",
        52: "{question}"
            "<br><br><i>{english}</i>",
        53: "{question}"
            "<br><br><i>{english}</i>",
        54: "{question}"
            "<br><br><i>{english}</i>",
        55: "{question}"
            "<br><br><i>{english}</i>",
        56: "{question}"
            "<br><br><i>{english}</i>",
        57: "{question}"
            "<br><br><i>{english}</i>",
        58: "{question}"
            "<br><br><i>{english}</i>",
        59: "{question}"
            "<br><br><i>{english}</i>",
        60: "{question}"
            "<br><br><i>{english}</i>",
        61: "{question}"
            "<br><br><i>{english}</i>",
        62: "{question}"
            "<br><br><i>{english}</i>",
        63: "{question}"
            "<br><br><i>{english}</i>",
        64: "{question}"
            "<br><br><i>{english}</i>",
        65: "{question}"
            "<br><br><i>{english}</i>",
        66: "{question}"
            "<br><br><i>{english}</i>",
        67: "{question}"
            "<br><br><i>{english}</i>",
        68: "{question}"
            "<br><br><i>{english}</i>",
        69: "{question}"
            "<br><br><i>{english}</i>",
        70: "{question}"
            "<br><br><i>{english}</i>",
        71: "{question}"
            "<br><br><i>{english}</i>",
        72: "{question}"
            "<br><br><i>{english}</i>",
        73: "{question}"
            "<br><br><i>{english}</i>",
        74: "{question}"
            "<br><br><i>{english}</i>",
        75: "{question}"
            "<br><br><i>{english}</i>",
        76: "{question}"
            "<br><br><i>{english}</i>",
        77: "{question}"
            "<br><br><i>{english}</i>",
        78: "{question}"
            "<br><br><i>{english}</i>",
        79: "{question}"
            "<br><br><i>{english}</i>",
        80: "{question}"
            "<br><br><i>{english}</i>",
        81: "{question}"
            "<br><br><i>{english}</i>",
        82: "{question}"
            "<br><br><i>{english}</i>",
        83: "{question}"
            "<br><br><i>{english}</i>",
        84: "{question}"
            "<br><br><i>{english}</i>",
        85: "{question}"
            "<br><br><i>{english}</i>",
        86: "{question}"
            "<br><br><i>{english}</i>",
        87: "{question}"
            "<br><br><i>{english}</i>",
    },

    pronomen: {
        1: "{english} \u25CF {case_english}",
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

        7: "{english} \u25CF {case_english}",
        8: "{question}"
            "<br><br><i>{english}</i>",
        9: "{question}"
            "<br><br><i>{english}</i>",
        10: "{question}"
            "<br><br><i>{english}</i>",
        11: "{german} \u25CF {gender_english}, {case_english}",
        12: "{question}"
            "<br><br><i>{english}</i>",
        13: "{german} \u25CF {gender_english}, {case_english}",
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
        21: "{question}"
            "<br><br><i>{english}</i>",
        22: "{question}"
            "<br><br><i>{english}</i>",

        23: "{question}"
            "<br><br><i>{english}</i>",
        24: "{question}"
            "<br><br><i>{english}</i>",
        25: "{question}"
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
        7: "{question}",

        8: "{english} \u25CF {case_english}",
        9: "{question}"
           "<br><br><i>{english}</i>",
        10: "{english} \u25CF {case_english}",
        11: "{question}"
           "<br><br><i>{english}</i>",
        12: "{question}",

        13: "{english} \u25CF {case_english}",
        14: "{question}"
           "<br><br><i>{english}</i>",
        15: "{question}",
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
        17: "{english}",
        18: "{question}"
            "<br><br><i>{english}</i>",

        19: "{english}",
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

        29: "{english}",
        30: "{question}"
            "<br><br><i>{english}</i>",
        31: "{english}",
        32: "{question}"
            "<br><br><i>{english}</i>",
        33: "{english}",
        34: "{question}",
        35: "{english}",
        36: "{question}",
        37: "{english}",
        38: "{question}",
        39: "{english}",
        40: "{question}",
        41: "{english}",
        42: "{question}",
        43: "{english}",
        44: "{question}",
    },

    adjektive: {
        1: "{english}",
        2: "{english}",
        3: "{english}",
        4: "{question}",
        5: "{question}",
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
        11: "{question}"
            "<br><br><i>{english}</i>",
        12: "{question}"
            "<br><br><i>{english}</i>",

        13: "{english}",
        14: "{english}",
        15: "{english}",
        16: "{question}",
        17: "{question}",
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
        25: "{english}",
        26: "{english}",
        27: "{question}",
        28: "{question}",
        29: "{question}",

        30: "{english}",
        31: "{english}",
        32: "{english}",
        33: "{english}",
        34: "{english}",
        35: "{english}",
    },

    adjektivdeklinationen: {
        1: "{question} \u25CF {case_english} \u25CF {adjective}",
        2: "{question} \u25CF {adjective}",
        3: "{question} \u25CF {case_english} \u25CF {adjective}",
        4: "{question} \u25CF {adjective}",
        5: "{question} \u25CF {case_english} \u25CF {adjective}",
        6: "{question} \u25CF {adjective}",
        7: "{question} \u25CF {case_english} \u25CF {adjective}",
        8: "{question} \u25CF {adjective}",
        9: "{question} \u25CF {case_english} \u25CF {adjective}",
        10: "{question} \u25CF {adjective}",
        11: "{question} \u25CF {adjective}",
        12: "{question} \u25CF {adjective}",

        13: "{question} \u25CF {case_english} \u25CF {adjective}",
        14: "{question} \u25CF {adjective}",
        15: "{question} \u25CF {case_english} \u25CF {adjective}",
        16: "{question} \u25CF {adjective}",
        17: "{question} \u25CF {case_english} \u25CF {adjective}",
        18: "{question} \u25CF {adjective}",

        19: "{question} \u25CF {case_english} \u25CF {adjective}",
        20: "{question} \u25CF {adjective}",
        21: "{question} \u25CF {case_english} \u25CF {adjective}",
        22: "{question} \u25CF {adjective}",

        23: "{question} \u25CF {case_english} \u25CF {adjective}",
        24: "{question} \u25CF {adjective}",
        25: "{question} \u25CF {case_english} \u25CF {adjective}",
        26: "{question} \u25CF {adjective}",
        27: "{question} \u25CF {case_english} \u25CF {adjective}",
        28: "{question} \u25CF {adjective}",
        29: "{question} \u25CF {case_english} \u25CF {adjective}",
        30: "{question} \u25CF {adjective}",
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
        1: "{root_english} → {root_german}"
           "<br><br>{english} → _____ ",
        2: "{english} \u25CF {prefix}",
        3: "{english}",

        4: "{root_english} → {root_german}"
           "<br><br>{english} → _____ ",
        5: "{english} \u25CF {prefix}",
        6: "{english}",

        7: "{root_english} → {root_german}"
           "<br><br>{english} → _____ ",
        8: "{root_english} → {root_german}"
           "<br><br>{english} → _____ ",
        9: "{root_english} → {root_german}"
           "<br><br>{english} → _____ ",
        10: "{root_english} → {root_german}"
            "<br><br>{english} → _____ ",
        11: "{english} \u25CF {prefix}",
        12: "{english} \u25CF {prefix}",
        14: "{english} \u25CF {prefix}",
        13: "{english} \u25CF {prefix}",
        15: "{english}",
        16: "{english}",
        17: "{english}",
        18: "{english}",

        19: "{root_english} → {root_german}"
            "<br><br>{english} → _____ ",
        20: "{root_english} → {root_german}"
            "<br><br>{english} → _____ ",
        21: "{root_english} → {root_german}"
            "<br><br>{english} → _____ ",
        22: "{root_english} → {root_german}"
            "<br><br>{english} → _____ ",
        23: "{english} \u25CF {prefix}",
        24: "{english} \u25CF {prefix}",
        25: "{english} \u25CF {prefix}",
        26: "{english} \u25CF {prefix}",
        27: "{english}",
        28: "{english}",
        29: "{english}",
        30: "{english}",
    },

    nomen_verben_verbindungen: {
        1: "{question}"
           "<br><br><i>{english}</i>",
        2: "{question}"
           "<br><br><i>{english}</i>",
        3: "{question}"
           "<br><br><i>{english}</i>",
        4: "{question}"
           "<br><br><i>{english}</i>",
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
