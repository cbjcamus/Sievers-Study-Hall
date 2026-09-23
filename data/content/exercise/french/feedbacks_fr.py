from data.data_processing.exercises import isolation, context, multiple_choice_native, multiple_choice_target, synonym, \
    antonym, prompt
from data.data_processing.units import (
    praepositionen, praepositionen_verben, praepositionen_adjektive, praepositionen_nomen, pronominaladverbien,
    artikel, pronomen, praepositionen_artikel, verben_artikel,
    konnektoren, fragen, adverbien, wortstellung,
    genus_regeln, genus, plural,
    adjektive, komparativ_superlativ, adjektivdeklinationen, adjektive_konjunktionen,
    verben, trennbare_verben, nomen_verben_verbindungen,
    praesens, imperativ, partizip_II, praeteritum, konjunktiv_II, konjunktiv_I, partizip_I,
    nomen_verben_wortstaemme, adjektive_verben_wortstaemme, adjektive_nomen_wortstaemme,
    zahlen, alpha,
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
        "<br><br>{explanation_french}"
        "<br><br>{german_wiktionary} = {french}"
        "<br><br>Réponse(s) correcte(s) : {correct_answers}",

    imperativ:
        "{german_wiktionary}, {person} → {first_correct_answer}"
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

    nomen_verben_wortstaemme:
        "{root_french} → {previous_question_wiktionary}"
        "<br><br>{french} → {first_correct_answer_wiktionary}"
        "<br><br>Réponse(s) correcte(s) : {correct_answers}",

    adjektive_verben_wortstaemme:
        "{root_french} → {previous_question_wiktionary}"
        "<br><br>{french} → {first_correct_answer_wiktionary}"
        "<br><br>Réponse(s) correcte(s) : {correct_answers}",

    adjektive_nomen_wortstaemme:
        "{root_french} → {previous_question_wiktionary}"
        "<br><br>{french} → {first_correct_answer_wiktionary}"
        "<br><br>Réponse(s) correcte(s) : {correct_answers}",

    genus:
        "{german}"
        "<br><br><i>{french}</i>"
        "{explanation_french}",

    plural:
        "{previous_question} &#8594 die {correct_answer}"
        "<br><br><i>{french}</i>",

    alpha:
        "{user_answer}"
        "<br><br><i>{translation}</i>"
        "<br><br>{explanation_french}"
        "{commentary}",
}

FEEDBACK_CATEGORY_FR = {

}

FEEDBACK_SUBCATEGORY_FR = {
    praepositionen: {
        context:
            "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        isolation:
            "{explanation_french}",
        synonym:
            "{french} = {correct_answers}",
        antonym:
            "{german} ↔ {first_correct_answer}"
            "<br><br>{french}"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
    },

    praepositionen_verben: {
        isolation:
            "{explanation_french}",
        context:
            "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
    },

    praepositionen_adjektive: {
        isolation:
            "{explanation_french}",
        context:
            "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
    },

    praepositionen_nomen: {
        isolation:
            "{explanation_french}",
        context:
            "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
    },

    konnektoren: {
        isolation:
            "{french} \u25CF {case_french} → {first_correct_answer_wiktionary}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers_wiktionary}",
        context:
            "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers_wiktionary}",
        synonym:
            "{french} = {correct_answers_wiktionary}",
        prompt:
            "{user_answer}"
            "<br><br><i>{translation}</i>"
            "<br><br>{explanation_english}"
            "{commentary}",
    },

    fragen: {
        isolation:
            "{french} = {first_correct_answer_wiktionary}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers_wiktionary}",
        context:
            "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers_wiktionary}",
        prompt:
            "{user_answer}"
            "<br><br><i>{translation}</i>"
            "<br><br>{explanation_english}"
            "{commentary}",
    },

    adverbien: {
        isolation:
            "{french} = {first_correct_answer_wiktionary}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers_wiktionary}",
        context:
            "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers_wiktionary}",
        synonym:
            "{french} = {first_correct_answer_wiktionary}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers_wiktionary}",
        antonym:
            "{german} ↔ {first_correct_answer_wiktionary}"
            "<br><br>{french}"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers_wiktionary}",
        prompt:
            "{user_answer}"
            "<br><br><i>{translation}</i>"
            "<br><br>{explanation_english}"
            "{commentary}",
    },

    verben: {
        isolation:
            "{french} = {correct_answer_wiktionary}",
        multiple_choice_native:
            "{german_wiktionary} = {correct_answer}",
        multiple_choice_target:
            "{french} = {correct_answer_wiktionary}",
    },

    nomen_verben_verbindungen: {
        isolation:
            "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        context:
            "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
    },

    adjektivdeklinationen: {
        isolation:
            "{german}"
            "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",
        context:
            "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",
    },
}

FEEDBACK_EXERCISE_FR = {
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

        41: "{french} \u25CF {gender_french} = {correct_answers}",
        42: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        43: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{person}, {gender_french}, {case_french} → {correct_answers}",
        44: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{person}, {gender_french}, {case_french} → {correct_answers}",

        45: "{german}, {gender_french}, {case_french} → {correct_answers}",
        46: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{gender_french}, {case_french} → {correct_answers}",
        47: "{german}, {gender_french}, {case_french} → {correct_answers}",
        48: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{gender_french}, {case_french} → {correct_answers}",
        49: "{german}, {gender_french}, {case_french} → {correct_answers}",
        50: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{gender_french}, {case_french} → {correct_answers}",
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

        40: "{french} \u25CF {case_french}, {gender_french} = {correct_answers}",
        41: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{person} \u25CF {case_french}, {gender_french} → {first_correct_answer}",
        31: "{german}, {gender_french}, {case_french} → {correct_answers}",
        32: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{gender_french}, {case_french} → {correct_answers}",
        33: "{german}, {gender_french}, {case_french} → {correct_answers}",
        34: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{gender_french}, {case_french} → {correct_answers}",
        39: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        42: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{person}, {case_french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        35: "{french} = {correct_answers}",
        36: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        37: "{french} = {correct_answers}",
        38: "{german}"
            "<br><br><i>{french}</i>"
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
           "<br><br>Règle : {explanation_french}",
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
        1: "{previous_question} → {first_correct_answer}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        2: "{previous_question} → {first_correct_answer}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        3: "{previous_question} → {first_correct_answer}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        4: "{previous_question} → {first_correct_answer}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        5: "{previous_question} → {first_correct_answer}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        6: "{previous_question} → {first_correct_answer}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        7: "{previous_question} → {first_correct_answer}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        8: "{previous_question} → {first_correct_answer}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        9: "{previous_question} → {first_correct_answer}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        10: "{previous_question} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        11: "{previous_question} → {first_correct_answer}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        12: "{previous_question} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        13: "{french} = {first_correct_answer}",
        14: "{french} = {first_correct_answer}",
        15: "{french} = {first_correct_answer}",
        16: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{case_french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        17: "{french} = {first_correct_answer}",
        18: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        19: "{french} = {first_correct_answer}",
        20: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        21: "{french} = {first_correct_answer}",
        22: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        23: "Génitif de {previous_question} : {first_correct_answer}",
        24: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
    },
}
