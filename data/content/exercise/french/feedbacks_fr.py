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

FEEDBACK_UNIT_FR = {
    pronominaladverbien:
        "{german}"
        "<br><br><i>{french}</i>"
        "<br><br>Réponse(s) correcte(s) : {correct_answers}"
        "<br><br>{explanation_french}",

    praepositionen_artikel:
        "{german}"
        "<br><br><i>{french}</i>"
        "<br><br>{person}, {gender_french}{case_french} → {article}"
        "<br><br>{explanation_french}"
        "<br><br>Réponse(s) correcte(s) : {correct_answers}",

    verben_artikel:
        "{german}"
        "<br><br><i>{french}</i>"
        "<br><br>{explanation_french}"
        "<br><br>Correct answer(s): {correct_answers}",

    adjektive:
        "{french} = {correct_answers}"
        "{explanation_french}",

    komparativ_superlativ:
        "{explanation_french}"
        "<br><br><i>{french}</i>"
        "<br><br>Réponse(s) correcte(s) : {correct_answers}",

    adjektive_konjunktionen:
        "{german}"
        "<br><br><i>{french}</i>"
        "<br><br>{explanation_french}"
        "<br><br>Réponse(s) correcte(s) : {correct_answers}",

    trennbare_verben:
        "{root_french} → {root_german}"
        "<br><br>{french} → {correct_answers}",

    praesens:
        "{german} → {person} {first_correct_answer}"
        "<br><br>{german} = {french}"
        "<br><br>Réponse(s) correcte(s) : {correct_answers}",

    partizip_II:
        "Partizip II {german} → {first_correct_answer}"
        "<br><br>{explanation_french}"
        "<br><br>{german} = {french}"
        "<br><br>Réponse(s) correcte(s) : {correct_answers}",

    praeteritum:
        "{german} → {person} {first_correct_answer}"
        "<br><br>{german} = {french}"
        "<br><br>Réponse(s) correcte(s) : {correct_answers}",

    imperativ:
        "{german}, {person} → {correct_answers}"
        "<br><br>{german} = {french}"
        "<br><br>Réponse(s) correcte(s) : {correct_answers}",

    konjunktiv_II:
        "{german} → {person} {first_correct_answer}"
        "<br><br>{german} = {french}"
        "<br><br>Réponse(s) correcte(s) : {correct_answers}",

    konjunktiv_I:
        "{german} → {person} {first_correct_answer}"
        "<br><br>{german} = {french}"
        "<br><br>Réponse(s) correcte(s) : {correct_answers}",

    partizip_I:
        "Partizip I {german} → {first_correct_answer}"
        "<br><br>{german} = {french}"
        "<br><br>{first_correct_answer} = {explanation_french}"
        "<br><br>Réponse(s) correcte(s) : {correct_answers}",

    adjektive_verben_wortstaemme:
        "{root_french} → {previous_question}"
        "<br><br>{french} → {first_correct_answer}"
        "<br><br>Réponse(s) correcte(s) : {correct_answers}",

    adjektive_nomen_wortstaemme:
        "{root_french} → {previous_question}"
        "<br><br>{french} → {first_correct_answer}"
        "<br><br>Réponse(s) correcte(s) : {correct_answers}",

    nomen_verben_wortstaemme:
        "{root_french} → {previous_question}"
        "<br><br>{french} → {first_correct_answer}"
        "<br><br>Réponse(s) correcte(s) : {correct_answers}",

    genus:
        "{german}"
        "<br><br><i>{french}</i>"
        "{explanation_french}",

    plural:
        "{previous_question} &#8594 die {correct_answer}"
        "<br><br><i>{french}</i>",

}

FEEDBACK_EXERCISE_FR = {

    praepositionen: {
        1: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{explanation_french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        2: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{explanation_french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        3: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{explanation_french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        4: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{explanation_french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        5: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{explanation_french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        6: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{explanation_french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        7: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{explanation_french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        8: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{explanation_french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        9: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{explanation_french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        10: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        11: "{french} = {correct_answers}",
        12: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        13: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        14: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        15: "{french} = {correct_answers}",
        16: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        17: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        18: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        19: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        20: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        21: "{french} = {correct_answers}",
        22: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        23: "{french} = {correct_answers}",
        24: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        25: "{french} = {correct_answers}",
        26: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        27: "{french} = {correct_answers}",
        28: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        29: "{french} = {correct_answers}",
        30: "{german} ↔ {first_correct_answer}"
            "<br><br>{french}"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
    },

    praepositionen_verben: {
        1: "{explanation_french}",
        2: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{explanation_french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        3: "{explanation_french}",
        4: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{explanation_french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        5: "{explanation_french}",
        6: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{explanation_french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        7: "{explanation_french}",
        8: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{explanation_french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        9: "{explanation_french}",
        10: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        11: "{explanation_french}",
        12: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        13: "{explanation_french}",
        14: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        15: "{explanation_french}",
        16: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        17: "{explanation_french}",
        18: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        19: "{explanation_french}",
        20: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        21: "{explanation_french}",
        22: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        23: "{explanation_french}",
        24: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        25: "{explanation_french}",
        26: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        27: "{explanation_french}",
        28: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        29: "{explanation_french}",
        30: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        31: "{explanation_french}",
        32: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        33: "{explanation_french}",
        34: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        35: "{explanation_french}",
        36: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        37: "{explanation_french}",
        38: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        39: "{explanation_french}",
        40: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
    },

    praepositionen_adjektive: {
        1: "{explanation_french}",
        2: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{explanation_french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        3: "{explanation_french}",
        4: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{explanation_french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        5: "{explanation_french}",
        6: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{explanation_french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        7: "{explanation_french}",
        8: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{explanation_french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        9: "{explanation_french}",
        10: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        11: "{explanation_french}",
        12: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        13: "{explanation_french}",
        14: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        15: "{explanation_french}",
        16: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        17: "{explanation_french}",
        18: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        19: "{explanation_french}",
        20: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        21: "{explanation_french}",
        22: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
    },

    praepositionen_nomen: {
        1: "{explanation_french}",
        2: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{explanation_french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        3: "{explanation_french}",
        4: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{explanation_french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        5: "{explanation_french}",
        6: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{explanation_french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        7: "{explanation_french}",
        8: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{explanation_french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        9: "{explanation_french}",
        10: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        11: "{explanation_french}",
        12: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        13: "{explanation_french}",
        14: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        15: "{explanation_french}",
        16: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        17: "{explanation_french}",
        18: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        19: "{explanation_french}",
        20: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        21: "{explanation_french}",
        22: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        23: "{explanation_french}",
        24: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        25: "{explanation_french}",
        26: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        27: "{explanation_french}",
        28: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        29: "{explanation_french}",
        30: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
    },

    artikel: {
        1: "{german}, {gender_french}, {case_french} → {correct_answers}",
        2: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{gender_french}, {case_french} → {correct_answers}",
        3: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{gender_french}, {case_french} → {correct_answers}",
        4: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{gender_french}, {case_french} → {correct_answers}",
        5: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{gender_french}, {case_french} → {correct_answers}",
        6: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{gender_french}, {case_french} → {correct_answers}",
        7: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{gender_french}, {case_french} → {correct_answers}",
        8: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{gender_french}, {case_french} → {correct_answers}",
        9: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{gender_french}, {case_french} → {correct_answers}",
        10: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{gender_french}, {case_french} → {correct_answers}",
        11: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{gender_french}, {case_french} → {correct_answers}",
        12: "{german}, {gender_french}, {case_french} → {correct_answers}",
        13: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{gender_french}, {case_french} → {correct_answers}",
        14: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{gender_french}, {case_french} → {correct_answers}",
        15: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{gender_french}, {case_french} → {correct_answers}",
        16: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{gender_french}, {case_french} → {correct_answers}",
        17: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{gender_french}, {case_french} → {correct_answers}",
        18: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{gender_french}, {case_french} → {correct_answers}",
        19: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{gender_french}, {case_french} → {correct_answers}",
        20: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{gender_french}, {case_french} → {correct_answers}",
        21: "{german}, {gender_french}, {case_french} → {correct_answers}",
        22: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{gender_french}, {case_french} → {correct_answers}",
        23: "{german}, {gender_french}, {case_french} → {correct_answers}",
        24: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{gender_french}, {case_french} → {correct_answers}",
        25: "{german}, {gender_french}, {case_french} → {correct_answers}",
        26: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{gender_french}, {case_french} → {correct_answers}",

        27: "{german}, {gender_french}, {case_french} → {correct_answers}",
        28: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{gender_french}, {case_french} → {correct_answers}",
        29: "{german}, {gender_french}, {case_french} → {correct_answers}",
        30: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{gender_french}, {case_french} → {correct_answers}",
        31: "{french} = {correct_answers}",
        32: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        33: "{german}, {gender_french}, {case_french} → {correct_answers}",
        34: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{gender_french}, {case_french} → {correct_answers}",
        35: "{gender_french}, {case_french} → {correct_answers}",
        36: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{gender_french}, {case_french} → {correct_answers}",
        37: "{german}, {gender_french}, {case_french} → {correct_answers}",
        38: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{person}, {gender_french}, {case_french} → {correct_answers}",

        39: "{german}, {gender_french}, {case_french} → {correct_answers}",
        40: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{gender_french}, {case_french} → {correct_answers}",

        41: "{german}, {gender_french}, {case_french} → {correct_answers}",
        42: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{gender_french}, {case_french} → {correct_answers}",
        43: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{person}, {gender_french}, {case_french} → {correct_answers}",
        44: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{person}, {gender_french}, {case_french} → {correct_answers}",
    },

    pronomen: {
        1: "{french}, {case_french} → {correct_answers}",
        2: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{person}, {case_french} → {correct_answers}",
        3: "{french}, {case_french} → {correct_answers}",
        4: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{person}, {case_french} → {correct_answers}",
        5: "{french}, {case_french} → {correct_answers}",
        6: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{person}, {case_french} → {correct_answers}",
        7: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{person}, {case_french} → {correct_answers}",
        8: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{person}, {case_french} → {correct_answers}",
        9: "{gender_french}, {case_french} → {correct_answers}"
           "<br><br>{previous_question} → {german}",
        10: "{gender_french}, {case_french} → {correct_answers}"
            "<br><br>{previous_question} → {german}",

        11: "{french}, {case_french} → {correct_answers}",
        12: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{person}, {case_french} → {correct_answers}",
        13: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{person}, {case_french} → {correct_answers}",
        14: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{person}, {case_french} → {correct_answers}",

        15: "{french} = {correct_answers}",
        16: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{case_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        17: "{gender_french} \u25CF {case_french} → {correct_answers}",
        18: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{gender_french}, {case_french} → {correct_answers}",
        19: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{gender_french}, {case_french} → {correct_answers}",
        20: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{gender_french}, {case_french} → {correct_answers}",
        21: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{gender_french}, {case_french} → {correct_answers}",
        22: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{gender_french}, {case_french} → {correct_answers}",
        23: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{gender_french}, {case_french} → {correct_answers}",

        24: "{french} = {correct_answers}",
        25: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{case_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        26: "{french} \u25CF {case_french} = {correct_answers}",
        27: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{person} \u25CF {case_french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        28: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{gender_french}, {case_french} → {correct_answers}",
        29: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{gender_french}, {case_french} → {correct_answers}",
        30: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        31: "{german}, {gender_french}, {case_french} → {correct_answers}",
        32: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{gender_french}, {case_french} → {correct_answers}",
        33: "{german}, {gender_french}, {case_french} → {correct_answers}",
        34: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{gender_french}, {case_french} → {correct_answers}",

        35: "{french} = {correct_answers}",
        36: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        37: "{french} = {correct_answers}",
        38: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        39: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        40: "{french}, {gender_french}, {case_french} → {correct_answers}",
        41: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{gender_french}, {case_french} → {correct_answers}",
        42: "{french}, {gender_french}, {case_french} → {correct_answers}",
        43: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{gender_french}, {case_french} → {correct_answers}",
    },

    konnektoren: {
        1: "{french} \u25CF {case_french} → {first_correct_answer}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        2: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{explanation_french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        3: "{french} \u25CF {case_french} → {first_correct_answer}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        4: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{explanation_french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        5: "{french} \u25CF {case_french} → {first_correct_answer}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        6: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{explanation_french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        7: "{french} \u25CF {case_french} → {first_correct_answer}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        8: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{explanation_french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        9: "{french} \u25CF {case_french} → {first_correct_answer}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        10: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        11: "{french} = {correct_answers}",

        12: "{french} \u25CF {case_french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        13: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        14: "{french} \u25CF {case_french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        15: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        16: "{french} \u25CF {case_french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        17: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        18: "{french} = {correct_answers}",

        19: "{french} \u25CF {case_french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        20: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        21: "{french} \u25CF {case_french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        22: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        23: "{french} \u25CF {case_french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        24: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        25: "{french} \u25CF {case_french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        26: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        27: "{french} \u25CF {case_french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        28: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        29: "{french} = {correct_answers}",
        30: "{french} = {correct_answers}",
        31: "{french} = {correct_answers}",
        32: "{french} = {correct_answers}",
    },

    fragen: {
        1: "{french} = {first_correct_answer}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        2: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{explanation_french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        3: "{french} = {first_correct_answer}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        4: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{explanation_french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        5: "{french} = {first_correct_answer}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        6: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{explanation_french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        7: "{french} = {first_correct_answer}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        8: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{explanation_french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        9: "{french} = {first_correct_answer}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        10: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        11: "{french} = {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        12: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        13: "{french} = {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        14: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        15: "{french} = {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        16: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
    },

    adverbien: {
        1: "{french} = {correct_answers}",
        2: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{explanation_french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        3: "{french} = {correct_answers}",
        4: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{explanation_french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        5: "{french} = {correct_answers}",
        6: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{explanation_french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        7: "{french} = {correct_answers}",
        8: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{explanation_french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        9: "{french} = {correct_answers}",
        10: "{german} ↔ {first_correct_answer}"
            "<br><br>{french}"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        11: "{french} = {correct_answers}",
        12: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        13: "{french} = {correct_answers}",
        14: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        15: "{french} = {correct_answers}",
        16: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        17: "{french} = {correct_answers}",
        18: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        19: "{french} = {correct_answers}",
        20: "{german} ↔ {first_correct_answer}"
            "<br><br>{french}"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        21: "{french} = {correct_answers}",
        22: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        23: "{french} = {correct_answers}",
        24: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        25: "{french} = {correct_answers}",
        26: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        27: "{french} = {correct_answers}",
        28: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        29: "{french} = {correct_answers}",
        30: "{german} ↔ {first_correct_answer}"
            "<br><br>{french}"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        31: "{french} = {correct_answers}",
        32: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        33: "{french} = {correct_answers}",
        34: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        35: "{french} = {correct_answers}",
        36: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        37: "{french} = {correct_answers}",
        38: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        39: "{french} = {correct_answers}",
        40: "{german} ↔ {first_correct_answer}"
            "<br><br>{french}"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        41: "{french} = {correct_answers}",
        42: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        43: "{french} = {correct_answers}",
        44: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        45: "{french} = {correct_answers}",
        46: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        47: "{french} = {correct_answers}",
        48: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        49: "{french} = {correct_answers}",
        50: "{german} ↔ {first_correct_answer}"
            "<br><br>{french}"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        51: "{french} = {correct_answers}",
        52: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        53: "{french} = {correct_answers}",
        54: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        55: "{french} = {correct_answers}",
        56: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        57: "{french} = {correct_answers}",
        58: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        59: "{french} = {correct_answers}",
        60: "{german} ↔ {first_correct_answer}"
            "<br><br>{french}"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        61: "{french} = {correct_answers}",
        62: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        63: "{french} = {correct_answers}",
        64: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        65: "{french} = {correct_answers}",
        66: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        67: "{french} = {correct_answers}",
        68: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        69: "{french} = {correct_answers}",
        70: "{german} ↔ {first_correct_answer}"
            "<br><br>{french}"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        71: "{french} = {correct_answers}",
        72: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        73: "{french} = {correct_answers}",
        74: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        75: "{french} = {correct_answers}",
        76: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        77: "{french} = {correct_answers}",
        78: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        79: "{french} = {correct_answers}",
        80: "{german} ↔ {first_correct_answer}"
            "<br><br>{french}"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
    },

    wortstellung: {
        1: "Placeholder",
    },

    adjektivdeklinationen: {
        1: "{german}"
           "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",
        2: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",
        3: "{german}"
           "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",
        4: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",
        5: "{german}"
           "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",
        6: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",
        7: "{german}"
           "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",
        8: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",
        9: "{german}"
           "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",
        10: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",
        11: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",
        12: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",
        13: "{german}"
            "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",
        14: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",

        15: "{german}"
            "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",
        16: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",
        17: "{german}"
            "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",
        18: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",
        19: "{german}"
            "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",
        20: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",
        21: "{german}"
            "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",
        22: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",

        23: "{german}"
            "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",
        24: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",
        25: "{german}"
            "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",
        26: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",
        27: "{german}"
            "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",
        28: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",

        29: "{german}"
            "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",
        30: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",
        31: "{german}"
            "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",
        32: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",
    },

    verben: {
        1: "{french} = {correct_answers}",
        2: "{french} = {correct_answers}",
        3: "{french} = {correct_answers}",
        4: "{french} = {correct_answers}",
        5: "{french} = {correct_answers}",

        6: "{french} = {correct_answers}",
        7: "{french} = {correct_answers}",
        8: "{french} = {correct_answers}",
        9: "{french} = {correct_answers}",
        10: "{french} = {correct_answers}",

        11: "{french} = {correct_answers}",
        12: "{french} = {correct_answers}",
        13: "{french} = {correct_answers}",
        14: "{french} = {correct_answers}",
        15: "{french} = {correct_answers}",
        16: "{previous_question} = {correct_answers}",
        17: "{previous_question} = {correct_answers}",
        18: "{previous_question} = {correct_answers}",
        19: "{previous_question} = {correct_answers}",
        20: "{previous_question} = {correct_answers}",

        21: "{french} = {correct_answers}",
        22: "{french} = {correct_answers}",
        23: "{french} = {correct_answers}",
        24: "{french} = {correct_answers}",
        25: "{french} = {correct_answers}",
        26: "{previous_question} = {correct_answers}",
        27: "{previous_question} = {correct_answers}",
        28: "{previous_question} = {correct_answers}",
        29: "{previous_question} = {correct_answers}",
        30: "{previous_question} = {correct_answers}",

        31: "{french} = {correct_answers}",
        32: "{french} = {correct_answers}",
        33: "{french} = {correct_answers}",
        34: "{french} = {correct_answers}",
        35: "{french} = {correct_answers}",
        36: "{french} = {correct_answers}",
        37: "{french} = {correct_answers}",
        38: "{french} = {correct_answers}",
        39: "{french} = {correct_answers}",
        40: "{french} = {correct_answers}",
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
           "<br><br><i>{french}</i>"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        2: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        3: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{explanation_french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        4: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{explanation_french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        5: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        6: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        7: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{explanation_french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        8: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{explanation_french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        9: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        10: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        11: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        12: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        13: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        14: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        15: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        16: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        17: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        18: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        19: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        20: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        21: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        22: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        23: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        24: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        25: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        26: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        27: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        28: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        29: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        30: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        31: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        32: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
    },

    genus_regeln: {
        1: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>Règle : {explanation_french}",
        2: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>Règle : {explanation_french}",
        3: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>Règle : explanation_french}",
        4: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>Règle : {explanation_french}",
        5: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>Exception à la règle : {explanation_french}",

        6: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>Règle : {explanation_french}",
        7: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>Règle : {explanation_french}",
        8: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>Règle : {explanation_french}",
        9: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>Règle : {explanation_french}",
        10: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>Exception à la règle : {explanation_french}",

        11: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>Règle : {explanation_french}",
        12: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>Règle : {explanation_french}",
        13: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>Règle : {explanation_french}",
        14: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>Règle : {explanation_french}",
        15: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>Exception à la règle : {explanation_french}",

        16: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>Règle : {explanation_french}",
        17: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>Règle : {explanation_french}",
        18: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>Règle : {explanation_french}",
        19: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>Règle : {explanation_french}",
        20: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>Exception à la règle : {explanation_french}",

        21: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>Règle : {explanation_french}",
        22: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>Règle : {explanation_french}",
        23: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>Règle : {explanation_french}",
        24: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>Règle : {explanation_french}",
        25: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>Règle : {explanation_french}",
        26: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>Règle : {explanation_french}",
        27: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>Exception à la règle : {explanation_french}",
    },

    zahlen: {
        1: "{previous_question} → {answer}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        2: "{previous_question} → {answer}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        3: "{previous_question} → {answer}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        4: "{previous_question} → {answer}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        5: "{previous_question} → {answer}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        6: "{previous_question} → {answer}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        7: "{previous_question} → {answer}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        8: "{previous_question} → {answer}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        9: "{previous_question} → {answer}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        10: "{previous_question} → {answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        11: "{previous_question} → {answer}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        12: "{previous_question} → {answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        13: "{french} = {answer}",
        14: "{french} = {answer}",
        15: "{french} = {answer}",
        16: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{case_french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        17: "{french} = {answer}",
        18: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        19: "{french} = {answer}",
        20: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        21: "{french} = {answer}",
        22: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        23: "Génitif {previous_question}: {answer}",
        24: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
    },
}
