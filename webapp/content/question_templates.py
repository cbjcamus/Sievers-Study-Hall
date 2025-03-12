from data_processing.exercises import (artikel, pronomen, konnektoren, praepositionen_grammatik, adjektivdeklinationen,
                                       praesens, praepositionen_konjugation, imperativ, perfekt, praeteritum,
                                       konjunktiv,
                                       partizip_I,
                                       verben, adjektive, adverbien, deverbale_substantive, trennbare_verben)

QUESTION_TEMPLATES = {
    artikel: {
        1: "Find the nominative definite article that fits in the following sentence:"
           "<br><br>{question} \u25CF {gender}",
        2: "Find the accusative definite article that fits in the following sentence:"
           "<br><br>{question} \u25CF {gender}",
        3: "Find the dative definite article that fits in the following sentence:"
           "<br><br>{question} \u25CF {gender}",
        4: "Find the definite article that fits in the following sentence:"
           "<br><br>{question} \u25CF {gender}",
        5: "Find the nominative indefinite article that fits in the following sentence:"
           "<br><br>{question} \u25CF {gender}",
        6: "Find the accusative indefinite article that fits in the following sentence:"
           "<br><br>{question} \u25CF {gender}",
        7: "Find the dative indefinite article that fits in the following sentence:"
           "<br><br>{question} \u25CF {gender}",
        8: "Find the indefinite article that fits in the following sentence:"
           "<br><br>{question} \u25CF {gender}",
        9: "Find the definite article that fits in the following sentence:"
           "<br><br>{question}",
        10: "Find the translation of the following article:"
            "<br><br><strong>{question}</strong>",
        11: "Find the missing article in the following sentence:"
            "<br><br>{question}"
            "<br><br>{english}",
        12: "Find the translation of the following article:"
            "<br><br><strong>{question}</strong>",
        13: "Find the missing article in the following sentence:"
            "<br><br>{question}"
            "<br><br>{english}",
    },

    pronomen: {
        1: "Find the nominative pronoun that fits in the following sentence:"
           "<br><br>{question} \u25CF {person}",
        2: "Find the accusative pronoun that fits in the following sentence:"
           "<br><br>{question} \u25CF {person}",
        3: "Find the dative pronoun that fits in the following sentence:"
           "<br><br>{question} \u25CF {person}",
        4: "Find the pronoun that fits in the following sentence:"
           "<br><br>{question} \u25CF {person}",
        5: "Find the reflexive pronoun that fits in the following sentence:"
           "<br><br>{question} \u25CF {person}",
        6: "Find the pronoun that fits in the following sentence:"
           "<br><br>{question} \u25CF {person}",
        7: "Find the translation of the following pronoun:"
           "<br><br><strong>{question}</strong>",
        8: "Find the missing pronoun in the following sentence:"
           "<br><br>{question}"
           "<br><br>{english}",
        9: "Find the missing nominative relative pronoun in the following sentence:"
           "<br><br>{question}",
        10: "Find the missing accusative relative pronoun in the following sentence:"
            "<br><br>{question}",
        11: "Find the missing dative relative pronoun in the following sentence:"
            "<br><br>{question}",
        12: "Find the missing genitive relative pronoun in the following sentence:"
            "<br><br>{question}",
        13: "Find the missing relative pronoun in the following sentence:"
            "<br><br>{question}",
        14: "Find the missing relative pronoun in the following sentence:"
            "<br><br>{question}",
    },

    konnektoren: {
        1: "Find the translation of the following connector:"
           "<br><br><strong>{question}</strong>",
        2: "Find the missing connector in the following sentence:¨"
           "<br><br>{question}"
           "<br><br>{english}",
        3: "Find the translation of the following connector:"
           "<br><br><strong>{question}</strong>",
        4: "Find the missing connector in the following sentence:"
           "<br><br>{question}"
           "<br><br>{english}",
        5: "Find the translation of the following connector:"
           "<br><br><strong>{question}</strong>",
        6: "Find the missing connector in the following sentence:"
           "<br><br>{question}"
           "<br><br>{english}",
        7: "Find the translation of the following connector:"
           "<br><br><strong>{question}</strong>",
        8: "Find the missing connector in the following sentence:"
           "<br><br>{question}"
           "<br><br>{english}",
    },

    praepositionen_grammatik: {
        1: "Find the translation of the following preposition:"
           "<br><br>{question}",
        2: "Find the preposition that fits in the following sentence:"
           "<br><br>{question}"
           "<br><br>{english}",
        3: "Find the preposition that fits in the following sentence:"
           "<br><br>{question}"
           "<br><br>{english}",
        4: "Find the preposition that fits in the following sentence:"
           "<br><br>{question}"
           "<br><br>{english}",
        5: "Find the preposition that fits in the following sentence:"
           "<br><br>{question}"
           "<br><br>{english}",
        6: "Find the preposition that fits in the following sentence:"
           "<br><br>{question}"
           "<br><br>{english}",
        7: "Find the preposition that fits in the following sentence:"
           "<br><br>{question}"
           "<br><br>{english}",
        8: "Find the preposition that fits in the following sentence:"
           "<br><br>{question}"
           "<br><br>{english}",
        9: "Find the translation of the following preposition:"
           "<br><br>{question}",
        10: "Find the preposition that fits in the following sentence:"
            "<br><br>{question}"
            "<br><br>{english}",
        11: "Find the translation of the following preposition:"
            "<br><br>{question}",
        12: "Find the preposition that fits in the following sentence:"
            "<br><br>{question}"
            "<br><br>{english}",
        13: "Find the preposition (durch or von) that fits in the following sentence:"
            "<br><br>{question}"
            "<br><br>{english}",
        14: "Find the preposition (aus or vor) that fits in the following sentence:"
            "<br><br>{question}"
            "<br><br>{english}",
        15: "Find the preposition (zu or für) and article that fits in the following sentence:"
            "<br><br>{question}"
            "<br><br>{english}",
        16: "Find the translation of the following preposition:"
            "<br><br>{question}",
        17: "Find the preposition that fits in the following sentence:"
            "<br><br>{question}"
            "<br><br>{english}",
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
        1: "Find the present tense of the following verb:"
           "<br><br>{question} \u25CF {person} _____",
        2: "Find the present tense of the following verb:"
           "<br><br>{question} \u25CF {person} _____",
        3: "Find the present tense of the following verb:"
           "<br><br>{question} \u25CF {person} _____",
        4: "Find the present tense of the following verb:"
           "<br><br>{question} \u25CF {person} _____",
        5: "Find the present tense of the following verb:"
           "<br><br>{question} \u25CF {person} _____",
        6: "Find the present tense of the following verb:"
           "<br><br>{question} \u25CF {person} _____",
        7: "Find the present tense of the following verb:"
           "<br><br>{question} \u25CF {person} _____",
        8: "Find the present tense of the following verb:"
           "<br><br>{question} \u25CF {person} _____",
        9: "Find the present tense of the following verb:"
           "<br><br>{question} \u25CF {person} _____",
        10: "Find the present tense of the following verb:"
            "<br><br>{question} \u25CF {person} _____",
        11: "Find the present tense of the following verb:"
            "<br><br>{question} \u25CF {person} _____",
        12: "Find the present tense of the following verb:"
            "<br><br>{question} \u25CF {person} _____",
        13: "Find the present tense of the following verb:"
            "<br><br>{question} \u25CF {person} _____",
        14: "Find the present tense of the following verb:"
            "<br><br>{question} \u25CF {person} _____",
        15: "Find the present tense of the following verb:"
            "<br><br>{question} \u25CF {person} _____",
        16: "Find the present tense of the following verb:"
            "<br><br>{question} \u25CF {person} _____",
        17: "Find the present tense of the following verb:"
            "<br><br>{question} \u25CF {person} _____",
        18: "Find the present tense of the following verb:"
            "<br><br>{question} \u25CF {person} _____",
        19: "Find the present tense of the following verb:"
            "<br><br>{question} \u25CF {person} _____",
        20: "Find the present tense of the following verb:"
            "<br><br>{question} \u25CF {person} _____",
        21: "Find the present tense of the following verb:"
            "<br><br>{question} \u25CF {person} _____",
        22: "Find the present tense of the following verb:"
            "<br><br>{question} \u25CF {person} _____",
        23: "Find the present tense of the following verb:"
            "<br><br>{question} \u25CF {person} _____",
        24: "Find the present tense of the following verb:"
            "<br><br>{question} \u25CF {person} _____",
    },

    praepositionen_konjugation :{
        1: "Find the preposition that match the following verb:"
           "<br><br>{english} = {question} _____",
        2: "Find the preposition that fits in the following sentence:"
           "<br><br>{question}"
           "<br><br>{english}",
        3: "Find the preposition that match the following verb:"
           "<br><br>{english} = {question} _____",
        4: "Find the preposition that fits in the following sentence:"
           "<br><br>{question}"
           "<br><br>{english}",
        5: "Find the preposition that match the following verb:"
           "<br><br>{english} = {question} _____",
        6: "Find the preposition that fits in the following sentence:"
           "<br><br>{question}"
           "<br><br>{english}",
        7: "Find the Da-Word that fits in the following sentence:"
           "<br><br>{question}"
           "<br><br>{english}",
        8: "Find the Wo-Word that fits in the following sentence:"
           "<br><br>{question}"
           "<br><br>{english}",
        9: "Find the preposition that match the following verb:"
           "<br><br>{english} = {question} _____",
        10: "Find the preposition that fits in the following sentence:"
            "<br><br>{question}"
            "<br><br>{english}",
        11: "Find the preposition that match the following noun:"
            "<br><br>{english} = {question} _____",
        12: "Find the preposition that fits in the following sentence:"
            "<br><br>{question}"
            "<br><br>{english}",
        13: "Find the preposition that match the following adjective:"
            "<br><br>{english} = {question} _____",
        14: "Find the preposition that fits in the following sentence:"
            "<br><br>{question}"
            "<br><br>{english}",
    },

    perfekt: {
        1: "Find the Partizip II of the following verb:"
           "<br><br>{question}",
        2: "Find the Partizip II of the following verb:"
           "<br><br>{question}",
        3: "Find the Partizip II of the following verb:"
           "<br><br>{question}",
        4: "Complete the sentence with a Partizip II:"
           "<br><br>{question}"
           "<br><br>{english}",
        5: "Complete the sentence with a Partizip II:"
           "<br><br>{question}"
           "<br><br>{english}",
        6: "Complete the sentence with the proper Hilfsverb:"
           "<br><br>{question}"
           "<br><br>{english}",
        7: "Complete the sentence with the proper Hilfsverb:"
           "<br><br>{question}"
           "<br><br>{english}",
        8: "Find the Partizip II of the following verb:"
           "<br><br>{question}",
        9: "Find the Partizip II of the following verb:"
           "<br><br>{question}",
        10: "Find the Partizip II of the following verb:"
           "<br><br>{question}",
        11: "Complete the sentence with a Partizip II:"
           "<br><br>{question}"
           "<br><br>{english}",
        12: "Complete the sentence with a Partizip II:"
           "<br><br>{question}"
           "<br><br>{english}",
        13: "Complete the sentence with the proper Hilfsverb:"
           "<br><br>{question}"
           "<br><br>{english}",
        14: "Complete the sentence with the proper Hilfsverb:"
           "<br><br>{question}"
           "<br><br>{english}",
        15: "Find the Partizip II of the following verb:"
           "<br><br>{question}",
        16: "Find the Partizip II of the following verb:"
           "<br><br>{question}",
        17: "Find the Partizip II of the following verb:"
           "<br><br>{question}",
        18: "Find the Partizip II of the following verb:"
            "<br><br>{question}",
        19: "Find the Partizip II of the following verb:"
            "<br><br>{question}",
        20: "Find the Partizip II of the following verb:"
            "<br><br>{question}",
        21: "Find the Partizip II of the following verb:"
            "<br><br>{question}",
        22: "Find the Partizip II of the following verb:"
            "<br><br>{question}",
        23: "Find the Partizip II of the following verb:"
            "<br><br>{question}",
    },

    praeteritum: {
        1: "Find the Präteritum of the following verb:"
           "<br><br>{question} \u25CF {person} _____",
        2: "Find the Präteritum (3rd Person Singular) of the following verb:"
           "<br><br>{question} \u25CF er/sie/es _____",
        3: "Find the Präteritum (3rd Person Singular) of the following verb:"
           "<br><br>{question} \u25CF er/sie/es _____",
        4: "Find the Präteritum (3rd Person Singular) of the following verb:"
           "<br><br>{question} \u25CF er/sie/es _____",
        5: "Find the Präteritum (3rd Person Singular) of the following verb:"
           "<br><br>{question} \u25CF er/sie/es _____",
        6: "Find the Präteritum (3rd Person Singular) of the following verb:"
           "<br><br>{question} \u25CF er/sie/es _____",
        7: "Find the Präteritum (3rd Person Singular) of the following verb:"
           "<br><br>{question} \u25CF er/sie/es _____",
        8: "Find the Präteritum (3rd Person Singular) of the following verb:"
           "<br><br>{question} \u25CF er/sie/es _____",
        9: "Find the Präteritum (3rd Person Singular) of the following verb:"
           "<br><br>{question} \u25CF er/sie/es _____",
        10: "Find the Präteritum (3rd Person Singular) of the following verb:"
           "<br><br>{question} \u25CF er/sie/es _____",
        11: "Find the Präteritum (3rd Person Singular) of the following verb:"
           "<br><br>{question} \u25CF er/sie/es _____",
        12: "Find the Präteritum (3rd Person Singular) of the following verb:"
           "<br><br>{question} \u25CF er/sie/es _____",
        13: "Find the Präteritum (3rd Person Singular) of the following verb:"
           "<br><br>{question} \u25CF er/sie/es _____",
        14: "Find the Präteritum (3rd Person Singular) of the following verb:"
           "<br><br>{question} \u25CF er/sie/es _____",
    },

    imperativ: {
        1: "Find the Imperative of the following verb:"
           "<br><br>{question} \u25CF {person} \u25CF _____",
        2: "Find the Imperative of the following verb:"
           "<br><br>{question} \u25CF {person} \u25CF _____",
        3: "Find the Imperative of the following verb:"
           "<br><br>{question} \u25CF {person} \u25CF _____",
        4: "Find the Imperative of the following verb:"
           "<br><br>{question} \u25CF {person} \u25CF _____",
        5: "Find the Imperative of the following verb:"
           "<br><br>{question} \u25CF {person} \u25CF _____",
        6: "Find the Imperative of the following verb:"
           "<br><br>{question} \u25CF {person} \u25CF _____",
    },

    konjunktiv: {
        1: "Find the Konjunktiv II of the following verb:"
           "<br><br>{question} \u25CF {person} _____",
    },

    partizip_I: {
        1: "Find the Partizip I of the following verb:"
           "<br><br>{question} \u25CF English: {english}",
        2: "Find the Partizip I of the following verb:"
           "<br><br>{question} \u25CF English: {english}",
        3: "Find the Partizip I of the following verb:"
           "<br><br>{question} \u25CF English: {english}",
    },

    adverbien: {
        1: "Find the translation of the following adverb:"
           "<br><br><strong>{question}</strong>",
        2: "Find the missing adverb in the following sentence:¨"
           "<br><br>{question}"
           "<br><br>{english}",
        3: "Find the translation of the following adverb:"
           "<br><br><strong>{question}</strong>",
        4: "Find the missing adverb in the following sentence:"
           "<br><br>{question}"
           "<br><br>{english}",
        5: "Find the translation of the following adverb:"
           "<br><br><strong>{question}</strong>",
        6: "Find the missing adverb in the following sentence:"
           "<br><br>{question}"
           "<br><br>{english}",
        7: "Find the translation of the following adverb:"
           "<br><br><strong>{question}</strong>",
        8: "Find the missing adverb in the following sentence:"
           "<br><br>{question}"
           "<br><br>{english}",
        9: "Find the translation of the following adverb:"
           "<br><br><strong>{question}</strong>",
        10: "Find the missing adverb in the following sentence:"
           "<br><br>{question}"
           "<br><br>{english}",
        11: "Find the translation of the following adverb:"
           "<br><br><strong>{question}</strong>",
        12: "Find the missing adverb in the following sentence:"
            "<br><br>{question}"
            "<br><br>{english}",
        13: "Find the translation of the following adverb:"
            "<br><br><strong>{question}</strong>",
        14: "Find the missing adverb in the following sentence:"
            "<br><br>{question}"
            "<br><br>{english}",
    },

    verben: {
        1: "Find the translation of the following verb:"
            "<br><br><strong>{question}</strong>",
        2: "Find the translation of the following verb:"
           "<br><br><strong>{question}</strong>",
        3: "Find the translation of the following verb:"
           "<br><br><strong>{question}</strong>",
        4: "Find the translation of the following verb:"
           "<br><br><strong>{question}</strong>",
        5: "Find the translation of the following verb:"
           "<br><br><strong>{question}</strong>",
        6: "Find the translation of the following verb:"
           "<br><br><strong>{question}</strong>",
        7: "Find the translation of the following verb:"
           "<br><br><strong>{question}</strong>",
        8: "Find the translation of the following verb:"
           "<br><br><strong>{question}</strong>",
        9: "Find the translation of the following verb:"
           "<br><br><strong>{question}</strong>",
        10: "Find the translation of the following verb:"
           "<br><br><strong>{question}</strong>",
        11: "Find the translation of the following verb:"
           "<br><br><strong>{question}</strong>",
        12: "Find the translation of the following verb:"
           "<br><br><strong>{question}</strong>",
        13: "Find the translation of the following verb:"
           "<br><br><strong>{question}</strong>",
        14: "Find the translation of the following verb:"
           "<br><br><strong>{question}</strong>",
        15: "Find the translation of the following verb:"
           "<br><br><strong>{question}</strong>",
        16: "Find the translation of the following verb:"
           "<br><br><strong>{question}</strong>",
        17: "Find the translation of the following verb:"
            "<br><br><strong>{question}</strong>",
        18: "Find the translation of the following verb:"
            "<br><br><strong>{question}</strong>",
        19: "Find the translation of the following verb:"
            "<br><br><strong>{question}</strong>",
        20: "Find the translation of the following verb:"
            "<br><br><strong>{question}</strong>",
    },

    trennbare_verben: {
        1: "Find the translation of the following (un)trennbare verb based on the specified root verb:"
           "<br><br><strong>{question}</strong> \u25CF {german}",
        2: "Find the translation of the following (un)trennbare verb based on the specified prefix:"
           "<br><br><strong>{question}</strong> \u25CF {prefix}",
        3: "Find the translation of the following (un)trennbare verb based on the specified root verb:"
           "<br><br><strong>{question}</strong> \u25CF {german}",
        4: "Find the translation of the following (un)trennbare verb based on the specified root verb:"
           "<br><br><strong>{question}</strong> \u25CF {german}",
        5: "Find the translation of the following (un)trennbare verb based on the specified prefix:"
           "<br><br><strong>{question}</strong> \u25CF {prefix}",
        6: "Find the translation of the following (un)trennbare verb based on the specified prefix:"
           "<br><br><strong>{question}</strong> \u25CF {prefix}",
        7: "Find the translation of the following (un)trennbare verb based on the specified root verb:"
           "<br><br><strong>{question}</strong> \u25CF {german}",
        8: "Find the translation of the following (un)trennbare verb based on the specified root verb:"
           "<br><br><strong>{question}</strong> \u25CF {german}",
        9: "Find the translation of the following (un)trennbare verb based on the specified prefix:"
           "<br><br><strong>{question}</strong> \u25CF {prefix}",
        10: "Find the translation of the following (un)trennbare verb based on the specified prefix:"
            "<br><br><strong>{question}</strong> \u25CF {prefix}",

    },

    deverbale_substantive: {
        1: "Find the noun that fits:"
           "<br><br>{english}: {german}"
           "<br><br>{question}: _____",
        2: "Find the noun that fits:"
           "<br><br>{english}: {german}"
           "<br><br>{question}: _____",
        3: "Find the noun that fits:"
           "<br><br>{english}: {german}"
           "<br><br>{question}: _____",
        4: "Find the noun that fits:"
           "<br><br>{english}: {german}"
           "<br><br>{question}: _____",
        5: "Find the noun that fits:"
           "<br><br>{english}: {german}"
           "<br><br>{question}: _____",
        6: "Find the noun that fits:"
           "<br><br>{english}: {german}"
           "<br><br>{question}: _____",
        7: "Find the noun that fits:"
           "<br><br>{english}: {german}"
           "<br><br>{question}: _____",
        8: "Find the noun that fits:"
           "<br><br>{english}: {german}"
           "<br><br>{question}: _____",
        9: "Find the noun that fits:"
           "<br><br>{english}: {german}"
           "<br><br>{question}: _____",
        10: "Find the noun that fits:"
            "<br><br>{english}: {german}"
            "<br><br>{question}: _____",
        11: "Find the noun that fits:"
            "<br><br>{english}: {german}"
            "<br><br>{question}: _____",
        12: "Find the noun that fits:"
            "<br><br>{english}: {german}"
            "<br><br>{question}: _____",
    },
}
