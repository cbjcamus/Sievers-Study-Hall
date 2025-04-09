from data_processing.exercises import (
    praepositionen_grammatik, praepositionen_verben, praepositionen_adjektive, praepositionen_nomen,
    artikel, pronomen, konnektoren, adjektivdeklinationen,
    praesens, imperativ, partizip_II, praeteritum, konjunktiv_II, konjunktiv_I, partizip_I,
    adverbien, verben, trennbare_verben, deverbale_nomen
)

# bullet point \u25CF
# arrow &#8594

QUESTION_TEMPLATES = {

    praepositionen_grammatik: {
        1: "Translate the following preposition:"
           "<br><br>{question}",
        2: "Complete the following sentence with the connector that fits:"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        3: "Complete the following sentence with the connector that fits:"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        4: "Complete the following sentence with the connector that fits:"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        5: "Complete the following sentence with the connector that fits:"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        6: "Complete the following sentence with the connector that fits:"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        7: "Complete the following sentence with the connector that fits:"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        8: "Complete the following sentence with the connector that fits:"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        9: "Complete the following sentence with the connector that fits:"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        10: "Complete the following sentence with the connector that fits:"
            "<br><br>{question}"
            "<br><br><i>{english}</i>",
        11: "Complete the following sentence with the connector that fits:"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        12: "Complete the following sentence with the connector that fits:"
            "<br><br>{question}"
            "<br><br><i>{english}</i>",
        13: "Complete the following sentence with the connector that fits:"
            "<br><br>{question}"
            "<br><br><i>{english}</i>",
        14: "Translate the following preposition:"
            "<br><br>{question}",
        15: "Complete the following sentence with the connector that fits:"
            "<br><br>{question}"
            "<br><br><i>{english}</i>",
        16: "Complete the following sentence with the connector that fits:"
            "<br><br>{question}"
            "<br><br><i>{english}</i>",
        17: "Translate the following preposition:"
            "<br><br>{question}",
        18: "Complete the following sentence with the connector that fits:"
            "<br><br>{question}"
            "<br><br><i>{english}</i>",
        19: "Translate the following preposition:"
            "<br><br>{question}",
        20: "Complete the following sentence with the connector that fits:"
            "<br><br>{question}"
            "<br><br><i>{english}</i>",
    },

    praepositionen_verben: {
        1: "Write the preposition that match the following verb:"
           "<br><br>{question} = {german} _____",
        2: "Complete the following sentence with the preposition that fits:"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        3: "Write the preposition that match the following verb:"
           "<br><br>{question} = {german} _____",
        4: "Complete the following sentence with the preposition that fits:"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        5: "Write the preposition that match the following verb:"
           "<br><br>{question} = {german} _____",
        6: "Complete the following sentence with the preposition that fits:"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        7: "Write the preposition that match the following verb:"
           "<br><br>{question} = {german} _____",
        8: "Complete the following sentence with the preposition that fits:"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        9: "Complete the following sentence with the Da-Wort that fits:"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        10: "Complete the following sentence with the Wo-Wort that fits:"
            "<br><br>{question}"
            "<br><br><i>{english}</i>",
        11: "Write the preposition that match the following verb:"
            "<br><br>{question} = {german} _____",
        12: "Complete the following sentence with the preposition that fits:"
            "<br><br>{question}"
            "<br><br><i>{english}</i>",
        13: "Write the preposition that match the following verb:"
            "<br><br>{question} = {german} _____",
        14: "Complete the following sentence with the preposition that fits:"
            "<br><br>{question}"
            "<br><br><i>{english}</i>",
        15: "Write the preposition that match the following verb:"
            "<br><br>{question} = {german} _____",
        16: "Complete the following sentence with the preposition that fits:"
            "<br><br>{question}"
            "<br><br><i>{english}</i>",
        17: "Write the preposition that match the following verb:"
            "<br><br>{question} = {german} _____",
        18: "Complete the following sentence with the preposition that fits:"
            "<br><br>{question}"
            "<br><br><i>{english}</i>",
        19: "Write the preposition that match the following verb:"
            "<br><br>{question} = {german} _____",
        20: "Complete the following sentence with the preposition that fits:"
            "<br><br>{question}"
            "<br><br><i>{english}</i>",
        21: "Write the preposition that match the following verb:"
            "<br><br>{question} = {german} _____",
        22: "Complete the following sentence with the preposition that fits:"
            "<br><br>{question}"
            "<br><br><i>{english}</i>",
    },

    praepositionen_adjektive: {
        1: "Write the preposition that match the following adjective:"
            "<br><br>{question} = {german} _____",
        2: "Complete the following sentence with the preposition that fits:"
            "<br><br>{question}"
            "<br><br><i>{english}</i>",
        3: "Write the preposition that match the following adjective:"
           "<br><br>{question} = {german} _____",
        4: "Complete the following sentence with the preposition that fits:"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        5: "Write the preposition that match the following adjective:"
           "<br><br>{question} = {german} _____",
        6: "Complete the following sentence with the preposition that fits:"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
    },

    praepositionen_nomen: {
        1: "Write the preposition that match the following noun:"
            "<br><br>{question} = {german} _____",
        2: "Complete the following sentence with the preposition that fits:"
            "<br><br>{question}"
            "<br><br><i>{english}</i>",
        3: "Write the preposition that match the following noun:"
           "<br><br>{question} = {german} _____",
        4: "Complete the following sentence with the preposition that fits:"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        5: "Write the preposition that match the following noun:"
           "<br><br>{question} = {german} _____",
        6: "Complete the following sentence with the preposition that fits:"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        7: "Write the preposition that match the following noun:"
           "<br><br>{question} = {german} _____",
        8: "Complete the following sentence with the preposition that fits:"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        9: "Write the preposition that match the following noun:"
           "<br><br>{question} = {german} _____",
        10: "Complete the following sentence with the preposition that fits:"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
    },

    artikel: {
        1: "Complete the following sentence with the definite article that fits:"
           "<br><br>{question}",
        2: "Translate the following article:"
            "<br><br>{question}",
        3: "Complete the following sentence with the article that fits:"
            "<br><br>{question}"
            "<br><br><i>{english}</i>",
        4: "Translate the following article:"
            "<br><br>{question}",
        5: "Complete the following sentence with the article that fits:"
            "<br><br>{question}"
            "<br><br><i>{english}</i>",
    },

    pronomen: {
        1: "Complete the following sentence with the nominative pronoun that fits:"
           "<br><br>{question} \u25CF {person}",
        2: "Complete the following sentence with the accusative pronoun that fits:"
           "<br><br>{question} \u25CF {person}",
        3: "Complete the following sentence with the dative pronoun that fits:"
           "<br><br>{question} \u25CF {person}",
        4: "Complete the following sentence with the pronoun that fits:"
           "<br><br>{question} \u25CF {person}",
        5: "Complete the following sentence with the reflexive pronoun that fits:"
           "<br><br>{question} \u25CF {person}",
        6: "Complete the following sentence with the pronoun that fits:"
           "<br><br>{question} \u25CF {person}",
        7: "Translate the following pronoun:"
           "<br><br>{question}",
        8: "Complete the following sentence with the pronoun that fits:"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        9: "Complete the following sentence with the nominative relative pronoun that fits:"
           "<br><br>{question}",
        10: "Complete the following sentence with the accusative relative pronoun that fits:"
            "<br><br>{question}",
        11: "Complete the following sentence with the dative relative pronoun that fits:"
            "<br><br>{question}",
        12: "Complete the following sentence with the genitive relative pronoun that fits:"
            "<br><br>{question}",
        13: "Complete the following sentence with the relative pronoun that fits:"
            "<br><br>{question}",
        14: "Complete the following sentence with the relative pronoun that fits:"
            "<br><br>{question}",
        15: "Complete the following sentence with the relative pronoun that fits – there may be more than one option:"
            "<br><br>{question}",
    },

    konnektoren: {
        1: "Translate the following connector:"
           "<br><br>{question} \u25CF {case}",
        2: "Complete the following sentence with the connector that fits:"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        3: "Translate the following connector:"
           "<br><br>{question} \u25CF {case}",
        4: "Complete the following sentence with the connector that fits:"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        5: "Translate the following connector:"
           "<br><br>{question} \u25CF {case}",
        6: "Complete the following sentence with the connector that fits:"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        7: "Find a synonym for the following connector:"
           "<br><br>{question}",
        8: "Translate the following connector:"
           "<br><br>{question} \u25CF {case}",
        9: "Complete the following sentence with the connector that fits:"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        10: "Find a synonym for the following connector:"
           "<br><br>{question}",
        11: "Translate the following connector:"
           "<br><br>{question} \u25CF {case}",
        12: "Complete the following sentence with the connector that fits:"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        13: "Find a synonym for the following connector:"
           "<br><br>{question}",
    },



    adjektivdeklinationen: {
        1: "Complete the sentence with the correct form of the specified adjective:"
           "<br><br>{question} \u25CF {case} \u25CF {adjective}",
        2: "Complete the sentence with the correct form of the specified adjective:"
           "<br><br>{question} \u25CF {adjective}",
        3: "Complete the sentence with the correct form of the specified adjective:"
           "<br><br>{question} \u25CF {adjective}",
        4: "Complete the sentence with the correct form of the specified adjective:"
           "<br><br>{question} \u25CF {adjective}",
        5: "Complete the sentence with the correct form of the specified adjective:"
           "<br><br>{question} \u25CF {adjective}",
        6: "Complete the sentence with the correct form of the specified adjective:"
           "<br><br>{question} \u25CF {adjective}",
        7: "Complete the sentence with the correct form of the specified adjective:"
           "<br><br>{question} \u25CF {adjective}",
        8: "Complete the sentence with the correct form of the specified adjective:"
           "<br><br>{question} \u25CF {adjective}",
        9: "Complete the sentence with the correct form of the specified adjective:"
           "<br><br>{question} \u25CF {case} \u25CF {adjective}",
        10: "Complete the sentence with the correct form of the specified adjective:"
            "<br><br>{question} \u25CF {adjective}",
        11: "Complete the sentence with the correct form of the specified adjective:"
            "<br><br>{question} \u25CF {adjective}",
        12: "Complete the sentence with the correct form of the specified adjective:"
            "<br><br>{question} \u25CF {adjective}",
        13: "Complete the sentence with the correct form of the specified adjective:"
            "<br><br>{question} \u25CF {adjective}",
        14: "Complete the sentence with the correct form of the specified adjective:"
            "<br><br>{question} \u25CF {adjective}",
        15: "Complete the sentence with the correct form of the specified adjective:"
            "<br><br>{question} \u25CF {case} \u25CF {adjective}",
        16: "Complete the sentence with the correct form of the specified adjective:"
            "<br><br>{question} \u25CF {adjective}",
    },

    praesens: {
        1: "Conjugate the following verb in the present tense:<br>"
           "<br>"
           "{alinea}{question} \u25CF {person} _____",
        2: "Conjugate the following verb in the present tense:<br>"
           "<br>"
           "{alinea}{question} \u25CF {person} _____",
        3: "Conjugate the following verb in the present tense:<br>"
           "<br>"
           "{alinea}{question} \u25CF {person} _____",
        4: "Conjugate the following verb in the present tense:<br>"
           "<br>"
           "{alinea}{question} \u25CF {person} _____",
        5: "Conjugate the following verb in the present tense:<br>"
           "<br>"
           "{alinea}{question} \u25CF {person} _____",
        6: "Conjugate the following verb in the present tense:<br>"
           "<br>"
           "{alinea}{question} \u25CF {person} _____",
        7: "Conjugate the following verb in the present tense:<br>"
           "<br>"
           "{alinea}{question} \u25CF {person} _____",
        8: "Conjugate the following verb in the present tense:<br>"
           "<br>"
           "{alinea}{question} \u25CF {person} _____",
        9: "Conjugate the following verb in the present tense:<br>"
           "<br>"
           "{alinea}{question} \u25CF {person} _____",
        10: "Conjugate the following verb in the present tense:<br>"
            "<br>"
            "{alinea}{question} \u25CF {person} _____",
        11: "Conjugate the following verb in the present tense:<br>"
            "<br>"
            "{alinea}{question} \u25CF {person} _____",
        12: "Conjugate the following verb in the present tense:<br>"
            "<br>"
            "{alinea}{question} \u25CF {person} _____",
        13: "Conjugate the following verb in the present tense:<br>"
            "<br>"
            "{alinea}{question} \u25CF {person} _____",
        14: "Conjugate the following verb in the present tense:<br>"
            "<br>"
            "{alinea}{question} \u25CF {person} _____",
        15: "Conjugate the following verb in the present tense:<br>"
            "<br>"
            "{alinea}{question} \u25CF {person} _____",
        16: "Conjugate the following verb in the present tense:<br>"
            "<br>"
            "{alinea}{question} \u25CF {person} _____",
        17: "Conjugate the following verb in the present tense:<br>"
            "<br>"
            "{alinea}{question} \u25CF {person} _____",
        18: "Conjugate the following verb in the present tense:<br>"
            "<br>"
            "{alinea}{question} \u25CF {person} _____",
        19: "Conjugate the following verb in the present tense:<br>"
            "<br>"
            "{alinea}{question} \u25CF {person} _____",
        20: "Conjugate the following verb in the present tense:<br>"
            "<br>"
            "{alinea}{question} \u25CF {person} _____",
        21: "Conjugate the following verb in the present tense:<br>"
            "<br>"
            "{alinea}{question} \u25CF {person} _____",
        22: "Conjugate the following verb in the present tense:<br>"
            "<br>"
            "{alinea}{question} \u25CF {person} _____",
        23: "Conjugate the following verb in the present tense:<br>"
            "<br>"
            "{alinea}{question} \u25CF {person} _____",
        24: "Conjugate the following verb in the present tense:<br>"
            "<br>"
            "{alinea}{question} \u25CF {person} _____",
    },

    partizip_II: {
        1: "Write the Partizip II of the following verb:"
           "<br><br>{question}",
        2: "Write the Partizip II of the following verb:"
           "<br><br>{question}",
        3: "Write the Partizip II of the following verb:"
           "<br><br>{question}",
        4: "Write the Partizip II of the following verb:"
           "<br><br>{question}",
        5: "Write the Partizip II of the following verb:"
           "<br><br>{question}",
        6: "Write the Partizip II of the following verb:"
           "<br><br>{question}",
        7: "Write the Partizip II of the following verb:"
           "<br><br>{question}",
        8: "Write the Partizip II of the following verb:"
           "<br><br>{question}",
        9: "Write the Partizip II of the following verb:"
           "<br><br>{question}",
        10: "Write the Partizip II of the following verb:"
            "<br><br>{question}",
        11: "Write the Partizip II of the following verb:"
            "<br><br>{question}",
        12: "Write the Partizip II of the following verb:"
            "<br><br>{question}",
        13: "Write the Partizip II of the following verb:"
            "<br><br>{question}",
        14: "Write the Partizip II of the following verb:"
            "<br><br>{question}",
        15: "Write the Partizip II of the following verb:"
            "<br><br>{question}",
        16: "Write the Partizip II of the following verb:"
            "<br><br>{question}",
        17: "Write the Partizip II of the following verb:"
            "<br><br>{question}",
        18: "Write the Partizip II of the following verb:"
            "<br><br>{question}",
        19: "Write the Partizip II of the following verb:"
            "<br><br>{question}",
        20: "Write the Partizip II of the following verb:"
            "<br><br>{question}",
    },

    praeteritum: {
        1: "Conjugate the following verb in the Präteritum:"
           "<br><br>{question} \u25CF {person} _____",
        2: "Conjugate the following verb in the Präteritum (3rd Person Singular):"
           "<br><br>{question} \u25CF er/sie/es _____",
        3: "Conjugate the following verb in the Präteritum (3rd Person Singular):"
           "<br><br>{question} \u25CF er/sie/es _____",
        4: "Conjugate the following verb in the Präteritum (3rd Person Singular):"
           "<br><br>{question} \u25CF er/sie/es _____",
        5: "Conjugate the following verb in the Präteritum (3rd Person Singular):"
           "<br><br>{question} \u25CF er/sie/es _____",
        6: "Conjugate the following verb in the Präteritum (3rd Person Singular):"
           "<br><br>{question} \u25CF er/sie/es _____",
        7: "Conjugate the following verb in the Präteritum (3rd Person Singular):"
           "<br><br>{question} \u25CF er/sie/es _____",
        8: "Conjugate the following verb in the Präteritum (3rd Person Singular):"
           "<br><br>{question} \u25CF er/sie/es _____",
        9: "Conjugate the following verb in the Präteritum (3rd Person Singular):"
           "<br><br>{question} \u25CF er/sie/es _____",
        10: "Conjugate the following verb in the Präteritum (3rd Person Singular):"
            "<br><br>{question} \u25CF er/sie/es _____",
        11: "Conjugate the following verb in the Präteritum (3rd Person Singular):"
            "<br><br>{question} \u25CF er/sie/es _____",
        12: "Conjugate the following verb in the Präteritum (3rd Person Singular):"
            "<br><br>{question} \u25CF er/sie/es _____",
        13: "Conjugate the following verb in the Präteritum (3rd Person Singular):"
            "<br><br>{question} \u25CF er/sie/es _____",
        14: "Conjugate the following verb in the Präteritum (3rd Person Singular):"
            "<br><br>{question} \u25CF er/sie/es _____",
        15: "Conjugate the following verb in the Präteritum (3rd Person Singular):"
            "<br><br>{question} \u25CF er/sie/es _____",
        16: "Conjugate the following verb in the Präteritum (3rd Person Singular):"
            "<br><br>{question} \u25CF er/sie/es _____",
        17: "Conjugate the following verb in the Präteritum (3rd Person Singular):"
            "<br><br>{question} \u25CF er/sie/es _____",
        18: "Conjugate the following verb in the Präteritum (3rd Person Singular):"
            "<br><br>{question} \u25CF er/sie/es _____",
        19: "Conjugate the following verb in the Präteritum (3rd Person Singular):"
            "<br><br>{question} \u25CF er/sie/es _____",
        20: "Conjugate the following verb in the Präteritum (3rd Person Singular):"
            "<br><br>{question} \u25CF er/sie/es _____",
        21: "Conjugate the following verb in the Präteritum (3rd Person Singular):"
            "<br><br>{question} \u25CF er/sie/es _____",
    },

    imperativ: {
        1: "Conjugate the following verb in the Imperativ:"
           "<br><br>{question} \u25CF {person} \u25CF _____",
        2: "Conjugate the following verb in the Imperativ:"
           "<br><br>{question} \u25CF {person} \u25CF _____",
        3: "Conjugate the following verb in the Imperativ:"
           "<br><br>{question} \u25CF {person} \u25CF _____",
        4: "Conjugate the following verb in the Imperativ:"
           "<br><br>{question} \u25CF {person} \u25CF _____",
        5: "Conjugate the following verb in the Imperativ:"
           "<br><br>{question} \u25CF {person} \u25CF _____",
        6: "Conjugate the following verb in the Imperativ:"
           "<br><br>{question} \u25CF {person} \u25CF _____",
    },

    konjunktiv_II: {
        1: "Conjugate the following verb in the Konjunktiv II:"
           "<br><br>{question} \u25CF {person} _____",
    },

    konjunktiv_I: {
        1: "Conjugate the following verb in the Konjunktiv I:"
           "<br><br>{question} \u25CF {person} _____",
        2: "Conjugate the following verb in the Konjunktiv I:"
           "<br><br>{question} \u25CF {person} _____",
        3: "Conjugate the following verb in the Konjunktiv I:"
           "<br><br>{question} \u25CF {person} _____",
        4: "Conjugate the following verb in the Konjunktiv I:"
           "<br><br>{question} \u25CF {person} _____",
        5: "Conjugate the following verb in the Konjunktiv I:"
           "<br><br>{question} \u25CF {person} _____",
        6: "Conjugate the following verb in the Konjunktiv I:"
           "<br><br>{question} \u25CF {person} _____",
    },

    partizip_I: {
        1: "Write the Partizip I of the following verb:"
           "<br><br>{question} \u25CF English: {english}",
        2: "Write the Partizip I of the following verb:"
           "<br><br>{question} \u25CF English: {english}",
        3: "Write the Partizip I of the following verb:"
           "<br><br>{question} \u25CF English: {english}",
    },

    adverbien: {
        1: "Translate the following adverb:"
           "<br><br>{question}",
        2: "Complete the following sentence with the adverb that fits:¨"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        3: "Translate the following adverb:"
           "<br><br>{question}",
        4: "Complete the following sentence with the adverb that fits:¨"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        5: "Translate the following adverb:"
           "<br><br>{question}",
        6: "Complete the following sentence with the adverb that fits:¨"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        7: "Translate the following adverb:"
           "<br><br>{question}",
        8: "Complete the following sentence with the adverb that fits:¨"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        9: "Translate the following adverb:"
           "<br><br>{question}",
        10: "Complete the following sentence with the adverb that fits:¨"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        11: "Translate the following adverb:"
           "<br><br>{question}",
        12: "Complete the following sentence with the adverb that fits:¨"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        13: "Translate the following adverb:"
           "<br><br>{question}",
        14: "Complete the following sentence with the adverb that fits:¨"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        15: "Translate the following adverb:"
           "<br><br>{question}",
        16: "Complete the following sentence with the adverb that fits:¨"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        17: "Translate the following adverb:"
           "<br><br>{question}",
        18: "Complete the following sentence with the adverb that fits:¨"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        19: "Translate the following adverb:"
            "<br><br>{question}",
        20: "Complete the following sentence with the adverb that fits:¨"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        21: "Translate the following adverb:"
           "<br><br>{question}",
        22: "Complete the following sentence with the adverb that fits:¨"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        23: "Translate the following adverb:"
           "<br><br>{question}",
        24: "Complete the following sentence with the adverb that fits:¨"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        25: "Translate the following adverb:"
            "<br><br>{question}",
        26: "Complete the following sentence with the adverb that fits:¨"
            "<br><br>{question}"
            "<br><br><i>{english}</i>",
        27: "Translate the following adverb:"
            "<br><br>{question}",
        28: "Complete the following sentence with the adverb that fits:¨"
            "<br><br>{question}"
            "<br><br><i>{english}</i>",
        29: "Translate the following adverb:"
            "<br><br>{question}",
        30: "Complete the following sentence with the adverb that fits:¨"
            "<br><br>{question}"
            "<br><br><i>{english}</i>",
        31: "Translate the following adverb:"
            "<br><br>{question}",
        32: "Complete the following sentence with the adverb that fits:¨"
            "<br><br>{question}"
            "<br><br><i>{english}</i>",
    },

    verben: {
        1: "Translate the following verb:"
           "<br><br>{question}",
        2: "Translate the following verb:"
           "<br><br>{question}",
        3: "Translate the following verb:"
           "<br><br>{question}",
        4: "Translate the following verb:"
           "<br><br>{question}",
        5: "Translate the following verb:"
           "<br><br>{question}",
        6: "Translate the following verb:"
           "<br><br>{question}",
        7: "Translate the following verb:"
           "<br><br>{question}",
        8: "Translate the following verb:"
           "<br><br>{question}",
        9: "Translate the following verb:"
           "<br><br>{question}",
        10: "Translate the following verb:"
            "<br><br>{question}",
        11: "Translate the following verb:"
            "<br><br>{question}",
        12: "Translate the following verb:"
            "<br><br>{question}",
        13: "Translate the following verb:"
            "<br><br>{question}",
        14: "Translate the following verb:"
            "<br><br>{question}",
        15: "Translate the following verb:"
            "<br><br>{question}",
        16: "Translate the following verb:"
            "<br><br>{question}",
        17: "Translate the following verb:"
            "<br><br>{question}",
        18: "Translate the following verb:"
            "<br><br>{question}",
        19: "Translate the following verb:"
            "<br><br>{question}",
        20: "Translate the following verb:"
            "<br><br>{question}",
    },

    trennbare_verben: {
        1: "Translate the following (un)trennbare verb based on the specified root verb:"
           "<br><br>{english} &#8594; {german}" 
           "<br><br>{question} &#8594; _____ ",
        2: "Translate the following (un)trennbare verb based on the specified prefix:"
           "<br><br>{question} \u25CF {prefix}",
        3: "Translate the following (un)trennbare verb based on the specified root verb:"
           "<br><br>{english} &#8594; {german}" 
           "<br><br>{question} &#8594; _____ ",
        4: "Translate the following (un)trennbare verb based on the specified root verb:"
           "<br><br>{english} &#8594; {german}" 
           "<br><br>{question} &#8594; _____ ",
        5: "Translate the following (un)trennbare verb based on the specified prefix:"
           "<br><br>{question} \u25CF {prefix}",
        6: "Translate the following (un)trennbare verb based on the specified prefix:"
           "<br><br>{question} \u25CF {prefix}",
        7: "Translate the following (un)trennbare verb based on the specified root verb:"
           "<br><br>{english} &#8594; {german}" 
           "<br><br>{question} &#8594; _____ ",
        8: "Translate the following (un)trennbare verb based on the specified root verb:"
           "<br><br>{english} &#8594; {german}" 
           "<br><br>{question} &#8594; _____ ",
        9: "Translate the following (un)trennbare verb based on the specified root verb:"
           "<br><br>{english} &#8594; {german}"
           "<br><br>{question} &#8594; _____ ",
        10: "Translate the following (un)trennbare verb based on the specified prefix:"
           "<br><br>{question} \u25CF {prefix}",
        11: "Translate the following (un)trennbare verb based on the specified prefix:"
           "<br><br>{question} \u25CF {prefix}",
        12: "Translate the following (un)trennbare verb based on the specified prefix:"
           "<br><br>{question} \u25CF {prefix}",
    },

    deverbale_nomen: {
        1: "Complete the blank with the noun that fits:"
           "<br><br>{english} &#8594 {german}"
           "<br><br>{question} &#8594 _____",
        2: "Complete the blank with the noun that fits:"
           "<br><br>{english} &#8594 {german}"
           "<br><br>{question} &#8594 _____",
        3: "Complete the blank with the noun that fits:"
           "<br><br>{english} &#8594 {german}"
           "<br><br>{question} &#8594 _____",
        4: "Complete the blank with the noun that fits:"
           "<br><br>{english} &#8594 {german}"
           "<br><br>{question} &#8594 _____",
        5: "Complete the blank with the noun that fits:"
           "<br><br>{english} &#8594 {german}"
           "<br><br>{question} &#8594 _____",
        6: "Complete the blank with the noun that fits:"
           "<br><br>{english} &#8594 {german}"
           "<br><br>{question} &#8594 _____",
        7: "Complete the blank with the noun that fits:"
           "<br><br>{english} &#8594 {german}"
           "<br><br>{question} &#8594 _____",
        8: "Complete the blank with the noun that fits:"
           "<br><br>{english} &#8594 {german}"
           "<br><br>{question} &#8594 _____",
        9: "Complete the blank with the noun that fits:"
           "<br><br>{english} &#8594 {german}"
           "<br><br>{question} &#8594 _____",
        10: "Complete the blank with the noun that fits:"
            "<br><br>{english} &#8594 {german}"
            "<br><br>{question} &#8594 _____",
        11: "Complete the blank with the noun that fits:"
            "<br><br>{english} &#8594 {german}"
            "<br><br>{question} &#8594 _____",
        12: "Complete the blank with the noun that fits:"
            "<br><br>{english} &#8594 {german}"
            "<br><br>{question} &#8594 _____",
        13: "Complete the blank with the noun that fits:"
            "<br><br>{english} &#8594 {german}"
            "<br><br>{question} &#8594 _____",
        14: "Complete the blank with the noun that fits:"
            "<br><br>{english} &#8594 {german}"
            "<br><br>{question} &#8594 _____",
        15: "Complete the blank with the noun that fits:"
            "<br><br>{english} &#8594 {german}"
            "<br><br>{question} &#8594 _____",
        16: "Complete the blank with the noun that fits:"
            "<br><br>{english} &#8594 {german}"
            "<br><br>{question} &#8594 _____",
    },

}
