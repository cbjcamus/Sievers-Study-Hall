from data.exercises import (artikel, pronomen, konnektoren, praepositionen_grammatik, adjektivDeklinationen,
                            praesens, praepositionen_konjugation, imperativ, perfekt, praeteritum, konjunktiv,
                            verben, adjektive, adverbien)

QUESTION_TEMPLATES = {
    artikel: {
        1: "Find the nominative, definite article that fits in the following sentence:"
            "<br><br>{question} \u25CF {gender}",
        2: "Find the accusative, definite article that fits in the following sentence:"
           "<br><br>{question} \u25CF {gender}",
        3: "Find the dative, definite article that fits in the following sentence:"
           "<br><br>{question} \u25CF {gender}",
        4: "Find the definite article that fits in the following sentence:"
           "<br><br>{question} \u25CF {gender}",
        5: "Find the nominative, indefinite article that fits in the following sentence:"
           "<br><br>{question} \u25CF {gender}",
        6: "Find the accusative, indefinite article that fits in the following sentence:"
           "<br><br>{question} \u25CF {gender}",
        7: "Find the dative, indefinite article that fits in the following sentence:"
           "<br><br>{question} \u25CF {gender}",
        8: "Find the indefinite article that fits in the following sentence:"
           "<br><br>{question} \u25CF {gender}",
        9: "Find the definite article that fits in the following sentence:"
           "<br><br>{question}",
        10: "Find the translation of the following article:"
            "<br><br><strong>{question}</strong>",
        11: "Find the missing article in the following sentence:"
            "<br><br>{question}"
            "<br><br>{english_text}",
        12: "Find the translation of the following article:"
            "<br><br><strong>{question}</strong>",
        13: "Find the missing article in the following sentence:"
            "<br><br>{question}"
            "<br><br>{english_text}",
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
           "<br><br>{english_text}",
        9: "Find the missing nominative, relative pronoun in the following sentence:"
           "<br><br>{question}",
        10: "Find the missing accusative, relative pronoun in the following sentence:"
           "<br><br>{question}",
        11: "Find the missing dative, relative pronoun in the following sentence:"
           "<br><br>{question}",
        12: "Find the missing genitive, relative pronoun in the following sentence:"
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
           "<br><br>{english_text}",
        3: "Find the translation of the following connector:"
           "<br><br><strong>{question}</strong>",
        4: "Find the missing connector in the following sentence:"
           "<br><br>{question}"
           "<br><br>{english_text}",
        5: "Find the translation of the following connector:"
           "<br><br><strong>{question}</strong>",
        6: "Find the missing connector in the following sentence:"
           "<br><br>{question}"
           "<br><br>{english_text}",
        7: "Find the translation of the following connector:"
           "<br><br><strong>{question}</strong>",
        8: "Find the missing connector in the following sentence:"
           "<br><br>{question}"
           "<br><br>{english_text}",
    },

    praepositionen_grammatik: {
        1: "Find the translation of the following preposition:"
           "<br><br>{question}",
        2: "Find the preposition that fits in the following sentence:"
           "<br><br>{question}"
           "<br><br>{english_text}",
        3: "Find the preposition that fits in the following sentence:"
           "<br><br>{question}"
           "<br><br>{english_text}",
        4: "Find the preposition that fits in the following sentence:"
           "<br><br>{question}"
           "<br><br>{english_text}",
        5: "Find the preposition that fits in the following sentence:"
           "<br><br>{question}"
           "<br><br>{english_text}",
        6: "Find the preposition that fits in the following sentence:"
           "<br><br>{question}"
           "<br><br>{english_text}",
        7: "Find the preposition that fits in the following sentence:"
           "<br><br>{question}"
           "<br><br>{english_text}",
        8: "Find the preposition that fits in the following sentence:"
           "<br><br>{question}"
           "<br><br>{english_text}",
        9: "Find the translation of the following preposition:"
           "<br><br>{question}",
        10: "Find the preposition that fits in the following sentence:"
           "<br><br>{question}"
           "<br><br>{english_text}",
        11: "Find the translation of the following preposition:"
           "<br><br>{question}",
        12: "Find the preposition that fits in the following sentence:"
           "<br><br>{question}"
           "<br><br>{english_text}",
    },

    adjektivDeklinationen: {
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
    },

    praepositionen_konjugation :{
        1: "Find the preposition that match the following verb:"
           "<br><br>{english_text} = {question} _____",
        2: "Find the preposition that fits in the following sentence:"
           "<br><br>{question}"
           "<br><br>{english_text}",
        3: "Find the preposition that match the following verb:"
           "<br><br>{english_text} = {question} _____",
        4: "Find the preposition that fits in the following sentence:"
           "<br><br>{question}"
           "<br><br>{english_text}",
        5: "Find the preposition that match the following verb:"
           "<br><br>{english_text} = {question} _____",
        6: "Find the preposition that fits in the following sentence:"
           "<br><br>{question}"
           "<br><br>{english_text}",
        7: "Find the Da-Word that fits in the following sentence:"
           "<br><br>{question}"
           "<br><br>{english_text}",
        8: "Find the Wo-Word that fits in the following sentence:"
           "<br><br>{question}"
           "<br><br>{english_text}",
        9: "Find the preposition that match the following verb:"
           "<br><br>{english_text} = {question} _____",
        10: "Find the preposition that fits in the following sentence:"
           "<br><br>{question}"
           "<br><br>{english_text}",
        11: "Find the preposition that match the following noun:"
           "<br><br>{english_text} = {question} _____",
        12: "Find the preposition that fits in the following sentence:"
            "<br><br>{question}"
            "<br><br>{english_text}",
        13: "Find the preposition that match the following adjective:"
            "<br><br>{english_text} = {question} _____",
        14: "Find the preposition that fits in the following sentence:"
            "<br><br>{question}"
            "<br><br>{english_text}",
    },

    perfekt: {
        1: "Find the Partizip II of the following verb:"
           "<br><br>{question}",
        2: "Complete the sentence with the Partizip II of the specified verb:"
           "<br><br>{question}"
           "<br><br>{english_text}",
        3: "Complete the sentence with the proper Hilfsverb:"
           "<br><br>{question}"
           "<br><br>{english_text}",
        4: "Find the Partizip II of the following verb:"
           "<br><br>{question}",
        5: "Complete the sentence with the Partizip II of the specified verb:"
           "<br><br>{question}"
           "<br><br>{english_text}",
        6: "Complete the sentence with the proper Hilfsverb:"
           "<br><br>{question}"
           "<br><br>{english_text}",
        7: "Find the Partizip II of the following verb:"
           "<br><br>{question}",
        8: "Find the Partizip II of the following verb:"
           "<br><br>{question}",
    },

    praeteritum: {
        1: "Find the präteritum of the following verb:"
           "<br><br>{question} \u25CF {person} _____",
        2: "Find the präteritum (3rd Person Singular) of the following verb:"
           "<br><br>{question} \u25CF er/sie/es _____",
        3: "Find the präteritum (3rd Person Singular) of the following verb:"
           "<br><br>{question} \u25CF er/sie/es _____",
        4: "Find the präteritum (3rd Person Singular) of the following verb:"
           "<br><br>{question} \u25CF er/sie/es _____",
        5: "Find the präteritum (3rd Person Singular) of the following verb:"
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
    },

    konjunktiv: {
        1: "Find the konjunktiv II of the following verb:"
           "<br><br>{question} \u25CF {person} _____",
    },

    adverbien: {
        1: "Find the translation of the following adverb:"
           "<br><br><strong>{question}</strong>",
        2: "Find the missing adverb in the following sentence:¨"
           "<br><br>{question}"
           "<br><br>{english_text}",
        3: "Find the translation of the following adverb:"
           "<br><br><strong>{question}</strong>",
        4: "Find the missing adverb in the following sentence:"
           "<br><br>{question}"
           "<br><br>{english_text}",
        5: "Find the translation of the following adverb:"
           "<br><br><strong>{question}</strong>",
        6: "Find the missing adverb in the following sentence:"
           "<br><br>{question}"
           "<br><br>{english_text}",
        7: "Find the translation of the following adverb:"
           "<br><br><strong>{question}</strong>",
        8: "Find the missing adverb in the following sentence:"
           "<br><br>{question}"
           "<br><br>{english_text}",
    },
}
