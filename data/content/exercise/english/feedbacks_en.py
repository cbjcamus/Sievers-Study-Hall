from data.data_processing.exercises import isolation, context, synonym, multiple_choice_native, multiple_choice_target, \
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
        "{german}"
        "<br><br><i>{english}</i>"
        "{indication_english}"
        "<br><br>{explanation_english}"
        "<br><br>Correct answer(s): {correct_answers_bullet_points}",

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
        "{root_english} → {root_german_wiktionary}"
        "<br><br>{english} → {correct_answer_wiktionary}",

    praesens:
        "{german_wiktionary} → {person} {first_correct_answer}"
        "<br><br>{german_wiktionary} = {english}"
        "<br><br>Correct answer(s): {correct_answers}",

    partizip_II:
        "Partizip II {german_wiktionary} → {first_correct_answer}"
        "<br><br>{explanation_english}"
        "<br><br>{german_wiktionary} = {english}"
        "<br><br>Correct answer(s): {correct_answers}",

    praeteritum:
        "{german_wiktionary} → {person} {first_correct_answer}"
        "<br><br>{explanation_english}"
        "<br><br>{german_wiktionary} = {english}"
        "<br><br>Correct answer: {correct_answers}",

    imperativ:
        "{german_wiktionary}, {person} → {first_correct_answer}"
        "<br><br>{german_wiktionary} = {english}"
        "<br><br>Correct answer(s): {correct_answers}",

    konjunktiv_II:
        "{german_wiktionary} → {person} {first_correct_answer}"
        "<br><br>{german_wiktionary} = {english}"
        "<br><br>Correct answer(s): {correct_answers}",

    konjunktiv_I:
        "{german_wiktionary} → {person} {first_correct_answer}"
        "<br><br>{german_wiktionary} = {english}"
        "<br><br>Correct answer(s): {correct_answers}",

    partizip_I:
        "Partizip I {german_wiktionary} → {first_correct_answer}"
        "<br><br>{german_wiktionary} = {english}"
        "<br><br>{first_correct_answer} = {explanation_english}"
        "<br><br>Correct answer(s): {correct_answers}",

    nomen_verben_wortstaemme:
        "{root_english} → {previous_question_wiktionary}"
        "<br><br>{english} → {first_correct_answer_wiktionary}"
        "<br><br>Correct answer(s): {correct_answers}",

    adjektive_verben_wortstaemme:
        "{root_english} → {previous_question_wiktionary}"
        "<br><br>{english} → {first_correct_answer_wiktionary}"
        "<br><br>Correct answer(s): {correct_answers}",

    adjektive_nomen_wortstaemme:
        "{root_english} → {previous_question_wiktionary}"
        "<br><br>{english} → {first_correct_answer_wiktionary}"
        "<br><br>Correct answer(s): {correct_answers}",

    genus:
        "{german}"
        "<br><br><i>{english}</i>"
        "{explanation_english}",

    plural:
        "{previous_question} → die {correct_answer}"
        "<br><br><i>{english}</i>",

    alpha:
        "{user_answer}"
        "<br><br><i>{translation}</i>"
        "<br><br>{explanation_english}"
        "{commentary}",
}

FEEDBACK_CATEGORY_EN = {

}

FEEDBACK_SUBCATEGORY_EN = {
    praepositionen: {
        context:
            "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        isolation:
            "{explanation_english}",
        synonym:
            "{english} = {correct_answers}",
        antonym:
            "{german} ↔ {first_correct_answer}"
            "<br><br>{english}"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
    },

    praepositionen_verben: {
        isolation:
            "{explanation_english}",
        context:
            "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
    },

    praepositionen_adjektive: {
        isolation:
            "{explanation_english}",
        context:
            "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
    },

    praepositionen_nomen: {
        isolation:
            "{explanation_english}",
        context:
            "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
    },

    konnektoren: {
        isolation:
            "{english} \u25CF {case_english} → {first_correct_answer_wiktionary}"
            "<br><br>Correct answer(s): {correct_answers_wiktionary}",
        context:
            "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers_wiktionary}",
        synonym:
            "{english} = {correct_answers_wiktionary}",
        prompt:
            "{user_answer}"
            "<br><br><i>{translation}</i>"
            "<br><br>{explanation_english}"
            "{commentary}",
    },

    fragen: {
        isolation:
            "{english} = {first_correct_answer_wiktionary}"
            "<br><br>Correct answer(s): {correct_answers_wiktionary}",
        context:
            "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers_wiktionary}",
        prompt:
            "{user_answer}"
            "<br><br><i>{translation}</i>"
            "<br><br>{explanation_english}"
            "{commentary}",
    },

    adverbien: {
        isolation:
            "{english} = {first_correct_answer_wiktionary}"
            "<br><br>Correct answer(s): {correct_answers_wiktionary}",
        context:
            "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers_wiktionary}",
        synonym:
            "{english} = {first_correct_answer_wiktionary}"
            "<br><br>Correct answer(s): {correct_answers_wiktionary}",
        antonym:
            "{german} ↔ {first_correct_answer_wiktionary}"
            "<br><br>{english}"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers_wiktionary}",
        prompt:
            "{user_answer}"
            "<br><br><i>{translation}</i>"
            "<br><br>{explanation_english}"
            "{commentary}",
    },

    verben: {
        isolation:
            "{english} = {correct_answer_wiktionary}",
        multiple_choice_native:
            "{german_wiktionary} = {correct_answer}",
        multiple_choice_target:
            "{english} = {correct_answer_wiktionary}",
    },

    nomen_verben_verbindungen: {
        isolation:
            "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        context:
            "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
    },

    adjektivdeklinationen: {
        isolation:
            "{german}"
            "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",
        context:
            "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{article_english}, {gender_english}, {case_english} → {correct_answers}",
    },
}

FEEDBACK_EXERCISE_EN = {
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

        41: "{english} \u25CF {gender_english} = {correct_answers}",
        42: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        43: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{person}, {gender_english}, {case_english} → {correct_answers}",
        44: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{person}, {gender_english}, {case_english} → {correct_answers}",

        45: "{german}, {gender_english}, {case_english} → {correct_answers}",
        46: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender_english}, {case_english} → {correct_answers}",
        47: "{german}, {gender_english}, {case_english} → {correct_answers}",
        48: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender_english}, {case_english} → {correct_answers}",
        49: "{german}, {gender_english}, {case_english} → {correct_answers}",
        50: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender_english}, {case_english} → {correct_answers}",
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

        31: "{english} \u25CF {case_english}, {gender_english} → {correct_answers}",
        32: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{person} \u25CF {case_english}, {gender_english} → {first_correct_answer}",
        33: "{german}, {gender_english}, {case_english} → {correct_answers}",
        34: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender_english}, {case_english} → {correct_answers}",
        35: "{german}, {gender_english}, {case_english} → {correct_answers}",
        36: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{gender_english}, {case_english} → {correct_answers}",
        37: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        38: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{person}, {case_english} → {first_correct_answer}"
            "<br><br>Correct answer(s): {correct_answers}",

        39: "{english} = {correct_answers}",
        40: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        41: "{english} = {correct_answers}",
        42: "{german}"
            "<br><br><i>{english}</i>"
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

        23: "Genitive of {previous_question}: {first_correct_answer}",
        24: "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
    },
}
