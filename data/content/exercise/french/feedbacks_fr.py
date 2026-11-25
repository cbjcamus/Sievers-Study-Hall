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

FEEDBACK_UNIT_FR = {
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

    partizip_II:
        "Partizip II {german_wiktionary} → {first_correct_answer}"
        "<br><br>{explanation_french}"
        "<br><br>{german_wiktionary} = {french}"
        "<br><br>Réponse(s) correcte(s) : {correct_answers}",

    perfekt:
        "{user_answer}"
        "<br><br><i>{translation}</i>"
        "<br><br>{explanation_french}"
        "<br><br>{cefr_level}"
        "{commentary}",

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

    genus_regeln:
        "{german}"
        "<br><br><i>{french}</i>"
        "<br><br>{explanation_french}",

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
            "<br><br>Réponse(s) correcte(s) : {correct_answer_praepositionen}",
        isolation:
            "{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answer_praepositionen}",
        synonym:
            "{french} = {correct_answers}",
        antonym:
            "{german} ↔ {first_correct_answer}"
            "<br><br>{french}"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        prompt:
            "{user_answer}"
            "<br><br><i>{translation}</i>"
            "<br><br>{explanation_french}"
            "<br><br>{cefr_level}"
            "{commentary}",
    },

    praepositionen_verben: {
        isolation:
            "{explanation_french}",
        context:
            "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        prompt:
            "{user_answer}"
            "<br><br><i>{translation}</i>"
            "<br><br>{explanation_french}"
            "<br><br>{cefr_level}"
            "{commentary}",
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

    pronominaladverbien: {
        context:
            "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}"
            "<br><br>{explanation_french}",
        prompt:
            "{user_answer}"
            "<br><br><i>{translation}</i>"
            "<br><br>{cefr_level}"
            "{commentary}",
    },

    artikel: {
        isolation:
            "{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        context:
            "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{gender_french}, {case_french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        prompt:
            "{user_answer}"
            "<br><br><i>{translation}</i>"
            "<br><br>{explanation_french}"
            "<br><br>{cefr_level}"
            "{commentary}",
    },

    pronomen: {
        isolation:
            "{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        context:
            "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        prompt:
            "{user_answer}"
            "<br><br><i>{translation}</i>"
            "<br><br>{explanation_french}"
            "<br><br>{cefr_level}"
            "{commentary}",
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
            "<br><br>{explanation_french}"
            "<br><br>{cefr_level}"
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
            "<br><br>{explanation_french}"
            "<br><br>{cefr_level}"
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
            "<br><br>{explanation_french}"
            "<br><br>{cefr_level}"
            "{commentary}",
    },

    verben: {
        isolation:
            "{french} = {first_correct_answer_wiktionary}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers_wiktionary}",
        prompt:
            "{user_answer}"
            "<br><br><i>{translation}</i>"
            "<br><br>{explanation_french}"
            "<br><br>{cefr_level}"
            "{commentary}",
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
        prompt:
            "{user_answer}"
            "<br><br><i>{translation}</i>"
            "<br><br>{explanation_french}"
            "<br><br>{cefr_level}"
            "{commentary}",
    },

    adjektive: {
        isolation:
            "{french} = {correct_answers}"
            "{explanation_french}",
        prompt:
            "{user_answer}"
            "<br><br><i>{translation}</i>"
            "<br><br>{explanation_french}"
            "<br><br>{cefr_level}"
            "{commentary}",
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

    praesens: {
        isolation:
            "{german_wiktionary} → {person} {first_correct_answer}"
            "<br><br>{german_wiktionary} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        prompt:
            "{user_answer}"
            "<br><br><i>{translation}</i>"
            "<br><br>{explanation_french}"
            "<br><br>{cefr_level}"
            "{commentary}",
    },

    praeteritum: {
        isolation:
            "{german_wiktionary} → {person} {first_correct_answer}"
            "<br><br>{explanation_french}"
            "<br><br>{german_wiktionary} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        prompt:
            "{user_answer}"
            "<br><br><i>{translation}</i>"
            "<br><br>{explanation_french}"
            "<br><br>{cefr_level}"
            "{commentary}",
    },
}

FEEDBACK_EXERCISE_FR = {
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
