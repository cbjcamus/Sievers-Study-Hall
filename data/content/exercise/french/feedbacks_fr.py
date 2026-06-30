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
        "<br><br>Réponse(s) correcte(s) : {correct_answers}",

    wortstellung:
        "{german}"
        "<br><br><i>{french}</i>"
        "{indication_french}"
        "<br><br>{explanation_french}"
        "<br><br>Réponse(s) correcte(s): {correct_answers_bullet_points}",

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
        "{root_french} → {root_german_wiktionary}"
        "<br><br>{french} → {correct_answer_wiktionary}",

    praesens:
        "{german_wiktionary} → {person} {first_correct_answer}"
        "<br><br>{german_wiktionary} = {french}"
        "<br><br>Réponse(s) correcte(s) : {correct_answers}",

    partizip_II:
        "Partizip II {german_wiktionary} → {first_correct_answer}"
        "<br><br>{explanation_french}"
        "<br><br>{german_wiktionary} = {french}"
        "<br><br>Réponse(s) correcte(s) : {correct_answers}",

    praeteritum:
        "{german_wiktionary} → {person} {first_correct_answer}"
        "<br><br>{german_wiktionary} = {french}"
        "<br><br>Réponse(s) correcte(s) : {correct_answers}",

    imperativ:
        "{german_wiktionary}, {person} → {correct_answers}"
        "<br><br>{german_wiktionary} = {french}"
        "<br><br>Réponse(s) correcte(s) : {correct_answers}",

    konjunktiv_II:
        "{german_wiktionary} → {person} {first_correct_answer}"
        "<br><br>{german_wiktionary} = {french}"
        "<br><br>Réponse(s) correcte(s) : {correct_answers}",

    konjunktiv_I:
        "{german_wiktionary} → {person} {first_correct_answer}"
        "<br><br>{german_wiktionary} = {french}"
        "<br><br>Réponse(s) correcte(s) : {correct_answers}",

    partizip_I:
        "Partizip I {german_wiktionary} → {first_correct_answer}"
        "<br><br>{german_wiktionary} = {french}"
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
        11: "{explanation_french}",
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
        15: "{explanation_french}",
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
        41: "{explanation_french}",
        42: "{german}"
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
        29: "{french} \u25CF {case_french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        30: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        31: "{french} = {correct_answers}",
        32: "{french} = {correct_answers}",
        33: "{french} = {correct_answers}",
        34: "{french} = {correct_answers}",
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
        1: "{french} = {correct_answer_wiktionary}",
        2: "{french} = {correct_answer_wiktionary}",
        3: "{french} = {correct_answer_wiktionary}",
        4: "{french} = {correct_answer_wiktionary}",

        5: "{french} = {correct_answer_wiktionary}",
        6: "{french} = {correct_answer_wiktionary}",
        7: "{french} = {correct_answer_wiktionary}",
        8: "{french} = {correct_answer_wiktionary}",

        9: "{german_wiktionary} = {correct_answer}",
        10: "{german_wiktionary} = {correct_answer}",
        11: "{german_wiktionary} = {correct_answer}",
        12: "{german_wiktionary} = {correct_answer}",
        13: "{german_wiktionary} = {correct_answer}",
        14: "{german_wiktionary} = {correct_answer}",
        15: "{german_wiktionary} = {correct_answer}",
        16: "{german_wiktionary} = {correct_answer}",
        17: "{french} = {correct_answer_wiktionary}",
        18: "{french} = {correct_answer_wiktionary}",
        19: "{french} = {correct_answer_wiktionary}",
        20: "{french} = {correct_answer_wiktionary}",
        21: "{french} = {correct_answer_wiktionary}",
        22: "{french} = {correct_answer_wiktionary}",
        23: "{french} = {correct_answer_wiktionary}",
        24: "{french} = {correct_answer_wiktionary}",

        25: "{german_wiktionary} = {correct_answer}",
        26: "{german_wiktionary} = {correct_answer}",
        27: "{german_wiktionary} = {correct_answer}",
        28: "{german_wiktionary} = {correct_answer}",
        29: "{german_wiktionary} = {correct_answer}",
        30: "{german_wiktionary} = {correct_answer}",
        31: "{german_wiktionary} = {correct_answer}",
        32: "{german_wiktionary} = {correct_answer}",
        33: "{german_wiktionary} = {correct_answer}",
        34: "{german_wiktionary} = {correct_answer}",
        35: "{german_wiktionary} = {correct_answer}",
        36: "{german_wiktionary} = {correct_answer}",
        37: "{german_wiktionary} = {correct_answer}",
        38: "{german_wiktionary} = {correct_answer}",
        39: "{german_wiktionary} = {correct_answer}",
        40: "{german_wiktionary} = {correct_answer}",
        41: "{french} = {correct_answer_wiktionary}",
        42: "{french} = {correct_answer_wiktionary}",
        43: "{french} = {correct_answer_wiktionary}",
        44: "{french} = {correct_answer_wiktionary}",
        45: "{french} = {correct_answer_wiktionary}",
        46: "{french} = {correct_answer_wiktionary}",
        47: "{french} = {correct_answer_wiktionary}",
        48: "{french} = {correct_answer_wiktionary}",
        49: "{french} = {correct_answer_wiktionary}",
        50: "{french} = {correct_answer_wiktionary}",
        51: "{french} = {correct_answer_wiktionary}",
        52: "{french} = {correct_answer_wiktionary}",
        53: "{french} = {correct_answer_wiktionary}",
        54: "{french} = {correct_answer_wiktionary}",
        55: "{french} = {correct_answer_wiktionary}",
        56: "{french} = {correct_answer_wiktionary}",

        57: "{german_wiktionary} = {correct_answer}",
        58: "{german_wiktionary} = {correct_answer}",
        59: "{german_wiktionary} = {correct_answer}",
        60: "{german_wiktionary} = {correct_answer}",
        61: "{german_wiktionary} = {correct_answer}",
        62: "{german_wiktionary} = {correct_answer}",
        63: "{german_wiktionary} = {correct_answer}",
        64: "{german_wiktionary} = {correct_answer}",
        65: "{german_wiktionary} = {correct_answer}",
        66: "{german_wiktionary} = {correct_answer}",
        67: "{german_wiktionary} = {correct_answer}",
        68: "{german_wiktionary} = {correct_answer}",
        69: "{german_wiktionary} = {correct_answer}",
        70: "{german_wiktionary} = {correct_answer}",
        71: "{german_wiktionary} = {correct_answer}",
        72: "{german_wiktionary} = {correct_answer}",
        73: "{german_wiktionary} = {correct_answer}",
        74: "{german_wiktionary} = {correct_answer}",
        75: "{german_wiktionary} = {correct_answer}",
        76: "{german_wiktionary} = {correct_answer}",
        77: "{german_wiktionary} = {correct_answer}",
        78: "{german_wiktionary} = {correct_answer}",
        79: "{german_wiktionary} = {correct_answer}",
        80: "{german_wiktionary} = {correct_answer}",
        81: "{german_wiktionary} = {correct_answer}",
        82: "{german_wiktionary} = {correct_answer}",
        83: "{german_wiktionary} = {correct_answer}",
        84: "{german_wiktionary} = {correct_answer}",
        85: "{german_wiktionary} = {correct_answer}",
        86: "{german_wiktionary} = {correct_answer}",
        87: "{german_wiktionary} = {correct_answer}",
        88: "{german_wiktionary} = {correct_answer}",
        89: "{french} = {correct_answer_wiktionary}",
        90: "{french} = {correct_answer_wiktionary}",
        91: "{french} = {correct_answer_wiktionary}",
        92: "{french} = {correct_answer_wiktionary}",
        93: "{french} = {correct_answer_wiktionary}",
        94: "{french} = {correct_answer_wiktionary}",
        95: "{french} = {correct_answer_wiktionary}",
        96: "{french} = {correct_answer_wiktionary}",
        97: "{french} = {correct_answer_wiktionary}",
        98: "{french} = {correct_answer_wiktionary}",
        99: "{french} = {correct_answer_wiktionary}",
        100: "{french} = {correct_answer_wiktionary}",
        101: "{french} = {correct_answer_wiktionary}",
        102: "{french} = {correct_answer_wiktionary}",
        103: "{french} = {correct_answer_wiktionary}",
        104: "{french} = {correct_answer_wiktionary}",
        105: "{french} = {correct_answer_wiktionary}",
        106: "{french} = {correct_answer_wiktionary}",
        107: "{french} = {correct_answer_wiktionary}",
        108: "{french} = {correct_answer_wiktionary}",
        109: "{french} = {correct_answer_wiktionary}",
        110: "{french} = {correct_answer_wiktionary}",
        111: "{french} = {correct_answer_wiktionary}",
        112: "{french} = {correct_answer_wiktionary}",
        113: "{french} = {correct_answer_wiktionary}",
        114: "{french} = {correct_answer_wiktionary}",
        115: "{french} = {correct_answer_wiktionary}",
        116: "{french} = {correct_answer_wiktionary}",
        117: "{french} = {correct_answer_wiktionary}",
        118: "{french} = {correct_answer_wiktionary}",
        119: "{french} = {correct_answer_wiktionary}",
        120: "{french} = {correct_answer_wiktionary}",
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
