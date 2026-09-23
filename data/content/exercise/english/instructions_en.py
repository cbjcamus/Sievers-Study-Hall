from data.data_processing.exercises import isolation, context, synonym, antonym, prompt
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

INSTRUCTION_UNIT_EN = {
    praepositionen_artikel:
        "Complete the following sentence with the preposition indicated and the article or pronoun that fits:",

    verben_artikel:
        "Complete the following sentence with the article or pronoun that fits:",

    wortstellung:
        "Build the sentence that translates the following English sentence, taking into account any indications provided:",

    verben:
        "Translate the following verb:",

    praesens:
        "Conjugate the following verb in the present tense:",

    partizip_II:
        "Write the past participle (Partizip II) of the following verb:",

    praeteritum:
        "Conjugate the following verb in the Präteritum:",

    imperativ:
        "Conjugate the following verb in the Imperativ:",

    konjunktiv_II:
        "Conjugate the following verb in the Konjunktiv II:",

    konjunktiv_I:
        "Conjugate the following verb in the Konjunktiv I:",

    partizip_I:
        "Write the Partizip I of the following verb:",

    genus_regeln:
        "Write the definite article (<i>der</i>, <i>die</i> or <i>das</i>) that fits the noun provided:",

    genus:
        "Write the definite article (<i>der</i>, <i>die</i> or <i>das</i>) that fits the noun provided:",

    plural:
        "Write the plural form of the German noun displayed below:",

    alpha:
        "Write one or two sentences using the following connector:",
}

INSTRUCTION_SUBCATEGORY_EN = {
    praepositionen_verben: {
        isolation: "Write the preposition that matches the following verb:",
        context: "Complete the following sentence with the preposition that fits:",
    },

    praepositionen_adjektive: {
        isolation: "Write the preposition that matches the following adjective:",
        context: "Complete the following sentence with the preposition that fits:",
    },

    praepositionen_nomen: {
        isolation: "Write the preposition that matches the following noun:",
        context: "Complete the following sentence with the preposition that fits:",
    },

    konnektoren: {
        isolation: "Translate the following connector:",
        context: "Complete the following sentence with the connector that fits:",
        synonym: "Find a synonym for the following connector:",
        prompt: "Write one or two sentences using the following connector:"
    },

    fragen: {
        isolation: "Translate the following question word:",
        context: "Complete the following sentence with the question word that fits:",
        prompt: "Write one or two sentences using the following question word:"
    },

    adverbien: {
        isolation: "Translate the following adverb:",
        context: "Complete the following sentence with the adverb that fits:",
        synonym: "Find a synonym for the following adverb:",
        antonym: "Write an antonym of the following adverb:",
        prompt: "Write one or two sentences using the following adverb:"
    },

    adjektive: {
        isolation: "Translate the following adjective:",
        synonym: "Find a synonym for the following adjective:",
    },
}

INSTRUCTION_CATEGORY_EN = {

}

INSTRUCTION_EXERCISE_EN = {

    alpha: {
        1: "Write a sentence (or a couple of sentences) that uses the following connector:",
        2: "Write a sentence (or a couple of sentences) that uses the following question word:",
        3: "Write a sentence (or a couple of sentences) that uses the following adverb:",
        4: "Write a sentence (or a couple of sentences) that uses the following adverb:",

        5: "Write a sentence (or a couple of sentences) that uses the following connector:",
        6: "Write a sentence (or a couple of sentences) that uses the following question word:",
        7: "Write a sentence (or a couple of sentences) that uses the following adverb:",
        8: "Write a sentence (or a couple of sentences) that uses the following adverb:",
        9: "Write a sentence (or a couple of sentences) that uses the following adverb:",
    },

    praepositionen: {
        1: "Complete the following sentence with the preposition that fits:",
        2: "Complete the following sentence with the preposition that fits:",
        3: "Complete the following sentence with the preposition that fits:",
        4: "Complete the following sentence with the preposition that fits:",
        5: "Complete the following sentence with the preposition that fits:",

        6: "Complete the following sentence with the preposition that fits:",
        7: "Complete the following sentence with the preposition that fits:",
        8: "Complete the following sentence with the preposition that fits:",
        9: "Complete the following sentence with the preposition that fits:",
        10: "Complete the following sentence with the preposition that fits:",

        11: "Complete the following sentence with the preposition that fits:",
        12: "Complete the following sentence with the preposition that fits:",
        13: "Translate the following preposition:",
        14: "Complete the following sentence with the preposition that fits:",

        15: "Complete the following sentence with the preposition that fits:",
        16: "Complete the following sentence with the preposition that fits:",
        17: "Complete the following sentence with the preposition that fits:",
        18: "Complete the following sentence with the preposition that fits:",
        19: "Translate the following preposition:",
        20: "Complete the following sentence with the preposition that fits:",

        21: "Complete the following sentence with the preposition that fits:",
        22: "Complete the following sentence with the preposition that fits:",
        23: "Complete the following sentence with the preposition that fits:",
        24: "Complete the following sentence with the preposition that fits:",
        25: "Translate the following preposition:",
        26: "Complete the following sentence with the preposition that fits:",
        27: "Translate the following prepositional phrase:",
        28: "Complete the following sentence with the prepositional phrase that fits:",
        29: "Find a synonym for the following preposition:",
        30: "Write an antonym for the following preposition:",

        31: "Translate the following preposition:",
        32: "Complete the following sentence with the preposition that fits:",
        33: "Translate the following postposition:",
        34: "Complete the following sentence with the postposition that fits:",
    },

    pronominaladverbien: {
        1: "Complete the following sentence with the pronominal adverb in <i>Da</i> that fits:",

        2: "Complete the following sentence with the pronominal adverb in <i>Da</i> that fits:",
        3: "Complete the following sentence with the pronominal adverb in <i>Da</i> that fits:",
        4: "Complete the following sentence with the pronominal adverb in <i>Wo</i> that fits:",

        5: "Complete the following sentence with the pronominal adverb in <i>Wo</i> that fits:",
    },

    artikel: {
        1: "Write the definite article that fits the case and gender provided:",
        2: "Complete the following sentence with the nominative definite article that fits:",
        3: "Complete the following sentence with the accusative definite article that fits:",
        4: "Complete the following sentence with the dative definite article that fits:",
        5: "Complete the following sentence with the feminine definite article that fits:",
        6: "Complete the following sentence with the masculine definite article that fits:",
        7: "Complete the following sentence with the neuter definite article that fits:",
        8: "Complete the following sentence with the plural definite article that fits:",
        9: "Complete the following sentence with the definite article that fits:",
        10: "Complete the following sentence with the definite article that fits:",
        11: "Complete the following sentence with the definite article that fits:",
        12: "Write the indefinite article that fits the case and gender provided:",
        13: "Complete the following sentence with the nominative indefinite article that fits:",
        14: "Complete the following sentence with the accusative indefinite article that fits:",
        15: "Complete the following sentence with the dative indefinite article that fits:",
        16: "Complete the following sentence with the feminine indefinite article that fits:",
        17: "Complete the following sentence with the masculine indefinite article that fits:",
        18: "Complete the following sentence with the neuter indefinite article that fits:",
        19: "Complete the following sentence with the indefinite article that fits:",
        20: "Complete the following sentence with the indefinite article that fits:",
        21: "Write the Kein-word that fits the case and gender provided:",
        22: "Complete the following sentence with the Kein-word that fits:",
        23: "Write the possessive article that fits the case and gender provided:",
        24: "Complete the following sentence with the possessive article that fits."
            "<br><br>All the possessive articles are based on singular pronouns "
            "(<i>Ich</i>, <i>Du</i>, <i>Er</i>, <i>Sie</i>, <i>Es</i>).",
        25: "Write the possessive article that fits the case and gender provided:",
        26: "Complete the following sentence with the possessive article that fits."
            "<br><br>All the possessive articles are based on plural (<i>Wir</i>, <i>Ihr</i>, <i>Sie</i>) or formal pronouns.",

        27: "Write the demonstrative article that fits the case and gender provided:",
        28: "Complete the following sentence with the demonstrative article that fits:",
        29: "Write the <i>jede</i>-word that fits the case and gender provided:",
        30: "Complete the following sentence with the jede-word that fits:",
        31: "Translate the following article:",
        32: "Complete the following sentence with the article that fits:",

        33: "Write the article that fits the case and gender provided:",
        34: "Complete the following sentence with the genitive article that fits:",
        35: "Write the article that fits the case and gender provided:",
        36: "Complete the following sentence with the genitive article that fits:",
        37: "Write the possessive article that fits the case and gender provided:",
        38: "Complete the following sentence with the possessive article that fits:",

        39: "Translate the following article based on the case and gender provided:",
        40: "Complete the following sentence with the article that fits:",

        41: "Translate the following article based on the case and gender provided:",
        42: "Complete the following sentence with the article that fits:",
        43: "Complete the following sentence with the article that fits:",
        44: "Complete the following sentence with the article that fits:",

        45: "Translate the following article based on the case and gender provided:",
        46: "Complete the following sentence with the article that fits:",
        47: "Translate the following article based on the case and gender provided:",
        48: "Complete the following sentence with the article that fits:",
        49: "Translate the following article based on the case and gender provided:",
        50: "Complete the following sentence with the article that fits:",
    },

    pronomen: {
        1: "Write the nominative pronoun that fits the person given:",
        2: "Complete the following sentence with the nominative pronoun that fits:",
        3: "Write the accusative pronoun that fits the person given:",
        4: "Complete the following sentence with the accusative pronoun that fits:",
        5: "Write the dative pronoun that fits the person given:",
        6: "Complete the following sentence with the dative pronoun that fits:",
        7: "Complete the following sentence with the pronoun that fits:",
        8: "Complete the following sentence with the pronoun that fits:",
        9: "Replace the indicated object with the pronoun that fits:",
        10: "Replace the indicated object with the pronoun that fits:",

        11: "Write the reflexive pronoun that fits the person and case given:",
        12: "Complete the following sentence with the reflexive pronoun that fits:",
        13: "Complete the following sentence with the pronoun that fits:",
        14: "Complete the following sentence with the pronoun that fits:",

        15: "Translate the following pronoun:",
        16: "Complete the following sentence with the pronoun that fits:",
        17: "Find the relative pronoun that fits the case and gender provided:",
        18: "Complete the following sentence with the nominative relative pronoun that fits:",
        19: "Complete the following sentence with the accusative relative pronoun that fits:",
        20: "Complete the following sentence with the dative relative pronoun that fits:",
        21: "Complete the following sentence with the genitive relative pronoun that fits:",
        22: "Complete the following sentence with the relative pronoun that fits:",
        23: "Complete the following sentence with the relative pronoun that fits:",

        24: "Translate the following pronoun:",
        25: "Complete the following sentence with the pronoun that fits:",
        26: "Translate the following pronoun:",
        27: "Complete the following sentence with the pronoun that fits:",
        28: "Complete the following sentence with the relative pronoun that fits:",
        29: "Complete the following sentence with the relative pronoun that fits:",
        30: "Complete the following sentence with the relative pronoun that fits – there may be more than one option:",

        31: "Translate the following pronoun:",
        32: "Complete the following sentence with the pronoun that fits:",
        33: "Provide the translation of the possessive pronoun that fits the case and gender provided:",
        34: "Complete the following sentence with the possessive pronoun that fits:",
        35: "Provide the translation of the possessive pronoun that fits the case and gender provided:",
        36: "Complete the following sentence with the possessive pronoun that fits:",
        37: "Complete the following sentence with the relative pronoun that fits:",
        38: "Complete the following sentence with the pronoun that fits:",

        39: "Translate the following pronoun in <i>die ...</i>:",
        40: "Complete the following sentence with the pronoun in <i>die ...</i> that fits:",
        41: "Translate the following pronoun:",
        42: "Complete the following sentence with the pronoun that fits:",
    },

    komparativ_superlativ: {
        1: "Write the comparative of the following adjective:",
        2: "Write the comparative of the following adjective:",
        3: "Write the comparative of the following adjective:",
        4: "Write the superlative of the following adjective:",
        5: "Write the superlative of the following adjective:",
        6: "Write the superlative of the following adjective:",

        7: "Write the comparative of the following adjective:",
        8: "Write the comparative of the following adjective:",
        9: "Write the comparative of the following adjective:",
        10: "Write the superlative of the following adjective:",
        11: "Write the superlative of the following adjective:",
        12: "Write the superlative of the following adjective:",
    },

    adjektivdeklinationen: {
        1: "Complete the sentence with the correct form of the specified adjective:",
        2: "Complete the sentence with the correct form of the specified adjective:",
        3: "Complete the sentence with the correct form of the specified adjective:",
        4: "Complete the sentence with the correct form of the specified adjective:",
        5: "Complete the sentence with the correct form of the specified adjective:",
        6: "Complete the sentence with the correct form of the specified adjective:",
        7: "Complete the sentence with the correct form of the specified adjective:",
        8: "Complete the sentence with the correct form of the specified adjective:",
        9: "Complete the sentence with the correct form of the specified adjective:",
        10: "Complete the sentence with the correct form of the specified adjective:",
        11: "Complete the sentence with the correct form of the specified adjective:",
        12: "Complete the sentence with the correct form of the specified adjective:",
        13: "Complete the sentence with the correct form of the specified adjective:",
        14: "Complete the sentence with the correct form of the specified adjective:",

        15: "Complete the sentence with the correct form of the specified adjective:",
        16: "Complete the sentence with the correct form of the specified adjective:",
        17: "Complete the sentence with the correct form of the specified adjective:",
        18: "Complete the sentence with the correct form of the specified adjective:",
        19: "Complete the sentence with the correct comparative form of the specified adjective:",
        20: "Complete the sentence with the correct comparative form of the specified adjective:",
        21: "Complete the sentence with the correct superlative form of the specified adjective:",
        22: "Complete the sentence with the correct superlative form of the specified adjective:",

        23: "Complete the sentence with the correct form of the specified adjective:",
        24: "Complete the sentence with the correct form of the specified adjective:",
        25: "Complete the sentence with the correct form of the specified adjective:",
        26: "Complete the sentence with the correct form of the specified adjective:",
        27: "Complete the sentence with the correct form of the specified adjective:",
        28: "Complete the sentence with the correct form of the specified adjective:",

        29: "Complete the sentence with the correct form of the specified adjective:",
        30: "Complete the sentence with the correct form of the specified adjective:",
        31: "Complete the sentence with the correct form of the specified adjective:",
        32: "Complete the sentence with the correct form of the specified adjective:",
    },

    adjektive_konjunktionen: {
        1: "Complete the following sentence with the conjunction or preposition that fits:",

        2: "Complete the following sentence with the conjunction that fits:",

        3: "Complete the following sentence with the conjunction that fits:",

        4: "Complete the following sentence with the conjunction or preposition that fits:",
    },

    trennbare_verben: {
        1: "Translate the following (in)separable verb based on the specified root verb:",
        2: "Translate the following (in)separable verb based on the specified prefix:",
        3: "Translate the following (in)separable verb:",

        4: "Translate the following (in)separable verb based on the specified root verb:",
        5: "Translate the following (in)separable verb based on the specified prefix:",
        6: "Translate the following (in)separable verb:",

        7: "Translate the following (in)separable verb based on the specified root verb:",
        8: "Translate the following (in)separable verb based on the specified root verb:",
        9: "Translate the following (in)separable verb based on the specified root verb:",
        10: "Translate the following (in)separable verb based on the specified root verb:",
        11: "Translate the following (in)separable verb based on the specified prefix:",
        12: "Translate the following (in)separable verb based on the specified prefix:",
        13: "Translate the following (in)separable verb based on the specified prefix:",
        14: "Translate the following (in)separable verb based on the specified prefix:",
        15: "Translate the following (in)separable verb:",
        16: "Translate the following (in)separable verb:",
        17: "Translate the following (in)separable verb:",
        18: "Translate the following (in)separable verb:",

        19: "Translate the following (in)separable verb based on the specified root verb:",
        20: "Translate the following (in)separable verb based on the specified root verb:",
        21: "Translate the following (in)separable verb based on the specified root verb:",
        22: "Translate the following (in)separable verb based on the specified root verb:",
        23: "Translate the following (in)separable verb based on the specified root verb:",
        24: "Translate the following (in)separable verb based on the specified root verb:",
        25: "Translate the following (in)separable verb based on the specified prefix:",
        26: "Translate the following (in)separable verb based on the specified prefix:",
        27: "Translate the following (in)separable verb based on the specified prefix:",
        28: "Translate the following (in)separable verb based on the specified prefix:",
        29: "Translate the following (in)separable verb based on the specified prefix:",
        30: "Translate the following (in)separable verb based on the specified prefix:",
        31: "Translate the following (in)separable verb:",
        32: "Translate the following (in)separable verb:",
        33: "Translate the following (in)separable verb:",
        34: "Translate the following (in)separable verb:",
        35: "Translate the following (in)separable verb:",
        36: "Translate the following (in)separable verb:",

        37: "Translate the following (in)separable verb based on the specified root verb:",
        38: "Translate the following (in)separable verb based on the specified root verb:",
        39: "Translate the following (in)separable verb based on the specified root verb:",
        40: "Translate the following (in)separable verb based on the specified root verb:",
        41: "Translate the following (in)separable verb based on the specified root verb:",
        42: "Translate the following (in)separable verb based on the specified root verb:",
        43: "Translate the following (in)separable verb based on the specified root verb:",
        44: "Translate the following (in)separable verb based on the specified root verb:",
        45: "Translate the following (in)separable verb based on the specified root verb:",
        46: "Translate the following (in)separable verb based on the specified root verb:",
        47: "Translate the following (in)separable verb based on the specified root verb:",
        48: "Translate the following (in)separable verb based on the specified root verb:",
        49: "Translate the following (in)separable verb based on the specified root verb:",
        50: "Translate the following (in)separable verb based on the specified root verb:",
        51: "Translate the following (in)separable verb based on the specified root verb:",
        52: "Translate the following (in)separable verb based on the specified root verb:",
        53: "Translate the following (in)separable verb based on the specified root verb:",
        54: "Translate the following (in)separable verb based on the specified root verb:",
        55: "Translate the following (in)separable verb based on the specified root verb:",
        56: "Translate the following (in)separable verb based on the specified root verb:",
        57: "Translate the following (in)separable verb based on the specified root verb:",
        58: "Translate the following (in)separable verb based on the specified root verb:",
        59: "Translate the following (in)separable verb based on the specified root verb:",
        60: "Translate the following (in)separable verb based on the specified root verb:",
        61: "Translate the following (in)separable verb based on the specified root verb:",
        62: "Translate the following (in)separable verb based on the specified root verb:",
        63: "Translate the following (in)separable verb based on the specified root verb:",
        64: "Translate the following (in)separable verb based on the specified root verb:",
        65: "Translate the following (in)separable verb based on the specified root verb:",
        66: "Translate the following (in)separable verb based on the specified root verb:",
        67: "Translate the following (in)separable verb based on the specified root verb:",
        68: "Translate the following (in)separable verb based on the specified root verb:",
        69: "Translate the following (in)separable verb based on the specified root verb:",
        70: "Translate the following (in)separable verb based on the specified prefix:",
        71: "Translate the following (in)separable verb based on the specified prefix:",
        72: "Translate the following (in)separable verb based on the specified prefix:",
        73: "Translate the following (in)separable verb based on the specified prefix:",
        74: "Translate the following (in)separable verb based on the specified prefix:",
        75: "Translate the following (in)separable verb based on the specified prefix:",
        76: "Translate the following (in)separable verb based on the specified prefix:",
        77: "Translate the following (in)separable verb based on the specified prefix:",
        78: "Translate the following (in)separable verb based on the specified prefix:",
        79: "Translate the following (in)separable verb based on the specified prefix:",
        80: "Translate the following (in)separable verb based on the specified prefix:",
        81: "Translate the following (in)separable verb based on the specified prefix:",
        82: "Translate the following (in)separable verb based on the specified prefix:",
        83: "Translate the following (in)separable verb based on the specified prefix:",
        84: "Translate the following (in)separable verb based on the specified prefix:",
        85: "Translate the following (in)separable verb based on the specified prefix:",
        86: "Translate the following (in)separable verb based on the specified prefix:",
        87: "Translate the following (in)separable verb:",
        88: "Translate the following (in)separable verb:",
        89: "Translate the following (in)separable verb:",
        90: "Translate the following (in)separable verb:",
        91: "Translate the following (in)separable verb:",
        92: "Translate the following (in)separable verb:",
        93: "Translate the following (in)separable verb:",
        94: "Translate the following (in)separable verb:",
        95: "Translate the following (in)separable verb:",
        96: "Translate the following (in)separable verb:",
        97: "Translate the following (in)separable verb:",
        98: "Translate the following (in)separable verb:",
        99: "Translate the following (in)separable verb:",
        100: "Translate the following (in)separable verb:",
        101: "Translate the following (in)separable verb:",
        102: "Translate the following (in)separable verb:",
        103: "Translate the following (in)separable verb:",
    },

    nomen_verben_verbindungen: {
        1: "Find the missing noun in the Noun-Verb Combination:",
        2: "Find the missing verb in the Noun-Verb Combination:",
        3: "Find the missing noun in the following sentence:",
        4: "Find the missing verb in the following sentence:",

        5: "Find the missing noun in the Noun-Verb Combination:",
        6: "Find the missing verb in the Noun-Verb Combination:",
        7: "Find the missing noun in the following sentence:",
        8: "Find the missing verb in the following sentence:",
        9: "Find the missing noun in the Noun-Verb Combination:",
        10: "Find the missing verb in the Noun-Verb Combination:",
        11: "Find the missing noun in the following sentence:",
        12: "Find the missing verb in the following sentence:",
        13: "Find the missing noun in the Noun-Verb Combination:",
        14: "Find the missing verb in the Noun-Verb Combination:",
        15: "Find the missing noun in the following sentence:",
        16: "Find the missing verb in the following sentence:",

        17: "Find the missing noun in the Noun-Verb Combination:",
        18: "Find the missing verb in the Noun-Verb Combination:",
        19: "Find the missing noun in the following sentence:",
        20: "Find the missing verb in the following sentence:",
        21: "Find the missing noun in the Noun-Verb Combination:",
        22: "Find the missing verb in the Noun-Verb Combination:",
        23: "Find the missing noun in the following sentence:",
        24: "Find the missing verb in the following sentence:",
        25: "Find the missing noun in the Noun-Verb Combination:",
        26: "Find the missing verb in the Noun-Verb Combination:",
        27: "Find the missing noun in the following sentence:",
        28: "Find the missing verb in the following sentence:",
        29: "Find the missing noun in the Noun-Verb Combination:",
        30: "Find the missing verb in the Noun-Verb Combination:",
        31: "Find the missing noun in the following sentence:",
        32: "Find the missing verb in the following sentence:",
    },

    adjektive_verben_wortstaemme: {
        1: "Find the missing adjective in the following adjective-verb pair:",
        2: "Find the missing verb in the following adjective-verb pair:",
        3: "Find the missing adjective in the following adjective-verb pair:",
        4: "Find the missing verb in the following adjective-verb pair:",

        5: "Find the missing adjective in the following adjective-verb pair:",
        6: "Find the missing verb in the following adjective-verb pair:",
        7: "Find the missing adjective in the following adjective-verb pair:",
        8: "Find the missing verb in the following adjective-verb pair:",
        9: "Find the missing adjective in the following adjective-verb pair:",
        10: "Find the missing verb in the following adjective-verb pair:",

        11: "Find the missing adjective in the following adjective-verb pair:",
        12: "Find the missing verb in the following adjective-verb pair:",
        13: "Find the missing adjective in the following adjective-verb pair:",
        14: "Find the missing verb in the following adjective-verb pair:",
        15: "Find the missing adjective in the following adjective-verb pair:",
        16: "Find the missing verb in the following adjective-verb pair:",
        17: "Find the missing adjective in the following adjective-verb pair:",
        18: "Find the missing verb in the following adjective-verb pair:",
        19: "Find the missing adjective in the following adjective-verb pair:",
        20: "Find the missing verb in the following adjective-verb pair:",
    },

    adjektive_nomen_wortstaemme: {
        1: "Find the missing adjective in the following adjective-noun pair:",
        2: "Find the missing noun in the following adjective-noun pair:",
        3: "Find the missing adjective in the following adjective-noun pair:",
        4: "Find the missing noun in the following adjective-noun pair:",

        5: "Find the missing adjective in the following adjective-noun pair:",
        6: "Find the missing noun in the following adjective-noun pair:",
        7: "Find the missing adjective in the following adjective-noun pair:",
        8: "Find the missing noun in the following adjective-noun pair:",

        9: "Find the missing adjective in the following adjective-noun pair:",
        10: "Find the missing noun in the following adjective-noun pair:",
        11: "Find the missing adjective in the following adjective-noun pair:",
        12: "Find the missing noun in the following adjective-noun pair:",
        13: "Find the missing adjective in the following adjective-noun pair:",
        14: "Find the missing noun in the following adjective-noun pair:",
        15: "Find the missing adjective in the following adjective-noun pair:",
        16: "Find the missing noun in the following adjective-noun pair:",
        17: "Find the missing adjective in the following adjective-noun pair:",
        18: "Find the missing noun in the following adjective-noun pair:",
    },

    nomen_verben_wortstaemme: {
        1: "Find the missing verb in the following noun-verb pair:",
        2: "Find the missing noun in the following noun-verb pair:",

        3: "Find the missing verb in the following noun-verb pair:",
        4: "Find the missing noun in the following noun-verb pair:",
        5: "Find the missing verb in the following noun-verb pair:",
        6: "Find the missing noun in the following noun-verb pair:",
        7: "Find the missing verb in the following noun-verb pair:",
        8: "Find the missing noun in the following noun-verb pair:",

        9: "Find the missing verb in the following noun-verb pair:",
        10: "Find the missing noun in the following noun-verb pair:",
        11: "Find the missing verb in the following noun-verb pair:",
        12: "Find the missing noun in the following noun-verb pair:",
        13: "Find the missing verb in the following noun-verb pair:",
        14: "Find the missing noun in the following noun-verb pair:",
        15: "Find the missing verb in the following noun-verb pair:",
        16: "Find the missing noun in the following noun-verb pair:",
        17: "Find the missing verb in the following noun-verb pair:",
        18: "Find the missing noun in the following noun-verb pair:",
        19: "Find the missing verb in the following noun-verb pair:",
        20: "Find the missing noun in the following noun-verb pair:",
        21: "Find the missing verb in the following noun-verb pair:",
        22: "Find the missing noun in the following noun-verb pair:",
        23: "Find the missing verb in the following noun-verb pair:",
        24: "Find the missing noun in the following noun-verb pair:",
        25: "Find the missing verb in the following noun-verb pair:",
        26: "Find the missing noun in the following noun-verb pair:",
        27: "Find the missing verb in the following noun-verb pair:",
        28: "Find the missing noun in the following noun-verb pair:",

        29: "Find the missing verb in the following noun-verb pair:",
        30: "Find the missing noun in the following noun-verb pair:",
        31: "Find the missing verb in the following noun-verb pair:",
        32: "Find the missing noun in the following noun-verb pair:",
        33: "Find the missing verb in the following noun-verb pair:",
        34: "Find the missing noun in the following noun-verb pair:",
        35: "Find the missing verb in the following noun-verb pair:",
        36: "Find the missing noun in the following noun-verb pair:",
        37: "Find the missing verb in the following noun-verb pair:",
        38: "Find the missing noun in the following noun-verb pair:",
        39: "Find the missing verb in the following noun-verb pair:",
        40: "Find the missing noun in the following noun-verb pair:",
        41: "Find the missing verb in the following noun-verb pair:",
        42: "Find the missing noun in the following noun-verb pair:",
        43: "Find the missing verb in the following noun-verb pair:",
        44: "Find the missing noun in the following noun-verb pair:",
        45: "Find the missing verb in the following noun-verb pair:",
        46: "Find the missing noun in the following noun-verb pair:",
        47: "Find the missing verb in the following noun-verb pair:",
        48: "Find the missing noun in the following noun-verb pair:",
        49: "Find the missing verb in the following noun-verb pair:",
        50: "Find the missing noun in the following noun-verb pair:",
        51: "Find the missing verb in the following noun-verb pair:",
        52: "Find the missing noun in the following noun-verb pair:",
        53: "Find the missing verb in the following noun-verb pair:",
        54: "Find the missing noun in the following noun-verb pair:",
        55: "Find the missing verb in the following noun-verb pair:",
        56: "Find the missing noun in the following noun-verb pair:",
        57: "Find the missing verb in the following noun-verb pair:",
        58: "Find the missing noun in the following noun-verb pair:",

        59: "Find the missing verb in the following noun-verb pair:",
        60: "Find the missing noun in the following noun-verb pair:",
        61: "Find the missing verb in the following noun-verb pair:",
        62: "Find the missing noun in the following noun-verb pair:",
        63: "Find the missing verb in the following noun-verb pair:",
        64: "Find the missing noun in the following noun-verb pair:",
        65: "Find the missing verb in the following noun-verb pair:",
        66: "Find the missing noun in the following noun-verb pair:",
        67: "Find the missing verb in the following noun-verb pair:",
        68: "Find the missing noun in the following noun-verb pair:",
        69: "Find the missing verb in the following noun-verb pair:",
        70: "Find the missing noun in the following noun-verb pair:",
        71: "Find the missing verb in the following noun-verb pair:",
        72: "Find the missing noun in the following noun-verb pair:",
        73: "Find the missing verb in the following noun-verb pair:",
        74: "Find the missing noun in the following noun-verb pair:",
        75: "Find the missing verb in the following noun-verb pair:",
        76: "Find the missing noun in the following noun-verb pair:",
        77: "Find the missing verb in the following noun-verb pair:",
        78: "Find the missing noun in the following noun-verb pair:",
        79: "Find the missing verb in the following noun-verb pair:",
        80: "Find the missing noun in the following noun-verb pair:",
        81: "Find the missing verb in the following noun-verb pair:",
        82: "Find the missing noun in the following noun-verb pair:",
        83: "Find the missing verb in the following noun-verb pair:",
        84: "Find the missing noun in the following noun-verb pair:",
        85: "Find the missing verb in the following noun-verb pair:",
        86: "Find the missing noun in the following noun-verb pair:",
        87: "Find the missing verb in the following noun-verb pair:",
        88: "Find the missing noun in the following noun-verb pair:",
        89: "Find the missing verb in the following noun-verb pair:",
        90: "Find the missing noun in the following noun-verb pair:",
        91: "Find the missing verb in the following noun-verb pair:",
        92: "Find the missing noun in the following noun-verb pair:",
    },

    zahlen: {
        1: "Write the following number in words:",
        2: "Write the following number in words:",
        3: "Write the following number in words:",
        4: "Write the following number in words:",
        5: "Write the following number in words:",
        6: "Write the following number in words:",
        7: "Write the following number in words:",
        8: "Write the following number in words:",
        9: "Write the following time in words:",
        10: "Write the following time in words:",

        11: "Write the following number in words:",
        12: "Write the following number in words:",
        13: "Translate the following ordinal number:",
        14: "Translate the following ordinal number:",
        15: "Translate the following ordinal number:",
        16: "Complete the following sentence with the ordinal number that fits:",

        17: "Translate the following sequential adverb:",
        18: "Complete the following sentence with the sequential adverb that fits:",
        19: "Translate the following adverb of frequency:",
        20: "Complete the following sentence with the adverb of frequency that fits:",

        21: "Translate the following fraction:",
        22: "Complete the following sentence with the fraction that fits:",

        23: "Write the genitive form of the following number in words:",
        24: "Complete the following sentence with the genitive form of the number that fits:",
    },
}
