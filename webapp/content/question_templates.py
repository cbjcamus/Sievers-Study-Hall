from data_processing.exercises import (artikel, pronomen, konnektoren, praepositionen_grammatik, adjektivdeklinationen,
                                       praesens, praepositionen_konjugation, imperativ, perfekt, praeteritum,
                                       konjunktiv,
                                       partizip_I,
                                       verben, adjektive, adverbien, deverbale_substantive, trennbare_verben)

QUESTION_TEMPLATES = {
    artikel: {
        1: "Complete the following sentence with the definite article that fits:"
           "<br><br>{question}",
        2: "Translate the following article:"
            "<br><br><strong>{question}</strong>",
        3: "Complete the following sentence with the article that fits:"
            "<br><br>{question}"
            "<br><br><i>{english}</i>",
        4: "Translate the following article:"
            "<br><br><strong>{question}</strong>",
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
           "<br><br><strong>{question}</strong>",
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
    },

    konnektoren: {
        1: "Translate the following connector:"
           "<br><br><strong>{question}</strong>",
        2: "Complete the following sentence with the connector that fits:"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        3: "Translate the following connector:"
           "<br><br><strong>{question}</strong>",
        4: "Complete the following sentence with the connector that fits:"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        5: "Translate the following connector:"
           "<br><br><strong>{question}</strong>",
        6: "Complete the following sentence with the connector that fits:"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        7: "Translate the following connector:"
           "<br><br><strong>{question}</strong>",
        8: "Complete the following sentence with the connector that fits:"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
    },

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
        9: "Translate the following preposition:"
           "<br><br>{question}",
        10: "Complete the following sentence with the connector that fits:"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        11: "Translate the following preposition:"
            "<br><br>{question}",
        12: "Complete the following sentence with the connector that fits:"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        13: "Complete the following sentence with the connector that fits:"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        14: "Complete the following sentence with the connector that fits:"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        15: "Complete the following sentence with the connector that fits:"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        16: "Translate the following preposition:"
            "<br><br>{question}",
        17: "Complete the following sentence with the connector that fits:"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
    },

    adjektivdeklinationen: {
        1: "Complete the sentence with the correct form of the specified adjektive:"
           "<br><br>{question} \u25CF {case} \u25CF {adjective}",
        2: "Complete the sentence with the correct form of the specified adjektive:"
           "<br><br>{question} \u25CF {adjective}",
        3: "Complete the sentence with the correct form of the specified adjektive:"
           "<br><br>{question} \u25CF {adjective}",
        4: "Complete the sentence with the correct form of the specified adjektive:"
           "<br><br>{question} \u25CF {adjective}",
        5: "Complete the sentence with the correct form of the specified adjektive:"
           "<br><br>{question} \u25CF {adjective}",
        6: "Complete the sentence with the correct form of the specified adjektive:"
           "<br><br>{question} \u25CF {adjective}",
        7: "Complete the sentence with the correct form of the specified adjektive:"
           "<br><br>{question} \u25CF {adjective}",
        8: "Complete the sentence with the correct form of the specified adjektive:"
           "<br><br>{question} \u25CF {adjective}",
        9: "Complete the sentence with the correct form of the specified adjektive:"
           "<br><br>{question} \u25CF {case} \u25CF {adjective}",
        10: "Complete the sentence with the correct form of the specified adjektive:"
            "<br><br>{question} \u25CF {adjective}",
        11: "Complete the sentence with the correct form of the specified adjektive:"
            "<br><br>{question} \u25CF {adjective}",
        12: "Complete the sentence with the correct form of the specified adjektive:"
            "<br><br>{question} \u25CF {adjective}",
        13: "Complete the sentence with the correct form of the specified adjektive:"
            "<br><br>{question} \u25CF {adjective}",
        14: "Complete the sentence with the correct form of the specified adjektive:"
            "<br><br>{question} \u25CF {adjective}",
        15: "Complete the sentence with the correct form of the specified adjektive:"
            "<br><br>{question} \u25CF {case} \u25CF {adjective}",
        16: "Complete the sentence with the correct form of the specified adjektive:"
            "<br><br>{question} \u25CF {adjective}",
    },

    praesens: {
        1: "Write the present tense of the following verb:<br>"
           "<br>"
           "{alinea}{question} \u25CF {person} _____",
        2: "Write the present tense of the following verb:<br>"
           "<br>"
           "{alinea}{question} \u25CF {person} _____",
        3: "Write the present tense of the following verb:<br>"
           "<br>"
           "{alinea}{question} \u25CF {person} _____",
        4: "Write the present tense of the following verb:<br>"
           "<br>"
           "{alinea}{question} \u25CF {person} _____",
        5: "Write the present tense of the following verb:<br>"
           "<br>"
           "{alinea}{question} \u25CF {person} _____",
        6: "Write the present tense of the following verb:<br>"
           "<br>"
           "{alinea}{question} \u25CF {person} _____",
        7: "Write the present tense of the following verb:<br>"
           "<br>"
           "{alinea}{question} \u25CF {person} _____",
        8: "Write the present tense of the following verb:<br>"
           "<br>"
           "{alinea}{question} \u25CF {person} _____",
        9: "Write the present tense of the following verb:<br>"
           "<br>"
           "{alinea}{question} \u25CF {person} _____",
        10: "Write the present tense of the following verb:<br>"
            "<br>"
            "{alinea}{question} \u25CF {person} _____",
        11: "Write the present tense of the following verb:<br>"
            "<br>"
            "{alinea}{question} \u25CF {person} _____",
        12: "Write the present tense of the following verb:<br>"
            "<br>"
            "{alinea}{question} \u25CF {person} _____",
        13: "Write the present tense of the following verb:<br>"
            "<br>"
            "{alinea}{question} \u25CF {person} _____",
        14: "Write the present tense of the following verb:<br>"
            "<br>"
            "{alinea}{question} \u25CF {person} _____",
        15: "Write the present tense of the following verb:<br>"
            "<br>"
            "{alinea}{question} \u25CF {person} _____",
        16: "Write the present tense of the following verb:<br>"
            "<br>"
            "{alinea}{question} \u25CF {person} _____",
        17: "Write the present tense of the following verb:<br>"
            "<br>"
            "{alinea}{question} \u25CF {person} _____",
        18: "Write the present tense of the following verb:<br>"
            "<br>"
            "{alinea}{question} \u25CF {person} _____",
        19: "Write the present tense of the following verb:<br>"
            "<br>"
            "{alinea}{question} \u25CF {person} _____",
        20: "Write the present tense of the following verb:<br>"
            "<br>"
            "{alinea}{question} \u25CF {person} _____",
        21: "Write the present tense of the following verb:<br>"
            "<br>"
            "{alinea}{question} \u25CF {person} _____",
        22: "Write the present tense of the following verb:<br>"
            "<br>"
            "{alinea}{question} \u25CF {person} _____",
        23: "Write the present tense of the following verb:<br>"
            "<br>"
            "{alinea}{question} \u25CF {person} _____",
        24: "Write the present tense of the following verb:<br>"
            "<br>"
            "{alinea}{question} \u25CF {person} _____",
    },

    praepositionen_konjugation: {
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
        9: "Write the preposition that match the following verb:"
           "<br><br>{question} = {german} _____",
        10: "Complete the following sentence with the preposition that fits:"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        11: "Write the preposition that match the following verb:"
           "<br><br>{question} = {german} _____",
        12: "Complete the following sentence with the preposition that fits:"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        13: "Complete the following sentence with the preposition that fits:"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        14: "Complete the following sentence with the preposition that fits:"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        15: "Complete the following sentence with the preposition that fits:"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        16: "Write the preposition that match the following verb:"
           "<br><br>{question} = {german} _____",
        17: "Complete the following sentence with the preposition that fits:"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        18: "Write the preposition that match the following noun:"
           "<br><br>{question} = {german} _____",
        19: "Complete the following sentence with the preposition that fits:"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        20: "Write the preposition that match the following noun:"
            "<br><br>{question} = {german} _____",
        21: "Complete the following sentence with the preposition that fits:"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        22: "Write the preposition that match the following noun:"
            "<br><br>{question} = {german} _____",
        23: "Complete the following sentence with the preposition that fits:"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        24: "Write the preposition that match the following adjective:"
           "<br><br>{question} = {german} _____",
        25: "Complete the following sentence with the preposition that fits:"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        26: "Write the preposition that match the following verb:"
           "<br><br>{question} = {german} _____",
        27: "Complete the following sentence with the preposition that fits:"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        28: "Write the preposition that match the following verb:"
            "<br><br>{question} = {german} _____",
        29: "Complete the following sentence with the preposition that fits:"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        30: "Write the preposition that match the following noun:"
           "<br><br>{question} = {german} _____",
        31: "Complete the following sentence with the preposition that fits:"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        32: "Write the preposition that match the following noun:"
            "<br><br>{question} = {german} _____",
        33: "Complete the following sentence with the preposition that fits:"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        34: "Write the preposition that match the following adjective:"
           "<br><br>{question} = {german} _____",
        35: "Complete the following sentence with the preposition that fits:"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
    },

    perfekt: {
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
    },

    praeteritum: {
        1: "Write the Präteritum of the following verb:"
           "<br><br>{question} \u25CF {person} _____",
        2: "Write the Präteritum (3rd Person Singular) of the following verb:"
           "<br><br>{question} \u25CF er/sie/es _____",
        3: "Write the Präteritum (3rd Person Singular) of the following verb:"
           "<br><br>{question} \u25CF er/sie/es _____",
        4: "Write the Präteritum (3rd Person Singular) of the following verb:"
           "<br><br>{question} \u25CF er/sie/es _____",
        5: "Write the Präteritum (3rd Person Singular) of the following verb:"
           "<br><br>{question} \u25CF er/sie/es _____",
        6: "Write the Präteritum (3rd Person Singular) of the following verb:"
           "<br><br>{question} \u25CF er/sie/es _____",
        7: "Write the Präteritum (3rd Person Singular) of the following verb:"
           "<br><br>{question} \u25CF er/sie/es _____",
        8: "Write the Präteritum (3rd Person Singular) of the following verb:"
           "<br><br>{question} \u25CF er/sie/es _____",
        9: "Write the Präteritum (3rd Person Singular) of the following verb:"
           "<br><br>{question} \u25CF er/sie/es _____",
        10: "Write the Präteritum (3rd Person Singular) of the following verb:"
            "<br><br>{question} \u25CF er/sie/es _____",
        11: "Write the Präteritum (3rd Person Singular) of the following verb:"
            "<br><br>{question} \u25CF er/sie/es _____",
        12: "Write the Präteritum (3rd Person Singular) of the following verb:"
            "<br><br>{question} \u25CF er/sie/es _____",
        13: "Write the Präteritum (3rd Person Singular) of the following verb:"
            "<br><br>{question} \u25CF er/sie/es _____",
        14: "Write the Präteritum (3rd Person Singular) of the following verb:"
            "<br><br>{question} \u25CF er/sie/es _____",
        15: "Write the Präteritum (3rd Person Singular) of the following verb:"
            "<br><br>{question} \u25CF er/sie/es _____",
        16: "Write the Präteritum (3rd Person Singular) of the following verb:"
            "<br><br>{question} \u25CF er/sie/es _____",
        17: "Write the Präteritum (3rd Person Singular) of the following verb:"
            "<br><br>{question} \u25CF er/sie/es _____",
    },

    imperativ: {
        1: "Write the Imperative of the following verb:"
           "<br><br>{question} \u25CF {person} \u25CF _____",
        2: "Write the Imperative of the following verb:"
           "<br><br>{question} \u25CF {person} \u25CF _____",
        3: "Write the Imperative of the following verb:"
           "<br><br>{question} \u25CF {person} \u25CF _____",
        4: "Write the Imperative of the following verb:"
           "<br><br>{question} \u25CF {person} \u25CF _____",
        5: "Write the Imperative of the following verb:"
           "<br><br>{question} \u25CF {person} \u25CF _____",
        6: "Write the Imperative of the following verb:"
           "<br><br>{question} \u25CF {person} \u25CF _____",
    },

    konjunktiv: {
        1: "Write the Konjunktiv II of the following verb:"
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
           "<br><br><strong>{question}</strong>",
        2: "Complete the following sentence with the adverb that fits:¨"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        3: "Translate the following adverb:"
           "<br><br><strong>{question}</strong>",
        4: "Complete the following sentence with the adverb that fits:¨"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        5: "Translate the following adverb:"
           "<br><br><strong>{question}</strong>",
        6: "Complete the following sentence with the adverb that fits:¨"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        7: "Translate the following adverb:"
           "<br><br><strong>{question}</strong>",
        8: "Complete the following sentence with the adverb that fits:¨"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        9: "Translate the following adverb:"
           "<br><br><strong>{question}</strong>",
        10: "Complete the following sentence with the adverb that fits:¨"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        11: "Translate the following adverb:"
            "<br><br><strong>{question}</strong>",
        12: "Complete the following sentence with the adverb that fits:¨"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
        13: "Translate the following adverb:"
            "<br><br><strong>{question}</strong>",
        14: "Complete the following sentence with the adverb that fits:¨"
           "<br><br>{question}"
           "<br><br><i>{english}</i>",
    },

    verben: {
        1: "Translate the following verb:"
           "<br><br><strong>{question}</strong>",
        2: "Translate the following verb:"
           "<br><br><strong>{question}</strong>",
        3: "Translate the following verb:"
           "<br><br><strong>{question}</strong>",
        4: "Translate the following verb:"
           "<br><br><strong>{question}</strong>",
        5: "Translate the following verb:"
           "<br><br><strong>{question}</strong>",
        6: "Translate the following verb:"
           "<br><br><strong>{question}</strong>",
        7: "Translate the following verb:"
           "<br><br><strong>{question}</strong>",
        8: "Translate the following verb:"
           "<br><br><strong>{question}</strong>",
        9: "Translate the following verb:"
           "<br><br><strong>{question}</strong>",
        10: "Translate the following verb:"
            "<br><br><strong>{question}</strong>",
        11: "Translate the following verb:"
            "<br><br><strong>{question}</strong>",
        12: "Translate the following verb:"
            "<br><br><strong>{question}</strong>",
        13: "Translate the following verb:"
            "<br><br><strong>{question}</strong>",
        14: "Translate the following verb:"
            "<br><br><strong>{question}</strong>",
        15: "Translate the following verb:"
            "<br><br><strong>{question}</strong>",
        16: "Translate the following verb:"
            "<br><br><strong>{question}</strong>",
        17: "Translate the following verb:"
            "<br><br><strong>{question}</strong>",
        18: "Translate the following verb:"
            "<br><br><strong>{question}</strong>",
        19: "Translate the following verb:"
            "<br><br><strong>{question}</strong>",
        20: "Translate the following verb:"
            "<br><br><strong>{question}</strong>",
    },

    trennbare_verben: {
        1: "Translate the following (un)trennbare verb based on the specified root verb:"
           "<br><br><strong>{question}</strong> \u25CF {german}",
        2: "Translate the following (un)trennbare verb based on the specified prefix:"
           "<br><br><strong>{question}</strong> \u25CF {prefix}",
        3: "Translate the following (un)trennbare verb based on the specified root verb:"
           "<br><br><strong>{question}</strong> \u25CF {german}",
        4: "Translate the following (un)trennbare verb based on the specified root verb:"
           "<br><br><strong>{question}</strong> \u25CF {german}",
        5: "Translate the following (un)trennbare verb based on the specified prefix:"
           "<br><br><strong>{question}</strong> \u25CF {prefix}",
        6: "Translate the following (un)trennbare verb based on the specified prefix:"
           "<br><br><strong>{question}</strong> \u25CF {prefix}",
        7: "Translate the following (un)trennbare verb based on the specified root verb:"
           "<br><br><strong>{question}</strong> \u25CF {german}",
        8: "Translate the following (un)trennbare verb based on the specified root verb:"
           "<br><br><strong>{question}</strong> \u25CF {german}",
        9: "Translate the following (un)trennbare verb based on the specified prefix:"
           "<br><br><strong>{question}</strong> \u25CF {prefix}",
        10: "Translate the following (un)trennbare verb based on the specified prefix:"
            "<br><br><strong>{question}</strong> \u25CF {prefix}",

    },

    deverbale_substantive: {
        1: "Complete the blank with the noun that fits:"
           "<br><br>{english}: {german}"
           "<br><br>{question}: _____",
        2: "Complete the blank with the noun that fits:"
           "<br><br>{english}: {german}"
           "<br><br>{question}: _____",
        3: "Complete the blank with the noun that fits:"
           "<br><br>{english}: {german}"
           "<br><br>{question}: _____",
        4: "Complete the blank with the noun that fits:"
           "<br><br>{english}: {german}"
           "<br><br>{question}: _____",
        5: "Complete the blank with the noun that fits:"
           "<br><br>{english}: {german}"
           "<br><br>{question}: _____",
        6: "Complete the blank with the noun that fits:"
           "<br><br>{english}: {german}"
           "<br><br>{question}: _____",
        7: "Complete the blank with the noun that fits:"
           "<br><br>{english}: {german}"
           "<br><br>{question}: _____",
        8: "Complete the blank with the noun that fits:"
           "<br><br>{english}: {german}"
           "<br><br>{question}: _____",
        9: "Complete the blank with the noun that fits:"
           "<br><br>{english}: {german}"
           "<br><br>{question}: _____",
        10: "Complete the blank with the noun that fits:"
            "<br><br>{english}: {german}"
            "<br><br>{question}: _____",
        11: "Complete the blank with the noun that fits:"
            "<br><br>{english}: {german}"
            "<br><br>{question}: _____",
        12: "Complete the blank with the noun that fits:"
            "<br><br>{english}: {german}"
            "<br><br>{question}: _____",
    },

}
