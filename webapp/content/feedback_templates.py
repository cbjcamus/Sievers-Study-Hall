from data.exercises import (artikel, pronomen, konnektoren, praepositionen_grammatik, adjektivdeklinationen,
                            praesens, praepositionen_konjugation, imperativ, perfekt, praeteritum, konjunktiv,
                            verben, adjektive, adverbien)

FEEDBACK_TEMPLATES = {
    artikel: {
        1: "{german}",
        2: "{german}",
        3: "{german}",
        4: "{german}",
        5: "{german}",
        6: "{german}",
        7: "{german}",
        8: "{german}",
        9: "{german}"
           "<br><br>{english}",
        10: "{previous_question} = {correct_answers}",
        11: "{german}"
           "<br><br>{english}",
        12: "{previous_question} = {correct_answers}",
        13: "{german}"
            "<br><br>{english}",
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
            "<br><br>{english}",
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
            "<br><br>{english}",
        3: "{previous_question} = {correct_answers}",
        4: "{german}"
            "<br><br>{english}",
        5: "{previous_question} = {correct_answers}",
        6: "{german}"
            "<br><br>{english}",
        7: "{previous_question} = {correct_answers}",
        8: "{german}"
            "<br><br>{english}",
    },

    praepositionen_grammatik: {
        1: "{previous_question} = {correct_answers}",
        2: "{german}"
           "<br><br>{english}",
        3: "{german}"
           "<br><br>{english}",
        4: "{german}"
           "<br><br>{english}",
        5: "{german}"
           "<br><br>{english}",
        6: "{german}"
           "<br><br>{english}",
        7: "{german}"
           "<br><br>{english}",
        8: "{german}"
           "<br><br>{english}",
        9: "{previous_question} = {correct_answers}",
        10: "{german}"
           "<br><br>{english}",
        11: "{previous_question} = {correct_answers}",
        12: "{german}"
            "<br><br>{english}",
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
    },

    praepositionen_konjugation: {
        1: "{english} = {previous_question} {correct_answers}",
        2: "{german}"
           "<br><br>{english}",
        3: "{english} = {previous_question} {correct_answers}",
        4: "{german}"
           "<br><br>{english}",
        5: "{english} = {previous_question} {correct_answers}",
        6: "{german}"
           "<br><br>{english}",
        7: "{german}"
           "<br><br>{english}",
        8: "{german}"
           "<br><br>{english}",
        9: "{english} = {previous_question} {correct_answers}",
        10: "{german}"
            "<br><br>{english}",
        11: "{english} = {previous_question} {correct_answers}",
        12: "{german}"
            "<br><br>{english}",
        13: "{english} = {previous_question} {correct_answers}",
        14: "{german}"
            "<br><br>{english}",
    },

    perfekt: {
        1: "Partizip II {previous_question}: {correct_answers}"
           "<br><br>{previous_question} = {english}",
        2: "{german}"
           "<br><br>{english}",
        3: "{german}"
           "<br><br>{english}",
        4: "Partizip II {previous_question}: {correct_answers}"
           "<br><br>{previous_question} = {english}",
        5: "{german}"
           "<br><br>{english}",
        6: "{german}"
           "<br><br>{english}",
        7: "Partizip II {previous_question}: {correct_answers}"
           "<br><br>{previous_question} = {english}",
        8: "Partizip II {previous_question}: {correct_answers}"
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
    },

    konjunktiv: {
        1: "{previous_question} → {person} {correct_answers}"
           "<br><br>{previous_question} = {english}",
    },

    adverbien: {
        1: "{previous_question} = {correct_answers}",
        2: "{german}"
           "<br><br>{english}",
        3: "{previous_question} = {correct_answers}",
        4: "{german}"
           "<br><br>{english}",
        5: "{previous_question} = {correct_answers}",
        6: "{german}"
           "<br><br>{english}",
        7: "{previous_question} = {correct_answers}",
        8: "{german}"
           "<br><br>{english}",
    },
}
