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

FEEDBACK_UNIT_EN = {
    pronominaladverbien:
        "{german}"
        "<br><br><i>{english}</i>"
        "<br><br>Correct answer(s): {correct_answers}"
        "<br><br>{explanation_english}",

    praepositionen_artikel:
        "{german}"
        "<br><br><i>{english}</i>"
        "<br><br>{person}, {gender_english}{case_english} → {article}"
        "<br><br>{explanation_english}"
        "<br><br>Correct answer(s): {correct_answers}",

    verben_artikel:
        "{german}"
        "<br><br><i>{english}</i>"
        "<br><br>{explanation_english}"
        "<br><br>Correct answer(s): {correct_answers}",

    wortstellung:
        "Placeholder",

    adjektive:
        "{english} = {correct_answers}"
        "{explanation_english}",

    komparativ_superlativ:
        "{explanation_english}"
        "<br><br><i>{english}</i>"
        "<br><br>Correct answer(s): {correct_answers}",

    adjektive_konjunktionen:
        "{german}"
        "<br><br><i>{english}</i>"
        "<br><br>{explanation_english}"
        "<br><br>Correct answer(s): {correct_answers}",

    trennbare_verben:
        "{root_english} → {root_german}"
        "<br><br>{english} → {correct_answers}",

    praesens:
        "{german} → {person} {first_correct_answer}"
        "<br><br>{german} = {english}"
        "<br><br>Correct answer(s): {correct_answers}",

    partizip_II:
        "Partizip II {german} → {first_correct_answer}"
        "<br><br>{explanation_english}"
        "<br><br>{german} = {english}"
        "<br><br>Correct answer(s): {correct_answers}",

    praeteritum:
        "{german} → {person} {correct_answers}"
        "<br><br>{explanation_english}"
        "<br><br>{german} = {english}"
        "<br><br>Correct answer: {correct_answers}",

    imperativ:
        "{german}, {person} → {correct_answers}"
        "<br><br>{german} = {english}"
        "<br><br>Correct answer(s): {correct_answers}",

    konjunktiv_II:
        "{german} → {person} {first_correct_answer}"
        "<br><br>{german} = {english}"
        "<br><br>Correct answer(s): {correct_answers}",

    konjunktiv_I:
        "{german} → {person} {first_correct_answer}"
        "<br><br>{german} = {english}"
        "<br><br>Correct answer(s): {correct_answers}",

    partizip_I:
        "Partizip I {german} → {first_correct_answer}"
        "<br><br>{german} = {english}"
        "<br><br>{first_correct_answer} = {explanation_english}"
        "<br><br>Correct answer(s): {correct_answers}",

    nomen_verben_wortstaemme:
        "{root_english} → {previous_question}"
        "<br><br>{english} → {first_correct_answer}"
        "<br><br>Correct answer(s): {correct_answers}",

    adjektive_verben_wortstaemme:
        "{root_english} → {previous_question}"
        "<br><br>{english} → {first_correct_answer}"
        "<br><br>Correct answer(s): {correct_answers}",

    adjektive_nomen_wortstaemme:
        "{root_english} → {previous_question}"
        "<br><br>{english} → {first_correct_answer}"
        "<br><br>Correct answer(s): {correct_answers}",

    genus:
        "{german}"
        "<br><br><i>{english}</i>"
        "{explanation_english}",

    plural:
        "{previous_question} &#8594 die {correct_answer}"
        "<br><br><i>{english}</i>",
}


FEEDBACK_EXERCISE_EN = {
    praepositionen: {
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

        17: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        18: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        19: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        20: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        21: "{english} = {correct_answers}",
        22: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        23: "{english} = {correct_answers}",
        24: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        25: "{english} = {correct_answers}",
        26: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        27: "{english} = {correct_answers}",
        28: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        29: "{english} = {correct_answers}",
        30: "{german} ↔ {first_correct_answer}"
            "<br><br>{english}"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
    },

    praepositionen_verben: {
        1: "{explanation_english}",
        2: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{explanation_english}"
           "<br><br>Correct answer(s): {correct_answers}",
        3: "{explanation_english}",
        4: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{explanation_english}"
           "<br><br>Correct answer(s): {correct_answers}",

        5: "{explanation_english}",
        6: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{explanation_english}"
           "<br><br>Correct answer(s): {correct_answers}",
        7: "{explanation_english}",
        8: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{explanation_english}"
           "<br><br>Correct answer(s): {correct_answers}",

        9: "{explanation_english}",
        10: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        11: "{explanation_english}",
        12: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        13: "{explanation_english}",
        14: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        15: "{explanation_english}",
        16: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",

        17: "{explanation_english}",
        18: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        19: "{explanation_english}",
        20: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        21: "{explanation_english}",
        22: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        23: "{explanation_english}",
        24: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",

        25: "{explanation_english}",
        26: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        27: "{explanation_english}",
        28: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        29: "{explanation_english}",
        30: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        31: "{explanation_english}",
        32: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",

        33: "{explanation_english}",
        34: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        35: "{explanation_english}",
        36: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        37: "{explanation_english}",
        38: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        39: "{explanation_english}",
        40: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
    },

    praepositionen_adjektive: {
        1: "{explanation_english}",
        2: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{explanation_english}"
           "<br><br>Correct answer(s): {correct_answers}",
        3: "{explanation_english}",
        4: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{explanation_english}"
           "<br><br>Correct answer(s): {correct_answers}",

        5: "{explanation_english}",
        6: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{explanation_english}"
           "<br><br>Correct answer(s): {correct_answers}",
        7: "{explanation_english}",
        8: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{explanation_english}"
           "<br><br>Correct answer(s): {correct_answers}",
        9: "{explanation_english}",
        10: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",

        11: "{explanation_english}",
        12: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        13: "{explanation_english}",
        14: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        15: "{explanation_english}",
        16: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",

        17: "{explanation_english}",
        18: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        19: "{explanation_english}",
        20: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        21: "{explanation_english}",
        22: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
    },

    praepositionen_nomen: {
        1: "{explanation_english}",
        2: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{explanation_english}"
           "<br><br>Correct answer(s): {correct_answers}",
        3: "{explanation_english}",
        4: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{explanation_english}"
           "<br><br>Correct answer(s): {correct_answers}",

        5: "{explanation_english}",
        6: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{explanation_english}"
           "<br><br>Correct answer(s): {correct_answers}",
        7: "{explanation_english}",
        8: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{explanation_english}"
           "<br><br>Correct answer(s): {correct_answers}",
        9: "{explanation_english}",
        10: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        11: "{explanation_english}",
        12: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",

        13: "{explanation_english}",
        14: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        15: "{explanation_english}",
        16: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        17: "{explanation_english}",
        18: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        19: "{explanation_english}",
        20: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        21: "{explanation_english}",
        22: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        23: "{explanation_english}",
        24: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        25: "{explanation_english}",
        26: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        27: "{explanation_english}",
        28: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",

        29: "{explanation_english}",
        30: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
    },


    artikel: {
        1: "{german}, {gender_english}, {case_english} → {correct_answers}",
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
        11: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender_english}, {case_english} → {correct_answers}",
        12: "{german}, {gender_english}, {case_english} → {correct_answers}",
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
        20: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender_english}, {case_english} → {correct_answers}",
        21: "{german}, {gender_english}, {case_english} → {correct_answers}",
        22: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender_english}, {case_english} → {correct_answers}",
        23: "{german}, {gender_english}, {case_english} → {correct_answers}",
        24: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender_english}, {case_english} → {correct_answers}",
        25: "{german}, {gender_english}, {case_english} → {correct_answers}",
        26: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender_english}, {case_english} → {correct_answers}",

        27: "{german}, {gender_english}, {case_english} → {correct_answers}",
        28: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender_english}, {case_english} → {correct_answers}",
        29: "{german}, {gender_english}, {case_english} → {correct_answers}",
        30: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender_english}, {case_english} → {correct_answers}",
        31: "{english} = {correct_answers}",
        32: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",

        33: "{german}, {gender_english}, {case_english} → {correct_answers}",
        34: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender_english}, {case_english} → {correct_answers}",
        35: "{gender_english}, {case_english} → {correct_answers}",
        36: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender_english}, {case_english} → {correct_answers}",
        37: "{german}, {gender_english}, {case_english} → {correct_answers}",
        38: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{person}, {gender_english}, {case_english} → {correct_answers}",

        39: "{german}, {gender_english}, {case_english} → {correct_answers}",
        40: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender_english}, {case_english} → {correct_answers}",

        41: "{german}, {gender_english}, {case_english} → {correct_answers}",
        42: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender_english}, {case_english} → {correct_answers}",
        43: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{person}, {gender_english}, {case_english} → {correct_answers}",
        44: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{person}, {gender_english}, {case_english} → {correct_answers}",
    },

    pronomen: {
        1: "{english}, {case_english} → {correct_answers}",
        2: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{person}, {case_english} → {correct_answers}",
        3: "{english}, {case_english} → {correct_answers}",
        4: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{person}, {case_english} → {correct_answers}",
        5: "{english}, {case_english} → {correct_answers}",
        6: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{person}, {case_english} → {correct_answers}",
        7: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{person}, {case_english} → {correct_answers}",
        8: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{person}, {case_english} → {correct_answers}",
        9: "{gender_english}, {case_english} → {correct_answers}"
           "<br><br>{previous_question} → {german}",
        10: "{gender_english}, {case_english} → {correct_answers}"
            "<br><br>{previous_question} → {german}",

        11: "{english}, {case_english} → {correct_answers}",
        12: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{person}, {case_english} → {correct_answers}",
        13: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{person}, {case_english} → {correct_answers}",
        14: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{person}, {case_english} → {correct_answers}",

        15: "{english} = {correct_answers}",
        16: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{case_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        17: "{gender_english}, {case_english} → {correct_answers}",
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

        24: "{english} = {correct_answers}",
        25: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{case_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        26: "{english} \u25CF {case_english} = {correct_answers}",
        27: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{person} \u25CF {case_english} → {first_correct_answer}"
            "<br><br>Correct answer(s): {correct_answers}",
        28: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender_english}, {case_english} → {correct_answers}",
        29: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender_english}, {case_english} → {correct_answers}",
        30: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        31: "{german}, {gender_english}, {case_english} → {correct_answers}",
        32: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender_english}, {case_english} → {correct_answers}",
        33: "{german}, {gender_english}, {case_english} → {correct_answers}",
        34: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender_english}, {case_english} → {correct_answers}",

        35: "{english} = {correct_answers}",
        36: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        37: "{english} = {correct_answers}",
        38: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        39: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",

        40: "{english}, {gender_english}, {case_english} → {correct_answers}",
        41: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender_english}, {case_english} → {correct_answers}",
        42: "{english}, {gender_english}, {case_english} → {correct_answers}",
        43: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender_english}, {case_english} → {correct_answers}",
    },

    konnektoren: {
        1: "{english} \u25CF {case_english} → {first_correct_answer}"
           "<br><br>Correct answer(s): {correct_answers}",
        2: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{explanation_english}"
           "<br><br>Correct answer(s): {correct_answers}",

        3: "{english} \u25CF {case_english} → {first_correct_answer}"
           "<br><br>Correct answer(s): {correct_answers}",
        4: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{explanation_english}"
           "<br><br>Correct answer(s): {correct_answers}",

        5: "{english} \u25CF {case_english} → {first_correct_answer}"
           "<br><br>Correct answer(s): {correct_answers}",
        6: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{explanation_english}"
           "<br><br>Correct answer(s): {correct_answers}",
        7: "{english} \u25CF {case_english} → {first_correct_answer}"
           "<br><br>Correct answer(s): {correct_answers}",
        8: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{explanation_english}"
           "<br><br>Correct answer(s): {correct_answers}",
        9: "{english} \u25CF {case_english} → {first_correct_answer}"
           "<br><br>Correct answer(s): {correct_answers}",
        10: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        11: "{english} = {correct_answers}",

        12: "{english} \u25CF {case_english} → {first_correct_answer}"
            "<br><br>Correct answer(s): {correct_answers}",
        13: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        14: "{english} \u25CF {case_english} → {first_correct_answer}"
            "<br><br>Correct answer(s): {correct_answers}",
        15: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        16: "{english} \u25CF {case_english} → {first_correct_answer}"
            "<br><br>Correct answer(s): {correct_answers}",
        17: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        18: "{english} = {correct_answers}",

        19: "{english} \u25CF {case_english} → {first_correct_answer}"
            "<br><br>Correct answer(s): {correct_answers}",
        20: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        21: "{english} \u25CF {case_english} → {first_correct_answer}"
            "<br><br>Correct answer(s): {correct_answers}",
        22: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        23: "{english} \u25CF {case_english} → {first_correct_answer}"
            "<br><br>Correct answer(s): {correct_answers}",
        24: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        25: "{english} \u25CF {case_english} → {first_correct_answer}"
            "<br><br>Correct answer(s): {correct_answers}",
        26: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        27: "{english} \u25CF {case_english} → {first_correct_answer}"
            "<br><br>Correct answer(s): {correct_answers}",
        28: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        29: "{english} = {correct_answers}",
        30: "{english} = {correct_answers}",
        31: "{english} = {correct_answers}",
        32: "{english} = {correct_answers}",
    },

    fragen: {
        1: "{english} = {first_correct_answer}"
           "<br><br>Correct answer(s): {correct_answers}",
        2: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{explanation_english}"
           "<br><br>Correct answer(s): {correct_answers}",

        3: "{english} = {first_correct_answer}"
           "<br><br>Correct answer(s): {correct_answers}",
        4: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{explanation_english}"
           "<br><br>Correct answer(s): {correct_answers}",

        5: "{english} = {first_correct_answer}"
           "<br><br>Correct answer(s): {correct_answers}",
        6: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{explanation_english}"
           "<br><br>Correct answer(s): {correct_answers}",

        7: "{english} = {first_correct_answer}"
           "<br><br>Correct answer(s): {correct_answers}",
        8: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{explanation_english}"
           "<br><br>Correct answer(s): {correct_answers}",
        9: "{english} = {first_correct_answer}"
           "<br><br>Correct answer(s): {correct_answers}",
        10: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",

        11: "{english} = {first_correct_answer}"
            "<br><br>Correct answer(s): {correct_answers}",
        12: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        13: "{english} = {first_correct_answer}"
            "<br><br>Correct answer(s): {correct_answers}",
        14: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",

        15: "{english} = {first_correct_answer}"
            "<br><br>Correct answer(s): {correct_answers}",
        16: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
    },

    adverbien: {
        1: "{english} = {correct_answers}",
        2: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{explanation_english}"
           "<br><br>Correct answer(s): {correct_answers}",
        3: "{english} = {correct_answers}",
        4: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{explanation_english}"
           "<br><br>Correct answer(s): {correct_answers}",

        5: "{english} = {correct_answers}",
        6: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{explanation_english}"
           "<br><br>Correct answer(s): {correct_answers}",
        7: "{english} = {correct_answers}",
        8: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{explanation_english}"
           "<br><br>Correct answer(s): {correct_answers}",
        9: "{english} = {correct_answers}",
        10: "{german} ↔ {first_correct_answer}"
            "<br><br>{english}"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",

        11: "{english} = {correct_answers}",
        12: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        13: "{english} = {correct_answers}",
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
        20: "{german} ↔ {first_correct_answer}"
            "<br><br>{english}"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",

        21: "{english} = {correct_answers}",
        22: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        23: "{english} = {correct_answers}",
        24: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        25: "{english} = {correct_answers}",
        26: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        27: "{english} = {correct_answers}",
        28: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        29: "{english} = {correct_answers}",
        30: "{german} ↔ {first_correct_answer}"
            "<br><br>{english}"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",

        31: "{english} = {correct_answers}",
        32: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        33: "{english} = {correct_answers}",
        34: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        35: "{english} = {correct_answers}",
        36: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        37: "{english} = {correct_answers}",
        38: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        39: "{english} = {correct_answers}",
        40: "{german} ↔ {first_correct_answer}"
            "<br><br>{english}"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",

        41: "{english} = {correct_answers}",
        42: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        43: "{english} = {correct_answers}",
        44: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        45: "{english} = {correct_answers}",
        46: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        47: "{english} = {correct_answers}",
        48: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        49: "{english} = {correct_answers}",
        50: "{german} ↔ {first_correct_answer}"
            "<br><br>{english}"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",

        51: "{english} = {correct_answers}",
        52: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        53: "{english} = {correct_answers}",
        54: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        55: "{english} = {correct_answers}",
        56: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        57: "{english} = {correct_answers}",
        58: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        59: "{english} = {correct_answers}",
        60: "{german} ↔ {first_correct_answer}"
            "<br><br>{english}"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",

        61: "{english} = {correct_answers}",
        62: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        63: "{english} = {correct_answers}",
        64: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        65: "{english} = {correct_answers}",
        66: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        67: "{english} = {correct_answers}",
        68: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        69: "{english} = {correct_answers}",
        70: "{german} ↔ {first_correct_answer}"
            "<br><br>{english}"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",

        71: "{english} = {correct_answers}",
        72: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        73: "{english} = {correct_answers}",
        74: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        75: "{english} = {correct_answers}",
        76: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        77: "{english} = {correct_answers}",
        78: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        79: "{english} = {correct_answers}",
        80: "{german} ↔ {first_correct_answer}"
            "<br><br>{english}"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
    },

    adjektivdeklinationen: {
        1: "{german}"
           "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",
        2: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",
        3: "{german}"
           "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",
        4: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",
        5: "{german}"
           "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",
        6: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",
        7: "{german}"
           "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",
        8: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",
        9: "{german}"
           "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",
        10: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",
        11: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",
        12: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",
        13: "{german}"
            "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",
        14: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",

        15: "{german}"
            "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",
        16: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",
        17: "{german}"
            "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",
        18: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",
        19: "{german}"
            "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",
        20: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",
        21: "{german}"
            "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",
        22: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",

        23: "{german}"
            "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",
        24: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",
        25: "{german}"
            "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",
        26: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",
        27: "{german}"
            "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",
        28: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",

        29: "{german}"
            "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",
        30: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",
        31: "{german}"
            "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",
        32: "{german}"
            "<br><br><i>{english}</i>"
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

        21: "{english} = {correct_answers}",
        22: "{english} = {correct_answers}",
        23: "{english} = {correct_answers}",
        24: "{english} = {correct_answers}",
        25: "{english} = {correct_answers}",
        26: "{previous_question} = {correct_answers}",
        27: "{previous_question} = {correct_answers}",
        28: "{previous_question} = {correct_answers}",
        29: "{previous_question} = {correct_answers}",
        30: "{previous_question} = {correct_answers}",

        31: "{english} = {correct_answers}",
        32: "{english} = {correct_answers}",
        33: "{english} = {correct_answers}",
        34: "{english} = {correct_answers}",
        35: "{english} = {correct_answers}",
        36: "{english} = {correct_answers}",
        37: "{english} = {correct_answers}",
        38: "{english} = {correct_answers}",
        39: "{english} = {correct_answers}",
        40: "{english} = {correct_answers}",
        41: "{previous_question} = {correct_answers}",
        42: "{previous_question} = {correct_answers}",
        43: "{previous_question} = {correct_answers}",
        44: "{previous_question} = {correct_answers}",
        45: "{previous_question} = {correct_answers}",
        46: "{previous_question} = {correct_answers}",
        47: "{previous_question} = {correct_answers}",
        48: "{previous_question} = {correct_answers}",
        49: "{previous_question} = {correct_answers}",
        50: "{previous_question} = {correct_answers}",
    },

    nomen_verben_verbindungen: {
        1: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",
        2: "{german}"
           "<br><br><i>{english}</i>"
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
           "<br><br>Correct answer(s): {correct_answers}",
        6: "{german}"
           "<br><br><i>{english}</i>"
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
           "<br><br>Correct answer(s): {correct_answers}",
        10: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",
        11: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{explanation_english}"
           "<br><br>Correct answer(s): {correct_answers}",
        12: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>{explanation_english}"
           "<br><br>Correct answer(s): {correct_answers}",
        13: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Correct answer(s): {correct_answers}",
        14: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        15: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        16: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",

        17: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        18: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        19: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        20: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        21: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        22: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        23: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        24: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        25: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        26: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        27: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        28: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        29: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        30: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        31: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        32: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
    },

    genus_regeln: {
        1: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Rule: {explanation_english}",
        2: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Rule: {explanation_english}",
        3: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Rule: {explanation_english}",
        4: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Rule: {explanation_english}",
        5: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Exception to the rule: {explanation_english}",

        6: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Rule: {explanation_english}",
        7: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Rule: {explanation_english}",
        8: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Rule: {explanation_english}",
        9: "{german}"
           "<br><br><i>{english}</i>"
           "<br><br>Rule: {explanation_english}",
        10: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Exception to the rule: {explanation_english}",

        11: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Rule: {explanation_english}",
        12: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Rule: {explanation_english}",
        13: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Rule: {explanation_english}",
        14: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Rule: {explanation_english}",
        15: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Exception to the rule: {explanation_english}",

        16: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Rule: {explanation_english}",
        17: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Rule: {explanation_english}",
        18: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Rule: {explanation_english}",
        19: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Rule: {explanation_english}",
        20: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Exception to the rule: {explanation_english}",

        21: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Rule: {explanation_english}",
        22: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Rule: {explanation_english}",
        23: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Rule: {explanation_english}",
        24: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Rule: {explanation_english}",
        25: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Rule: {explanation_english}",
        26: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Rule: {explanation_english}",
        27: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Exception to the rule: {explanation_english}",
    },

    zahlen :{
        1: "{previous_question} → {first_correct_answer}"
           "<br><br>Correct answer(s): {correct_answers}",
        2: "{previous_question} → {first_correct_answer}"
           "<br><br>Correct answer(s): {correct_answers}",
        3: "{previous_question} → {first_correct_answer}"
           "<br><br>Correct answer(s): {correct_answers}",
        4: "{previous_question} → {first_correct_answer}"
           "<br><br>Correct answer(s): {correct_answers}",
        5: "{previous_question} → {first_correct_answer}"
           "<br><br>Correct answer(s): {correct_answers}",
        6: "{previous_question} → {first_correct_answer}"
           "<br><br>Correct answer(s): {correct_answers}",
        7: "{previous_question} → {first_correct_answer}"
           "<br><br>Correct answer(s): {correct_answers}",
        8: "{previous_question} → {first_correct_answer}"
           "<br><br>Correct answer(s): {correct_answers}",
        9: "{previous_question} → {first_correct_answer}"
           "<br><br>Correct answer(s): {correct_answers}",
        10: "{previous_question} → {first_correct_answer}"
            "<br><br>Correct answer(s): {correct_answers}",

        11: "{previous_question} → {first_correct_answer}"
           "<br><br>Correct answer(s): {correct_answers}",
        12: "{previous_question} → {first_correct_answer}"
            "<br><br>Correct answer(s): {correct_answers}",
        13: "{english} = {first_correct_answer}",
        14: "{english} = {first_correct_answer}",
        15: "{english} = {first_correct_answer}",
        16: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{case_english} → {first_correct_answer}"
            "<br><br>Correct answer(s): {correct_answers}",

        17: "{english} = {first_correct_answer}",
        18: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        19: "{english} = {first_correct_answer}",
        20: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",

        21: "{english} = {first_correct_answer}",
        22: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",

        23: "Genitive {previous_question}: {first_correct_answer}",
        24: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
    },
}
