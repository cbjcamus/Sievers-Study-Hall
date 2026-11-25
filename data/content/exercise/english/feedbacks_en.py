from data.data_processing.exercises import isolation, context, synonym, antonym, prompt
from data.data_processing.units import (
    praepositionen, praepositionen_verben, praepositionen_adjektive, praepositionen_nomen, pronominaladverbien,
    artikel, pronomen, praepositionen_artikel, verben_artikel,
    konnektoren, fragen, adverbien, wortstellung,
    genus_regeln, genus, plural,
    adjektive, komparativ_superlativ, adjektivdeklinationen, adjektive_konjunktionen,
    verben, trennbare_verben, nomen_verben_verbindungen,
    praesens, imperativ, partizip_II, praeteritum, perfekt, konjunktiv_II, konjunktiv_I, partizip_I,
    nomen_verben_wortstaemme, adjektive_verben_wortstaemme, adjektive_nomen_wortstaemme,
    zahlen, alpha,
)

FEEDBACK_UNIT_EN = {
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

    perfekt:
        "{user_answer}"
        "<br><br><i>{translation}</i>"
        "<br><br>{explanation_english}"
        "<br><br>{cefr_level}"
        "{commentary}",

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

    genus_regeln:
        "{german}"
        "<br><br><i>{english}</i>"
        "<br><br>{explanation_english}",

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
            "<br><br>Correct answer(s): {correct_answer_praepositionen}",
        isolation:
            "{explanation_english}"
            "<br><br>Correct answer(s): {correct_answer_praepositionen}",
        prompt:
            "{user_answer}"
            "<br><br><i>{translation}</i>"
            "<br><br>{explanation_english}"
            "<br><br>{cefr_level}"
            "{commentary}",
        synonym:
            "{english} = {list_of_synonyms}"
            "<br><br>Correct answer(s): {correct_answers}",
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
        prompt:
            "{user_answer}"
            "<br><br><i>{translation}</i>"
            "<br><br>{explanation_english}"
            "<br><br>{cefr_level}"
            "{commentary}",
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

    pronominaladverbien: {
        context:
            "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>Correct answer(s): {correct_answers}"
            "<br><br>{explanation_english}",
        prompt:
            "{user_answer}"
            "<br><br><i>{translation}</i>"
            "<br><br>{cefr_level}"
            "{commentary}",
    },

    artikel: {
        isolation:
            "{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        context:
            "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        prompt:
            "{user_answer}"
            "<br><br><i>{translation}</i>"
            "<br><br>{explanation_english}"
            "<br><br>{cefr_level}"
            "{commentary}",
    },

    pronomen: {
        isolation:
            "{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        context:
            "{german}"
            "<br><br><i>{english}</i>"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers}",
        prompt:
            "{user_answer}"
            "<br><br><i>{translation}</i>"
            "<br><br>{explanation_english}"
            "<br><br>{cefr_level}"
            "{commentary}",
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
        prompt:
            "{user_answer}"
            "<br><br><i>{translation}</i>"
            "<br><br>{explanation_english}"
            "<br><br>{cefr_level}"
            "{commentary}",
        synonym:
            "{english} = {list_of_synonyms_wiktionary}"
            "<br><br>Correct answer(s): {correct_answers_wiktionary}",
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
            "<br><br>{cefr_level}"
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
        prompt:
            "{user_answer}"
            "<br><br><i>{translation}</i>"
            "<br><br>{explanation_english}"
            "<br><br>{cefr_level}"
            "{commentary}",
        synonym:
            "{english} = {list_of_synonyms_wiktionary}"
            "<br><br>Correct answer(s): {correct_answers_wiktionary}",
        antonym:
            "{german} ↔ {first_correct_answer_wiktionary}"
            "<br><br>{english}"
            "<br><br>{explanation_english}"
            "<br><br>Correct answer(s): {correct_answers_wiktionary}",
    },

    verben: {
        isolation:
            "{english} = {first_correct_answer_wiktionary}"
            "<br><br>Correct answer(s): {correct_answers_wiktionary}",
        prompt:
            "{user_answer}"
            "<br><br><i>{translation}</i>"
            "<br><br>{explanation_english}"
            "<br><br>{cefr_level}"
            "{commentary}",
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
        prompt:
            "{user_answer}"
            "<br><br><i>{translation}</i>"
            "<br><br>{explanation_english}"
            "<br><br>{cefr_level}"
            "{commentary}",
    },

    adjektive: {
        isolation:
            "{english} = {correct_answers}"
            "{explanation_english}",
        prompt:
            "{user_answer}"
            "<br><br><i>{translation}</i>"
            "<br><br>{explanation_english}"
            "<br><br>{cefr_level}"
            "{commentary}",
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

    praesens: {
        isolation:
            "{german_wiktionary} → {person} {first_correct_answer}"
            "<br><br>{german_wiktionary} = {english}"
            "<br><br>Correct answer(s): {correct_answers}",
        prompt:
            "{user_answer}"
            "<br><br><i>{translation}</i>"
            "<br><br>{explanation_english}"
            "<br><br>{cefr_level}"
            "{commentary}",
    },

    praeteritum: {
        isolation:
            "{german_wiktionary} → {person} {first_correct_answer}"
            "<br><br>{explanation_english}"
            "<br><br>{german_wiktionary} = {english}"
            "<br><br>Correct answer: {correct_answers}",
        prompt:
            "{user_answer}"
            "<br><br><i>{translation}</i>"
            "<br><br>{explanation_english}"
            "<br><br>{cefr_level}"
            "{commentary}",
    },

}

FEEDBACK_EXERCISE_EN = {
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
