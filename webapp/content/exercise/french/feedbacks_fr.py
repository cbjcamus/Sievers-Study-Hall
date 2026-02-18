from data.data_processing.units import (
    praepositionen_grammatik, praepositionen_verben, praepositionen_adjektive, praepositionen_nomen,
    praepositionen_artikel, praepositionen_adverbien,
    artikel, pronomen, konnektoren, fragen, adverbien, wortstellung,
    adjektive, adjektivdeklinationen, adjektive_konjunktionen,
    verben, trennbare_verben, nomen_verben_verbindungen, nomen_verben_wortstaemme,
    praesens, imperativ, partizip_II, praeteritum, praeteritum_partizip_II, konjunktiv_II, konjunktiv_I, partizip_I,
    genus_regeln, genus_routledge, genus_goethe,
    zahlen,
)

FEEDBACK_FR = {

    praepositionen_grammatik: {
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
        19: "{french} = {correct_answers}",
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
        28: "{german} ↔ {first_correct_answer}"
            "<br><br>{french}"
            "<br><br>{explanation_french}"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",

        29: "{german}"
            "<br><br><i>{french}</i>"
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
        9: "{german}"
           "<br><br><i>{french}</i>"
           "<br><br>{explanation_french}"
           "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        10: "{german}"
            "<br><br><i>{french}</i>"
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
    },

    praepositionen_adverbien: {
        1: "Something",
        2: "Something",
        3: "Something",
        4: "Something",
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
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
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
        21: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{gender_french}, {case_french} → {correct_answers}",
        22: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{gender_french}, {case_french} → {correct_answers}",

        23: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{gender_french}, {case_french} → {correct_answers}",
        24: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{gender_french}, {case_french} → {correct_answers}",
        25: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
        26: "{german}, {gender_french}, {case_french} → {correct_answers}",
        27: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{gender_french}, {case_french} → {correct_answers}",
        28: "{german}, {gender_french}, {case_french} → {correct_answers}",
        29: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>{gender_french}, {case_french} → {correct_answers}",

        30: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>Réponse(s) correcte(s) : {correct_answers}",
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
        1: "{french} = {correct_answers}",
        2: "{french} = {correct_answers}",
        3: "{french} ↔ {correct_answers}",
        4: "{previous_question} ↔ {correct_answers}",
        5: "{previous_question} ↔ {correct_answers}",
        6: "Comparatif {previous_question} (<i>{french}</i>) → {correct_answers}",
        7: "Comparatif {previous_question} (<i>{french}</i>) → {correct_answers}",
        8: "Comparatif {previous_question} (<i>{french}</i>) → {correct_answers}",
        9: "Superlatif {previous_question} (<i>{french}</i>) → {correct_answers}",
        10: "Superlatif {previous_question} (<i>{french}</i>) → {correct_answers}",
        11: "Superlatif {previous_question} (<i>{french}</i>) → {correct_answers}",

        12: "{french} = {correct_answers}",
        13: "{french} = {correct_answers}",
        14: "{french} ↔ {correct_answers}",
        15: "{previous_question} ↔ {correct_answers}",
        16: "{previous_question} ↔ {correct_answers}",
        17: "Comparatif {previous_question} (<i>{french}</i>) → {correct_answers}",
        18: "Comparatif {previous_question} (<i>{french}</i>) → {correct_answers}",
        19: "Comparatif {previous_question} (<i>{french}</i>) → {correct_answers}",
        20: "Superlatif {previous_question} (<i>{french}</i>) → {correct_answers}",
        21: "Superlatif {previous_question} (<i>{french}</i>) → {correct_answers}",
        22: "Superlatif {previous_question} (<i>{french}</i>) → {correct_answers}",

        23: "{french} = {correct_answers}",
        24: "{french} = {correct_answers}",
        25: "{french} = {correct_answers}",
        26: "{previous_question} = {correct_answers}",
        27: "{previous_question} = {correct_answers}",
        28: "{previous_question} = {correct_answers}",

        29: "{french} = {correct_answers}",
        30: "{french} = {correct_answers}",
        31: "{french} = {correct_answers}",
        32: "{french} = {correct_answers}",
        33: "{french} = {correct_answers}",
        34: "{french} = {correct_answers}",
    },

    adjektivdeklinationen: {
        1: "{german}"
           "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",
        2: "{german}"
           "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",
        3: "{german}"
           "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",
        4: "{german}"
           "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",
        5: "{german}"
           "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",
        6: "{german}"
           "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",
        7: "{german}"
           "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",
        8: "{german}"
           "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",
        9: "{german}"
           "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",
        10: "{german}"
            "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",
        11: "{german}"
            "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",
        12: "{german}"
            "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",
        13: "{german}"
            "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",
        14: "{german}"
            "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",

        15: "{german}"
            "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",
        16: "{german}"
            "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",
        17: "{german}"
            "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",
        18: "{german}"
            "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",
        19: "{german}"
            "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",
        20: "{german}"
            "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",
        21: "{german}"
            "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",
        22: "{german}"
            "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",
        23: "{german}"
            "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",
        24: "{german}"
            "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",

        25: "{german}"
            "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",
        26: "{german}"
            "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",

        27: "{german}"
            "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",
        28: "{german}"
            "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",
        29: "{german}"
            "<br><br>{article_french}, {gender_french}, {case_french} → {correct_answers}",
        30: "{german}"
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

    praesens: {
        1: "{previous_question} → {person} {correct_answers}"
           "<br><br>{previous_question} = {french}",
        2: "{previous_question} → {person} {correct_answers}"
           "<br><br>{previous_question} = {french}",
        3: "{previous_question} → {person} {correct_answers}"
           "<br><br>{previous_question} = {french}",
        4: "{previous_question} → {person} {correct_answers}"
           "<br><br>{previous_question} = {french}",
        5: "{previous_question} → {person} {correct_answers}"
           "<br><br>{previous_question} = {french}",
        6: "{previous_question} → {person} {correct_answers}"
           "<br><br>{previous_question} = {french}",
        7: "{previous_question} → {person} {correct_answers}"
           "<br><br>{previous_question} = {french}",
        8: "{previous_question} → {person} {correct_answers}"
           "<br><br>{previous_question} = {french}",
        9: "{previous_question} → {person} {correct_answers}"
           "<br><br>{previous_question} = {french}",
        10: "{previous_question} → {person} {correct_answers}"
            "<br><br>{previous_question} = {french}",
        11: "{previous_question} → {person} {correct_answers}"
            "<br><br>{previous_question} = {french}",
        12: "{previous_question} → {person} {correct_answers}"
            "<br><br>{previous_question} = {french}",
        13: "{previous_question} → {person} {correct_answers}"
            "<br><br>{previous_question} = {french}",
        14: "{previous_question} → {person} {correct_answers}"
            "<br><br>{previous_question} = {french}",
        15: "{previous_question} → {person} {correct_answers}"
            "<br><br>{previous_question} = {french}",
        16: "{previous_question} → {person} {correct_answers}"
            "<br><br>{previous_question} = {french}",
        17: "{previous_question} → {person} {correct_answers}"
            "<br><br>{previous_question} = {french}",
        18: "{previous_question} → {person} {correct_answers}"
            "<br><br>{previous_question} = {french}",
        19: "{previous_question} → {person} {correct_answers}"
            "<br><br>{previous_question} = {french}",
        20: "{previous_question} → {person} {correct_answers}"
            "<br><br>{previous_question} = {french}",

        21: "{previous_question} → {person} {correct_answers}"
            "<br><br>{previous_question} = {french}",
        22: "{previous_question} → {person} {correct_answers}"
            "<br><br>{previous_question} = {french}",
        23: "{previous_question} → {person} {correct_answers}"
            "<br><br>{previous_question} = {french}",
        24: "{previous_question} → {person} {correct_answers}"
            "<br><br>{previous_question} = {french}",
        25: "{previous_question} → {person} {correct_answers}"
            "<br><br>{previous_question} = {french}",
        26: "{previous_question} → {person} {correct_answers}"
            "<br><br>{previous_question} = {french}",
        27: "{previous_question} → {person} {correct_answers}"
            "<br><br>{previous_question} = {french}",
        28: "{previous_question} → {person} {correct_answers}"
            "<br><br>{previous_question} = {french}",
        29: "{previous_question} → {person} {correct_answers}"
            "<br><br>{previous_question} = {french}",
        30: "{previous_question} → {person} {correct_answers}"
            "<br><br>{previous_question} = {french}",
        31: "{previous_question} → {person} {correct_answers}"
            "<br><br>{previous_question} = {french}",
        32: "{previous_question} → {person} {correct_answers}"
            "<br><br>{previous_question} = {french}",
        33: "{previous_question} → {person} {correct_answers}"
            "<br><br>{previous_question} = {french}",
        34: "{previous_question} → {person} {correct_answers}"
            "<br><br>{previous_question} = {french}",
        35: "{previous_question} → {person} {correct_answers}"
            "<br><br>{previous_question} = {french}",
        36: "{previous_question} → {person} {correct_answers}"
            "<br><br>{previous_question} = {french}",
        37: "{previous_question} → {person} {correct_answers}"
            "<br><br>{previous_question} = {french}",
        38: "{previous_question} → {person} {correct_answers}"
            "<br><br>{previous_question} = {french}",
        39: "{previous_question} → {person} {correct_answers}"
            "<br><br>{previous_question} = {french}",
        40: "{previous_question} → {person} {correct_answers}"
            "<br><br>{previous_question} = {french}",
    },

    partizip_II: {
        1: "Partizip II {previous_question} → {correct_answers}"
           "<br><br>{german}"
           "<br><br>{previous_question} = {french}",
        2: "Partizip II {previous_question} → {correct_answers}"
           "<br><br>{german}"
           "<br><br>{previous_question} = {french}",
        3: "Partizip II {previous_question} → {correct_answers}"
           "<br><br>{german}"
           "<br><br>{previous_question} = {french}",
        4: "Partizip II {previous_question} → {correct_answers}"
           "<br><br>{german}"
           "<br><br>{previous_question} = {french}",
        5: "Partizip II {previous_question} → {correct_answers}"
           "<br><br>{german}"
           "<br><br>{previous_question} = {french}",
        6: "Partizip II {previous_question} → {correct_answers}"
           "<br><br>{german}"
           "<br><br>{previous_question} = {french}",
        7: "Partizip II {previous_question} → {correct_answers}"
           "<br><br>{german}"
           "<br><br>{previous_question} = {french}",

        8: "Partizip II {previous_question} → {correct_answers}"
           "<br><br>{german}"
           "<br><br>{previous_question} = {french}",
        9: "Partizip II {previous_question} → {correct_answers}"
           "<br><br>{german}"
           "<br><br>{previous_question} = {french}",
        10: "Partizip II {previous_question} → {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        11: "Partizip II {previous_question} → {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        12: "Partizip II {previous_question} → {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        13: "Partizip II {previous_question} → {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        14: "Partizip II {previous_question} → {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",

        15: "Partizip II {previous_question} → {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        16: "Partizip II {previous_question} → {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        17: "Partizip II {previous_question} → {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        18: "Partizip II {previous_question} → {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        19: "Partizip II {previous_question} → {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        20: "Partizip II {previous_question} → {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        21: "Partizip II {previous_question} → {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        22: "Partizip II {previous_question} → {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        23: "Partizip II {previous_question} → {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        24: "Partizip II {previous_question} → {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        25: "Partizip II {previous_question} → {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        26: "Partizip II {previous_question} → {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        27: "Partizip II {previous_question} → {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",

        28: "Partizip II {previous_question} → {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        29: "Partizip II {previous_question} → {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        30: "Partizip II {previous_question} → {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        31: "Partizip II {previous_question} → {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        32: "Partizip II {previous_question} → {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        33: "Partizip II {previous_question} → {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        34: "Partizip II {previous_question} → {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        35: "Partizip II {previous_question} → {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        36: "Partizip II {previous_question} → {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        37: "Partizip II {previous_question} → {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        38: "Partizip II {previous_question} → {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        39: "Partizip II {previous_question} → {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        40: "Partizip II {previous_question} → {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",

        41: "Partizip II {previous_question} → {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        42: "Partizip II {previous_question} → {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        43: "Partizip II {previous_question} → {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        44: "Partizip II {previous_question} → {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        45: "Partizip II {previous_question} → {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        46: "Partizip II {previous_question} → {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        47: "Partizip II {previous_question} → {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        48: "Partizip II {previous_question} → {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        49: "Partizip II {previous_question} → {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        50: "Partizip II {previous_question} → {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        51: "Partizip II {previous_question} → {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        52: "Partizip II {previous_question} → {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        53: "Partizip II {previous_question} → {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        54: "Partizip II {previous_question} → {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        55: "Partizip II {previous_question} → {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        56: "Partizip II {previous_question} → {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        57: "Partizip II {previous_question} → {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        58: "Partizip II {previous_question} → {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        59: "Partizip II {previous_question} → {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        60: "Partizip II {previous_question} → {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        61: "Partizip II {previous_question} → {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        62: "Partizip II {previous_question} → {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        63: "Partizip II {previous_question} → {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        64: "Partizip II {previous_question} → {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        65: "Partizip II {previous_question} → {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        66: "Partizip II {previous_question} → {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
    },

    praeteritum: {
        1: "{previous_question} → {person} {correct_answers}"
           "<br><br>{previous_question} = {french}",

        2: "{previous_question} → er/sie/es {correct_answers}"
           "<br><br>{german}"
           "<br><br>{previous_question} = {french}",
        3: "{previous_question} → er/sie/es {correct_answers}"
           "<br><br>{german}"
           "<br><br>{previous_question} = {french}",
        4: "{previous_question} → er/sie/es {correct_answers}"
           "<br><br>{german}"
           "<br><br>{previous_question} = {french}",
        5: "{previous_question} → er/sie/es {correct_answers}"
           "<br><br>{german}"
           "<br><br>{previous_question} = {french}",
        6: "{previous_question} → er/sie/es {correct_answers}"
           "<br><br>{german}"
           "<br><br>{previous_question} = {french}",
        7: "{previous_question} → er/sie/es {correct_answers}"
           "<br><br>{german}"
           "<br><br>{previous_question} = {french}",
        8: "{previous_question} → er/sie/es {correct_answers}"
           "<br><br>{german}"
           "<br><br>{previous_question} = {french}",
        9: "{previous_question} → er/sie/es {correct_answers}"
           "<br><br>{german}"
           "<br><br>{previous_question} = {french}",
        10: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        11: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        12: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        13: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        14: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        15: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",

        16: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        17: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        18: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        19: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        20: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        21: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        22: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        23: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        24: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        25: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        26: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        27: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        28: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",

        29: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        30: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        31: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        32: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        33: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        34: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        35: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        36: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        37: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        38: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        39: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        40: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        41: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",

        42: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        43: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        44: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        45: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        46: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        47: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        48: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        49: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        50: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        51: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        52: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        53: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        54: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        55: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        56: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        57: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        58: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        59: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        60: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        61: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        62: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        63: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        64: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        65: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        66: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
        67: "{previous_question} → er/sie/es {correct_answers}"
            "<br><br>{german}"
            "<br><br>{previous_question} = {french}",
    },

    praeteritum_partizip_II: {
        1: "{previous_question}, {correct_answers}"
           "<br><br>{previous_question} = {french}"
           "<br><br>Réponse correcte : {correct_answers}",
        2: "{previous_question}, {correct_answers}"
           "<br><br>{previous_question} = {french}"
           "<br><br>Réponse correcte : {correct_answers}",
        3: "{previous_question}, {correct_answers}"
           "<br><br>{previous_question} = {french}"
           "<br><br>Réponse correcte : {correct_answers}",
        4: "{previous_question}, {correct_answers}"
           "<br><br>{previous_question} = {french}"
           "<br><br>Réponse correcte : {correct_answers}",
        5: "{previous_question}, {correct_answers}"
           "<br><br>{previous_question} = {french}"
           "<br><br>Réponse correcte : {correct_answers}",
        6: "{previous_question}, {correct_answers}"
           "<br><br>{previous_question} = {french}"
           "<br><br>Réponse correcte : {correct_answers}",
        7: "{previous_question}, {correct_answers}"
           "<br><br>{previous_question} = {french}"
           "<br><br>Réponse correcte : {correct_answers}",
        8: "{previous_question}, {correct_answers}"
           "<br><br>{previous_question} = {french}"
           "<br><br>Réponse correcte : {correct_answers}",
        9: "{previous_question}, {correct_answers}"
           "<br><br>{previous_question} = {french}"
           "<br><br>Réponse correcte : {correct_answers}",
        10: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse correcte : {correct_answers}",
        11: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse correcte : {correct_answers}",
        12: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse correcte : {correct_answers}",
        13: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse correcte : {correct_answers}",
        14: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse correcte : {correct_answers}",

        15: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse correcte : {correct_answers}",
        16: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse correcte : {correct_answers}",
        17: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse correcte : {correct_answers}",
        18: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse correcte : {correct_answers}",
        19: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse correcte : {correct_answers}",
        20: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse correcte : {correct_answers}",
        21: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse correcte : {correct_answers}",
        22: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse correcte : {correct_answers}",
        23: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse correcte : {correct_answers}",
        24: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse correcte : {correct_answers}",
        25: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse correcte : {correct_answers}",
        26: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse correcte : {correct_answers}",
        27: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse correcte : {correct_answers}",

        28: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse correcte : {correct_answers}",
        29: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse correcte : {correct_answers}",
        30: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse correcte : {correct_answers}",
        31: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse correcte : {correct_answers}",
        32: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse correcte : {correct_answers}",
        33: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse correcte : {correct_answers}",
        34: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse correcte : {correct_answers}",
        35: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse correcte : {correct_answers}",
        36: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse correcte : {correct_answers}",
        37: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse correcte : {correct_answers}",
        38: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse correcte : {correct_answers}",
        39: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse correcte : {correct_answers}",
        40: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse correcte : {correct_answers}",

        41: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse correcte : {correct_answers}",
        42: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse correcte : {correct_answers}",
        43: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse correcte : {correct_answers}",
        44: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse correcte : {correct_answers}",
        45: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse correcte : {correct_answers}",
        46: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse correcte : {correct_answers}",
        47: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse correcte : {correct_answers}",
        48: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse correcte : {correct_answers}",
        49: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse correcte : {correct_answers}",
        50: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse correcte : {correct_answers}",
        51: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse correcte : {correct_answers}",
        52: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse correcte : {correct_answers}",
        53: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse correcte : {correct_answers}",
        54: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse correcte : {correct_answers}",
        55: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse correcte : {correct_answers}",
        56: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse correcte : {correct_answers}",
        57: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse correcte : {correct_answers}",
        58: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse correcte : {correct_answers}",
        59: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse correcte : {correct_answers}",
        60: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse correcte : {correct_answers}",
        61: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse correcte : {correct_answers}",
        62: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse correcte : {correct_answers}",
        63: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse correcte : {correct_answers}",
        64: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse correcte : {correct_answers}",
        65: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse correcte : {correct_answers}",
        66: "{previous_question}, {correct_answers}"
            "<br><br>{previous_question} = {french}"
            "<br><br>Réponse correcte : {correct_answers}",
    },

    imperativ: {
        1: "{previous_question}, {person} → {correct_answers}"
           "<br><br>{previous_question} = {french}",
        2: "{previous_question}, {person} → {correct_answers}"
           "<br><br>{previous_question} = {french}",
        3: "{previous_question}, {person} → {correct_answers}"
           "<br><br>{previous_question} = {french}",
        4: "{previous_question}, {person} → {correct_answers}"
           "<br><br>{previous_question} = {french}",
        5: "{previous_question}, {person} → {correct_answers}"
           "<br><br>{previous_question} = {french}",
        6: "{previous_question}, {person} → {correct_answers}"
           "<br><br>{previous_question} = {french}",

        7: "{previous_question}, {person} → {correct_answers}"
           "<br><br>{previous_question} = {french}",
        8: "{previous_question}, {person} → {correct_answers}"
           "<br><br>{previous_question} = {french}",
        9: "{previous_question}, {person} → {correct_answers}"
           "<br><br>{previous_question} = {french}",
        10: "{previous_question}, {person} → {correct_answers}"
            "<br><br>{previous_question} = {french}",
        11: "{previous_question}, {person} → {correct_answers}"
            "<br><br>{previous_question} = {french}",
        12: "{previous_question}, {person} → {correct_answers}"
            "<br><br>{previous_question} = {french}",
    },

    konjunktiv_II: {
        1: "{previous_question} → {person} {correct_answers}"
           "<br><br>{previous_question} = {french}",
    },

    konjunktiv_I: {
        1: "{previous_question} → {person} {correct_answers}"
           "<br><br>{previous_question} = {french}",
        2: "{previous_question} → {person} {correct_answers}"
           "<br><br>{previous_question} = {french}",
        3: "{previous_question} → {person} {correct_answers}"
           "<br><br>{previous_question} = {french}",
        4: "{previous_question} → {person} {correct_answers}"
           "<br><br>{previous_question} = {french}",
        5: "{previous_question} → {person} {correct_answers}"
           "<br><br>{previous_question} = {french}",
        6: "{previous_question} → {person} {correct_answers}"
           "<br><br>{previous_question} = {french}",
    },

    partizip_I: {
        1: "Partizip I {previous_question} → {correct_answers}"
           "<br><br>{previous_question} = {french}",
        2: "Partizip I {previous_question} → {correct_answers}"
           "<br><br>{previous_question} = {french}",
        3: "Partizip I {previous_question} → {correct_answers}"
           "<br><br>{previous_question} = {french}",
        4: "Partizip I {previous_question} → {correct_answers}"
           "<br><br>{previous_question} = {french}",
        5: "Partizip I {previous_question} → {correct_answers}"
           "<br><br>{previous_question} = {french}",
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

    genus_routledge: {
        1: "{german}"
           "<br><br><i>{french}</i>",
        2: "{german}"
           "<br><br><i>{french}</i>",
        3: "{german}"
           "<br><br><i>{french}</i>",
        4: "{german}"
           "<br><br><i>{french}</i>",
        5: "{german}"
           "<br><br><i>{french}</i>",
        6: "{german}"
           "<br><br><i>{french}</i>",
        7: "{german}"
           "<br><br><i>{french}</i>",
        8: "{german}"
           "<br><br><i>{french}</i>",
        9: "{german}"
           "<br><br><i>{french}</i>",
        10: "{german}"
            "<br><br><i>{french}</i>",
        11: "{german}"
            "<br><br><i>{french}</i>",
        12: "{german}"
            "<br><br><i>{french}</i>",
        13: "{german}"
            "<br><br><i>{french}</i>",
        14: "{german}"
            "<br><br><i>{french}</i>",
        15: "{german}"
            "<br><br><i>{french}</i>",
        16: "{german}"
            "<br><br><i>{french}</i>",
        17: "{german}"
            "<br><br><i>{french}</i>",
        18: "{german}"
            "<br><br><i>{french}</i>",
        19: "{german}"
            "<br><br><i>{french}</i>",
        20: "{german}"
            "<br><br><i>{french}</i>",
        21: "{german}"
            "<br><br><i>{french}</i>",
        22: "{german}"
            "<br><br><i>{french}</i>",
        23: "{german}"
            "<br><br><i>{french}</i>",
        24: "{german}"
            "<br><br><i>{french}</i>",
        25: "{german}"
            "<br><br><i>{french}</i>",

        26: "{german}"
            "<br><br><i>{french}</i>",
        27: "{german}"
            "<br><br><i>{french}</i>",
        28: "{german}"
            "<br><br><i>{french}</i>",
        29: "{german}"
            "<br><br><i>{french}</i>",
        30: "{german}"
            "<br><br><i>{french}</i>",
        31: "{german}"
            "<br><br><i>{french}</i>",
        32: "{german}"
            "<br><br><i>{french}</i>",
        33: "{german}"
            "<br><br><i>{french}</i>",
        34: "{german}"
            "<br><br><i>{french}</i>",
        35: "{german}"
            "<br><br><i>{french}</i>",
        36: "{german}"
            "<br><br><i>{french}</i>",
        37: "{german}"
            "<br><br><i>{french}</i>",
        38: "{german}"
            "<br><br><i>{french}</i>",
        39: "{german}"
            "<br><br><i>{french}</i>",
        40: "{german}"
            "<br><br><i>{french}</i>",
        41: "{german}"
            "<br><br><i>{french}</i>",
        42: "{german}"
            "<br><br><i>{french}</i>",
        43: "{german}"
            "<br><br><i>{french}</i>",
        44: "{german}"
            "<br><br><i>{french}</i>",
        45: "{german}"
            "<br><br><i>{french}</i>",
        46: "{german}"
            "<br><br><i>{french}</i>",
        47: "{german}"
            "<br><br><i>{french}</i>",
        48: "{german}"
            "<br><br><i>{french}</i>",
        49: "{german}"
            "<br><br><i>{french}</i>",
        50: "{german}"
            "<br><br><i>{french}</i>",

        51: "{german}"
            "<br><br><i>{french}</i>",
        52: "{german}"
            "<br><br><i>{french}</i>",
        53: "{german}"
            "<br><br><i>{french}</i>",
        54: "{german}"
            "<br><br><i>{french}</i>",
        55: "{german}"
            "<br><br><i>{french}</i>",
        56: "{german}"
            "<br><br><i>{french}</i>",
        57: "{german}"
            "<br><br><i>{french}</i>",
        58: "{german}"
            "<br><br><i>{french}</i>",
        59: "{german}"
            "<br><br><i>{french}</i>",
        60: "{german}"
            "<br><br><i>{french}</i>",
        61: "{german}"
            "<br><br><i>{french}</i>",
        62: "{german}"
            "<br><br><i>{french}</i>",
        63: "{german}"
            "<br><br><i>{french}</i>",
        64: "{german}"
            "<br><br><i>{french}</i>",
        65: "{german}"
            "<br><br><i>{french}</i>",
        66: "{german}"
            "<br><br><i>{french}</i>",
        67: "{german}"
            "<br><br><i>{french}</i>",
        68: "{german}"
            "<br><br><i>{french}</i>",
        69: "{german}"
            "<br><br><i>{french}</i>",
        70: "{german}"
            "<br><br><i>{french}</i>",
        71: "{german}"
            "<br><br><i>{french}</i>",
        72: "{german}"
            "<br><br><i>{french}</i>",
        73: "{german}"
            "<br><br><i>{french}</i>",
        74: "{german}"
            "<br><br><i>{french}</i>",
        75: "{german}"
            "<br><br><i>{french}</i>",
        76: "{german}"
            "<br><br><i>{french}</i>",
        77: "{german}"
            "<br><br><i>{french}</i>",
        78: "{german}"
            "<br><br><i>{french}</i>",
        79: "{german}"
            "<br><br><i>{french}</i>",
        80: "{german}"
            "<br><br><i>{french}</i>",
        81: "{german}"
            "<br><br><i>{french}</i>",
        82: "{german}"
            "<br><br><i>{french}</i>",
        83: "{german}"
            "<br><br><i>{french}</i>",
        84: "{german}"
            "<br><br><i>{french}</i>",
        85: "{german}"
            "<br><br><i>{french}</i>",
        86: "{german}"
            "<br><br><i>{french}</i>",
        87: "{german}"
            "<br><br><i>{french}</i>",
        88: "{german}"
            "<br><br><i>{french}</i>",
        89: "{german}"
            "<br><br><i>{french}</i>",
    },

    genus_goethe: {
        1: "{german}"
           "<br><br><i>{french}</i>",
        2: "{german}"
           "<br><br><i>{french}</i>",
        3: "{german}"
           "<br><br><i>{french}</i>",
        4: "{german}"
           "<br><br><i>{french}</i>",
        5: "{german}"
           "<br><br><i>{french}</i>",
        6: "{german}"
           "<br><br><i>{french}</i>",
        7: "{german}"
           "<br><br><i>{french}</i>",
        8: "{german}"
           "<br><br><i>{french}</i>",
        9: "{german}"
           "<br><br><i>{french}</i>",
        10: "{german}"
            "<br><br><i>{french}</i>",
        11: "{german}"
            "<br><br><i>{french}</i>",
        12: "{german}"
            "<br><br><i>{french}</i>",
        13: "{german}"
            "<br><br><i>{french}</i>",
        14: "{german}"
            "<br><br><i>{french}</i>",
        15: "{german}"
            "<br><br><i>{french}</i>",
        16: "{german}"
            "<br><br><i>{french}</i>",
        17: "{german}"
            "<br><br><i>{french}</i>",
        18: "{german}"
            "<br><br><i>{french}</i>",
        19: "{german}"
            "<br><br><i>{french}</i>",
        20: "{german}"
            "<br><br><i>{french}</i>",

        21: "{german}"
            "<br><br><i>{french}</i>",
        22: "{german}"
            "<br><br><i>{french}</i>",
        23: "{german}"
            "<br><br><i>{french}</i>",
        24: "{german}"
            "<br><br><i>{french}</i>",
        25: "{german}"
            "<br><br><i>{french}</i>",
        26: "{german}"
            "<br><br><i>{french}</i>",
        27: "{german}"
            "<br><br><i>{french}</i>",
        28: "{german}"
            "<br><br><i>{french}</i>",
        29: "{german}"
            "<br><br><i>{french}</i>",
        30: "{german}"
            "<br><br><i>{french}</i>",
        31: "{german}"
            "<br><br><i>{french}</i>",
        32: "{german}"
            "<br><br><i>{french}</i>",
        33: "{german}"
            "<br><br><i>{french}</i>",
        34: "{german}"
            "<br><br><i>{french}</i>",
        35: "{german}"
            "<br><br><i>{french}</i>",

        36: "{german}"
            "<br><br><i>{french}</i>",
        37: "{german}"
            "<br><br><i>{french}</i>",
        38: "{german}"
            "<br><br><i>{french}</i>",
        39: "{german}"
            "<br><br><i>{french}</i>",
        40: "{german}"
            "<br><br><i>{french}</i>",
        41: "{german}"
            "<br><br><i>{french}</i>",
        42: "{german}"
            "<br><br><i>{french}</i>",
        43: "{german}"
            "<br><br><i>{french}</i>",
        44: "{german}"
            "<br><br><i>{french}</i>",
        45: "{german}"
            "<br><br><i>{french}</i>",
        46: "{german}"
            "<br><br><i>{french}</i>",
        47: "{german}"
            "<br><br><i>{french}</i>",
        48: "{german}"
            "<br><br><i>{french}</i>",
        49: "{german}"
            "<br><br><i>{french}</i>",
        50: "{german}"
            "<br><br><i>{french}</i>",
        51: "{german}"
            "<br><br><i>{french}</i>",
        52: "{german}"
            "<br><br><i>{french}</i>",
        53: "{german}"
            "<br><br><i>{french}</i>",
        54: "{german}"
            "<br><br><i>{french}</i>",
        55: "{german}"
            "<br><br><i>{french}</i>",
        56: "{german}"
            "<br><br><i>{french}</i>",
        57: "{german}"
            "<br><br><i>{french}</i>",
        58: "{german}"
            "<br><br><i>{french}</i>",
        59: "{german}"
            "<br><br><i>{french}</i>",
        60: "{german}"
            "<br><br><i>{french}</i>",
        61: "{german}"
            "<br><br><i>{french}</i>",
        62: "{german}"
            "<br><br><i>{french}</i>",
        63: "{german}"
            "<br><br><i>{french}</i>",
        64: "{german}"
            "<br><br><i>{french}</i>",
        65: "{german}"
            "<br><br><i>{french}</i>",
        66: "{german}"
            "<br><br><i>{french}</i>",
        67: "{german}"
            "<br><br><i>{french}</i>",
        68: "{german}"
            "<br><br><i>{french}</i>",
        69: "{german}"
            "<br><br><i>{french}</i>",
        70: "{german}"
            "<br><br><i>{french}</i>",
        71: "{german}"
            "<br><br><i>{french}</i>",
        72: "{german}"
            "<br><br><i>{french}</i>",
        73: "{german}"
            "<br><br><i>{french}</i>",
        74: "{german}"
            "<br><br><i>{french}</i>",
        75: "{german}"
            "<br><br><i>{french}</i>",
        76: "{german}"
            "<br><br><i>{french}</i>",
        77: "{german}"
            "<br><br><i>{french}</i>",
        78: "{german}"
            "<br><br><i>{french}</i>",
        79: "{german}"
            "<br><br><i>{french}</i>",
        80: "{german}"
            "<br><br><i>{french}</i>",
        81: "{german}"
            "<br><br><i>{french}</i>",
        82: "{german}"
            "<br><br><i>{french}</i>",
        83: "{german}"
            "<br><br><i>{french}</i>",
        84: "{german}"
            "<br><br><i>{french}</i>",
        85: "{german}"
            "<br><br><i>{french}</i>",
        86: "{german}"
            "<br><br><i>{french}</i>",
        87: "{german}"
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
            "<br><br>Correct answer(s): {correct_answers}",

        17: "{french} = {answer}",
        18: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
        19: "{french} = {answer}",
        20: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>Correct answer(s): {correct_answers}",

        21: "{french} = {answer}",
        22: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>Correct answer(s): {correct_answers}",

        23: "Génitif {previous_question}: {answer}",
        24: "{german}"
            "<br><br><i>{french}</i>"
            "<br><br>Correct answer(s): {correct_answers}",
    },

}
