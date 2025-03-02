from data.exercises import (artikel, pronomen, konnektoren, praepositionen_grammatik, adjektivDeklinationen,
                            praesens, praepositionen_konjugation, imperativ, perfekt, praeteritum, konjunktiv,
                            verben, adjektive, adverbien)

FEEDBACK_TEMPLATES = {
    artikel: {
        1: "{german_text}",
        2: "{german_text}",
        3: "{german_text}",
        4: "{german_text}",
        5: "{german_text}",
        6: "{german_text}",
        7: "{german_text}",
        8: "{german_text}",
        9: "{german_text}"
           "<br><br>{english_text}",
        10: "{previous_question} = {correct_answers}",
        11: "{german_text}"
           "<br><br>{english_text}",
        12: "{previous_question} = {correct_answers}",
        13: "{german_text}"
            "<br><br>{english_text}",
    },

    pronomen: {
        1: "{german_text}"
           "<br><br>{person}, {case} → {correct_answers}",
        2: "{german_text}"
           "<br><br>{person}, {case} → {correct_answers}",
        3: "{german_text}"
           "<br><br>{person}, {case} → {correct_answers}",
        4: "{german_text}"
           "<br><br>{person}, {case} → {correct_answers}",
        5: "{german_text}"
           "<br><br>{person}, {case} → {correct_answers}",
        6: "{german_text}"
           "<br><br>{person}, {case} → {correct_answers}",
        7: "{previous_question} = {correct_answers}",
        8: "{german_text}"
            "<br><br>{english_text}",
        9: "{german_text}"
           "<br><br>{person}, {case} → {correct_answers}",
        10: "{german_text}"
           "<br><br>{person}, {case} → {correct_answers}",
        11: "{german_text}"
           "<br><br>{person}, {case} → {correct_answers}",
        12: "{german_text}"
           "<br><br>{person}, {case} → {correct_answers}",
        13: "{german_text}"
           "<br><br>{person}, {case} → {correct_answers}",
        14: "{german_text}"
           "<br><br>{person}, {case} → {correct_answers}",
    },

    konnektoren: {
        1: "{previous_question} = {correct_answers}",
        2: "{german_text}"
            "<br><br>{english_text}",
        3: "{previous_question} = {correct_answers}",
        4: "{german_text}"
            "<br><br>{english_text}",
        5: "{previous_question} = {correct_answers}",
        6: "{german_text}"
            "<br><br>{english_text}",
        7: "{previous_question} = {correct_answers}",
        8: "{german_text}"
            "<br><br>{english_text}",
    },

    praepositionen_grammatik: {
        1: "{previous_question} = {correct_answers}",
        2: "{german_text}"
           "<br><br>{english_text}",
        3: "{german_text}"
           "<br><br>{english_text}",
        4: "{german_text}"
           "<br><br>{english_text}",
        5: "{german_text}"
           "<br><br>{english_text}",
        6: "{german_text}"
           "<br><br>{english_text}",
        7: "{german_text}"
           "<br><br>{english_text}",
        8: "{german_text}"
           "<br><br>{english_text}",
        9: "{previous_question} = {correct_answers}",
        10: "{german_text}"
           "<br><br>{english_text}",
        11: "{previous_question} = {correct_answers}",
        12: "{german_text}"
            "<br><br>{english_text}",
    },

    adjektivDeklinationen: {
        1: "{german_text}"
           "<br><br>{article}, {gender}, {case} → {correct_answers}",
        2: "{german_text}"
           "<br><br>{article}, {gender}, {case} → {correct_answers}",
        3: "{german_text}"
           "<br><br>{article}, {gender}, {case} → {correct_answers}",
        4: "{german_text}"
           "<br><br>{article}, {gender}, {case} → {correct_answers}",
        5: "{german_text}"
           "<br><br>{article}, {gender}, {case} → {correct_answers}",
        6: "{german_text}"
           "<br><br>{article}, {gender}, {case} → {correct_answers}",
        7: "{german_text}"
           "<br><br>{article}, {gender}, {case} → {correct_answers}",
        8: "{german_text}"
           "<br><br>{article}, {gender}, {case} → {correct_answers}",
        9: "{german_text}"
           "<br><br>{article}, {gender}, {case} → {correct_answers}",
        10: "{german_text}"
           "<br><br>{article}, {gender}, {case} → {correct_answers}",
        11: "{german_text}"
           "<br><br>{article}, {gender}, {case} → {correct_answers}",
        12: "{german_text}"
           "<br><br>{article}, {gender}, {case} → {correct_answers}",
        13: "{german_text}"
           "<br><br>{article}, {gender}, {case} → {correct_answers}",
        14: "{german_text}"
           "<br><br>{article}, {gender}, {case} → {correct_answers}",
        15: "{german_text}"
            "<br><br>{article}, {gender}, {case} → {correct_answers}",
        16: "{german_text}"
            "<br><br>{article}, {gender}, {case} → {correct_answers}",
    },

    praesens: {
        1: "{previous_question} → {person} {correct_answers}"
           "<br><br>{previous_question} = {english_text}",
        2: "{previous_question} → {person} {correct_answers}"
           "<br><br>{previous_question} = {english_text}",
        3: "{previous_question} → {person} {correct_answers}"
           "<br><br>{previous_question} = {english_text}",
        4: "{previous_question} → {person} {correct_answers}"
           "<br><br>{previous_question} = {english_text}",
        5: "{previous_question} → {person} {correct_answers}"
           "<br><br>{previous_question} = {english_text}",
        6: "{previous_question} → {person} {correct_answers}"
           "<br><br>{previous_question} = {english_text}",
        7: "{previous_question} → {person} {correct_answers}"
           "<br><br>{previous_question} = {english_text}",
        8: "{previous_question} → {person} {correct_answers}"
           "<br><br>{previous_question} = {english_text}",
        9: "{previous_question} → {person} {correct_answers}"
           "<br><br>{previous_question} = {english_text}",
        10: "{previous_question} → {person} {correct_answers}"
           "<br><br>{previous_question} = {english_text}",
    },

    praepositionen_konjugation: {
        1: "{english_text} = {previous_question} {correct_answers}",
        2: "{german_text}"
           "<br><br>{english_text}",
        3: "{english_text} = {previous_question} {correct_answers}",
        4: "{german_text}"
           "<br><br>{english_text}",
        5: "{english_text} = {previous_question} {correct_answers}",
        6: "{german_text}"
           "<br><br>{english_text}",
        7: "{german_text}"
           "<br><br>{english_text}",
        8: "{german_text}"
           "<br><br>{english_text}",
        9: "{english_text} = {previous_question} {correct_answers}",
        10: "{german_text}"
            "<br><br>{english_text}",
        11: "{english_text} = {previous_question} {correct_answers}",
        12: "{german_text}"
            "<br><br>{english_text}",
        13: "{english_text} = {previous_question} {correct_answers}",
        14: "{german_text}"
            "<br><br>{english_text}",
    },

    perfekt: {
        1: "Partizip II {previous_question}: {correct_answers}"
           "<br><br>{previous_question} = {english_text}",
        2: "{german_text}"
           "<br><br>{english_text}",
        3: "{german_text}"
           "<br><br>{english_text}",
        4: "Partizip II {previous_question}: {correct_answers}"
           "<br><br>{previous_question} = {english_text}",
        5: "{german_text}"
           "<br><br>{english_text}",
        6: "{german_text}"
           "<br><br>{english_text}",
        7: "Partizip II {previous_question}: {correct_answers}"
           "<br><br>{previous_question} = {english_text}",
        8: "Partizip II {previous_question}: {correct_answers}"
           "<br><br>{previous_question} = {english_text}",
    },

    praeteritum: {
        1: "{previous_question} → {person} {correct_answers}"
           "<br><br>{previous_question} = {english_text}",
        2: "{previous_question} → er/sie/es {correct_answers}"
           "<br><br>{previous_question} = {english_text}",
        3: "{previous_question} → er/sie/es {correct_answers}"
           "<br><br>{previous_question} = {english_text}",
        4: "{previous_question} → er/sie/es {correct_answers}"
           "<br><br>{previous_question} = {english_text}",
        5: "{previous_question} → er/sie/es {correct_answers}"
           "<br><br>{previous_question} = {english_text}",
    },

    imperativ: {
        1: "{previous_question}, {person} → {correct_answers}"
           "<br><br>{previous_question} = {english_text}",
        2: "{previous_question}, {person} → {correct_answers}"
           "<br><br>{previous_question} = {english_text}",
        3: "{previous_question}, {person} → {correct_answers}"
           "<br><br>{previous_question} = {english_text}",
        4: "{previous_question}, {person} → {correct_answers}"
           "<br><br>{previous_question} = {english_text}",
        5: "{previous_question}, {person} → {correct_answers}"
           "<br><br>{previous_question} = {english_text}",
    },

    konjunktiv: {
        1: "{previous_question} → {person} {correct_answers}"
           "<br><br>{previous_question} = {english_text}",
    },

    adverbien: {
        1: "{previous_question} = {correct_answers}",
        2: "{german_text}"
           "<br><br>{english_text}",
        3: "{previous_question} = {correct_answers}",
        4: "{german_text}"
           "<br><br>{english_text}",
        5: "{previous_question} = {correct_answers}",
        6: "{german_text}"
           "<br><br>{english_text}",
        7: "{previous_question} = {correct_answers}",
        8: "{german_text}"
           "<br><br>{english_text}",
    },
}
