from data.data_processing.units import (
    praepositionen_grammatik, praepositionen_verben, praepositionen_adjektive, praepositionen_nomen,
    artikel, pronomen, konnektoren, fragen, adverbien,
    praesens, imperativ, partizip_II, praeteritum, praeteritum_partizip_II,  konjunktiv_II, konjunktiv_I, partizip_I,
    adjektive, adjektivdeklinationen,
    trennbare_verben, verben, deverbale_nomen
)

# bullet point \u25CF
# arrow &#8594

QUESTION = {

    praepositionen_grammatik: {
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
        10: "{question}",
        11: "{question}"
            "<br><br><i>{english}</i>",

        12: "{question}"
            "<br><br><i>{english}</i>",
        13: "{question}"
            "<br><br><i>{english}</i>",
        14: "{question}",
        15: "{question}"
            "<br><br><i>{english}</i>",

        16: "{question}",
        17: "{question}"
            "<br><br><i>{english}</i>",
        18: "{question}",
        19: "{question}"
            "<br><br><i>{english}</i>",
    },

    praepositionen_verben: {
        1: "{english} = {question}",
        2: "{question}"
           "<br><br><i>{english}</i>",
        3: "{english} = {question}",
        4: "{question}"
           "<br><br><i>{english}</i>",

        5: "{english} = {question}",
        6: "{question}"
           "<br><br><i>{english}</i>",
        7: "{english} = {question}",
        8: "{question}"
           "<br><br><i>{english}</i>",
        9: "{question}"
           "<br><br><i>{english}</i>",
        10: "{question}"
            "<br><br><i>{english}</i>",

        11: "{english} = {question}",
        12: "{question}"
            "<br><br><i>{english}</i>",
        13: "{english} = {question}",
        14: "{question}"
            "<br><br><i>{english}</i>",
        15: "{english} = {question}",
        16: "{question}"
            "<br><br><i>{english}</i>",
        17: "{english} = {question}",
        18: "{question}"
            "<br><br><i>{english}</i>",

        19: "{english} = {question}",
        20: "{question}"
            "<br><br><i>{english}</i>",
        21: "{english} = {question}",
        22: "{question}"
            "<br><br><i>{english}</i>",
        23: "{english} = {question}",
        24: "{question}"
            "<br><br><i>{english}</i>",
        25: "{english} = {question}",
        26: "{question}"
            "<br><br><i>{english}</i>",

        27: "{english} = {question}",
        28: "{question}"
            "<br><br><i>{english}</i>",
        29: "{english} = {question}",
        30: "{question}"
            "<br><br><i>{english}</i>",
        31: "{english} = {question}",
        32: "{question}"
            "<br><br><i>{english}</i>",
    },

    praepositionen_adjektive: {
        1: "{english} = {question}",
        2: "{question}"
           "<br><br><i>{english}</i>",

        3: "{english} = {question}",
        4: "{question}"
           "<br><br><i>{english}</i>",

        5: "{english} = {question}",
        6: "{question}"
           "<br><br><i>{english}</i>",
    },

    praepositionen_nomen: {
        1: "{question} = {german} _____",
        2: "{question}"
            "<br><br><i>{english}</i>",
        3: "{question} = {german} _____",
        4: "{question}"
           "<br><br><i>{english}</i>",

        5: "{question} = {german} _____",
        6: "{question}"
           "<br><br><i>{english}</i>",
        7: "{question} = {german} _____",
        8: "{question}"
           "<br><br><i>{english}</i>",
        9: "{question} = {german} _____",
        10: "{question}"
           "<br><br><i>{english}</i>",

        11: "{question} = {german} _____",
        12: "{question}"
           "<br><br><i>{english}</i>",
        13: "{question} = {german} _____",
        14: "{question}"
           "<br><br><i>{english}</i>",
        15: "{question} = {german} _____",
        16: "{question}"
            "<br><br><i>{english}</i>",
    },

    artikel: {
        1: "{question} \u25CF {gender}, {case}",
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
        11: "{question} \u25CF {gender}, {case}",
        12: "{question}"
           "<br><br><i>{english}</i>",
        13: "{question}"
           "<br><br><i>{english}</i>",
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
        19: "{question}"
            "<br><br><i>{english}</i>",
        20: "{question} \u25CF {gender}, {case}",
        21: "{question}"
            "<br><br><i>{english}</i>",
        22: "{question} \u25CF {gender}, {case}",
        23: "{question}"
            "<br><br><i>{english}</i>",
        24: "{question} \u25CF {gender}, {case}",
        25: "{question}"
            "<br><br><i>{english}</i>",

        26: "{question} \u25CF {gender}, {case}",
        27: "{question}"
            "<br><br><i>{english}</i>",
        28: "{question} \u25CF {gender}, {case}",
        29: "{question}"
            "<br><br><i>{english}</i>",
        30: "{question}"
            "<br><br><i>{english}</i>",
        31: "{question}"
            "<br><br><i>{english}</i>",
        32: "{question}",
        33: "{question}"
            "<br><br><i>{english}</i>",

        34: "{question} \u25CF {gender}, {case}",
        35: "{question}"
            "<br><br><i>{english}</i>",
        36: "{question} \u25CF {gender}, {case}",
        37: "{question}"
            "<br><br><i>{english}</i>",
        38: "{question} \u25CF {gender}, {case}",
        39: "{question}"
            "<br><br><i>{english}</i>",

        40: "{question} \u25CF {gender}, {case}",
        41: "{question}"
            "<br><br><i>{english}</i>",

        42: "{question} \u25CF {gender}, {case}",
        43: "{question}"
            "<br><br><i>{english}</i>",
    },

    pronomen: {
        1: "{question} \u25CF {person}",
        2: "{question} \u25CF {person}",
        3: "{question} \u25CF {person}",
        4: "{question} \u25CF {person}",

        5: "{question} \u25CF {person}",
        6: "{question} \u25CF {person}",
        7: "{question} \u25CF {person}",
        8: "{question} \u25CF {gender}, {case}",
        9: "{question}"
            "<br><br><i>{english}</i>",
        10: "{question} \u25CF {gender}, {case}",
        11: "{question}"
            "<br><br><i>{english}</i>",

        12: "{question}",
        13: "{question}"
           "<br><br><i>{english}</i>",
        14: "{question}",
        15: "{question}",
        16: "{question}",
        17: "{question}",
        18: "{question}",

        19: "{question}",
        20: "{question}",
    },

    konnektoren: {
        1: "{question} \u25CF {case}",
        2: "{question}"
           "<br><br><i>{english}</i>",

        3: "{question} \u25CF {case}",
        4: "{question}"
           "<br><br><i>{english}</i>",

        5: "{question} \u25CF {case}",
        6: "{question}"
           "<br><br><i>{english}</i>",
        7: "{question}",

        8: "{question} \u25CF {case}",
        9: "{question}"
           "<br><br><i>{english}</i>",
        10: "{question} \u25CF {case}",
        11: "{question}"
           "<br><br><i>{english}</i>",
        12: "{question}",

        13: "{question} \u25CF {case}",
        14: "{question}"
           "<br><br><i>{english}</i>",
        15: "{question}",
    },

    fragen: {
        1: "{question}",
        2: "{question}"
           "<br><br><i>{english}</i>",

        3: "{question}",
        4: "{question}"
           "<br><br><i>{english}</i>",

        5: "{question}",
        6: "{question}"
           "<br><br><i>{english}</i>",

        7: "{question}",
        8: "{question}"
           "<br><br><i>{english}</i>",
        9: "{question}",
        10: "{question}"
           "<br><br><i>{english}</i>",

        11: "{question}",
        12: "{question}"
            "<br><br><i>{english}</i>",
    },

    adverbien: {
        1: "{question}",
        2: "{question}"
           "<br><br><i>{english}</i>",
        3: "{question}",
        4: "{question}"
           "<br><br><i>{english}</i>",

        5: "{question}",
        6: "{question}"
           "<br><br><i>{english}</i>",
        7: "{question}",
        8: "{question}"
           "<br><br><i>{english}</i>",
        9: "{question}",
        10: "{question}"
            "<br><br><i>{english}</i>",

        11: "{question}",
        12: "{question}"
            "<br><br><i>{english}</i>",
        13: "{question}",
        14: "{question}"
            "<br><br><i>{english}</i>",
        15: "{question}",
        16: "{question}"
            "<br><br><i>{english}</i>",
        17: "{question}",
        18: "{question}"
            "<br><br><i>{english}</i>",
        19: "{question}",
        20: "{question}"
            "<br><br><i>{english}</i>",

        21: "{question}",
        22: "{question}"
            "<br><br><i>{english}</i>",
        23: "{question}",
        24: "{question}"
            "<br><br><i>{english}</i>",
        25: "{question}",
        26: "{question}"
            "<br><br><i>{english}</i>",
        27: "{question}",
        28: "{question}"
            "<br><br><i>{english}</i>",
        29: "{question}",
        30: "{question}"
            "<br><br><i>{english}</i>",
        31: "{question}",
        32: "{question}"
            "<br><br><i>{english}</i>",

        33: "{question}",
        34: "{question}"
            "<br><br><i>{english}</i>",
        35: "{question}",
        36: "{question}"
            "<br><br><i>{english}</i>",
        37: "{question}",
        38: "{question}"
            "<br><br><i>{english}</i>",
        39: "{question}",
        40: "{question}"
            "<br><br><i>{english}</i>",
        41: "{question}",
        42: "{question}"
            "<br><br><i>{english}</i>",
        43: "{question}",
        44: "{question}"
            "<br><br><i>{english}</i>",
    },

    praesens: {
        1: "{question} \u25CF {person} _____",
        2: "{question} \u25CF {person} _____",
        3: "{question} \u25CF {person} _____",
        4: "{question} \u25CF {person} _____",
        5: "{question} \u25CF {person} _____",
        6: "{question} \u25CF {person} _____",
        7: "{question} \u25CF {person} _____",
        8: "{question} \u25CF {person} _____",
        9: "{question} \u25CF {person} _____",
        10: "{question} \u25CF {person} _____",
        11: "{question} \u25CF {person} _____",
        12: "{question} \u25CF {person} _____",
        13: "{question} \u25CF {person} _____",
        14: "{question} \u25CF {person} _____",
        15: "{question} \u25CF {person} _____",
        16: "{question} \u25CF {person} _____",
        17: "{question} \u25CF {person} _____",
        18: "{question} \u25CF {person} _____",
        19: "{question} \u25CF {person} _____",
        20: "{question} \u25CF {person} _____",

        21: "{question} \u25CF {person} _____",
        22: "{question} \u25CF {person} _____",
        23: "{question} \u25CF {person} _____",
        24: "{question} \u25CF {person} _____",
        25: "{question} \u25CF {person} _____",
        26: "{question} \u25CF {person} _____",
        27: "{question} \u25CF {person} _____",
        28: "{question} \u25CF {person} _____",
        29: "{question} \u25CF {person} _____",
        30: "{question} \u25CF {person} _____",
        31: "{question} \u25CF {person} _____",
        32: "{question} \u25CF {person} _____",
        33: "{question} \u25CF {person} _____",
        34: "{question} \u25CF {person} _____",
        35: "{question} \u25CF {person} _____",
        36: "{question} \u25CF {person} _____",
        37: "{question} \u25CF {person} _____",
        38: "{question} \u25CF {person} _____",
        39: "{question} \u25CF {person} _____",
        40: "{question} \u25CF {person} _____",
    },

    partizip_II: {
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
        13: "{question}",
        14: "{question}",
        15: "{question}",
        16: "{question}",
        17: "{question}",
        18: "{question}",
        19: "{question}",
        20: "{question}",

        21: "{question}",
        22: "{question}",
        23: "{question}",
        24: "{question}",
        25: "{question}",
        26: "{question}",
        27: "{question}",
        28: "{question}",
        29: "{question}",
        30: "{question}",
    },

    praeteritum: {
        1: "{question} \u25CF {person} _____",

        2: "{question} \u25CF er/sie/es _____",
        3: "{question} \u25CF er/sie/es _____",
        4: "{question} \u25CF er/sie/es _____",
        5: "{question} \u25CF er/sie/es _____",
        6: "{question} \u25CF er/sie/es _____",
        7: "{question} \u25CF er/sie/es _____",
        8: "{question} \u25CF er/sie/es _____",
        9: "{question} \u25CF er/sie/es _____",
        10: "{question} \u25CF er/sie/es _____",
        11: "{question} \u25CF er/sie/es _____",

        12: "{question} \u25CF er/sie/es _____",
        13: "{question} \u25CF er/sie/es _____",
        14: "{question} \u25CF er/sie/es _____",
        15: "{question} \u25CF er/sie/es _____",
        16: "{question} \u25CF er/sie/es _____",
        17: "{question} \u25CF er/sie/es _____",
        18: "{question} \u25CF er/sie/es _____",
        19: "{question} \u25CF er/sie/es _____",
        20: "{question} \u25CF er/sie/es _____",
        21: "{question} \u25CF er/sie/es _____",

        22: "{question} \u25CF er/sie/es _____",
        23: "{question} \u25CF er/sie/es _____",
        24: "{question} \u25CF er/sie/es _____",
        25: "{question} \u25CF er/sie/es _____",
        26: "{question} \u25CF er/sie/es _____",
        27: "{question} \u25CF er/sie/es _____",
        28: "{question} \u25CF er/sie/es _____",
        29: "{question} \u25CF er/sie/es _____",
        30: "{question} \u25CF er/sie/es _____",
        31: "{question} \u25CF er/sie/es _____",
    },

    praeteritum_partizip_II: {
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
        13: "{question}",
        14: "{question}",
        15: "{question}",
        16: "{question}",
        17: "{question}",
        18: "{question}",
        19: "{question}",
        20: "{question}",
        21: "{question}",

        22: "{question}",
        23: "{question}",
        24: "{question}",
        25: "{question}",
        26: "{question}",
        27: "{question}",
        28: "{question}",
        29: "{question}",
        30: "{question}",
        31: "{question}",
    },

    imperativ: {
        1: "{question} \u25CF {person} \u25CF _____",
        2: "{question} \u25CF {person} \u25CF _____",
        3: "{question} \u25CF {person} \u25CF _____",
        4: "{question} \u25CF {person} \u25CF _____",
        5: "{question} \u25CF {person} \u25CF _____",
        6: "{question} \u25CF {person} \u25CF _____",

        7: "{question} \u25CF {person} \u25CF _____",
        8: "{question} \u25CF {person} \u25CF _____",
        9: "{question} \u25CF {person} \u25CF _____",
        10: "{question} \u25CF {person} \u25CF _____",
        11: "{question} \u25CF {person} \u25CF _____",
        12: "{question} \u25CF {person} \u25CF _____",
    },

    konjunktiv_II: {
        1: "{question} \u25CF {person} _____",
    },

    konjunktiv_I: {
        1: "{question} \u25CF {person} _____",
        2: "{question} \u25CF {person} _____",
        3: "{question} \u25CF {person} _____",
        4: "{question} \u25CF {person} _____",
        5: "{question} \u25CF {person} _____",
        6: "{question} \u25CF {person} _____",
    },

    partizip_I: {
        1: "{question}",
        2: "{question}",
        3: "{question}",
        4: "{question}",
        5: "{question}",
    },

    adjektive: {
        1: "{question}",
        2: "{question}",
        3: "{question}",
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
    },

    adjektivdeklinationen: {
        1: "{question} \u25CF {case} \u25CF {adjective}",
        2: "{question} \u25CF {adjective}",
        3: "{question} \u25CF {case} \u25CF {adjective}",
        4: "{question} \u25CF {adjective}",
        5: "{question} \u25CF {case} \u25CF {adjective}",
        6: "{question} \u25CF {adjective}",
        7: "{question} \u25CF {adjective}",
        8: "{question} \u25CF {adjective}",
        9: "{question} \u25CF {adjective}",
        10: "{question} \u25CF {adjective}",
        11: "{question} \u25CF {adjective}",
        12: "{question} \u25CF {adjective}",

        13: "{question} \u25CF {case} \u25CF {adjective}",
        14: "{question} \u25CF {adjective}",
        15: "{question} \u25CF {case} \u25CF {adjective}",
        16: "{question} \u25CF {adjective}",

        17: "{question} \u25CF {case} \u25CF {adjective}",
        18: "{question} \u25CF {adjective}",
        19: "{question} \u25CF {case} \u25CF {adjective}",
        20: "{question} \u25CF {adjective}",

        21: "{question} \u25CF {case} \u25CF {adjective}",
        22: "{question} \u25CF {adjective}",
        23: "{question} \u25CF {case} \u25CF {adjective}",
        24: "{question} \u25CF {adjective}",
    },

    trennbare_verben: {
        1: "{english} &#8594; {german}"
           "<br><br>{question} &#8594; _____ ",
        2: "{question} \u25CF {prefix}",
        3: "{question}",

        4: "{english} &#8594; {german}"
           "<br><br>{question} &#8594; _____ ",
        5: "{question} \u25CF {prefix}",
        6: "{question}",

        7: "{english} &#8594; {german}"
           "<br><br>{question} &#8594; _____ ",
        8: "{english} &#8594; {german}"
           "<br><br>{question} &#8594; _____ ",
        9: "{english} &#8594; {german}"
           "<br><br>{question} &#8594; _____ ",
        10: "{english} &#8594; {german}"
           "<br><br>{question} &#8594; _____ ",
        11: "{question} \u25CF {prefix}",
        12: "{question} \u25CF {prefix}",
        13: "{question} \u25CF {prefix}",
        14: "{question} \u25CF {prefix}",
        15: "{question}",
        16: "{question}",
        17: "{question}",
        18: "{question}",

        19: "{english} &#8594; {german}"
           "<br><br>{question} &#8594; _____ ",
        20: "{english} &#8594; {german}"
            "<br><br>{question} &#8594; _____ ",
        21: "{english} &#8594; {german}"
            "<br><br>{question} &#8594; _____ ",
        22: "{english} &#8594; {german}"
            "<br><br>{question} &#8594; _____ ",
        23: "{question} \u25CF {prefix}",
        24: "{question} \u25CF {prefix}",
        25: "{question} \u25CF {prefix}",
        26: "{question} \u25CF {prefix}",
        27: "{question}",
        28: "{question}",
        29: "{question}",
        30: "{question}",
    },

    verben: {
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
        13: "{question}",
        14: "{question}",
        15: "{question}",
        16: "{question}",
        17: "{question}",
        18: "{question}",
        19: "{question}",
        20: "{question}",

        21: "{question}",
        22: "{question}",
        23: "{question}",
        24: "{question}",
        25: "{question}",
        26: "{question}",
        27: "{question}",
        28: "{question}",
        29: "{question}",
        30: "{question}",
    },

    deverbale_nomen: {
        1: "{english} &#8594 {german}"
           "<br><br>{question} &#8594 _____",
        2: "{english} &#8594 {german}"
           "<br><br>{question} &#8594 _____",
        3: "{english} &#8594 {german}"
           "<br><br>{question} &#8594 _____",
        4: "{english} &#8594 {german}"
           "<br><br>{question} &#8594 _____",
        5: "{english} &#8594 {german}"
           "<br><br>{question} &#8594 _____",
        6: "{english} &#8594 {german}"
           "<br><br>{question} &#8594 _____",
        7: "{english} &#8594 {german}"
           "<br><br>{question} &#8594 _____",
        8: "{english} &#8594 {german}"
           "<br><br>{question} &#8594 _____",
        9: "{english} &#8594 {german}"
           "<br><br>{question} &#8594 _____",
        10: "{english} &#8594 {german}"
            "<br><br>{question} &#8594 _____",
        11: "{english} &#8594 {german}"
            "<br><br>{question} &#8594 _____",
        12: "{english} &#8594 {german}"
            "<br><br>{question} &#8594 _____",
        13: "{english} &#8594 {german}"
            "<br><br>{question} &#8594 _____",
        14: "{english} &#8594 {german}"
            "<br><br>{question} &#8594 _____",
        15: "{english} &#8594 {german}"
            "<br><br>{question} &#8594 _____",
        16: "{english} &#8594 {german}"
            "<br><br>{question} &#8594 _____",
    },

}
