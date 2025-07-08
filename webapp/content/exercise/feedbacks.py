from data.data_processing.units import (
    praepositionen_grammatik, praepositionen_verben, praepositionen_adjektive, praepositionen_nomen,
    artikel, pronomen, konnektoren, fragen, adverbien,
    praesens, imperativ, partizip_II, praeteritum, praeteritum_partizip_II, konjunktiv_II, konjunktiv_I, partizip_I,
    adjektive, adjektivdeklinationen,
    trennbare_verben, verben,
    deverbale_nomen
)

FEEDBACK = {

    praepositionen_grammatik: {
        1: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{explanation}"
           "<br><br>Correct answer(s): {correct_answers}",
        2: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{explanation}"
           "<br><br>Correct answer(s): {correct_answers}",
        3: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{explanation}"
           "<br><br>Correct answer(s): {correct_answers}",
        4: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{explanation}"
           "<br><br>Correct answer(s): {correct_answers}",

        5: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{explanation}"
           "<br><br>Correct answer(s): {correct_answers}",
        6: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{explanation}"
           "<br><br>Correct answer(s): {correct_answers}",
        7: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{explanation}"
           "<br><br>Correct answer(s): {correct_answers}",

        8: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{explanation}"
           "<br><br>Correct answer(s): {correct_answers}",
        9: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation}"
           "<br><br>Correct answer(s): {correct_answers}",
        10: "{previous_question} = {correct_answers}",
        11: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation}"
            "<br><br>Correct answer(s): {correct_answers}",

        12: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{explanation}"
            "<br><br>Correct answer(s): {correct_answers}",
        13: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation}"
            "<br><br>Correct answer(s): {correct_answers}",
        14: "{previous_question} = {correct_answers}",
        15: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation}"
            "<br><br>Correct answer(s): {correct_answers}",

        16: "{previous_question} = {correct_answers}",
        17: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation}"
            "<br><br>Correct answer(s): {correct_answers}",
        18: "{previous_question} = {correct_answers}",
        19: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation}"
            "<br><br>Correct answer(s): {correct_answers}",
    },

    praepositionen_verben: {
        1: "{english} = {german} + {case}",
        2: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",
        3: "{english} = {german} + {case}",
        4: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",

        5: "{english} = {german} + {case}",
        6: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",
        7: "{english} = {german} + {case}",
        8: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",
        9: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",
        10: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",

        11: "{english} = {german} + {case}",
        12: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        13: "{english} = {german} + {case}",
        14: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",

        15: "{english} = {german} + {case}",
        16: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        17: "{english} = {german} + {case}",
        18: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",

        19: "{english} = {german} + {case}",
        20: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        21: "{english} = {german} + {case}",
        22: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
    },

    praepositionen_adjektive: {
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
    },

    artikel: {
        1: "{previous_question}, {gender}, {case} → {correct_answers}",
        2: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender}, {case} → {correct_answers}",
        3: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender}, {case} → {correct_answers}",
        4: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender}, {case} → {correct_answers}",
        5: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{gender}, {case} → {correct_answers}",
        6: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{gender}, {case} → {correct_answers}",
        7: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{gender}, {case} → {correct_answers}",
        8: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{gender}, {case} → {correct_answers}",
        9: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender}, {case} → {correct_answers}",
        10: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender}, {case} → {correct_answers}",
        11: "{previous_question}, {gender}, {case} → {correct_answers}",
        12: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender}, {case} → {correct_answers}",
        13: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender}, {case} → {correct_answers}",
        14: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender}, {case} → {correct_answers}",
        15: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender}, {case} → {correct_answers}",
        16: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender}, {case} → {correct_answers}",
        17: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender}, {case} → {correct_answers}",
        18: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender}, {case} → {correct_answers}",
        19: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender}, {case} → {correct_answers}",
        20: "{previous_question}, {gender}, {case} → {correct_answers}",
        21: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender}, {case} → {correct_answers}",
        22: "{previous_question}, {gender}, {case} → {correct_answers}",
        23: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender}, {case} → {correct_answers}",
        24: "{previous_question}, {gender}, {case} → {correct_answers}",
        25: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender}, {case} → {correct_answers}",

        26: "{previous_question}, {gender}, {case} → {correct_answers}",
        27: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender}, {case} → {correct_answers}",
        28: "{previous_question}, {gender}, {case} → {correct_answers}",
        29: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender}, {case} → {correct_answers}",
        30: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        31: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        32: "{previous_question} = {correct_answers}",
        33: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",

        34: "{previous_question}, {gender}, {case} → {correct_answers}",
        35: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender}, {case} → {correct_answers}",
        36: "{gender}, {case} → {correct_answers}",
        37: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender}, {case} → {correct_answers}",
        38: "{previous_question}, {gender}, {case} → {correct_answers}",
        39: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender}, {case} → {correct_answers}",

        40: "{previous_question}, {gender}, {case} → {correct_answers}",
        41: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender}, {case} → {correct_answers}",

        42: "{previous_question}, {gender}, {case} → {correct_answers}",
        43: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender}, {case} → {correct_answers}",
    },

    pronomen: {
        1: "{german}"
           "<br><br>{person}, {case} → {correct_answers}",
        2: "{german}"
           "<br><br>{person}, {case} → {correct_answers}",
        3: "{german}"
           "<br><br>{person}, {case} → {correct_answers}",
        4: "{german}"
           "<br><br>{person}, {case} → {correct_answers}",

        5: "{german}"
           "<br><br>{person}, {case} → {correct_answers}",
        6: "{german}"
           "<br><br>{person}, {case} → {correct_answers}",
        7: "{german}"
           "<br><br>{person}, {case} → {correct_answers}",
        8: "{previous_question}, {gender}, {case} → {correct_answers}",
        9: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender}, {case} → {correct_answers}",
        10: "{previous_question}, {gender}, {case} → {correct_answers}",
        11: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender}, {case} → {correct_answers}",

        12: "{previous_question} = {correct_answers}",
        13: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",
        14: "{german}"
           "<br><br>{gender}, {case} → {correct_answers}",
        15: "{german}"
           "<br><br>{gender}, {case} → {correct_answers}",
        16: "{german}"
           "<br><br>{gender}, {case} → {correct_answers}",
        17: "{german}"
           "<br><br>{gender}, {case} → {correct_answers}",
        18: "{german}"
           "<br><br>{gender}, {case} → {correct_answers}",

        19: "{german}"
           "<br><br>{gender}, {case} → {correct_answers}",
        20: "{german}"
            "<br><br>Correct answer(s): {correct_answers}",
    },

    konnektoren: {
        1: "{previous_question} ({case}) → {correct_answers} ",
        2: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",

        3: "{previous_question} ({case}) → {correct_answers} ",
        4: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",

        5: "{previous_question} ({case}) → {correct_answers} ",
        6: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",
        7: "{english} = {correct_answers}",

        8: "{previous_question} ({case}) → {correct_answers} ",
        9: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",
        10: "{previous_question} ({case}) → {correct_answers} ",
        11: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",
        12: "{english} = {correct_answers}",

        13: "{previous_question} ({case}) → {correct_answers} ",
        14: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",
        15: "{english} = {correct_answers}",
    },

    fragen: {
        1: "{previous_question} = {correct_answers}",
        2: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",

        3: "{previous_question} = {correct_answers}",
        4: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",

        5: "{previous_question} = {correct_answers}",
        6: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",

        7: "{previous_question} = {correct_answers}",
        8: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",
    },

    adverbien: {
        1: "{previous_question} = {correct_answers}",
        2: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",
        3: "{previous_question} = {correct_answers}",
        4: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",

        5: "{previous_question} = {correct_answers}",
        6: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",
        7: "{previous_question} = {correct_answers}",
        8: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",

        9: "{previous_question} = {correct_answers}",
        10: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        11: "{previous_question} = {correct_answers}",
        12: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        13: "{previous_question} = {correct_answers}",
        14: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        15: "{previous_question} = {correct_answers}",
        16: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",

        17: "{previous_question} = {correct_answers}",
        18: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        19: "{previous_question} = {correct_answers}",
        20: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        21: "{previous_question} = {correct_answers}",
        22: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        23: "{previous_question} = {correct_answers}",
        24: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",

        25: "{previous_question} = {correct_answers}",
        26: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        27: "{previous_question} = {correct_answers}",
        28: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        29: "{previous_question} = {correct_answers}",
        30: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        31: "{previous_question} = {correct_answers}",
        32: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
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
        1: "Partizip I of {previous_question} = {correct_answers}",
        2: "Partizip I of {previous_question} = {correct_answers}",
        3: "Partizip I of {previous_question} = {correct_answers}",
    },

    adjektive: {
        1: "{previous_question} = {correct_answers}",
        2: "{previous_question} = {correct_answers}",
        3: "{previous_question} ↔ {correct_answers}",
        4: "Comparative {previous_question} (<i>{english}</i>) → {correct_answers}",
        5: "Comparative {previous_question} (<i>{english}</i>) → {correct_answers}",
        6: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",
        7: "Superlative {previous_question} (<i>{english}</i>) → {correct_answers}",
        8: "Superlative {previous_question} (<i>{english}</i>) → {correct_answers}",

    },

    adjektivdeklinationen: {
        1: "{german}"
           "<br><br>{article}, {gender}, {case} → {correct_answers}",
        2: "{german}"
           "<br><br>{article}, {gender}, {case} → {correct_answers}",
        3: "{german}"
           "<br><br>{article}, {gender}, {case} → {correct_answers}",
        4: "{german}"
           "<br><br>{article}, {gender}, {case} → {correct_answers}",
        5: "{german}"
           "<br><br>{article}, {gender}, {case} → {correct_answers}",
        6: "{german}"
           "<br><br>{article}, {gender}, {case} → {correct_answers}",
        7: "{german}"
           "<br><br>{article}, {gender}, {case} → {correct_answers}",
        8: "{german}"
           "<br><br>{article}, {gender}, {case} → {correct_answers}",
        9: "{german}"
           "<br><br>{article}, {gender}, {case} → {correct_answers}",
        10: "{german}"
            "<br><br>{article}, {gender}, {case} → {correct_answers}",
        11: "{german}"
           "<br><br>{article}, {gender}, {case} → {correct_answers}",
        12: "{german}"
            "<br><br>{article}, {gender}, {case} → {correct_answers}",

        13: "{german}"
            "<br><br>{article}, {gender}, {case} → {correct_answers}",
        14: "{german}"
            "<br><br>{article}, {gender}, {case} → {correct_answers}",
        15: "{german}"
            "<br><br>{article}, {gender}, {case} → {correct_answers}",
        16: "{german}"
            "<br><br>{article}, {gender}, {case} → {correct_answers}",

        17: "{german}"
            "<br><br>{article}, {gender}, {case} → {correct_answers}",
        18: "{german}"
            "<br><br>{article}, {gender}, {case} → {correct_answers}",
        19: "{german}"
            "<br><br>{article}, {gender}, {case} → {correct_answers}",
        20: "{german}"
            "<br><br>{article}, {gender}, {case} → {correct_answers}",

        21: "{german}"
            "<br><br>{article}, {gender}, {case} → {correct_answers}",
        22: "{german}"
            "<br><br>{article}, {gender}, {case} → {correct_answers}",
    },

    trennbare_verben: {
        1: "{english} &#8594; {german}"
           "<br><br>{previous_question} &#8594; {correct_answers}",
        2: "{english} &#8594; {german}"
           "<br><br>{previous_question} &#8594; {correct_answers}",

        3: "{english} &#8594; {german}"
           "<br><br>{previous_question} &#8594; {correct_answers}",
        4: "{english} &#8594; {german}"
           "<br><br>{previous_question} &#8594; {correct_answers}",

        5: "{english} &#8594; {german}"
           "<br><br>{previous_question} &#8594; {correct_answers}",
        6: "{english} &#8594; {german}"
           "<br><br>{previous_question} &#8594; {correct_answers}",
        7: "{english} &#8594; {german}"
           "<br><br>{previous_question} &#8594; {correct_answers}",
        8: "{english} &#8594; {german}"
           "<br><br>{previous_question} &#8594; {correct_answers}",

        9: "{english} &#8594; {german}"
           "<br><br>{previous_question} &#8594; {correct_answers}",
        10: "{english} &#8594; {german}"
            "<br><br>{previous_question} &#8594; {correct_answers}",
        11: "{english} &#8594; {german}"
            "<br><br>{previous_question} &#8594; {correct_answers}",
        12: "{english} &#8594; {german}"
            "<br><br>{previous_question} &#8594; {correct_answers}",
        13: "{english} &#8594; {german}"
            "<br><br>{previous_question} &#8594; {correct_answers}",
        14: "{english} &#8594; {german}"
            "<br><br>{previous_question} &#8594; {correct_answers}",
    },

    verben:{
        1: "{previous_question} = {correct_answers}",
        2: "{previous_question} = {correct_answers}",
        3: "{previous_question} = {correct_answers}",

        4: "{previous_question} = {correct_answers}",
        5: "{previous_question} = {correct_answers}",
        6: "{previous_question} = {correct_answers}",

        7: "{previous_question} = {correct_answers}",
        8: "{previous_question} = {correct_answers}",
        9: "{previous_question} = {correct_answers}",
        10: "{previous_question} = {correct_answers}",
        11: "{previous_question} = {correct_answers}",
        12: "{previous_question} = {correct_answers}",

        13: "{previous_question} = {correct_answers}",
        14: "{previous_question} = {correct_answers}",
        15: "{previous_question} = {correct_answers}",
        16: "{previous_question} = {correct_answers}",
        17: "{previous_question} = {correct_answers}",
        18: "{previous_question} = {correct_answers}",
        19: "{previous_question} = {correct_answers}",
        20: "{previous_question} = {correct_answers}",
    },

    deverbale_nomen: {
        1: "{english} &#8594 {german}"
           "<br><br>{previous_question} &#8594 {correct_answers}",
        2: "{english} &#8594 {german}"
           "<br><br>{previous_question} &#8594 {correct_answers}",
        3: "{english} &#8594 {german}"
           "<br><br>{previous_question} &#8594 {correct_answers}",
        4: "{english} &#8594 {german}"
           "<br><br>{previous_question} &#8594 {correct_answers}",
        5: "{english} &#8594 {german}"
           "<br><br>{previous_question} &#8594 {correct_answers}",
        6: "{english} &#8594 {german}"
           "<br><br>{previous_question} &#8594 {correct_answers}",
        7: "{english} &#8594 {german}"
           "<br><br>{previous_question} &#8594 {correct_answers}",
        8: "{english} &#8594 {german}"
           "<br><br>{previous_question} &#8594 {correct_answers}",
        9: "{english} &#8594 {german}"
           "<br><br>{previous_question} &#8594 {correct_answers}",
        10: "{english} &#8594 {german}"
           "<br><br>{previous_question} &#8594 {correct_answers}",
        11: "{english} &#8594 {german}"
           "<br><br>{previous_question} &#8594 {correct_answers}",
        12: "{english} &#8594 {german}"
           "<br><br>{previous_question} &#8594 {correct_answers}",
        13: "{english} &#8594 {german}"
            "<br><br>{previous_question} &#8594 {correct_answers}",
        14: "{english} &#8594 {german}"
            "<br><br>{previous_question} &#8594 {correct_answers}",
        15: "{english} &#8594 {german}"
            "<br><br>{previous_question} &#8594 {correct_answers}",
        16: "{english} &#8594 {german}"
            "<br><br>{previous_question} &#8594 {correct_answers}",
    },
}
