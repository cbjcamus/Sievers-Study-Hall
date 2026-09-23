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

QUESTION_UNIT_EN = {
    pronominaladverbien:
        "{question}"
        "<br><br><i>{english}</i>",

    praepositionen_artikel:
        "{question} \u25CF {preposition} \u25CF {person}"
        "<br><br><i>{english}</i>",

    verben_artikel:
        "{question} \u25CF {person}"
        "<br><br><i>{english}</i>",

    wortstellung:
        "<i>{english}</i>"
        "{indication_english}",

    komparativ_superlativ:
        "{german}"
        "<br><br><i>{english}</i>",

    adjektive_konjunktionen:
        "{question}"
        "<br><br><i>{english}</i>",

    nomen_verben_verbindungen:
        "{question}"
        "<br><br><i>{english}</i>",

    praesens:
        "{german} \u25CF {person} _____"
        "<br><br><i>{english}</i>",

    partizip_II:
        "{german}"
        "<br><br><i>{english}</i>",

    praeteritum:
        "{german} \u25CF {person} _____"
        "<br><br><i>{english}</i>",

    imperativ:
        "{german} \u25CF {person} \u25CF _____"
        "<br><br><i>{english}</i>",

    konjunktiv_II:
        "{german} \u25CF {person} _____"
        "<br><br><i>{english}</i>",

    konjunktiv_I:
        "{german} \u25CF {person} _____"
        "<br><br><i>{english}</i>",

    partizip_I:
        "{german}"
        "<br><br><i>{english}</i>",

    adjektive_verben_wortstaemme:
        "{root_english} → {question}"
        "<br><br>{english} → _____",

    adjektive_nomen_wortstaemme:
        "{root_english} → {question}"
        "<br><br>{english} → _____",

    nomen_verben_wortstaemme:
        "{root_english} → {question}"
        "<br><br>{english} → _____",

    genus_regeln:
        "{question}"
        "<br><br><i>{english}</i>",

    genus:
        "{question}"
        "<br><br><i>{english}</i>",

    plural:
        "Singular: {question}"
        "<br><br>Plural: die _____"
        "<br><br><i>{english}</i>",

    alpha:
        "{german}"
        "<br><br><i>{english} \u25CF {case_english}</i>",
}

QUESTION_SUBCATEGORY_EN = {
    praepositionen: {
        context:
            "{question}"
            "<br><br><i>{english}</i>",
        isolation:
            "{english}",
        synonym:
            "{question}"
            "<br><br><i>\"{german}\"</i>",
        antonym:
            "{german}",
    },

    praepositionen_verben: {
        isolation:
            "{english} = {question}",
        context:
            "{question}"
            "<br><br><i>{english}</i>",
    },

    praepositionen_adjektive: {
        isolation:
            "{english} = {question}",
        context:
            "{question}"
            "<br><br><i>{english}</i>",
    },

    praepositionen_nomen: {
        isolation:
            "{english} = {question}",
        context:
            "{question}"
            "<br><br><i>{english}</i>",
    },

    konnektoren: {
        isolation:
            "{english} \u25CF {case_english}",
        context:
            "{question}"
            "<br><br><i>{english}</i>",
        synonym:
            "{question}"
            "<br><br><i>\"{german}\"</i>",
        prompt:
            "{german}"
            "<br><br><i>{english} \u25CF {case_english}</i>",
    },

    fragen: {
        isolation:
            "{english}",
        context:
            "{question}"
            "<br><br><i>{english}</i>",
        prompt:
            "{german}"
            "<br><br><i>{english}</i>",
    },

    adverbien: {
        isolation:
            "{english}",
        context:
            "{question}"
            "<br><br><i>{english}</i>",
        synonym:
            "{question}"
            "<br><br><i>\"{german}\"</i>",
        antonym:
            "{german}",
        prompt:
            "{german}"
            "<br><br><i>{english}</i>",
    },

    adjektive: {
        isolation:
            "{english}",
        synonym:
            "{german}",
    },

    adjektivdeklinationen: {
        isolation:
            "{question} \u25CF {case_english} \u25CF {adjective}",
        context:
            "{question} \u25CF {adjective}"
            "<br><br><i>{english}</i>",
    },

    verben: {
        isolation:
            "{english}",
        multiple_choice_native:
            "{german}",
        multiple_choice_target:
            "{english}",
    },
}

QUESTION_CATEGORY_EN = {

}

QUESTION_EXERCISE_EN = {
    alpha: {
        1: "{german}"
           "<br><br><i>{english} \u25CF {case_english}</i>",
        2: "{german}"
           "<br><br><i>{english}</i>",
        3: "{german}"
           "<br><br><i>{english}</i>",
        4: "{german}"
           "<br><br><i>{english}</i>",

        5: "{german}"
           "<br><br><i>{english} \u25CF {case_english}</i>",
        6: "{german}"
           "<br><br><i>{english}</i>",
        7: "{german}"
           "<br><br><i>{english}</i>",
        8: "{german}"
           "<br><br><i>{english}</i>",
        9: "{german}"
           "<br><br><i>{english}</i>",
    },

    praepositionen: {
        1: "{question}"
           "<br><br><i>{english}</i>",
        2: "{question}"
           "<br><br><i>{english}</i>",
        3: "{question}"
           "<br><br><i>{english}</i>",
        4: "{question}"
           "<br><br><i>{english}</i>",
        5: "{question}"
           "<br><br><i>{english}</i>",

        6: "{question}"
           "<br><br><i>{english}</i>",
        7: "{question}"
           "<br><br><i>{english}</i>",
        8: "{question}"
           "<br><br><i>{english}</i>",
        9: "{question}"
           "<br><br><i>{english}</i>",
        10: "{question}"
           "<br><br><i>{english}</i>",

        11: "{question}"
           "<br><br><i>{english}</i>",
        12: "{question}"
            "<br><br><i>{english}</i>",
        13: "{english}",
        14: "{question}"
            "<br><br><i>{english}</i>",

        15: "{question}"
            "<br><br><i>{english}</i>",
        16: "{question}"
            "<br><br><i>{english}</i>",
        17: "{question}"
            "<br><br><i>{english}</i>",
        18: "{question}"
            "<br><br><i>{english}</i>",
        19: "{english}",
        20: "{question}"
            "<br><br><i>{english}</i>",

        21: "{question}"
            "<br><br><i>{english}</i>",
        22: "{question}"
            "<br><br><i>{english}</i>",
        23: "{question}"
            "<br><br><i>{english}</i>",
        24: "{question}"
            "<br><br><i>{english}</i>",
        25: "{english}",
        26: "{question}"
            "<br><br><i>{english}</i>",
        27: "{english}",
        28: "{question}"
            "<br><br><i>{english}</i>",
        29: "{question}"
            "<br><br><i>\"{german}\"</i>",
        30: "{german}",

        31: "{english}",
        32: "{question}"
            "<br><br><i>{english}</i>",
        33: "{english}",
        34: "{question}"
            "<br><br><i>{english}</i>",
    },

    artikel: {
        1: "{german} \u25CF {gender_english} \u25CF {case_english}",
        2: "{question} \u25CF {gender_english} \u25CF {case_english}"
           "<br><br><i>{english}</i>",
        3: "{question} \u25CF {gender_english} \u25CF {case_english}"
           "<br><br><i>{english}</i>",
        4: "{question} \u25CF {gender_english} \u25CF {case_english}"
           "<br><br><i>{english}</i>",
        5: "{question} \u25CF {gender_english} \u25CF {case_english}"
           "<br><br><i>{english}</i>",
        6: "{question} \u25CF {gender_english} \u25CF {case_english}"
           "<br><br><i>{english}</i>",
        7: "{question} \u25CF {gender_english} \u25CF {case_english}"
           "<br><br><i>{english}</i>",
        8: "{question} \u25CF {gender_english} \u25CF {case_english}"
           "<br><br><i>{english}</i>",
        9: "{question} \u25CF {gender_english} \u25CF {case_english}"
           "<br><br><i>{english}</i>",
        10: "{question} \u25CF {gender_english} \u25CF {case_english}"
            "<br><br><i>{english}</i>",
        11: "{question} \u25CF {gender_english} \u25CF {case_english}"
            "<br><br><i>{english}</i>",
        12: "{german} \u25CF {gender_english} \u25CF {case_english}",
        13: "{question} \u25CF {gender_english} \u25CF {case_english}"
            "<br><br><i>{english}</i>",
        14: "{question} \u25CF {gender_english} \u25CF {case_english}"
            "<br><br><i>{english}</i>",
        15: "{question} \u25CF {gender_english} \u25CF {case_english}"
            "<br><br><i>{english}</i>",
        16: "{question} \u25CF {gender_english} \u25CF {case_english}"
            "<br><br><i>{english}</i>",
        17: "{question} \u25CF {gender_english} \u25CF {case_english}"
            "<br><br><i>{english}</i>",
        18: "{question} \u25CF {gender_english} \u25CF {case_english}"
            "<br><br><i>{english}</i>",
        19: "{question} \u25CF {gender_english} \u25CF {case_english}"
            "<br><br><i>{english}</i>",
        20: "{question} \u25CF {gender_english} \u25CF {case_english}"
            "<br><br><i>{english}</i>",
        21: "{german} \u25CF {gender_english}, {case_english}",
        22: "{question}"
            "<br><br><i>{english}</i>",
        23: "{german} \u25CF {gender_english}, {case_english}",
        24: "{question}"
            "<br><br><i>{english}</i>",
        25: "{german} \u25CF {gender_english}, {case_english}",
        26: "{question}"
            "<br><br><i>{english}</i>",

        27: "{german} \u25CF {gender_english}, {case_english}",
        28: "{question}"
            "<br><br><i>{english}</i>",
        29: "{german} \u25CF {gender_english}, {case_english}",
        30: "{question}"
            "<br><br><i>{english}</i>",
        31: "{english}",
        32: "{question}"
            "<br><br><i>{english}</i>",

        33: "{german} \u25CF {gender_english}, {case_english}",
        34: "{question}"
            "<br><br><i>{english}</i>",
        35: "{german} \u25CF {gender_english}, {case_english}",
        36: "{question}"
            "<br><br><i>{english}</i>",
        37: "{german} \u25CF {gender_english}, {case_english}",
        38: "{question} \u25CF {person}" 
            "<br><br><i>{english}</i>",

        39: "{german} \u25CF {gender_english}, {case_english}",
        40: "{question}"
            "<br><br><i>{english}</i>",

        41: "{english} \u25CF {gender_english}",
        42: "{question}"
            "<br><br><i>{english}</i>",
        43: "{question}"
            "<br><br><i>{english}</i>"
            "<br><br>Article: {person}",
        44: "{question}"
            "<br><br><i>{english}</i>"
            "<br><br>Article: {person}",

        45: "{german} \u25CF {gender_english}, {case_english}",
        46: "{question}"
            "<br><br><i>{english}</i>",
        47: "{german} \u25CF {gender_english}, {case_english}",
        48: "{question}"
            "<br><br><i>{english}</i>",
        49: "{german} \u25CF {gender_english}, {case_english}",
        50: "{question}"
            "<br><br><i>{english}</i>",
    },

    pronomen: {
        1: "{english}",
        2: "{question}"
           "<br><br><i>{english}</i>",
        3: "{english}",
        4: "{question}"
           "<br><br><i>{english}</i>",
        5: "{english}",
        6: "{question}"
           "<br><br><i>{english}</i>",
        7: "{question}"
           "<br><br><i>{english}</i>",
        8: "{question}"
           "<br><br><i>{english}</i>",
        9: "{question} \u25CF {person}"
           "<br><br><i>{english}</i>",
        10: "{question} \u25CF {person}"
            "<br><br><i>{english}</i>",

        11: "{english} \u25CF {case_english}",
        12: "{question}"
            "<br><br><i>{english}</i>",
        13: "{question}"
            "<br><br><i>{english}</i>",
        14: "{question}"
            "<br><br><i>{english}</i>",

        15: "{english}",
        16: "{question}"
            "<br><br><i>{english}</i>",
        17: "{gender_english} \u25CF {case_english}",
        18: "{question}"
            "<br><br><i>{english}</i>",
        19: "{question}"
            "<br><br><i>{english}</i>",
        20: "{question}"
            "<br><br><i>{english}</i>",
        21: "{question}"
            "<br><br><i>{english}</i>",
        22: "{question}"
            "<br><br><i>{english}</i>",
        23: "{question}"
            "<br><br><i>{english}</i>",

        24: "{english}",
        25: "{question}"
            "<br><br><i>{english}</i>",
        26: "{english} \u25CF {case_english}",
        27: "{question}"
            "<br><br><i>{english}</i>",
        28: "{question}"
            "<br><br><i>{english}</i>",
        29: "{question}"
            "<br><br><i>{english}</i>",
        30: "{question}"
            "<br><br><i>{english}</i>",

        31: "{english} \u25CF {case_english}, {gender_english}",
        32: "{question}"
            "<br><br><i>{english}</i>",
        33: "{german} \u25CF {gender_english}, {case_english}",
        34: "{question}"
            "<br><br><i>{english}</i>",
        35: "{german} \u25CF {gender_english}, {case_english}",
        36: "{question}"
            "<br><br><i>{english}</i>",
        37: "{question}"
            "<br><br><i>{english}</i>",
        38: "{question}"
            "<br><br><i>{english}</i>",

        39: "{english}",
        40: "{question}"
            "<br><br><i>{english}</i>",
        41: "{english}",
        42: "{question}"
            "<br><br><i>{english}</i>",
    },

    trennbare_verben: {
        1: "{root_english} → {root_german}"
           "<br><br>{english} → _____",
        2: "{english} \u25CF {prefix}",
        3: "{english}",

        4: "{root_english} → {root_german}"
           "<br><br>{english} → _____",
        5: "{english} \u25CF {prefix}",
        6: "{english}",

        7: "{root_english} → {root_german}"
           "<br><br>{english} → _____",
        8: "{root_english} → {root_german}"
           "<br><br>{english} → _____",
        9: "{root_english} → {root_german}"
           "<br><br>{english} → _____",
        10: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        11: "{english} \u25CF {prefix}",
        12: "{english} \u25CF {prefix}",
        13: "{english} \u25CF {prefix}",
        14: "{english} \u25CF {prefix}",
        15: "{english}",
        16: "{english}",
        17: "{english}",
        18: "{english}",

        19: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        20: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        21: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        22: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        23: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        24: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        25: "{english} \u25CF {prefix}",
        26: "{english} \u25CF {prefix}",
        27: "{english} \u25CF {prefix}",
        28: "{english} \u25CF {prefix}",
        29: "{english} \u25CF {prefix}",
        30: "{english} \u25CF {prefix}",
        31: "{english}",
        32: "{english}",
        33: "{english}",
        34: "{english}",
        35: "{english}",
        36: "{english}",

        37: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        38: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        39: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        40: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        41: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        42: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        43: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        44: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        45: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        46: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        47: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        48: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        49: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        50: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        51: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        52: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        53: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        54: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        55: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        56: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        57: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        58: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        59: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        60: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        61: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        62: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        63: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        64: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        65: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        66: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        67: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        68: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        69: "{root_english} → {root_german}"
            "<br><br>{english} → _____",
        70: "{english} \u25CF {prefix}",
        71: "{english} \u25CF {prefix}",
        72: "{english} \u25CF {prefix}",
        73: "{english} \u25CF {prefix}",
        74: "{english} \u25CF {prefix}",
        75: "{english} \u25CF {prefix}",
        76: "{english} \u25CF {prefix}",
        77: "{english} \u25CF {prefix}",
        78: "{english} \u25CF {prefix}",
        79: "{english} \u25CF {prefix}",
        80: "{english} \u25CF {prefix}",
        81: "{english} \u25CF {prefix}",
        82: "{english} \u25CF {prefix}",
        83: "{english} \u25CF {prefix}",
        84: "{english} \u25CF {prefix}",
        85: "{english} \u25CF {prefix}",
        86: "{english} \u25CF {prefix}",
        87: "{english}",
        88: "{english}",
        89: "{english}",
        90: "{english}",
        91: "{english}",
        92: "{english}",
        93: "{english}",
        94: "{english}",
        95: "{english}",
        96: "{english}",
        97: "{english}",
        98: "{english}",
        99: "{english}",
        100: "{english}",
        101: "{english}",
        102: "{english}",
        103: "{english}",
    },

    zahlen: {
        1: "{question}",
        2: "{question}",
        3: "{question}",
        4: "{question}",
        5: "{question}",
        6: "{question}",
        7: "{question}",
        8: "{question}",
        9: "{question}",
        10: "{question}",

        11: "{question}",
        12: "{question}",
        13: "{english}",
        14: "{english}",
        15: "{english}",
        16: "{question}"
            "<br><br><i>{english}</i>",

        17: "{english}",
        18: "{question}"
            "<br><br><i>{english}</i>",
        19: "{english}",
        20: "{question}"
            "<br><br><i>{english}</i>",

        21: "{english}",
        22: "{question}"
            "<br><br><i>{english}</i>",

        23: "{question}",
        24: "{question}"
            "<br><br><i>{english}</i>",
    },

}
