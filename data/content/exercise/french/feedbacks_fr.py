from data.data_processing.units import (
    praepositionen, praepositionen_verben, praepositionen_adjektive, praepositionen_nomen, pronominaladverbien,
    artikel, pronomen, praepositionen_artikel, verben_artikel,
    konnektoren, fragen, adverbien, wortstellung,
    genus_regeln, genus, plural,
    adjektive, komparativ_superlativ, adjektivdeklinationen, adjektive_konjunktionen,
    verben, trennbare_verben, nomen_verben_verbindungen,
    praesens, imperativ, partizip_II, praeteritum, praeteritum_partizip_II, konjunktiv_II, konjunktiv_I, partizip_I,
    nomen_verben_wortstaemme, adjektive_verben_wortstaemme, adjektive_nomen_wortstaemme,
    zahlen,
)

FEEDBACK_FR = {

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

    pronominaladverbien: {
        1: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}"
           "<br><br>{explanation_french}",

        2: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}"
           "<br><br>{explanation_french}",
        3: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}"
           "<br><br>{explanation_french}",
        4: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}"
           "<br><br>{explanation_french}",

        5: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}"
           "<br><br>{explanation_french}",
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
        11: "{german}, {gender_french}, {case_french} → {correct_answers}",
        12: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{gender_french}, {case_french} → {correct_answers}",
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
        20: "{german}, {gender_french}, {case_french} → {correct_answers}",
        21: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{gender_french}, {case_french} → {correct_answers}",
        22: "{german}, {gender_french}, {case_french} → {correct_answers}",
        23: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{gender_french}, {case_french} → {correct_answers}",
        24: "{german}, {gender_french}, {case_french} → {correct_answers}",
        25: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{gender_french}, {case_french} → {correct_answers}",

        26: "{german}, {gender_french}, {case_french} → {correct_answers}",
        27: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{gender_french}, {case_french} → {correct_answers}",
        28: "{german}, {gender_french}, {case_french} → {correct_answers}",
        29: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{gender_french}, {case_french} → {correct_answers}",
        30: "{french} = {correct_answers}",
        31: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        32: "{german}, {gender_french}, {case_french} → {correct_answers}",
        33: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{gender_french}, {case_french} → {correct_answers}",
        34: "{gender_french}, {case_french} → {correct_answers}",
        35: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{gender_french}, {case_french} → {correct_answers}",
        36: "{german}, {gender_french}, {case_french} → {correct_answers}",
        37: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{person}, {gender_french}, {case_french} → {correct_answers}",

        38: "{german}, {gender_french}, {case_french} → {correct_answers}",
        39: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{gender_french}, {case_french} → {correct_answers}",

        40: "{german}, {gender_french}, {case_french} → {correct_answers}",
        41: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{gender_french}, {case_french} → {correct_answers}",
        42: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{person}, {gender_french}, {case_french} → {correct_answers}",
        43: "{german}"
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

    praepositionen_artikel: {
        1: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{person}, {gender_french}{case_french} → {article}"
           "<br><br>{explanation_french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        2: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{person}, {gender_french}{case_french} → {article}"
           "<br><br>{explanation_french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        3: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{person}, {gender_french}{case_french} → {article}"
           "<br><br>{explanation_french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        4: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{person}, {gender_french}{case_french} → {article}"
           "<br><br>{explanation_french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        5: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{person}, {gender_french}{case_french} → {article}"
           "<br><br>{explanation_french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        6: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{person}, {gender_french}{case_french} → {article}"
           "<br><br>{explanation_french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        7: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{person}, {gender_french}{case_french} → {article}"
           "<br><br>{explanation_french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        8: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{person}, {gender_french}{case_french} → {article}"
           "<br><br>{explanation_french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        9: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{person}, {gender_french}{case_french} → {article}"
           "<br><br>{explanation_french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        10: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{person}, {gender_french}{case_french} → {article}"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        11: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{person}, {gender_french}{case_french} → {article}"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        12: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{person}, {gender_french}{case_french} → {article}"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        13: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{person}, {gender_french}{case_french} → {article}"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        14: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{person}, {gender_french}{case_french} → {article}"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        15: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{person}, {gender_french}{case_french} → {article}"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        16: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{person}, {gender_french}{case_french} → {article}"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        17: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{person}, {gender_french}{case_french} → {article}"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        18: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{person}, {gender_french}{case_french} → {article}"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        19: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{person}, {gender_french}{case_french} → {article}"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        20: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{person}, {gender_french}{case_french} → {article}"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        21: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{person}, {gender_french}{case_french} → {article}"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        22: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{person}, {gender_french}{case_french} → {article}"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        23: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{person}, {gender_french}{case_french} → {article}"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        24: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{person}, {gender_french}{case_french} → {article}"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        25: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{person}, {gender_french}{case_french} → {article}"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        26: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{person}, {gender_french}{case_french} → {article}"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        27: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{person}, {gender_french}{case_french} → {article}"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        28: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{person}, {gender_french}{case_french} → {article}"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        29: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{person}, {gender_french}{case_french} → {article}"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        30: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{person}, {gender_french}{case_french} → {article}"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        31: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{person}, {gender_french}{case_french} → {article}"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        32: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{person}, {gender_french}{case_french} → {article}"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        33: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{person}, {gender_french}{case_french} → {article}"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        34: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{person}, {gender_french}{case_french} → {article}"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        35: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{person}, {gender_french}{case_french} → {article}"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        36: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{person}, {gender_french}{case_french} → {article}"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
    },

    verben_artikel: {
        1: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{explanation_french}"
           "<br><br>Correct answer(s): {correct_answers}",
        2: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{explanation_french}"
           "<br><br>Correct answer(s): {correct_answers}",
        3: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{explanation_french}"
           "<br><br>Correct answer(s): {correct_answers}",

        4: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{explanation_french}"
           "<br><br>Correct answer(s): {correct_answers}",
        5: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{explanation_french}"
           "<br><br>Correct answer(s): {correct_answers}",
        6: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{explanation_french}"
           "<br><br>Correct answer(s): {correct_answers}",

        7: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{explanation_french}"
           "<br><br>Correct answer(s): {correct_answers}",
        8: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{explanation_french}"
           "<br><br>Correct answer(s): {correct_answers}",
        9: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{explanation_french}"
           "<br><br>Correct answer(s): {correct_answers}",
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
        10: "{german}"
            "<br><br><i>{french}</i>"
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

    adjektive: {
        1: "{french} = {correct_answers}"
           "{explanation_french}",
        2: "{french} = {correct_answers}"
           "{explanation_french}",
        3: "{french} = {correct_answers}"
           "{explanation_french}",

        4: "{french} = {correct_answers}"
           "{explanation_french}",
        5: "{french} = {correct_answers}"
           "{explanation_french}",
        6: "{french} = {correct_answers}"
           "{explanation_french}",

        7: "{french} = {correct_answers}"
           "{explanation_french}",
        8: "{french} = {correct_answers}"
           "{explanation_french}",
        9: "{french} = {correct_answers}"
           "{explanation_french}",
        10: "{french} = {correct_answers}"
            "{explanation_french}",
        11: "{french} = {correct_answers}"
            "{explanation_french}",
        12: "{french} = {correct_answers}"
            "{explanation_french}",

        13: "{french} = {correct_answers}"
            "{explanation_french}",
        14: "{french} = {correct_answers}"
            "{explanation_french}",
        15: "{french} = {correct_answers}"
            "{explanation_french}",
        16: "{french} = {correct_answers}"
            "{explanation_french}",
        17: "{french} = {correct_answers}"
            "{explanation_french}",
        18: "{french} = {correct_answers}"
            "{explanation_french}",
        19: "{french} = {correct_answers}"
            "{explanation_french}",
        20: "{french} = {correct_answers}"
            "{explanation_french}",
        21: "{french} = {correct_answers}"
            "{explanation_french}",
        22: "{french} = {correct_answers}"
            "{explanation_french}",
        23: "{french} = {correct_answers}"
            "{explanation_french}",
        24: "{french} = {correct_answers}"
            "{explanation_french}",
    },

    komparativ_superlativ: {
        1: "{explanation_french}"
           "<br><br><i>{french}</i>"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        2: "{explanation_french}"
           "<br><br><i>{french}</i>"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        3: "{explanation_french}"
           "<br><br><i>{french}</i>"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        4: "{explanation_french}"
           "<br><br><i>{french}</i>"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        5: "{explanation_french}"
           "<br><br><i>{french}</i>"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        6: "{explanation_french}"
           "<br><br><i>{french}</i>"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        7: "{explanation_french}"
           "<br><br><i>{french}</i>"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        8: "{explanation_french}"
           "<br><br><i>{french}</i>"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        9: "{explanation_french}"
           "<br><br><i>{french}</i>"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        10: "{explanation_french}"
            "<br><br><i>{french}</i>"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        11: "{explanation_french}"
            "<br><br><i>{french}</i>"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        12: "{explanation_french}"
            "<br><br><i>{french}</i>"
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
    },

    adjektive_konjunktionen: {
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

    trennbare_verben: {
        1: "{root_french} → {root_german}"
           "<br><br>{french} → {correct_answers}",
        2: "{root_french} → {root_german}"
           "<br><br>{french} → {correct_answers}",
        3: "{root_french} → {root_german}"
           "<br><br>{french} → {correct_answers}",

        4: "{root_french} → {root_german}"
           "<br><br>{french} → {correct_answers}",
        5: "{root_french} → {root_german}"
           "<br><br>{french} → {correct_answers}",
        6: "{root_french} → {root_german}"
           "<br><br>{french} → {correct_answers}",

        7: "{root_french} → {root_german}"
           "<br><br>{french} → {correct_answers}",
        8: "{root_french} → {root_german}"
           "<br><br>{french} → {correct_answers}",
        9: "{root_french} → {root_german}"
           "<br><br>{french} → {correct_answers}",
        10: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",
        11: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",
        12: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",
        13: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",
        14: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",
        15: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",
        16: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",
        17: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",
        18: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",

        19: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",
        20: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",
        21: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",
        22: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",
        23: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",
        24: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",
        25: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",
        26: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",
        27: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",
        28: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",
        29: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",
        30: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",

        31: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",
        32: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",
        33: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",
        34: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",
        35: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",
        36: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",
        37: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",
        38: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",
        39: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",
        40: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",
        41: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",
        42: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",
        43: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",
        44: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",
        45: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",
        46: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",
        47: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",
        48: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",
        49: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",
        50: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",
        51: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",
        52: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",
        53: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",
        54: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",
        55: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",
        56: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",
        57: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",
        58: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",
        59: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",
        60: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",
        61: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",
        62: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",
        63: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",
        64: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",
        65: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",
        66: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",
        67: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",
        68: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",
        69: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",
        70: "{root_french} → {root_german}"
            "<br><br>{french} → {correct_answers}",
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

    praesens: {
        1: "{german} → {person} {first_correct_answer}"
           "<br><br>{german} = {french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        2: "{german} → {person} {first_correct_answer}"
           "<br><br>{german} = {french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        3: "{german} → {person} {first_correct_answer}"
           "<br><br>{german} = {french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        4: "{german} → {person} {first_correct_answer}"
           "<br><br>{german} = {french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        5: "{german} → {person} {first_correct_answer}"
           "<br><br>{german} = {french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        6: "{german} → {person} {first_correct_answer}"
           "<br><br>{german} = {french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        7: "{german} → {person} {first_correct_answer}"
           "<br><br>{german} = {french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        8: "{german} → {person} {first_correct_answer}"
           "<br><br>{german} = {french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        9: "{german} → {person} {first_correct_answer}"
           "<br><br>{german} = {french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        10: "{german} → {person} {first_correct_answer}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        11: "{german} → {person} {first_correct_answer}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        12: "{german} → {person} {first_correct_answer}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        13: "{german} → {person} {first_correct_answer}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        14: "{german} → {person} {first_correct_answer}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        15: "{german} → {person} {first_correct_answer}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        16: "{german} → {person} {first_correct_answer}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        17: "{german} → {person} {first_correct_answer}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        18: "{german} → {person} {first_correct_answer}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        19: "{german} → {person} {first_correct_answer}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        20: "{german} → {person} {first_correct_answer}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        21: "{german} → {person} {first_correct_answer}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        22: "{german} → {person} {first_correct_answer}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        23: "{german} → {person} {first_correct_answer}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        24: "{german} → {person} {first_correct_answer}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        25: "{german} → {person} {first_correct_answer}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        26: "{german} → {person} {first_correct_answer}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        27: "{german} → {person} {first_correct_answer}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        28: "{german} → {person} {first_correct_answer}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        29: "{german} → {person} {first_correct_answer}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        30: "{german} → {person} {first_correct_answer}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        31: "{german} → {person} {first_correct_answer}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        32: "{german} → {person} {first_correct_answer}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        33: "{german} → {person} {first_correct_answer}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        34: "{german} → {person} {first_correct_answer}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        35: "{german} → {person} {first_correct_answer}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        36: "{german} → {person} {first_correct_answer}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        37: "{german} → {person} {first_correct_answer}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        38: "{german} → {person} {first_correct_answer}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        39: "{german} → {person} {first_correct_answer}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        40: "{german} → {person} {first_correct_answer}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
    },

    partizip_II: {
        1: "Partizip II {german} → {first_correct_answer}"
           "<br><br>{explanation_french}"
           "<br><br>{german} = {french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        2: "Partizip II {german} → {first_correct_answer}"
           "<br><br>{explanation_french}"
           "<br><br>{german} = {french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        3: "Partizip II {german} → {first_correct_answer}"
           "<br><br>{explanation_french}"
           "<br><br>{german} = {french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        4: "Partizip II {german} → {first_correct_answer}"
           "<br><br>{explanation_french}"
           "<br><br>{german} = {french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        5: "Partizip II {german} → {first_correct_answer}"
           "<br><br>{explanation_french}"
           "<br><br>{german} = {french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        6: "Partizip II {german} → {first_correct_answer}"
           "<br><br>{explanation_french}"
           "<br><br>{german} = {french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        7: "Partizip II {german} → {first_correct_answer}"
           "<br><br>{explanation_french}"
           "<br><br>{german} = {french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        8: "Partizip II {german} → {first_correct_answer}"
           "<br><br>{explanation_french}"
           "<br><br>{german} = {french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        9: "Partizip II {german} → {first_correct_answer}"
           "<br><br>{explanation_french}"
           "<br><br>{german} = {french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        10: "Partizip II {german} → {first_correct_answer}"
            "<br><br>{explanation_french}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        11: "Partizip II {german} → {first_correct_answer}"
            "<br><br>{explanation_french}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        12: "Partizip II {german} → {first_correct_answer}"
            "<br><br>{explanation_french}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        13: "Partizip II {german} → {first_correct_answer}"
            "<br><br>{explanation_french}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        14: "Partizip II {german} → {first_correct_answer}"
            "<br><br>{explanation_french}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        15: "Partizip II {german} → {first_correct_answer}"
            "<br><br>{explanation_french}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        16: "Partizip II {german} → {first_correct_answer}"
            "<br><br>{explanation_french}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        17: "Partizip II {german} → {first_correct_answer}"
            "<br><br>{explanation_french}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        18: "Partizip II {german} → {first_correct_answer}"
            "<br><br>{explanation_french}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        19: "Partizip II {german} → {first_correct_answer}"
            "<br><br>{explanation_french}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        20: "Partizip II {german} → {first_correct_answer}"
            "<br><br>{explanation_french}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        21: "Partizip II {german} → {first_correct_answer}"
            "<br><br>{explanation_french}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        22: "Partizip II {german} → {first_correct_answer}"
            "<br><br>{explanation_french}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        23: "Partizip II {german} → {first_correct_answer}"
            "<br><br>{explanation_french}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        24: "Partizip II {german} → {first_correct_answer}"
            "<br><br>{explanation_french}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        25: "Partizip II {german} → {first_correct_answer}"
            "<br><br>{explanation_french}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        26: "Partizip II {german} → {first_correct_answer}"
            "<br><br>{explanation_french}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        27: "Partizip II {german} → {first_correct_answer}"
            "<br><br>{explanation_french}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        28: "Partizip II {german} → {first_correct_answer}"
            "<br><br>{explanation_french}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        29: "Partizip II {german} → {first_correct_answer}"
            "<br><br>{explanation_french}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        30: "Partizip II {german} → {first_correct_answer}"
            "<br><br>{explanation_french}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        31: "Partizip II {german} → {first_correct_answer}"
            "<br><br>{explanation_french}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        32: "Partizip II {german} → {first_correct_answer}"
            "<br><br>{explanation_french}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        33: "Partizip II {german} → {first_correct_answer}"
            "<br><br>{explanation_french}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        34: "Partizip II {german} → {first_correct_answer}"
            "<br><br>{explanation_french}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        35: "Partizip II {german} → {first_correct_answer}"
            "<br><br>{explanation_french}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        36: "Partizip II {german} → {first_correct_answer}"
            "<br><br>{explanation_french}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        37: "Partizip II {german} → {first_correct_answer}"
            "<br><br>{explanation_french}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        38: "Partizip II {german} → {first_correct_answer}"
            "<br><br>{explanation_french}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        39: "Partizip II {german} → {first_correct_answer}"
            "<br><br>{explanation_french}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        40: "Partizip II {german} → {first_correct_answer}"
            "<br><br>{explanation_french}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        41: "Partizip II {german} → {first_correct_answer}"
            "<br><br>{explanation_french}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        42: "Partizip II {german} → {first_correct_answer}"
            "<br><br>{explanation_french}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        43: "Partizip II {german} → {first_correct_answer}"
            "<br><br>{explanation_french}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        44: "Partizip II {german} → {first_correct_answer}"
            "<br><br>{explanation_french}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        45: "Partizip II {german} → {first_correct_answer}"
            "<br><br>{explanation_french}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        46: "Partizip II {german} → {first_correct_answer}"
            "<br><br>{explanation_french}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        47: "Partizip II {german} → {first_correct_answer}"
            "<br><br>{explanation_french}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        48: "Partizip II {german} → {first_correct_answer}"
            "<br><br>{explanation_french}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        49: "Partizip II {german} → {first_correct_answer}"
            "<br><br>{explanation_french}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        50: "Partizip II {german} → {first_correct_answer}"
            "<br><br>{explanation_french}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        51: "Partizip II {german} → {first_correct_answer}"
            "<br><br>{explanation_french}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        52: "Partizip II {german} → {first_correct_answer}"
            "<br><br>{explanation_french}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        53: "Partizip II {german} → {first_correct_answer}"
            "<br><br>{explanation_french}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        54: "Partizip II {german} → {first_correct_answer}"
            "<br><br>{explanation_french}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        55: "Partizip II {german} → {first_correct_answer}"
            "<br><br>{explanation_french}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        56: "Partizip II {german} → {first_correct_answer}"
            "<br><br>{explanation_french}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        57: "Partizip II {german} → {first_correct_answer}"
            "<br><br>{explanation_french}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        58: "Partizip II {german} → {first_correct_answer}"
            "<br><br>{explanation_french}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        59: "Partizip II {german} → {first_correct_answer}"
            "<br><br>{explanation_french}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        60: "Partizip II {german} → {first_correct_answer}"
            "<br><br>{explanation_french}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        61: "Partizip II {german} → {first_correct_answer}"
            "<br><br>{explanation_french}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        62: "Partizip II {german} → {first_correct_answer}"
            "<br><br>{explanation_french}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        63: "Partizip II {german} → {first_correct_answer}"
            "<br><br>{explanation_french}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        64: "Partizip II {german} → {first_correct_answer}"
            "<br><br>{explanation_french}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        65: "Partizip II {german} → {first_correct_answer}"
            "<br><br>{explanation_french}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        66: "Partizip II {german} → {first_correct_answer}"
            "<br><br>{explanation_french}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
    },

    praeteritum: {
        1: "{german} → {person} {first_correct_answer}"
           "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        2: "{german} → er/sie/es {first_correct_answer}"
           "<br><br>{explanation_french}"
           "<br><br>{german} = {french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        3: "{german} → er/sie/es {first_correct_answer}"
           "<br><br>{explanation_french}"
           "<br><br>{german} = {french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        4: "{german} → er/sie/es {first_correct_answer}"
           "<br><br>{explanation_french}"
           "<br><br>{german} = {french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        5: "{german} → er/sie/es {first_correct_answer}"
           "<br><br>{explanation_french}"
           "<br><br>{german} = {french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        6: "{german} → er/sie/es {first_correct_answer}"
           "<br><br>{explanation_french}"
           "<br><br>{german} = {french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        7: "{german} → er/sie/es {first_correct_answer}"
           "<br><br>{explanation_french}"
           "<br><br>{german} = {french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        8: "{german} → er/sie/es {first_correct_answer}"
           "<br><br>{explanation_french}"
           "<br><br>{german} = {french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        9: "{german} → er/sie/es {first_correct_answer}"
           "<br><br>{explanation_french}"
           "<br><br>{german} = {french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        10: "{previous_question} → er/sie/es {first_correct_answer}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        11: "{previous_question} → er/sie/es {first_correct_answer}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        12: "{previous_question} → er/sie/es {first_correct_answer}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        13: "{previous_question} → er/sie/es {first_correct_answer}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        14: "{previous_question} → er/sie/es {first_correct_answer}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        15: "{previous_question} → er/sie/es {first_correct_answer}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        16: "{previous_question} → er/sie/es {first_correct_answer}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        17: "{previous_question} → er/sie/es {first_correct_answer}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        18: "{previous_question} → er/sie/es {first_correct_answer}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        19: "{previous_question} → er/sie/es {first_correct_answer}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        20: "{previous_question} → er/sie/es {first_correct_answer}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        21: "{previous_question} → er/sie/es {first_correct_answer}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        22: "{previous_question} → er/sie/es {first_correct_answer}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        23: "{previous_question} → er/sie/es {first_correct_answer}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        24: "{previous_question} → er/sie/es {first_correct_answer}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        25: "{previous_question} → er/sie/es {first_correct_answer}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        26: "{previous_question} → er/sie/es {first_correct_answer}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        27: "{previous_question} → er/sie/es {first_correct_answer}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        28: "{previous_question} → er/sie/es {first_correct_answer}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        29: "{previous_question} → er/sie/es {first_correct_answer}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        30: "{previous_question} → er/sie/es {first_correct_answer}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        31: "{previous_question} → er/sie/es {first_correct_answer}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        32: "{previous_question} → er/sie/es {first_correct_answer}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        33: "{previous_question} → er/sie/es {first_correct_answer}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        34: "{previous_question} → er/sie/es {first_correct_answer}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        35: "{previous_question} → er/sie/es {first_correct_answer}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        36: "{previous_question} → er/sie/es {first_correct_answer}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        37: "{previous_question} → er/sie/es {first_correct_answer}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        38: "{previous_question} → er/sie/es {first_correct_answer}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        39: "{previous_question} → er/sie/es {first_correct_answer}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        40: "{previous_question} → er/sie/es {first_correct_answer}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        41: "{previous_question} → er/sie/es {first_correct_answer}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        42: "{previous_question} → er/sie/es {first_correct_answer}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        43: "{previous_question} → er/sie/es {first_correct_answer}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        44: "{previous_question} → er/sie/es {first_correct_answer}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        45: "{previous_question} → er/sie/es {first_correct_answer}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        46: "{previous_question} → er/sie/es {first_correct_answer}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        47: "{previous_question} → er/sie/es {first_correct_answer}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        48: "{previous_question} → er/sie/es {first_correct_answer}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        49: "{previous_question} → er/sie/es {first_correct_answer}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        50: "{previous_question} → er/sie/es {first_correct_answer}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        51: "{previous_question} → er/sie/es {first_correct_answer}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        52: "{previous_question} → er/sie/es {first_correct_answer}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        53: "{previous_question} → er/sie/es {first_correct_answer}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        54: "{previous_question} → er/sie/es {first_correct_answer}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        55: "{previous_question} → er/sie/es {first_correct_answer}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        56: "{previous_question} → er/sie/es {first_correct_answer}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        57: "{previous_question} → er/sie/es {first_correct_answer}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        58: "{previous_question} → er/sie/es {first_correct_answer}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        59: "{previous_question} → er/sie/es {first_correct_answer}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        60: "{previous_question} → er/sie/es {first_correct_answer}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        61: "{previous_question} → er/sie/es {first_correct_answer}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        62: "{previous_question} → er/sie/es {first_correct_answer}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        63: "{previous_question} → er/sie/es {first_correct_answer}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        64: "{previous_question} → er/sie/es {first_correct_answer}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        65: "{previous_question} → er/sie/es {first_correct_answer}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        66: "{previous_question} → er/sie/es {first_correct_answer}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        67: "{previous_question} → er/sie/es {first_correct_answer}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
    },

    imperativ: {
        1: "{german}, {person} → {correct_answers}"
           "<br><br>{german} = {french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        2: "{german}, {person} → {correct_answers}"
           "<br><br>{german} = {french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        3: "{german}, {person} → {correct_answers}"
           "<br><br>{german} = {french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        4: "{german}, {person} → {correct_answers}"
           "<br><br>{german} = {french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        5: "{german}, {person} → {correct_answers}"
           "<br><br>{german} = {french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        6: "{german}, {person} → {correct_answers}"
           "<br><br>{german} = {french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        7: "{german}, {person} → {correct_answers}"
           "<br><br>{german} = {french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        8: "{german}, {person} → {correct_answers}"
           "<br><br>{german} = {french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        9: "{german}, {person} → {correct_answers}"
           "<br><br>{german} = {french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        10: "{german}, {person} → {correct_answers}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        11: "{german}, {person} → {correct_answers}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        12: "{german}, {person} → {correct_answers}"
            "<br><br>{german} = {french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
    },

    konjunktiv_II: {
        1: "{german} → {person} {first_correct_answer}"
           "<br><br>{german} = {french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
    },

    konjunktiv_I: {
        1: "{german} → {person} {first_correct_answer}"
           "<br><br>{german} = {french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        2: "{german} → {person} {first_correct_answer}"
           "<br><br>{german} = {french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        3: "{german} → {person} {first_correct_answer}"
           "<br><br>{german} = {french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        4: "{german} → {person} {first_correct_answer}"
           "<br><br>{german} = {french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        5: "{german} → {person} {first_correct_answer}"
           "<br><br>{german} = {french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        6: "{german} → {person} {first_correct_answer}"
           "<br><br>{german} = {french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
    },

    partizip_I: {
        1: "Partizip I {german} → {first_correct_answer}"
           "<br><br>{german} = {french}"
           "<br><br>{first_correct_answer} = {explanation_french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        2: "Partizip I {german} → {first_correct_answer}"
           "<br><br>{german} = {french}"
           "<br><br>{first_correct_answer} = {explanation_french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        3: "Partizip I {german} → {first_correct_answer}"
           "<br><br>{german} = {french}"
           "<br><br>{first_correct_answer} = {explanation_french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        4: "Partizip I {german} → {first_correct_answer}"
           "<br><br>{german} = {french}"
           "<br><br>{first_correct_answer} = {explanation_french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        5: "Partizip I {german} → {first_correct_answer}"
           "<br><br>{german} = {french}"
           "<br><br>{first_correct_answer} = {explanation_french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
    },

    adjektive_verben_wortstaemme: {
        1: "{root_french} → {previous_question}"
           "<br><br>{french} → {first_correct_answer}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        2: "{root_french} → {previous_question}"
           "<br><br>{french} → {first_correct_answer}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        3: "{root_french} → {previous_question}"
           "<br><br>{french} → {first_correct_answer}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        4: "{root_french} → {previous_question}"
           "<br><br>{french} → {first_correct_answer}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        5: "{root_french} → {previous_question}"
           "<br><br>{french} → {first_correct_answer}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        6: "{root_french} → {previous_question}"
           "<br><br>{french} → {first_correct_answer}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        7: "{root_french} → {previous_question}"
           "<br><br>{french} → {first_correct_answer}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        8: "{root_french} → {previous_question}"
           "<br><br>{french} → {first_correct_answer}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        9: "{root_french} → {previous_question}"
           "<br><br>{french} → {first_correct_answer}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        10: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        11: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        12: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        13: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        14: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        15: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        16: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        17: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        18: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        19: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        20: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
    },

    adjektive_nomen_wortstaemme: {
        1: "{root_french} → {previous_question}"
           "<br><br>{french} → {first_correct_answer}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        2: "{root_french} → {previous_question}"
           "<br><br>{french} → {first_correct_answer}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        3: "{root_french} → {previous_question}"
           "<br><br>{french} → {first_correct_answer}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        4: "{root_french} → {previous_question}"
           "<br><br>{french} → {first_correct_answer}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        5: "{root_french} → {previous_question}"
           "<br><br>{french} → {first_correct_answer}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        6: "{root_french} → {previous_question}"
           "<br><br>{french} → {first_correct_answer}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        7: "{root_french} → {previous_question}"
           "<br><br>{french} → {first_correct_answer}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        8: "{root_french} → {previous_question}"
           "<br><br>{french} → {first_correct_answer}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        9: "{root_french} → {previous_question}"
           "<br><br>{french} → {first_correct_answer}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        10: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        11: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        12: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        13: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        14: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        15: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        16: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        17: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        18: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
    },

    nomen_verben_wortstaemme: {
        1: "{root_french} → {previous_question}"
           "<br><br>{french} → {first_correct_answer}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        2: "{root_french} → {previous_question}"
           "<br><br>{french} → {first_correct_answer}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        3: "{root_french} → {previous_question}"
           "<br><br>{french} → {first_correct_answer}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        4: "{root_french} → {previous_question}"
           "<br><br>{french} → {first_correct_answer}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        5: "{root_french} → {previous_question}"
           "<br><br>{french} → {first_correct_answer}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        6: "{root_french} → {previous_question}"
           "<br><br>{french} → {first_correct_answer}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        7: "{root_french} → {previous_question}"
           "<br><br>{french} → {first_correct_answer}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        8: "{root_french} → {previous_question}"
           "<br><br>{french} → {first_correct_answer}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        9: "{root_french} → {previous_question}"
           "<br><br>{french} → {first_correct_answer}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        10: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        11: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        12: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        13: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        14: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        15: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        16: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        17: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        18: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        19: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        20: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        21: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        22: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        23: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        24: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        25: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        26: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        27: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        28: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        29: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        30: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        31: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        32: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        33: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        34: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        35: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        36: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        37: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        38: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        39: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        40: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        41: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        42: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        43: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        44: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        45: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        46: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        47: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        48: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        49: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        50: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        51: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        52: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        53: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        54: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        55: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        56: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        57: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        58: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        59: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        60: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        61: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        62: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        63: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        64: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        65: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        66: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        67: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        68: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        69: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        70: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        71: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        72: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        73: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        74: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        75: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        76: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        77: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        78: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        79: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        80: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        81: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        82: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        83: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        84: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        85: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        86: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        87: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        88: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        89: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        90: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        91: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        92: "{root_french} → {previous_question}"
            "<br><br>{french} → {first_correct_answer}"
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

    genus: {
        1: "{german}"
           "<br><br><i>{french}</i>"
           "{explanation_french}",
        2: "{german}"
           "<br><br><i>{french}</i>"
           "{explanation_french}",
        3: "{german}"
           "<br><br><i>{french}</i>"
           "{explanation_french}",
        4: "{german}"
           "<br><br><i>{french}</i>"
           "{explanation_french}",
        5: "{german}"
           "<br><br><i>{french}</i>"
           "{explanation_french}",
        6: "{german}"
           "<br><br><i>{french}</i>"
           "{explanation_french}",
        7: "{german}"
           "<br><br><i>{french}</i>"
           "{explanation_french}",
        8: "{german}"
           "<br><br><i>{french}</i>"
           "{explanation_french}",
        9: "{german}"
           "<br><br><i>{french}</i>"
           "{explanation_french}",
        10: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        11: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        12: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        13: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        14: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        15: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        16: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        17: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        18: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        19: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        20: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        21: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        22: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        23: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        24: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        25: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",

        26: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        27: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        28: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        29: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        30: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        31: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        32: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        33: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        34: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        35: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        36: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        37: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        38: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        39: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        40: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        41: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        42: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        43: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        44: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        45: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        46: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        47: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        48: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        49: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        50: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",

        51: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        52: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        53: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        54: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        55: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        56: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        57: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        58: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        59: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        60: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        61: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        62: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        63: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        64: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        65: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        66: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        67: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        68: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        69: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        70: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        71: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        72: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        73: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        74: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        75: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        76: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        77: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        78: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        79: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        80: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        81: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        82: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        83: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        84: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        85: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        86: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        87: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        88: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        89: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        90: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        91: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        92: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        93: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        94: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        95: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        96: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        97: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        98: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
        99: "{german}"
            "<br><br><i>{french}</i>"
            "{explanation_french}",
    },

    plural: {
        1: "{previous_question} &#8594 die {correct_answer}"
           "<br><br><i>{french}</i>",
        2: "{previous_question} &#8594 die {correct_answer}"
           "<br><br><i>{french}</i>",
        3: "{previous_question} &#8594 die {correct_answer}"
           "<br><br><i>{french}</i>",
        4: "{previous_question} &#8594 die {correct_answer}"
           "<br><br><i>{french}</i>",
        5: "{previous_question} &#8594 die {correct_answer}"
           "<br><br><i>{french}</i>",
        6: "{previous_question} &#8594 die {correct_answer}"
           "<br><br><i>{french}</i>",
        7: "{previous_question} &#8594 die {correct_answer}"
           "<br><br><i>{french}</i>",
        8: "{previous_question} &#8594 die {correct_answer}"
           "<br><br><i>{french}</i>",
        9: "{previous_question} &#8594 die {correct_answer}"
           "<br><br><i>{french}</i>",
        10: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        11: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        12: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        13: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        14: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        15: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        16: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        17: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        18: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        19: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        20: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        21: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        22: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        23: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        24: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        25: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",

        26: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        27: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        28: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        29: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        30: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        31: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        32: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        33: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        34: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        35: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        36: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        37: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        38: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        39: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        40: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        41: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        42: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        43: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        44: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        45: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        46: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        47: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        48: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        49: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        50: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",

        51: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        52: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        53: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        54: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        55: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        56: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        57: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        58: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        59: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        60: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        61: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        62: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        63: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        64: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        65: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        66: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        67: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        68: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        69: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        70: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        71: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        72: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        73: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        74: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        75: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        76: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        77: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        78: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        79: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        80: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        81: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        82: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        83: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
        84: "{previous_question} &#8594 die {correct_answer}"
            "<br><br><i>{french}</i>",
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
