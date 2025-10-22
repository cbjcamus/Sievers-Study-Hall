from data.data_processing.units import (
    praepositionen_grammatik, praepositionen_verben, praepositionen_adjektive, praepositionen_nomen,
    praepositionen_artikel,
    artikel, artikel_genus, pronomen, konnektoren, fragen, adverbien,
    adjektive, adjektivdeklinationen,
    verben, trennbare_verben, nomen_verben_verbindungen,
    praesens, imperativ, partizip_II, praeteritum, praeteritum_partizip_II, konjunktiv_II, konjunktiv_I, partizip_I,
)

FEEDBACK_EN = {

    praepositionen_grammatik: {
        1: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{explanation_english}"
           "<br><br>Correct answer(s): {correct_answers}",
        2: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{explanation_english}"
           "<br><br>Correct answer(s): {correct_answers}",
        3: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{explanation_english}"
           "<br><br>Correct answer(s): {correct_answers}",
        4: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{explanation_english}"
           "<br><br>Correct answer(s): {correct_answers}",

        5: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{explanation_english}"
           "<br><br>Correct answer(s): {correct_answers}",
        6: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{explanation_english}"
           "<br><br>Correct answer(s): {correct_answers}",
        7: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{explanation_english}"
           "<br><br>Correct answer(s): {correct_answers}",
        8: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{explanation_english}"
           "<br><br>Correct answer(s): {correct_answers}",

        9: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
           "<br><br>Correct answer(s): {correct_answers}",
        10: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{explanation_english}"
           "<br><br>Correct answer(s): {correct_answers}",
        11: "{english} = {correct_answers}",
        12: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",

        13: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        14: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        15: "{english} = {correct_answers}",
        16: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",

        17: "{english} = {correct_answers}",
        18: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        19: "{english} = {correct_answers}",
        20: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
    },

    praepositionen_verben: {
        1: "{english} = {german} + {case_english}",
        2: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",
        3: "{english} = {german} + {case_english}",
        4: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",

        5: "{english} = {german} + {case_english}",
        6: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",
        7: "{english} = {german} + {case_english}",
        8: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",
        9: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",
        10: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",

        11: "{english} = {german} + {case_english}",
        12: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        13: "{english} = {german} + {case_english}",
        14: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        15: "{english} = {german} + {case_english}",
        16: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        17: "{english} = {german} + {case_english}",
        18: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",

        19: "{english} = {german} + {case_english}",
        20: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        21: "{english} = {german} + {case_english}",
        22: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        23: "{english} = {german} + {case_english}",
        24: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        25: "{english} = {german} + {case_english}",
        26: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",

        27: "{english} = {german} + {case_english}",
        28: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        29: "{english} = {german} + {case_english}",
        30: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        31: "{english} = {german} + {case_english}",
        32: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        33: "{english} = {german} + {case_english}",
        34: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
    },

    praepositionen_adjektive: {
        1: "{english} = {german}",
        2: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        3: "{english} = {german}",
        4: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",

        5: "{english} = {german}",
        6: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        7: "{english} = {german}",
        8: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",
        9: "{english} = {german}",
        10: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",

        11: "{english} = {german}",
        12: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",
        13: "{english} = {german}",
        14: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",
        15: "{english} = {german}",
        16: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",
    },

    praepositionen_nomen: {
        1: "{previous_question} = {german} {correct_answers}",
        2: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        3: "{previous_question} = {german} {correct_answers}",
        4: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",

        5: "{previous_question} = {german} {correct_answers}",
        6: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        7: "{previous_question} = {german} {correct_answers}",
        8: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        9: "{previous_question} = {german} {correct_answers}",
        10: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",

        11: "{previous_question} = {german} {correct_answers}",
        12: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",
        13: "{previous_question} = {german} {correct_answers}",
        14: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",
        15: "{previous_question} = {german} {correct_answers}",
        16: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
    },

    praepositionen_artikel: {
        1: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{case_english}, {gender_english} → {correct_answers}",
        2: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{case_english}, {gender_english} → {correct_answers}",
        3: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{case_english}, {gender_english} → {correct_answers}",
        4: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{case_english}, {gender_english} → {correct_answers}",
        5: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{case_english}, {gender_english} → {correct_answers}",
        6: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{case_english}, {gender_english} → {correct_answers}",
        7: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{case_english}, {gender_english} → {correct_answers}",
        8: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{case_english}, {gender_english} → {correct_answers}",
        9: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{case_english}, {gender_english} → {correct_answers}",
    },

    artikel: {
        1: "{previous_question}, {gender_english}, {case_english} → {correct_answers}",
        2: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender_english}, {case_english} → {correct_answers}",
        3: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender_english}, {case_english} → {correct_answers}",
        4: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender_english}, {case_english} → {correct_answers}",
        5: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{gender_english}, {case_english} → {correct_answers}",
        6: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{gender_english}, {case_english} → {correct_answers}",
        7: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{gender_english}, {case_english} → {correct_answers}",
        8: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{gender_english}, {case_english} → {correct_answers}",
        9: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender_english}, {case_english} → {correct_answers}",
        10: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender_english}, {case_english} → {correct_answers}",
        11: "{previous_question}, {gender_english}, {case_english} → {correct_answers}",
        12: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender_english}, {case_english} → {correct_answers}",
        13: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender_english}, {case_english} → {correct_answers}",
        14: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender_english}, {case_english} → {correct_answers}",
        15: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender_english}, {case_english} → {correct_answers}",
        16: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender_english}, {case_english} → {correct_answers}",
        17: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender_english}, {case_english} → {correct_answers}",
        18: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender_english}, {case_english} → {correct_answers}",
        19: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender_english}, {case_english} → {correct_answers}",
        20: "{previous_question}, {gender_english}, {case_english} → {correct_answers}",
        21: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender_english}, {case_english} → {correct_answers}",
        22: "{previous_question}, {gender_english}, {case_english} → {correct_answers}",
        23: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender_english}, {case_english} → {correct_answers}",
        24: "{previous_question}, {gender_english}, {case_english} → {correct_answers}",
        25: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender_english}, {case_english} → {correct_answers}",

        26: "{previous_question}, {gender_english}, {case_english} → {correct_answers}",
        27: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender_english}, {case_english} → {correct_answers}",
        28: "{previous_question}, {gender_english}, {case_english} → {correct_answers}",
        29: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender_english}, {case_english} → {correct_answers}",
        30: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        31: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        32: "{english} = {correct_answers}",
        33: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",

        34: "{previous_question}, {gender_english}, {case_english} → {correct_answers}",
        35: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender_english}, {case_english} → {correct_answers}",
        36: "{gender_english}, {case_english} → {correct_answers}",
        37: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender_english}, {case_english} → {correct_answers}",
        38: "{previous_question}, {gender_english}, {case_english} → {correct_answers}",
        39: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{person}, {gender_english}, {case_english} → {correct_answers}",

        40: "{previous_question}, {gender_english}, {case_english} → {correct_answers}",
        41: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender_english}, {case_english} → {correct_answers}",

        42: "{previous_question}, {gender_english}, {case_english} → {correct_answers}",
        43: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender_english}, {case_english} → {correct_answers}",
    },

    artikel_genus: {
        1: "{german}"
            "<br><br><i>{english}</i>",
        2: "{german}"
           "<br><br><i>{english}</i>",
        3: "{german}"
           "<br><br><i>{english}</i>",
        4: "{german}"
           "<br><br><i>{english}</i>",
        5: "{german}"
           "<br><br><i>{english}</i>",
        6: "{german}"
           "<br><br><i>{english}</i>",
        7: "{german}"
           "<br><br><i>{english}</i>",
        8: "{german}"
           "<br><br><i>{english}</i>",
        9: "{german}"
           "<br><br><i>{english}</i>",
        10: "{german}"
           "<br><br><i>{english}</i>",
        11: "{german}"
           "<br><br><i>{english}</i>",
        12: "{german}"
           "<br><br><i>{english}</i>",
        13: "{german}"
           "<br><br><i>{english}</i>",
        14: "{german}"
           "<br><br><i>{english}</i>",
        15: "{german}"
           "<br><br><i>{english}</i>",
        16: "{german}"
           "<br><br><i>{english}</i>",
        17: "{german}"
           "<br><br><i>{english}</i>",
        18: "{german}"
           "<br><br><i>{english}</i>",
        19: "{german}"
           "<br><br><i>{english}</i>",
        20: "{german}"
            "<br><br><i>{english}</i>",

        21: "{german}"
            "<br><br><i>{english}</i>",
        22: "{german}"
            "<br><br><i>{english}</i>",
        23: "{german}"
            "<br><br><i>{english}</i>",
        24: "{german}"
            "<br><br><i>{english}</i>",
        25: "{german}"
            "<br><br><i>{english}</i>",
        26: "{german}"
            "<br><br><i>{english}</i>",
        27: "{german}"
            "<br><br><i>{english}</i>",
        28: "{german}"
            "<br><br><i>{english}</i>",
        29: "{german}"
            "<br><br><i>{english}</i>",
        30: "{german}"
            "<br><br><i>{english}</i>",
        31: "{german}"
            "<br><br><i>{english}</i>",
        32: "{german}"
            "<br><br><i>{english}</i>",
        33: "{german}"
            "<br><br><i>{english}</i>",
        34: "{german}"
            "<br><br><i>{english}</i>",
        35: "{german}"
            "<br><br><i>{english}</i>",

        36: "{german}"
            "<br><br><i>{english}</i>",
        37: "{german}"
            "<br><br><i>{english}</i>",
        38: "{german}"
            "<br><br><i>{english}</i>",
        39: "{german}"
            "<br><br><i>{english}</i>",
        40: "{german}"
            "<br><br><i>{english}</i>",
        41: "{german}"
            "<br><br><i>{english}</i>",
        42: "{german}"
            "<br><br><i>{english}</i>",
        43: "{german}"
            "<br><br><i>{english}</i>",
        44: "{german}"
            "<br><br><i>{english}</i>",
        45: "{german}"
            "<br><br><i>{english}</i>",
        46: "{german}"
            "<br><br><i>{english}</i>",
        47: "{german}"
            "<br><br><i>{english}</i>",
        48: "{german}"
            "<br><br><i>{english}</i>",
        49: "{german}"
            "<br><br><i>{english}</i>",
        50: "{german}"
            "<br><br><i>{english}</i>",
        51: "{german}"
            "<br><br><i>{english}</i>",
        52: "{german}"
            "<br><br><i>{english}</i>",
        53: "{german}"
            "<br><br><i>{english}</i>",
        54: "{german}"
            "<br><br><i>{english}</i>",
        55: "{german}"
            "<br><br><i>{english}</i>",
        56: "{german}"
            "<br><br><i>{english}</i>",
        57: "{german}"
            "<br><br><i>{english}</i>",
        58: "{german}"
            "<br><br><i>{english}</i>",
        59: "{german}"
            "<br><br><i>{english}</i>",
        60: "{german}"
            "<br><br><i>{english}</i>",
        61: "{german}"
            "<br><br><i>{english}</i>",
        62: "{german}"
            "<br><br><i>{english}</i>",
        63: "{german}"
            "<br><br><i>{english}</i>",
        64: "{german}"
            "<br><br><i>{english}</i>",
        65: "{german}"
            "<br><br><i>{english}</i>",
        66: "{german}"
            "<br><br><i>{english}</i>",
        67: "{german}"
            "<br><br><i>{english}</i>",
        68: "{german}"
            "<br><br><i>{english}</i>",
        69: "{german}"
            "<br><br><i>{english}</i>",
        70: "{german}"
            "<br><br><i>{english}</i>",
        71: "{german}"
            "<br><br><i>{english}</i>",
        72: "{german}"
            "<br><br><i>{english}</i>",
        73: "{german}"
            "<br><br><i>{english}</i>",
        74: "{german}"
            "<br><br><i>{english}</i>",
        75: "{german}"
            "<br><br><i>{english}</i>",
        76: "{german}"
            "<br><br><i>{english}</i>",
        77: "{german}"
            "<br><br><i>{english}</i>",
        78: "{german}"
            "<br><br><i>{english}</i>",
        79: "{german}"
            "<br><br><i>{english}</i>",
        80: "{german}"
            "<br><br><i>{english}</i>",
        81: "{german}"
            "<br><br><i>{english}</i>",
        82: "{german}"
            "<br><br><i>{english}</i>",
        83: "{german}"
            "<br><br><i>{english}</i>",
        84: "{german}"
            "<br><br><i>{english}</i>",
        85: "{german}"
            "<br><br><i>{english}</i>",
        86: "{german}"
            "<br><br><i>{english}</i>",
        87: "{german}"
            "<br><br><i>{english}</i>",
    },

    pronomen: {
        1: "{english}, {case_english} → {correct_answers}",
        2: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{person}, {case_english} → {correct_answers}",
        3: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{person}, {case_english} → {correct_answers}",
        4: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{person}, {case_english} → {correct_answers}",
        5: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{person}, {case_english} → {correct_answers}",
        6: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{person}, {case_english} → {correct_answers}",

        7: "{english}, {case_english} → {correct_answers}",
        8: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{person}, {case_english} → {correct_answers}",
        9: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{person}, {case_english} → {correct_answers}",
        10: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{person}, {case_english} → {correct_answers}",
        11: "{german}, {gender_english}, {case_english} → {correct_answers}",
        12: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender_english}, {case_english} → {correct_answers}",
        13: "{german}, {gender_english}, {case_english} → {correct_answers}",
        14: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender_english}, {case_english} → {correct_answers}",

        15: "{english} = {correct_answers}",
        16: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        17: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender_english}, {case_english} → {correct_answers}",
        18: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender_english}, {case_english} → {correct_answers}",
        19: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender_english}, {case_english} → {correct_answers}",
        20: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender_english}, {case_english} → {correct_answers}",
        21: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender_english}, {case_english} → {correct_answers}",
        22: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender_english}, {case_english} → {correct_answers}",

        23: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender_english}, {case_english} → {correct_answers}",
        24: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender_english}, {case_english} → {correct_answers}",
        25: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
    },

    konnektoren: {
        1: "{english} ({case_english}) → {correct_answers} ",
        2: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",

        3: "{english} ({case_english}) → {correct_answers} ",
        4: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",

        5: "{english} ({case_english}) → {correct_answers} ",
        6: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",
        7: "{english} = {correct_answers}",

        8: "{english} ({case_english}) → {correct_answers} ",
        9: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",
        10: "{english} ({case_english}) → {correct_answers} ",
        11: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",
        12: "{english} = {correct_answers}",

        13: "{english} ({case_english}) → {correct_answers} ",
        14: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",
        15: "{english} = {correct_answers}",
    },

    fragen: {
        1: "{english} = {correct_answers}",
        2: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",

        3: "{english} = {correct_answers}",
        4: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",

        5: "{english} = {correct_answers}",
        6: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",

        7: "{english} = {correct_answers}",
        8: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",
        9: "{english} = {correct_answers}",
        10: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",

        11: "{english} = {correct_answers}",
        12: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
    },

    adverbien: {
        1: "{english} = {correct_answers}",
        2: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",
        3: "{english} = {correct_answers}",
        4: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",

        5: "{english} = {correct_answers}",
        6: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",
        7: "{english} = {correct_answers}",
        8: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",
        9: "{english} = {correct_answers}",
        10: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",

        11: "{english} = {correct_answers}",
        12: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        13: "{english} = {correct_answers}",
        14: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        15: "{english} = {correct_answers}",
        16: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        17: "{english} = {correct_answers}",
        18: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",

        19: "{english} = {correct_answers}",
        20: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        21: "{english} = {correct_answers}",
        22: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        23: "{english} = {correct_answers}",
        24: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        25: "{english} = {correct_answers}",
        26: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        27: "{english} = {correct_answers}",
        28: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",

        29: "{english} = {correct_answers}",
        30: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        31: "{english} = {correct_answers}",
        32: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        33: "{english} = {correct_answers}",
        34: "{previous_question} = {correct_answers}",
        35: "{english} = {correct_answers}",
        36: "{previous_question} = {correct_answers}",
        37: "{english} = {correct_answers}",
        38: "{previous_question} = {correct_answers}",
        39: "{english} = {correct_answers}",
        40: "{previous_question} = {correct_answers}",
        41: "{english} = {correct_answers}",
        42: "{previous_question} = {correct_answers}",
        43: "{english} = {correct_answers}",
        44: "{previous_question} = {correct_answers}",
    },

    adjektive: {
        1: "{english} = {correct_answers}",
        2: "{english} = {correct_answers}",
        3: "{english} ↔ {correct_answers}",
        4: "{previous_question} ↔ {correct_answers}",
        5: "{previous_question} ↔ {correct_answers}",
        6: "Comparative {previous_question} (<i>{english}</i>) → {correct_answers}",
        7: "Comparative {previous_question} (<i>{english}</i>) → {correct_answers}",
        8: "Comparative {previous_question} (<i>{english}</i>) → {correct_answers}",
        9: "Superlative {previous_question} (<i>{english}</i>) → {correct_answers}",
        10: "Superlative {previous_question} (<i>{english}</i>) → {correct_answers}",
        11: "Superlative {previous_question} (<i>{english}</i>) → {correct_answers}",
        12: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",

        13: "{english} = {correct_answers}",
        14: "{english} = {correct_answers}",
        15: "{english} ↔ {correct_answers}",
        16: "{previous_question} ↔ {correct_answers}",
        17: "{previous_question} ↔ {correct_answers}",
        18: "Comparative {previous_question} (<i>{english}</i>) → {correct_answers}",
        19: "Comparative {previous_question} (<i>{english}</i>) → {correct_answers}",
        20: "Comparative {previous_question} (<i>{english}</i>) → {correct_answers}",
        21: "Superlative {previous_question} (<i>{english}</i>) → {correct_answers}",
        22: "Superlative {previous_question} (<i>{english}</i>) → {correct_answers}",
        23: "Superlative {previous_question} (<i>{english}</i>) → {correct_answers}",

        24: "{english} = {correct_answers}",
        25: "{english} = {correct_answers}",
        26: "{english} = {correct_answers}",
        27: "{previous_question} = {correct_answers}",
        28: "{previous_question} = {correct_answers}",
        29: "{previous_question} = {correct_answers}",

        30: "{english} = {correct_answers}",
        31: "{english} = {correct_answers}",
        32: "{english} = {correct_answers}",
        33: "{english} = {correct_answers}",
        34: "{english} = {correct_answers}",
        35: "{english} = {correct_answers}",
    },

    adjektivdeklinationen: {
        1: "{german}"
           "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",
        2: "{german}"
           "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",
        3: "{german}"
           "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",
        4: "{german}"
           "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",
        5: "{german}"
           "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",
        6: "{german}"
           "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",
        7: "{german}"
           "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",
        8: "{german}"
           "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",
        9: "{german}"
           "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",
        10: "{german}"
            "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",
        11: "{german}"
            "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",
        12: "{german}"
            "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",

        13: "{german}"
            "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",
        14: "{german}"
            "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",
        15: "{german}"
            "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",
        16: "{german}"
            "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",
        17: "{german}"
            "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",
        18: "{german}"
            "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",

        19: "{german}"
            "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",
        20: "{german}"
            "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",
        21: "{german}"
            "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",
        22: "{german}"
            "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",

        23: "{german}"
            "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",
        24: "{german}"
            "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",
        25: "{german}"
            "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",
        26: "{german}"
            "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",
        27: "{german}"
            "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",
        28: "{german}"
            "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",
        29: "{german}"
            "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",
        30: "{german}"
            "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",
    },

    verben: {
        1: "{english} = {correct_answers}",
        2: "{english} = {correct_answers}",
        3: "{english} = {correct_answers}",
        4: "{english} = {correct_answers}",
        5: "{english} = {correct_answers}",

        6: "{english} = {correct_answers}",
        7: "{english} = {correct_answers}",
        8: "{english} = {correct_answers}",
        9: "{english} = {correct_answers}",
        10: "{english} = {correct_answers}",

        11: "{english} = {correct_answers}",
        12: "{english} = {correct_answers}",
        13: "{english} = {correct_answers}",
        14: "{english} = {correct_answers}",
        15: "{english} = {correct_answers}",
        16: "{previous_question} = {correct_answers}",
        17: "{previous_question} = {correct_answers}",
        18: "{previous_question} = {correct_answers}",
        19: "{previous_question} = {correct_answers}",
        20: "{previous_question} = {correct_answers}",

        21: "{previous_question} = {correct_answers}",
        22: "{previous_question} = {correct_answers}",
        23: "{previous_question} = {correct_answers}",
        24: "{previous_question} = {correct_answers}",
        25: "{previous_question} = {correct_answers}",
        26: "{previous_question} = {correct_answers}",
        27: "{previous_question} = {correct_answers}",
        28: "{previous_question} = {correct_answers}",
        29: "{previous_question} = {correct_answers}",
        30: "{previous_question} = {correct_answers}",
        31: "{previous_question} = {correct_answers}",

        32: "{previous_question} = {correct_answers}",
        33: "{previous_question} = {correct_answers}",
        34: "{previous_question} = {correct_answers}",
        35: "{previous_question} = {correct_answers}",
        36: "{previous_question} = {correct_answers}",
        37: "{previous_question} = {correct_answers}",
        38: "{previous_question} = {correct_answers}",
        39: "{previous_question} = {correct_answers}",
        40: "{previous_question} = {correct_answers}",
    },

    trennbare_verben: {
        1: "{root_english} → {root_german}"
           "<br><br>{english} → {correct_answers}",
        2: "{root_english} → {root_german}"
           "<br><br>{english} → {correct_answers}",
        3: "{root_english} → {root_german}"
           "<br><br>{english} → {correct_answers}",

        4: "{root_english} → {root_german}"
           "<br><br>{english} → {correct_answers}",
        5: "{root_english} → {root_german}"
           "<br><br>{english} → {correct_answers}",
        6: "{root_english} → {root_german}"
           "<br><br>{english} → {correct_answers}",

        7: "{root_english} → {root_german}"
           "<br><br>{english} → {correct_answers}",
        8: "{root_english} → {root_german}"
           "<br><br>{english} → {correct_answers}",
        9: "{root_english} → {root_german}"
           "<br><br>{english} → {correct_answers}",
        10: "{root_english} → {root_german}"
            "<br><br>{english} → {correct_answers}",
        11: "{root_english} → {root_german}"
            "<br><br>{english} → {correct_answers}",
        12: "{root_english} → {root_german}"
            "<br><br>{english} → {correct_answers}",
        13: "{root_english} → {root_german}"
            "<br><br>{english} → {correct_answers}",
        14: "{root_english} → {root_german}"
            "<br><br>{english} → {correct_answers}",
        15: "{root_english} → {root_german}"
            "<br><br>{english} → {correct_answers}",
        16: "{root_english} → {root_german}"
            "<br><br>{english} → {correct_answers}",
        17: "{root_english} → {root_german}"
            "<br><br>{english} → {correct_answers}",
        18: "{root_english} → {root_german}"
            "<br><br>{english} → {correct_answers}",

        19: "{root_english} → {root_german}"
            "<br><br>{english} → {correct_answers}",
        20: "{root_english} → {root_german}"
            "<br><br>{english} → {correct_answers}",
        21: "{root_english} → {root_german}"
            "<br><br>{english} → {correct_answers}",
        22: "{root_english} → {root_german}"
            "<br><br>{english} → {correct_answers}",
        23: "{root_english} → {root_german}"
            "<br><br>{english} → {correct_answers}",
        24: "{root_english} → {root_german}"
            "<br><br>{english} → {correct_answers}",
        25: "{root_english} → {root_german}"
            "<br><br>{english} → {correct_answers}",
        26: "{root_english} → {root_german}"
            "<br><br>{english} → {correct_answers}",
        27: "{root_english} → {root_german}"
            "<br><br>{english} → {correct_answers}",
        28: "{root_english} → {root_german}"
            "<br><br>{english} → {correct_answers}",
        29: "{root_english} → {root_german}"
            "<br><br>{english} → {correct_answers}",
        30: "{root_english} → {root_german}"
            "<br><br>{english} → {correct_answers}",
    },

    nomen_verben_verbindungen: {
        1: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answers: {correct_answers}",
        2: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answers: {correct_answers}",
        3: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answers: {correct_answers}",
        4: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answers: {correct_answers}",
    },

    praesens: {
        1: "{previous_question} → {person} {correct_answers}"
           "<br><br>{previous_question} = {english}",
        2: "{previous_question} → {person} {correct_answers}"
           "<br><br>{previous_question} = {english}",
        3: "{previous_question} → {person} {correct_answers}"
           "<br><br>{previous_question} = {english}",
        4: "{previous_question} → {person} {correct_answers}"
           "<br><br>{previous_question} = {english}",
        5: "{previous_question} → {person} {correct_answers}"
           "<br><br>{previous_question} = {english}",
        6: "{previous_question} → {person} {correct_answers}"
           "<br><br>{previous_question} = {english}",
        7: "{previous_question} → {person} {correct_answers}"
           "<br><br>{previous_question} = {english}",
        8: "{previous_question} → {person} {correct_answers}"
           "<br><br>{previous_question} = {english}",
        9: "{previous_question} → {person} {correct_answers}"
           "<br><br>{previous_question} = {english}",
        10: "{previous_question} → {person} {correct_answers}"
           "<br><br>{previous_question} = {english}",
        11: "{previous_question} → {person} {correct_answers}"
            "<br><br>{previous_question} = {english}",
        12: "{previous_question} → {person} {correct_answers}"
            "<br><br>{previous_question} = {english}",
        13: "{previous_question} → {person} {correct_answers}"
            "<br><br>{previous_question} = {english}",
        14: "{previous_question} → {person} {correct_answers}"
            "<br><br>{previous_question} = {english}",
        15: "{previous_question} → {person} {correct_answers}"
            "<br><br>{previous_question} = {english}",
        16: "{previous_question} → {person} {correct_answers}"
            "<br><br>{previous_question} = {english}",
        17: "{previous_question} → {person} {correct_answers}"
            "<br><br>{previous_question} = {english}",
        18: "{previous_question} → {person} {correct_answers}"
            "<br><br>{previous_question} = {english}",
        19: "{previous_question} → {person} {correct_answers}"
            "<br><br>{previous_question} = {english}",
        20: "{previous_question} → {person} {correct_answers}"
            "<br><br>{previous_question} = {english}",

        21: "{previous_question} → {person} {correct_answers}"
            "<br><br>{previous_question} = {english}",
        22: "{previous_question} → {person} {correct_answers}"
            "<br><br>{previous_question} = {english}",
        23: "{previous_question} → {person} {correct_answers}"
            "<br><br>{previous_question} = {english}",
        24: "{previous_question} → {person} {correct_answers}"
            "<br><br>{previous_question} = {english}",
        25: "{previous_question} → {person} {correct_answers}"
           "<br><br>{previous_question} = {english}",
        26: "{previous_question} → {person} {correct_answers}"
           "<br><br>{previous_question} = {english}",
        27: "{previous_question} → {person} {correct_answers}"
           "<br><br>{previous_question} = {english}",
        28: "{previous_question} → {person} {correct_answers}"
           "<br><br>{previous_question} = {english}",
        29: "{previous_question} → {person} {correct_answers}"
           "<br><br>{previous_question} = {english}",
        30: "{previous_question} → {person} {correct_answers}"
           "<br><br>{previous_question} = {english}",
        31: "{previous_question} → {person} {correct_answers}"
           "<br><br>{previous_question} = {english}",
        32: "{previous_question} → {person} {correct_answers}"
           "<br><br>{previous_question} = {english}",
        33: "{previous_question} → {person} {correct_answers}"
           "<br><br>{previous_question} = {english}",
        34: "{previous_question} → {person} {correct_answers}"
            "<br><br>{previous_question} = {english}",
        35: "{previous_question} → {person} {correct_answers}"
            "<br><br>{previous_question} = {english}",
        36: "{previous_question} → {person} {correct_answers}"
            "<br><br>{previous_question} = {english}",
        37: "{previous_question} → {person} {correct_answers}"
            "<br><br>{previous_question} = {english}",
        38: "{previous_question} → {person} {correct_answers}"
            "<br><br>{previous_question} = {english}",
        39: "{previous_question} → {person} {correct_answers}"
            "<br><br>{previous_question} = {english}",
        40: "{previous_question} → {person} {correct_answers}"
            "<br><br>{previous_question} = {english}",
    },

    partizip_II: {
        1: "Partizip II {previous_question}: {correct_answers}"
           "<br><br>{previous_question} = {english}",
        2: "Partizip II {previous_question}: {correct_answers}"
           "<br><br>{previous_question} = {english}",
        3: "Partizip II {previous_question}: {correct_answers}"
           "<br><br>{previous_question} = {english}",
        4: "Partizip II {previous_question}: {correct_answers}"
           "<br><br>{previous_question} = {english}",
        5: "Partizip II {previous_question}: {correct_answers}"
           "<br><br>{previous_question} = {english}",

        6: "Partizip II {previous_question}: {correct_answers}"
           "<br><br>{previous_question} = {english}",
        7: "Partizip II {previous_question}: {correct_answers}"
           "<br><br>{previous_question} = {english}",
        8: "Partizip II {previous_question}: {correct_answers}"
           "<br><br>{previous_question} = {english}",
        9: "Partizip II {previous_question}: {correct_answers}"
           "<br><br>{previous_question} = {english}",
        10: "Partizip II {previous_question}: {correct_answers}"
            "<br><br>{previous_question} = {english}",

        11: "Partizip II {previous_question}: {correct_answers}"
            "<br><br>{previous_question} = {english}",
        12: "Partizip II {previous_question}: {correct_answers}"
            "<br><br>{previous_question} = {english}",
        13: "Partizip II {previous_question}: {correct_answers}"
            "<br><br>{previous_question} = {english}",
        14: "Partizip II {previous_question}: {correct_answers}"
            "<br><br>{previous_question} = {english}",
        15: "Partizip II {previous_question}: {correct_answers}"
            "<br><br>{previous_question} = {english}",
        16: "Partizip II {previous_question}: {correct_answers}"
            "<br><br>{previous_question} = {english}",
        17: "Partizip II {previous_question}: {correct_answers}"
            "<br><br>{previous_question} = {english}",
        18: "Partizip II {previous_question}: {correct_answers}"
            "<br><br>{previous_question} = {english}",
        19: "Partizip II {previous_question}: {correct_answers}"
            "<br><br>{previous_question} = {english}",
        20: "Partizip II {previous_question}: {correct_answers}"
            "<br><br>{previous_question} = {english}",

        21: "Partizip II {previous_question}: {correct_answers}"
            "<br><br>{previous_question} = {english}",
        22: "Partizip II {previous_question}: {correct_answers}"
            "<br><br>{previous_question} = {english}",
        23: "Partizip II {previous_question}: {correct_answers}"
            "<br><br>{previous_question} = {english}",
        24: "Partizip II {previous_question}: {correct_answers}"
            "<br><br>{previous_question} = {english}",
        25: "Partizip II {previous_question}: {correct_answers}"
            "<br><br>{previous_question} = {english}",
        26: "Partizip II {previous_question}: {correct_answers}"
            "<br><br>{previous_question} = {english}",
        27: "Partizip II {previous_question}: {correct_answers}"
            "<br><br>{previous_question} = {english}",
        28: "Partizip II {previous_question}: {correct_answers}"
            "<br><br>{previous_question} = {english}",
        29: "Partizip II {previous_question}: {correct_answers}"
            "<br><br>{previous_question} = {english}",
        30: "Partizip II {previous_question}: {correct_answers}"
            "<br><br>{previous_question} = {english}",

        31: "Partizip II {previous_question}: {correct_answers}"
            "<br><br>{previous_question} = {english}",
        32: "Partizip II {previous_question}: {correct_answers}"
            "<br><br>{previous_question} = {english}",
        33: "Partizip II {previous_question}: {correct_answers}"
            "<br><br>{previous_question} = {english}",
        34: "Partizip II {previous_question}: {correct_answers}"
            "<br><br>{previous_question} = {english}",
        35: "Partizip II {previous_question}: {correct_answers}"
            "<br><br>{previous_question} = {english}",
        36: "Partizip II {previous_question}: {correct_answers}"
            "<br><br>{previous_question} = {english}",
        37: "Partizip II {previous_question}: {correct_answers}"
            "<br><br>{previous_question} = {english}",
        38: "Partizip II {previous_question}: {correct_answers}"
            "<br><br>{previous_question} = {english}",
        39: "Partizip II {previous_question}: {correct_answers}"
            "<br><br>{previous_question} = {english}",
        40: "Partizip II {previous_question}: {correct_answers}"
            "<br><br>{previous_question} = {english}",
    },

    praeteritum: {
        1: "{previous_question} → {person} {correct_answers}"
           "<br><br>{previous_question} = {english}",

        2: "{previous_question} → er/sie/es {correct_answers}"
           "<br><br>{previous_question} = {english}",
        3: "{previous_question} → er/sie/es {correct_answers}"
           "<br><br>{previous_question} = {english}",
        4: "{previous_question} → er/sie/es {correct_answers}"
           "<br><br>{previous_question} = {english}",
        5: "{previous_question} → er/sie/es {correct_answers}"
           "<br><br>{previous_question} = {english}",
        6: "{previous_question} → er/sie/es {correct_answers}"
           "<br><br>{previous_question} = {english}",
        7: "{previous_question} → er/sie/es {correct_answers}"
           "<br><br>{previous_question} = {english}",
        8: "{previous_question} → er/sie/es {correct_answers}"
           "<br><br>{previous_question} = {english}",
        9: "{previous_question} → er/sie/es {correct_answers}"
           "<br><br>{previous_question} = {english}",
        10: "{previous_question} → er/sie/es {correct_answers}"
           "<br><br>{previous_question} = {english}",
        11: "{previous_question} → er/sie/es {correct_answers}"
           "<br><br>{previous_question} = {english}",

        12: "{previous_question} → er/sie/es {correct_answers}"
           "<br><br>{previous_question} = {english}",
        13: "{previous_question} → er/sie/es {correct_answers}"
           "<br><br>{previous_question} = {english}",
        14: "{previous_question} → er/sie/es {correct_answers}"
           "<br><br>{previous_question} = {english}",
        15: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{previous_question} = {english}",
        16: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{previous_question} = {english}",
        17: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{previous_question} = {english}",
        18: "{previous_question} → er/sie/es {correct_answers}",
        19: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{previous_question} = {english}",
        20: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{previous_question} = {english}",
        21: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{previous_question} = {english}",

        22: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{previous_question} = {english}",
        23: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{previous_question} = {english}",
        24: "{previous_question} → er/sie/es {correct_answers}"
           "<br><br>{previous_question} = {english}",
        25: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{previous_question} = {english}",
        26: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{previous_question} = {english}",
        27: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{previous_question} = {english}",
        28: "{previous_question} → er/sie/es {correct_answers}",
        29: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{previous_question} = {english}",
        30: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{previous_question} = {english}",
        31: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{previous_question} = {english}",
        32: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{previous_question} = {english}",
        33: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{previous_question} = {english}",
        34: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{previous_question} = {english}",
        35: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{previous_question} = {english}",
        36: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{previous_question} = {english}",
        37: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{previous_question} = {english}",
        38: "{previous_question} → er/sie/es {correct_answers}",
        39: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{previous_question} = {english}",
        40: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{previous_question} = {english}",
        41: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{previous_question} = {english}",
    },

    praeteritum_partizip_II: {
        1: "{previous_question}, {correct_answers}"
           "<br><br>{previous_question} = {english}",

        2: "{previous_question}, {correct_answers}"
           "<br><br>{previous_question} = {english}",
        3: "{previous_question}, {correct_answers}"
           "<br><br>{previous_question} = {english}",
        4: "{previous_question}, {correct_answers}"
           "<br><br>{previous_question} = {english}",
        5: "{previous_question}, {correct_answers}"
           "<br><br>{previous_question} = {english}",
        6: "{previous_question}, {correct_answers}"
           "<br><br>{previous_question} = {english}",
        7: "{previous_question}, {correct_answers}"
           "<br><br>{previous_question} = {english}",
        8: "{previous_question}, {correct_answers}"
           "<br><br>{previous_question} = {english}",
        9: "{previous_question}, {correct_answers}"
           "<br><br>{previous_question} = {english}",
        10: "{previous_question}, {correct_answers}"
           "<br><br>{previous_question} = {english}",
        11: "{previous_question}, {correct_answers}"
           "<br><br>{previous_question} = {english}",

        12: "{previous_question}, {correct_answers}"
           "<br><br>{previous_question} = {english}",
        13: "{previous_question}, {correct_answers}"
           "<br><br>{previous_question} = {english}",
        14: "{previous_question}, {correct_answers}"
           "<br><br>{previous_question} = {english}",
        15: "{previous_question}, {correct_answers}"
           "<br><br>{previous_question} = {english}",
        16: "{previous_question}, {correct_answers}"
           "<br><br>{previous_question} = {english}",
        17: "{previous_question}, {correct_answers}"
           "<br><br>{previous_question} = {english}",
        18: "{previous_question}, {correct_answers}"
           "<br><br>{previous_question} = {english}",
        19: "{previous_question}, {correct_answers}"
           "<br><br>{previous_question} = {english}",
        20: "{previous_question}, {correct_answers}"
           "<br><br>{previous_question} = {english}",
        21: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {english}",

        22: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {english}",
        23: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {english}",
        24: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {english}",
        25: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {english}",
        26: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {english}",
        27: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {english}",
        28: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {english}",
        29: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {english}",
        30: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {english}",
        31: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {english}",
        32: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {english}",
        33: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {english}",
        34: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {english}",
        35: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {english}",
        36: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {english}",
        37: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {english}",
        38: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {english}",
        39: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {english}",
        40: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {english}",
        41: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {english}",
    },

    imperativ: {
        1: "{previous_question}, {person} → {correct_answers}"
           "<br><br>{previous_question} = {english}",
        2: "{previous_question}, {person} → {correct_answers}"
           "<br><br>{previous_question} = {english}",
        3: "{previous_question}, {person} → {correct_answers}"
           "<br><br>{previous_question} = {english}",
        4: "{previous_question}, {person} → {correct_answers}"
           "<br><br>{previous_question} = {english}",
        5: "{previous_question}, {person} → {correct_answers}"
           "<br><br>{previous_question} = {english}",
        6: "{previous_question}, {person} → {correct_answers}"
           "<br><br>{previous_question} = {english}",

        7: "{previous_question}, {person} → {correct_answers}"
           "<br><br>{previous_question} = {english}",
        8: "{previous_question}, {person} → {correct_answers}"
           "<br><br>{previous_question} = {english}",
        9: "{previous_question}, {person} → {correct_answers}"
           "<br><br>{previous_question} = {english}",
        10: "{previous_question}, {person} → {correct_answers}"
           "<br><br>{previous_question} = {english}",
        11: "{previous_question}, {person} → {correct_answers}"
           "<br><br>{previous_question} = {english}",
        12: "{previous_question}, {person} → {correct_answers}"
           "<br><br>{previous_question} = {english}",
    },

    konjunktiv_II: {
        1: "{previous_question} → {person} {correct_answers}"
           "<br><br>{previous_question} = {english}",
    },

    konjunktiv_I: {
        1: "{previous_question} → {person} {correct_answers}"
           "<br><br>{previous_question} = {english}",
        2: "{previous_question} → {person} {correct_answers}"
           "<br><br>{previous_question} = {english}",
        3: "{previous_question} → {person} {correct_answers}"
           "<br><br>{previous_question} = {english}",
        4: "{previous_question} → {person} {correct_answers}"
           "<br><br>{previous_question} = {english}",
        5: "{previous_question} → {person} {correct_answers}"
           "<br><br>{previous_question} = {english}",
        6: "{previous_question} → {person} {correct_answers}"
           "<br><br>{previous_question} = {english}",
    },

    partizip_I: {
        1: "Partizip I {previous_question}: {correct_answers}",
        2: "Partizip I {previous_question}: {correct_answers}",
        3: "Partizip I {previous_question}: {correct_answers}",
        4: "Partizip I {previous_question}: {correct_answers}",
        5: "Partizip I {previous_question}: {correct_answers}",
    },

}
