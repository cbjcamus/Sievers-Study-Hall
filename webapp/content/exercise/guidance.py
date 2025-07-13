from data.data_processing.units import (
    praepositionen_grammatik, praepositionen_verben, praepositionen_adjektive, praepositionen_nomen,
    artikel, pronomen, konnektoren, fragen, adverbien,
    praesens, imperativ, partizip_II, praeteritum, praeteritum_partizip_II,  konjunktiv_II, konjunktiv_I, partizip_I,
    adjektive, adjektivdeklinationen,
    trennbare_verben, verben, deverbale_nomen
)

# bullet point \u25CF

GUIDANCE = {

    praepositionen_grammatik: {
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
        16: "Translate the following preposition:",
        17: "Complete the following sentence with the preposition that fits:",

        18: "Translate the following preposition:",
        19: "Complete the following sentence with the preposition that fits:",
        20: "Translate the following preposition:",
        21: "Complete the following sentence with the preposition that fits:",
    },

    praepositionen_verben: {
        1: "Write the preposition that match the following verb:",
        2: "Complete the following sentence with the preposition that fits:",
        3: "Write the preposition that match the following verb:",
        4: "Complete the following sentence with the preposition that fits:",

        5: "Write the preposition that match the following verb:",
        6: "Complete the following sentence with the preposition that fits:",
        7: "Write the preposition that match the following verb:",
        8: "Complete the following sentence with the preposition that fits:",
        9: "Complete the following sentence with the Da-Wort that fits:",
        10: "Complete the following sentence with the Wo-Wort that fits:",

        11: "Write the preposition that match the following verb:",
        12: "Complete the following sentence with the preposition that fits:",
        13: "Write the preposition that match the following verb:",
        14: "Complete the following sentence with the preposition that fits:",

        15: "Write the preposition that match the following verb:",
        16: "Complete the following sentence with the preposition that fits:",
        17: "Write the preposition that match the following verb:",
        18: "Complete the following sentence with the preposition that fits:",

        19: "Write the preposition that match the following verb:",
        20: "Complete the following sentence with the preposition that fits:",
        21: "Write the preposition that match the following verb:",
        22: "Complete the following sentence with the preposition that fits:",
    },

    praepositionen_adjektive: {
        1: "Write the preposition that match the following adjective:",
        2: "Complete the following sentence with the preposition that fits:",

        3: "Write the preposition that match the following adjective:",
        4: "Complete the following sentence with the preposition that fits:",

        5: "Write the preposition that match the following adjective:",
        6: "Complete the following sentence with the preposition that fits:",
    },

    praepositionen_nomen: {
        1: "Write the preposition that match the following noun:",
        2: "Complete the following sentence with the preposition that fits:",

        3: "Write the preposition that match the following noun:",
        4: "Complete the following sentence with the preposition that fits:",
        5: "Write the preposition that match the following noun:",
        6: "Complete the following sentence with the preposition that fits:",

        7: "Write the preposition that match the following noun:",
        8: "Complete the following sentence with the preposition that fits:",
        9: "Write the preposition that match the following noun:",
        10: "Complete the following sentence with the preposition that fits:",
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
        11: "Write the indefinite article that fits the case and gender provided:",
        12: "Complete the following sentence with the nominative indefinite article that fits:",
        13: "Complete the following sentence with the accusative indefinite article that fits:",
        14: "Complete the following sentence with the dative indefinite article that fits:",
        15: "Complete the following sentence with the feminine indefinite article that fits:",
        16: "Complete the following sentence with the masculine indefinite article that fits:",
        17: "Complete the following sentence with the neuter indefinite article that fits:",
        18: "Complete the following sentence with the indefinite article that fits:",
        19: "Complete the following sentence with the indefinite article that fits:",
        20: "Write the Kein-word that fits the case and gender provided:",
        21: "Complete the following sentence with the Kein-word that fits:",
        22: "Write the possessive article that fits the case and gender provided.",
        23: "Complete the following sentence with the possessive article that fits."
            "<br><br>All the possessive articles are based on singular pronouns (Ich, Du, Er, Sie, Es).",
        24: "Write the possessive article that fits the case and gender provided.",
        25: "Complete the following sentence with the possessive article that fits."
            "<br><br>All the possessive articles are based on plural (Wir, Ihr, Sie) or formal pronouns.",

        26: "Write the demonstrative article that fits the case and gender provided:",
        27: "Complete the following sentence with the demonstrative article that fits:",
        28: "Write jede-word that fits the case and gender provided:",
        29: "Complete the following sentence with the jede-word that fits:",
        30: "Complete the following sentence with the article that fits:",
        31: "Complete the following sentence with the article that fits:",
        32: "Translate the following article:",
        33: "Complete the following sentence with the article that fits:",

        34: "Write the article that fits the case and gender provided:",
        35: "Complete the following sentence with the genitive article that fits:",
        36: "Write the article that fits the case and gender provided:",
        37: "Complete the following sentence with the genitive article that fits:",
        38: "Write the possessive article that fits the case and gender provided:",
        39: "Complete the following sentence with the possessive article that fits:",

        40: "Translate the following article based on the case and gender provided:",
        41: "Complete the following sentence with the article that fits:",

        42: "Translate the following article based on the case and gender provided:",
        43: "Complete the following sentence with the article that fits:",
    },

    pronomen: {
        1: "Complete the following sentence with the nominative pronoun that fits:",
        2: "Complete the following sentence with the accusative pronoun that fits:",
        3: "Complete the following sentence with the dative pronoun that fits:",
        4: "Complete the following sentence with the pronoun that fits:",

        5: "Complete the following sentence with the reflexive pronoun that fits:",
        6: "Complete the following sentence with the pronoun that fits:",
        7: "Complete the following sentence with the pronoun that fits:",
        8: "Provide the translation of the possessive pronoun that fits the case and gender provided:",
        9: "Complete the following sentence with the possessive provide that fits:",
        10: "Provide the translation of the possessive pronoun that fits the case and gender provided:",
        11: "Complete the following sentence with the possessive pronoun that fits:",

        12: "Translate the following pronoun:",
        13: "Complete the following sentence with the pronoun that fits:",
        14: "Complete the following sentence with the nominative relative pronoun that fits:",
        15: "Complete the following sentence with the accusative relative pronoun that fits:",
        16: "Complete the following sentence with the dative relative pronoun that fits:",
        17: "Complete the following sentence with the genitive relative pronoun that fits:",
        18: "Complete the following sentence with the relative pronoun that fits:",

        19: "Complete the following sentence with the relative pronoun that fits:",
        20: "Complete the following sentence with the relative pronoun that fits – there may be more than one option:",
    },

    konnektoren: {
        1: "Translate the following connector:",
        2: "Complete the following sentence with the connector that fits:",

        3: "Translate the following connector:",
        4: "Complete the following sentence with the connector that fits:",

        5: "Translate the following connector:",
        6: "Complete the following sentence with the connector that fits:",
        7: "Find a synonym for the following connector:",

        8: "Translate the following connector:",
        9: "Complete the following sentence with the connector that fits:",
        10: "Translate the following connector:",
        11: "Complete the following sentence with the connector that fits:",
        12: "Find a synonym for the following connector:",

        13: "Translate the following connector:",
        14: "Complete the following sentence with the connector that fits:",
        15: "Find a synonym for the following connector:",
    },

    fragen: {
        1: "Translate the following question word:",
        2: "Complete the following sentence with the question word that fits:",

        3: "Translate the following question word:",
        4: "Complete the following sentence with the question word that fits:",

        5: "Translate the following question word:",
        6: "Complete the following sentence with the question word that fits:",

        7: "Translate the following question word:",
        8: "Complete the following sentence with the question word that fits:",
    },

    adverbien: {
        1: "Translate the following adverb:",
        2: "Complete the following sentence with the adverb that fits:",
        3: "Translate the following adverb:",
        4: "Complete the following sentence with the adverb that fits:",

        5: "Translate the following adverb:",
        6: "Complete the following sentence with the adverb that fits:",
        7: "Translate the following adverb:",
        8: "Complete the following sentence with the adverb that fits:",

        9: "Translate the following adverb:",
        10: "Complete the following sentence with the adverb that fits:",
        11: "Translate the following adverb:",
        12: "Complete the following sentence with the adverb that fits:",
        13: "Translate the following adverb:",
        14: "Complete the following sentence with the adverb that fits:",
        15: "Translate the following adverb:",
        16: "Complete the following sentence with the adverb that fits:",

        17: "Translate the following adverb:",
        18: "Complete the following sentence with the adverb that fits:",
        19: "Translate the following adverb:",
        20: "Complete the following sentence with the adverb that fits:",
        21: "Translate the following adverb:",
        22: "Complete the following sentence with the adverb that fits:",
        23: "Translate the following adverb:",
        24: "Complete the following sentence with the adverb that fits:",

        25: "Translate the following adverb:",
        26: "Complete the following sentence with the adverb that fits:",
        27: "Translate the following adverb:",
        28: "Complete the following sentence with the adverb that fits:",
        29: "Translate the following adverb:",
        30: "Complete the following sentence with the adverb that fits:",
        31: "Translate the following adverb:",
        32: "Complete the following sentence with the adverb that fits:",
    },

    praesens: {
        1: "Conjugate the following verb in the present tense:",
        2: "Conjugate the following verb in the present tense:",
        3: "Conjugate the following verb in the present tense:",
        4: "Conjugate the following verb in the present tense:",
        5: "Conjugate the following verb in the present tense:",
        6: "Conjugate the following verb in the present tense:",
        7: "Conjugate the following verb in the present tense:",
        8: "Conjugate the following verb in the present tense:",
        9: "Conjugate the following verb in the present tense:",
        10: "Conjugate the following verb in the present tense:",
        11: "Conjugate the following verb in the present tense:",
        12: "Conjugate the following verb in the present tense:",

        13: "Conjugate the following verb in the present tense:",
        14: "Conjugate the following verb in the present tense:",
        15: "Conjugate the following verb in the present tense:",
        16: "Conjugate the following verb in the present tense:",
        17: "Conjugate the following verb in the present tense:",
        18: "Conjugate the following verb in the present tense:",
        19: "Conjugate the following verb in the present tense:",
        20: "Conjugate the following verb in the present tense:",
        21: "Conjugate the following verb in the present tense:",
        22: "Conjugate the following verb in the present tense:",
        23: "Conjugate the following verb in the present tense:",
        24: "Conjugate the following verb in the present tense:",
    },

    partizip_II: {
        1: "Write the Partizip II of the following verb:",
        2: "Write the Partizip II of the following verb:",
        3: "Write the Partizip II of the following verb:",

        4: "Write the Partizip II of the following verb:",
        5: "Write the Partizip II of the following verb:",
        6: "Write the Partizip II of the following verb:",

        7: "Write the Partizip II of the following verb:",
        8: "Write the Partizip II of the following verb:",
        9: "Write the Partizip II of the following verb:",
        10: "Write the Partizip II of the following verb:",
        11: "Write the Partizip II of the following verb:",
        12: "Write the Partizip II of the following verb:",

        13: "Write the Partizip II of the following verb:",
        14: "Write the Partizip II of the following verb:",
        15: "Write the Partizip II of the following verb:",
        16: "Write the Partizip II of the following verb:",
        17: "Write the Partizip II of the following verb:",
        18: "Write the Partizip II of the following verb:",
        19: "Write the Partizip II of the following verb:",
        20: "Write the Partizip II of the following verb:",
    },

    praeteritum: {
        1: "Conjugate the following verb in the Präteritum:",

        2: "Conjugate the following verb in the Präteritum (3<sup>rd</sup> Person Singular):",
        3: "Conjugate the following verb in the Präteritum (3<sup>rd</sup> Person Singular):",
        4: "Conjugate the following verb in the Präteritum (3<sup>rd</sup> Person Singular):",
        5: "Conjugate the following verb in the Präteritum (3<sup>rd</sup> Person Singular):",
        6: "Conjugate the following verb in the Präteritum (3<sup>rd</sup> Person Singular):",
        7: "Conjugate the following verb in the Präteritum (3<sup>rd</sup> Person Singular):",

        8: "Conjugate the following verb in the Präteritum (3<sup>rd</sup> Person Singular):",
        9: "Conjugate the following verb in the Präteritum (3<sup>rd</sup> Person Singular):",
        10: "Conjugate the following verb in the Präteritum (3<sup>rd</sup> Person Singular):",
        11: "Conjugate the following verb in the Präteritum (3<sup>rd</sup> Person Singular):",
        12: "Conjugate the following verb in the Präteritum (3<sup>rd</sup> Person Singular):",
        13: "Conjugate the following verb in the Präteritum (3<sup>rd</sup> Person Singular):",

        14: "Conjugate the following verb in the Präteritum (3<sup>rd</sup> Person Singular):",
        15: "Conjugate the following verb in the Präteritum (3<sup>rd</sup> Person Singular):",
        16: "Conjugate the following verb in the Präteritum (3<sup>rd</sup> Person Singular):",
        17: "Conjugate the following verb in the Präteritum (3<sup>rd</sup> Person Singular):",
        18: "Conjugate the following verb in the Präteritum (3<sup>rd</sup> Person Singular):",
        19: "Conjugate the following verb in the Präteritum (3<sup>rd</sup> Person Singular):",
        20: "Conjugate the following verb in the Präteritum (3<sup>rd</sup> Person Singular):",
        21: "Conjugate the following verb in the Präteritum (3<sup>rd</sup> Person Singular):",
    },

    praeteritum_partizip_II: {
        1: "Write the Präteritum (3<sup>rd</sup> Person Singular) and Partizip II of the following verb."
           "<br><br>Use the formats \"spielte gespielt\" or \"spielte, gespielt\".",

        2: "Write the Präteritum (3<sup>rd</sup> Person Singular) and Partizip II of the following verb."
           "<br><br>Use the formats \"spielte gespielt\" or \"spielte, gespielt\".",
        3: "Write the Präteritum (3<sup>rd</sup> Person Singular) and Partizip II of the following verb."
           "<br><br>Use the formats \"spielte gespielt\" or \"spielte, gespielt\".",
        4: "Write the Präteritum (3<sup>rd</sup> Person Singular) and Partizip II of the following verb."
           "<br><br>Use the formats \"spielte gespielt\" or \"spielte, gespielt\".",
        5: "Write the Präteritum (3<sup>rd</sup> Person Singular) and Partizip II of the following verb."
           "<br><br>Use the formats \"spielte gespielt\" or \"spielte, gespielt\".",
        6: "Write the Präteritum (3<sup>rd</sup> Person Singular) and Partizip II of the following verb."
           "<br><br>Use the formats \"spielte gespielt\" or \"spielte, gespielt\".",
        7: "Write the Präteritum (3<sup>rd</sup> Person Singular) and Partizip II of the following verb."
           "<br><br>Use the formats \"spielte gespielt\" or \"spielte, gespielt\".",

        8: "Write the Präteritum (3<sup>rd</sup> Person Singular) and Partizip II of the following verb."
           "<br><br>Use the formats \"spielte gespielt\" or \"spielte, gespielt\".",
        9: "Write the Präteritum (3<sup>rd</sup> Person Singular) and Partizip II of the following verb."
           "<br><br>Use the formats \"spielte gespielt\" or \"spielte, gespielt\".",
        10: "Write the Präteritum (3<sup>rd</sup> Person Singular) and Partizip II of the following verb."
           "<br><br>Use the formats \"spielte gespielt\" or \"spielte, gespielt\".",
        11: "Write the Präteritum (3<sup>rd</sup> Person Singular) and Partizip II of the following verb."
           "<br><br>Use the formats \"spielte gespielt\" or \"spielte, gespielt\".",
        12: "Write the Präteritum (3<sup>rd</sup> Person Singular) and Partizip II of the following verb."
           "<br><br>Use the formats \"spielte gespielt\" or \"spielte, gespielt\".",
        13: "Write the Präteritum (3<sup>rd</sup> Person Singular) and Partizip II of the following verb."
           "<br><br>Use the formats \"spielte gespielt\" or \"spielte, gespielt\".",

        14: "Write the Präteritum (3<sup>rd</sup> Person Singular) and Partizip II of the following verb."
           "<br><br>Use the formats \"spielte gespielt\" or \"spielte, gespielt\".",
        15: "Write the Präteritum (3<sup>rd</sup> Person Singular) and Partizip II of the following verb."
           "<br><br>Use the formats \"spielte gespielt\" or \"spielte, gespielt\".",
        16: "Write the Präteritum (3<sup>rd</sup> Person Singular) and Partizip II of the following verb."
           "<br><br>Use the formats \"spielte gespielt\" or \"spielte, gespielt\".",
        17: "Write the Präteritum (3<sup>rd</sup> Person Singular) and Partizip II of the following verb."
           "<br><br>Use the formats \"spielte gespielt\" or \"spielte, gespielt\".",
        18: "Write the Präteritum (3<sup>rd</sup> Person Singular) and Partizip II of the following verb."
           "<br><br>Use the formats \"spielte gespielt\" or \"spielte, gespielt\".",
        19: "Write the Präteritum (3<sup>rd</sup> Person Singular) and Partizip II of the following verb."
           "<br><br>Use the formats \"spielte gespielt\" or \"spielte, gespielt\".",
        20: "Write the Präteritum (3<sup>rd</sup> Person Singular) and Partizip II of the following verb."
           "<br><br>Use the formats \"spielte gespielt\" or \"spielte, gespielt\".",
        21: "Write the Präteritum (3<sup>rd</sup> Person Singular) and Partizip II of the following verb."
           "<br><br>Use the formats \"spielte gespielt\" or \"spielte, gespielt\".",
    },

    imperativ: {
        1: "Conjugate the following verb in the Imperativ:",
        2: "Conjugate the following verb in the Imperativ:",
        3: "Conjugate the following verb in the Imperativ:",

        4: "Conjugate the following verb in the Imperativ:",
        5: "Conjugate the following verb in the Imperativ:",
        6: "Conjugate the following verb in the Imperativ:",
    },

    konjunktiv_II: {
        1: "Conjugate the following verb in the Konjunktiv II:",
    },

    konjunktiv_I: {
        1: "Conjugate the following verb in the Konjunktiv I:",
        2: "Conjugate the following verb in the Konjunktiv I:",
        3: "Conjugate the following verb in the Konjunktiv I:",
        4: "Conjugate the following verb in the Konjunktiv I:",
        5: "Conjugate the following verb in the Konjunktiv I:",
        6: "Conjugate the following verb in the Konjunktiv I:",
    },

    partizip_I: {
        1: "Write the Partizip I of the following verb:",
        2: "Write the Partizip I of the following verb:",
        3: "Write the Partizip I of the following verb:",
    },

    adjektive: {
        1: "Translate the adjective given in German.",
        2: "Translate the adjective given in German.",
        3: "Write the opposite of the adjective given in German.",
        4: "Write the Comparative of the following adjective:",
        5: "Write the Comparative of the following adjective:",
        6: "Complete the following sentence with the comparative conjunction that fits:",
        7: "Write the Superlative of the following adjective:",
        8: "Write the Superlative of the following adjective:",
    },

    adjektivdeklinationen: {
        1: "Complete the given sentence with the correct declension of the specified adjective.",
        2: "Complete the given sentence with the correct declension of the specified adjective.",
        3: "Complete the given sentence with the correct declension of the specified adjective.",
        4: "Complete the given sentence with the correct declension of the specified adjective.",
        5: "Complete the given sentence with the correct declension of the specified adjective.",
        6: "Complete the given sentence with the correct declension of the specified adjective.",
        7: "Complete the given sentence with the correct declension of the specified adjective.",
        8: "Complete the given sentence with the correct declension of the specified adjective.",
        9: "Complete the given sentence with the correct declension of the specified adjective.",
        10: "Complete the given sentence with the correct declension of the specified adjective.",
        11: "Complete the given sentence with the correct declension of the specified adjective.",
        12: "Complete the given sentence with the correct declension of the specified adjective.",

        13: "Complete the given sentence with the correct declension of the specified adjective.",
        14: "Complete the given sentence with the correct declension of the specified adjective.",
        15: "Complete the given sentence with the correct declension of the specified adjective.",
        16: "Complete the given sentence with the correct declension of the specified adjective.",

        17: "Complete the given sentence with the correct declension of the specified adjective.",
        18: "Complete the given sentence with the correct declension of the specified adjective.",
        19: "Complete the given sentence with the correct declension of the specified adjective.",
        20: "Complete the given sentence with the correct declension of the specified adjective.",

        21: "Complete the given sentence with the correct declension of the specified adjective.",
        22: "Complete the given sentence with the correct declension of the specified adjective.",
    },

    trennbare_verben: {
        1: "Translate the following (un)trennbare verb based on the specified root verb:",
        2: "Translate the following (un)trennbare verb based on the specified prefix:",

        3: "Translate the following (un)trennbare verb based on the specified root verb:",
        4: "Translate the following (un)trennbare verb based on the specified prefix:",

        5: "Translate the following (un)trennbare verb based on the specified root verb:",
        6: "Translate the following (un)trennbare verb based on the specified root verb:",
        7: "Translate the following (un)trennbare verb based on the specified prefix:",
        8: "Translate the following (un)trennbare verb based on the specified prefix:",

        9: "Translate the following (un)trennbare verb based on the specified root verb:",
        10: "Translate the following (un)trennbare verb based on the specified root verb:",
        11: "Translate the following (un)trennbare verb based on the specified root verb:",
        12: "Translate the following (un)trennbare verb based on the specified prefix:",
        13: "Translate the following (un)trennbare verb based on the specified prefix:",
        14: "Translate the following (un)trennbare verb based on the specified prefix:",
    },

    verben: {
        1: "Find the translation of the given verb in German."
           "<br><br>⚠️ Do not write any reflexive pronouns, even for reflexive verbs."
           "<br><br>⚠️ Synonyms are not available for this exercise. Read carefully the entire English translation.",
        2: "Find the translation of the given verb in German."
           "<br><br>⚠️ Do not write any reflexive pronouns, even for reflexive verbs."
           "<br><br>⚠️ Synonyms are not available for this exercise. Read carefully the entire English translation.",
        3: "Find the translation of the given verb in German."
           "<br><br>⚠️ Do not write any reflexive pronouns, even for reflexive verbs."
           "<br><br>⚠️ Synonyms are not available for this exercise. Read carefully the entire English translation.",
        4: "Find the translation of the given verb in German."
           "<br><br>⚠️ Do not write any reflexive pronouns, even for reflexive verbs."
           "<br><br>⚠️ Synonyms are not available for this exercise. Read carefully the entire English translation.",
        5: "Find the translation of the given verb in German."
           "<br><br>⚠️ Do not write any reflexive pronouns, even for reflexive verbs."
           "<br><br>⚠️ Synonyms are not available for this exercise. Read carefully the entire English translation.",

        6: "Find the translation of the given verb in German."
           "<br><br>⚠️ Do not write any reflexive pronouns, even for reflexive verbs."
           "<br><br>⚠️ Synonyms are not available for this exercise. Read carefully the entire English translation.",
        7: "Find the translation of the given verb in German."
           "<br><br>⚠️ Do not write any reflexive pronouns, even for reflexive verbs."
           "<br><br>⚠️ Synonyms are not available for this exercise. Read carefully the entire English translation.",
        8: "Find the translation of the given verb in German."
           "<br><br>⚠️ Do not write any reflexive pronouns, even for reflexive verbs."
           "<br><br>⚠️ Synonyms are not available for this exercise. Read carefully the entire English translation.",
        9: "Find the translation of the given verb in German."
           "<br><br>⚠️ Do not write any reflexive pronouns, even for reflexive verbs."
           "<br><br>⚠️ Synonyms are not available for this exercise. Read carefully the entire English translation.",
        10: "Find the translation of the given verb in German."
           "<br><br>⚠️ Do not write any reflexive pronouns, even for reflexive verbs."
           "<br><br>⚠️ Synonyms are not available for this exercise. Read carefully the entire English translation.",
    },

    deverbale_nomen: {
        1: "Complete the blank with the noun that fits:",
        2: "Complete the blank with the noun that fits:",
        3: "Complete the blank with the noun that fits:",
        4: "Complete the blank with the noun that fits:",
        5: "Complete the blank with the noun that fits:",
        6: "Complete the blank with the noun that fits:",
        7: "Complete the blank with the noun that fits:",
        8: "Complete the blank with the noun that fits:",
        9: "Complete the blank with the noun that fits:",
        10: "Complete the blank with the noun that fits:",
        11: "Complete the blank with the noun that fits:",
        12: "Complete the blank with the noun that fits:",
        13: "Complete the blank with the noun that fits:",
        14: "Complete the blank with the noun that fits:",
        15: "Complete the blank with the noun that fits:",
        16: "Complete the blank with the noun that fits:",
    },

}
# arrow &#8594

