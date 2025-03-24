from data_processing.exercises import (artikel, pronomen, konnektoren, praepositionen_grammatik, adjektivdeklinationen,
                                       praesens, praepositionen_konjugation, imperativ, perfekt, praeteritum, konjunktiv,
                                       partizip_I,
                                       adverbien, verben, trennbare_verben, adjektive, deverbale_substantive,)


FEEDBACK_TEMPLATES = {
    artikel: {
        1: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        2: "{previous_question} = {correct_answers}",
        3: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        4: "{previous_question} = {correct_answers}",
        5: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
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
        7: "{previous_question} = {correct_answers}",
        8: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",
        9: "{german}"
           "<br><br>{person}, {case} → {correct_answers}",
        10: "{german}"
           "<br><br>{person}, {case} → {correct_answers}",
        11: "{german}"
           "<br><br>{person}, {case} → {correct_answers}",
        12: "{german}"
           "<br><br>{person}, {case} → {correct_answers}",
        13: "{german}"
           "<br><br>{person}, {case} → {correct_answers}",
        14: "{german}"
           "<br><br>{person}, {case} → {correct_answers}",
    },

    konnektoren: {
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

    praepositionen_grammatik: {
        1: "{previous_question} = {correct_answers}",
        2: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",
        3: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",
        4: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",
        5: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",
        6: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",
        7: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",
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
        13: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",
        14: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",
        15: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",
        16: "{previous_question} = {correct_answers}",
        17: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",
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

    praepositionen_konjugation: {
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
        13: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",
        14: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",
        15: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",
        16: "{previous_question} = {german} {correct_answers}",
        17: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",
        18: "{previous_question} = {german} {correct_answers}",
        19: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",
        20: "{previous_question} = {german} {correct_answers}",
        21: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",
        22: "{previous_question} = {german} {correct_answers}",
        23: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",
        24: "{previous_question} = {german} {correct_answers}",
        25: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",
        26: "{previous_question} = {german} {correct_answers}",
        27: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",
        28: "{previous_question} = {german} {correct_answers}",
        29: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",
        30: "{previous_question} = {german} {correct_answers}",
        31: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",
        32: "{previous_question} = {german} {correct_answers}",
        33: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",
        34: "{previous_question} = {german} {correct_answers}",
        35: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",
    },

    perfekt: {
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

    konjunktiv: {
        1: "{previous_question} → {person} {correct_answers}"
           "<br><br>{previous_question} = {english}",
    },

    partizip_I: {
        1: "Partizip I of {previous_question} = {correct_answers}"
           "<br><br>English: {english}",
        2: "Partizip I of {previous_question} = {correct_answers}"
           "<br><br>English: {english}",
        3: "Partizip I of {previous_question} = {correct_answers}"
           "<br><br>English: {english}",
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

    trennbare_verben: {
        1: "{english} = {german}"
           "<br><br>{previous_question} = {correct_answers}",
        2: "{english} = {german}"
           "<br><br>{previous_question} = {correct_answers}",
        3: "{english} = {german}"
           "<br><br>{previous_question} = {correct_answers}",
        4: "{english} = {german}"
           "<br><br>{previous_question} = {correct_answers}",
        5: "{english} = {german}"
           "<br><br>{previous_question} = {correct_answers}",
        6: "{english} = {german}"
           "<br><br>{previous_question} = {correct_answers}",
        7: "{english} = {german}"
           "<br><br>{previous_question} = {correct_answers}",
        8: "{english} = {german}"
           "<br><br>{previous_question} = {correct_answers}",
        9: "{english} = {german}"
           "<br><br>{previous_question} = {correct_answers}",
        10: "{english} = {german}"
            "<br><br>{previous_question} = {correct_answers}",
    },

    deverbale_substantive: {
        1: "{english}: {german}"
           "<br><br>{previous_question}: {correct_answers}",
        2: "{english}: {german}"
           "<br><br>{previous_question}: {correct_answers}",
        3: "{english}: {german}"
           "<br><br>{previous_question}: {correct_answers}",
        4: "{english}: {german}"
           "<br><br>{previous_question}: {correct_answers}",
        5: "{english}: {german}"
           "<br><br>{previous_question}: {correct_answers}",
        6: "{english}: {german}"
           "<br><br>{previous_question}: {correct_answers}",
        7: "{english}: {german}"
           "<br><br>{previous_question}: {correct_answers}",
        8: "{english}: {german}"
           "<br><br>{previous_question}: {correct_answers}",
        9: "{english}: {german}"
           "<br><br>{previous_question}: {correct_answers}",
        10: "{english}: {german}"
           "<br><br>{previous_question}: {correct_answers}",
        11: "{english}: {german}"
           "<br><br>{previous_question}: {correct_answers}",
        12: "{english}: {german}"
           "<br><br>{previous_question}: {correct_answers}",
    },
}
