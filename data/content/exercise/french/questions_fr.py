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

QUESTION_UNIT_FR = {
    pronominaladverbien:
        "{question}"
        "<br><br><i>{french}</i>",

    praepositionen_artikel:
        "{question} \u25CF {preposition} \u25CF {person}"
        "<br><br><i>{french}</i>",

    verben_artikel:
        "{question} \u25CF {person}"
        "<br><br><i>{french}</i>",

    wortstellung:
        "<i>{french}</i>"
        "{indication_french}",

    komparativ_superlativ:
        "{german}"
        "<br><br><i>{french}</i>",

    adjektive_konjunktionen:
        "{question}"
        "<br><br><i>{french}</i>",

    nomen_verben_verbindungen:
        "{question}"
        "<br><br><i>{french}</i>",

    praesens:
        "{german} \u25CF {person} _____"
        "<br><br><i>{french}</i>",

    partizip_II:
        "{german}"
        "<br><br><i>{french}</i>",

    praeteritum:
        "{german} \u25CF {person} _____"
        "<br><br><i>{french}</i>",

    imperativ:
        "{german} \u25CF {person} \u25CF _____"
        "<br><br><i>{french}</i>",

    konjunktiv_II:
        "{german} \u25CF {person} _____"
        "<br><br><i>{french}</i>",

    konjunktiv_I:
        "{german} \u25CF {person} _____"
        "<br><br><i>{french}</i>",

    partizip_I:
        "{german}"
        "<br><br><i>{french}</i>",

    adjektive_verben_wortstaemme:
        "{root_french} → {question}"
        "<br><br>{french} → _____",

    adjektive_nomen_wortstaemme:
        "{root_french} → {question}"
        "<br><br>{french} → _____",

    nomen_verben_wortstaemme:
        "{root_french} → {question}"
        "<br><br>{french} → _____",

    genus_regeln:
        "{question}"
        "<br><br><i>{french}</i>",

    genus:
        "{question}"
        "<br><br><i>{french}</i>",

    plural:
        "Singulier : {question}"
        "<br><br>Pluriel : die _____"
        "<br><br><i>{french}</i>",

    alpha:
        "{question}"
        "<br><br><i>{french} \u25CF {case_french}</i>",
}

QUESTION_SUBCATEGORY_FR = {
    praepositionen: {
        context:
            "{question}"
            "<br><br><i>{french}</i>",
        isolation:
            "{french}",
        synonym:
            "{question}"
            "<br><br><i>\"{german}\"</i>",
        antonym:
            "{german}",
    },

    praepositionen_verben: {
        isolation:
            "{french} = {question}",
        context:
            "{question}"
            "<br><br><i>{french}</i>",
    },

    praepositionen_adjektive: {
        isolation:
            "{french} = {question}",
        context:
            "{question}"
            "<br><br><i>{french}</i>",
    },

    praepositionen_nomen: {
        isolation:
            "{french} = {question}",
        context:
            "{question}"
            "<br><br><i>{french}</i>",
    },

    konnektoren: {
        isolation:
            "{french} \u25CF {case_french}",
        context:
            "{question}"
            "<br><br><i>{french}</i>",
        synonym:
            "{question}"
            "<br><br><i>\"{german}\"</i>",
        prompt:
            "{german}"
            "<br><br><i>{french} \u25CF {case_french}</i>",
    },

    fragen: {
        isolation:
            "{french}",
        context:
            "{question}"
            "<br><br><i>{french}</i>",
        prompt:
            "{german}"
            "<br><br><i>{french}</i>",
    },

    adverbien: {
        isolation:
            "{french}",
        context:
            "{question}"
            "<br><br><i>{french}</i>",
        synonym:
            "{question}"
            "<br><br><i>\"{german}\"</i>",
        antonym:
            "{german}",
        prompt:
            "{german}"
            "<br><br><i>{french}</i>",
    },

    adjektive: {
        isolation:
            "{french}",
        synonym:
            "{german}",
    },

    adjektivdeklinationen: {
        isolation:
            "{question} \u25CF {case_french} \u25CF {adjective}",
        context:
            "{question} \u25CF {adjective}"
            "<br><br><i>{french}</i>",
    },

    verben: {
        isolation:
            "{french}",
        multiple_choice_native:
            "{german}",
        multiple_choice_target:
            "{french}",
    },
}

QUESTION_CATEGORY_FR = {

}

QUESTION_EXERCISE_FR = {
    praepositionen: {
        1: "{question}"
           "<br><br><i>{french}</i>",
        2: "{question}"
           "<br><br><i>{french}</i>",
        3: "{question}"
           "<br><br><i>{french}</i>",
        4: "{question}"
           "<br><br><i>{french}</i>",
        5: "{question}"
           "<br><br><i>{french}</i>",

        6: "{question}"
           "<br><br><i>{french}</i>",
        7: "{question}"
           "<br><br><i>{french}</i>",
        8: "{question}"
           "<br><br><i>{french}</i>",
        9: "{question}"
           "<br><br><i>{french}</i>",
        10: "{question}"
           "<br><br><i>{french}</i>",

        11: "{question}"
           "<br><br><i>{french}</i>",
        12: "{question}"
            "<br><br><i>{french}</i>",
        13: "{french}",
        14: "{question}"
            "<br><br><i>{french}</i>",

        15: "{question}"
            "<br><br><i>{french}</i>",
        16: "{question}"
            "<br><br><i>{french}</i>",
        17: "{question}"
            "<br><br><i>{french}</i>",
        18: "{question}"
            "<br><br><i>{french}</i>",
        19: "{french}",
        20: "{question}"
            "<br><br><i>{french}</i>",

        21: "{question}"
            "<br><br><i>{french}</i>",
        22: "{question}"
            "<br><br><i>{french}</i>",
        23: "{question}"
            "<br><br><i>{french}</i>",
        24: "{question}"
            "<br><br><i>{french}</i>",
        25: "{french}",
        26: "{question}"
            "<br><br><i>{french}</i>",
        27: "{french}",
        28: "{question}"
            "<br><br><i>{french}</i>",
        29: "{question}"
            "<br><br><i>\"{german}\"</i>",
        30: "{german}",

        31: "{french}",
        32: "{question}"
            "<br><br><i>{french}</i>",
        33: "{french}",
        34: "{question}"
            "<br><br><i>{french}</i>",
    },

    artikel: {
        1: "{german} \u25CF {gender_french}, {case_french}",
        2: "{question}"
           "<br><br><i>{french}</i>",
        3: "{question}"
           "<br><br><i>{french}</i>",
        4: "{question}"
           "<br><br><i>{french}</i>",
        5: "{question}"
           "<br><br><i>{french}</i>",
        6: "{question}"
           "<br><br><i>{french}</i>",
        7: "{question}"
           "<br><br><i>{french}</i>",
        8: "{question}"
           "<br><br><i>{french}</i>",
        9: "{question}"
           "<br><br><i>{french}</i>",
        10: "{question}"
            "<br><br><i>{french}</i>",
        11: "{question}"
            "<br><br><i>{french}</i>",
        12: "{german} \u25CF {gender_french}, {case_french}",
        13: "{question}"
            "<br><br><i>{french}</i>",
        14: "{question}"
            "<br><br><i>{french}</i>",
        15: "{question}"
            "<br><br><i>{french}</i>",
        16: "{question}"
            "<br><br><i>{french}</i>",
        17: "{question}"
            "<br><br><i>{french}</i>",
        18: "{question}"
            "<br><br><i>{french}</i>",
        19: "{question}"
            "<br><br><i>{french}</i>",
        20: "{question}"
            "<br><br><i>{french}</i>",
        21: "{german} \u25CF {gender_french}, {case_french}",
        22: "{question}"
            "<br><br><i>{french}</i>",
        23: "{german} \u25CF {gender_french}, {case_french}",
        24: "{question}"
            "<br><br><i>{french}</i>",
        25: "{german} \u25CF {gender_french}, {case_french}",
        26: "{question}"
            "<br><br><i>{french}</i>",

        27: "{german} \u25CF {gender_french}, {case_french}",
        28: "{question}"
            "<br><br><i>{french}</i>",
        29: "{german} \u25CF {gender_french}, {case_french}",
        30: "{question}"
            "<br><br><i>{french}</i>",
        31: "{french}",
        32: "{question}"
            "<br><br><i>{french}</i>",

        33: "{german} \u25CF {gender_french}, {case_french}",
        34: "{question}"
            "<br><br><i>{french}</i>",
        35: "{german} \u25CF {gender_french}, {case_french}",
        36: "{question}"
            "<br><br><i>{french}</i>",
        37: "{german} \u25CF {gender_french}, {case_french}",
        38: "{question} \u25CF {person}" 
            "<br><br><i>{french}</i>",

        39: "{german} \u25CF {gender_french}, {case_french}",
        40: "{question}"
            "<br><br><i>{french}</i>",

        41: "{french} \u25CF {gender_french}",
        42: "{question}"
            "<br><br><i>{french}</i>",
        43: "{question}"
            "<br><br><i>{french}</i>"
            "<br><br>Article : {person}",
        44: "{question}"
            "<br><br><i>{french}</i>"
            "<br><br>Article : {person}",

        45: "{german} \u25CF {gender_french}, {case_french}",
        46: "{question}"
            "<br><br><i>{french}</i>",
        47: "{german} \u25CF {gender_french}, {case_french}",
        48: "{question}"
            "<br><br><i>{french}</i>",
        49: "{german} \u25CF {gender_french}, {case_french}",
        50: "{question}"
            "<br><br><i>{french}</i>",
    },

    pronomen: {
        1: "{french}",
        2: "{question}"
           "<br><br><i>{french}</i>",
        3: "{french}",
        4: "{question}"
           "<br><br><i>{french}</i>",
        5: "{french}",
        6: "{question}"
           "<br><br><i>{french}</i>",
        7: "{question}"
           "<br><br><i>{french}</i>",
        8: "{question}"
           "<br><br><i>{french}</i>",
        9: "{question} \u25CF {person}"
           "<br><br><i>{french}</i>",
        10: "{question} \u25CF {person}"
            "<br><br><i>{french}</i>",

        11: "{french} \u25CF {case_french}",
        12: "{question}"
            "<br><br><i>{french}</i>",
        13: "{question}"
            "<br><br><i>{french}</i>",
        14: "{question}"
            "<br><br><i>{french}</i>",

        15: "{french}",
        16: "{question}"
            "<br><br><i>{french}</i>",
        17: "{gender_french} \u25CF {case_french}",
        18: "{question}"
            "<br><br><i>{french}</i>",
        19: "{question}"
            "<br><br><i>{french}</i>",
        20: "{question}"
            "<br><br><i>{french}</i>",
        21: "{question}"
            "<br><br><i>{french}</i>",
        22: "{question}"
            "<br><br><i>{french}</i>",
        23: "{question}"
            "<br><br><i>{french}</i>",

        24: "{french}",
        25: "{question}"
            "<br><br><i>{french}</i>",
        26: "{french} \u25CF {case_french}",
        27: "{question}"
            "<br><br><i>{french}</i>",
        28: "{question}"
            "<br><br><i>{french}</i>",
        29: "{question}"
            "<br><br><i>{french}</i>",
        30: "{question}"
            "<br><br><i>{french}</i>",

        31: "{french} \u25CF {case_french}, {gender_french}",
        32: "{question}"
            "<br><br><i>{french}</i>",
        33: "{german} \u25CF {gender_french}, {case_french}",
        34: "{question}"
            "<br><br><i>{french}</i>",
        35: "{german} \u25CF {gender_french}, {case_french}",
        36: "{question}"
            "<br><br><i>{french}</i>",
        37: "{question}"
            "<br><br><i>{french}</i>",
        38: "{question}"
            "<br><br><i>{french}</i>",

        39: "{french}",
        40: "{question}"
            "<br><br><i>{french}</i>",
        41: "{french}",
        42: "{question}"
            "<br><br><i>{french}</i>",
    },

    trennbare_verben: {
        1: "{root_french} → {root_german}"
           "<br><br>{french} → _____",
        2: "{french} \u25CF {prefix}",
        3: "{french}",

        4: "{root_french} → {root_german}"
           "<br><br>{french} → _____",
        5: "{french} \u25CF {prefix}",
        6: "{french}",

        7: "{root_french} → {root_german}"
           "<br><br>{french} → _____",
        8: "{root_french} → {root_german}"
           "<br><br>{french} → _____",
        9: "{root_french} → {root_german}"
           "<br><br>{french} → _____",
        10: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        11: "{french} \u25CF {prefix}",
        12: "{french} \u25CF {prefix}",
        14: "{french} \u25CF {prefix}",
        13: "{french} \u25CF {prefix}",
        15: "{french}",
        16: "{french}",
        17: "{french}",
        18: "{french}",

        19: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        20: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        21: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        22: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        23: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        24: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        25: "{french} \u25CF {prefix}",
        26: "{french} \u25CF {prefix}",
        27: "{french} \u25CF {prefix}",
        28: "{french} \u25CF {prefix}",
        29: "{french} \u25CF {prefix}",
        30: "{french} \u25CF {prefix}",
        31: "{french}",
        32: "{french}",
        33: "{french}",
        34: "{french}",
        35: "{french}",
        36: "{french}",

        37: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        38: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        39: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        40: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        41: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        42: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        43: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        44: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        45: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        46: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        47: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        48: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        49: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        50: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        51: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        52: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        53: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        54: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        55: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        56: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        57: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        58: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        59: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        60: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        61: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        62: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        63: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        64: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        65: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        66: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        67: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        68: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        69: "{root_french} → {root_german}"
            "<br><br>{french} → _____",
        70: "{french} \u25CF {prefix}",
        71: "{french} \u25CF {prefix}",
        72: "{french} \u25CF {prefix}",
        73: "{french} \u25CF {prefix}",
        74: "{french} \u25CF {prefix}",
        75: "{french} \u25CF {prefix}",
        76: "{french} \u25CF {prefix}",
        77: "{french} \u25CF {prefix}",
        78: "{french} \u25CF {prefix}",
        79: "{french} \u25CF {prefix}",
        80: "{french} \u25CF {prefix}",
        81: "{french} \u25CF {prefix}",
        82: "{french} \u25CF {prefix}",
        83: "{french} \u25CF {prefix}",
        84: "{french} \u25CF {prefix}",
        85: "{french} \u25CF {prefix}",
        86: "{french} \u25CF {prefix}",
        87: "{french}",
        88: "{french}",
        89: "{french}",
        90: "{french}",
        91: "{french}",
        92: "{french}",
        93: "{french}",
        94: "{french}",
        95: "{french}",
        96: "{french}",
        97: "{french}",
        98: "{french}",
        99: "{french}",
        100: "{french}",
        101: "{french}",
        102: "{french}",
        103: "{french}",
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
        13: "{french}",
        14: "{french}",
        15: "{french}",
        16: "{question}"
            "<br><br><i>{french}</i>",

        17: "{french}",
        18: "{question}"
            "<br><br><i>{french}</i>",
        19: "{french}",
        20: "{question}"
            "<br><br><i>{french}</i>",

        21: "{french}",
        22: "{question}"
            "<br><br><i>{french}</i>",

        23: "{question}",
        24: "{question}"
            "<br><br><i>{french}</i>",
    },
}
