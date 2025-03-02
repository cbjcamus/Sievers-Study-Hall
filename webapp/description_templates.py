from data.exercises import (artikel, pronomen, konnektoren, praepositionen_grammatik, adjektivDeklinationen,
                            praesens, praepositionen_konjugation, imperativ, perfekt, praeteritum, konjunktiv,
                            verben, adjektive, adverbien)

DESCRIPTION_TEMPLATES = {
    artikel: {
        1: "Nominative, Definite Articles in sentences",
        2: "Accusative, Definite Articles in sentences",
        3: "Dative, Definite Articles in sentences",
        4: "Nominative, Accusative, and Dative Definite Articles in sentences",
        5: "Nominative, Indefinite Articles in sentences",
        6: "Accusative, Indefinite Articles in sentences",
        7: "Dative, Indefinite Articles in sentences",
        8: "Nominative, Accusative, and Dative Indefinite Articles in sentences",
        9: "Accusative and Dative Definite Articles with prepositions in sentences",
        10: "Simple (A2) Articles in isolation",
        11: "Simple (A2) Articles in sentences",
        12: "Common (B2) Articles in isolation",
        13: "Common (B2) Articles in sentences",
    },

    pronomen: {
        1: "Nominative Pronouns in sentences",
        2: "Accusative Pronouns in sentences",
        3: "Dative Pronouns in sentences",
        4: "Accusative and Dative Pronouns in sentences",
        5: "Reflexive Pronouns in sentences",
        6: "Accusative, Dative, and Reflexive Pronouns in sentences",
        7: "Familiar (B1) Pronouns in isolation",
        8: "Familiar (B1) Pronouns in sentences",
        9: "Nominative, Relative Pronouns in sentences",
        10: "Accusative, Relative Pronouns in sentences",
        11: "Dative, Relative Pronouns in sentences",
        12: "Genitive, Relative Pronouns in sentences",
        13: "Nominative, Accusative, Dative, and Genitive, Relative Pronouns in sentences",
        14: "Nominative, Accusative, Dative, and Genitive, Relative Pronouns in sentences",
    },

    konnektoren: {
        1: "Basic (A1) Connectors in isolation",
        2: "Basic (A1) Connectors in sentences",
        3: "Simple (A2) Connectors in isolation",
        4: "Simple (A2) Connectors in sentences",
        5: "Familiar (B1) Connectors in isolation",
        6: "Familiar (B1) Connectors in sentences",
        7: "Common (B2) Connectors in isolation",
        8: "Common (B2) Connectors in sentences",
    },

    praepositionen_grammatik: {
        1: "Basic (A1) Prepositions in isolation",
        2: "Temporal Prepositions in sentences",
        3: "Local (Place) Prepositions in sentences",
        4: "Local (Direction) Prepositions in sentences",
        5: "Modal and Causal Prepositions in sentences",
        6: "Comparative Prepositions in sentences",
        7: "Review of Basic (A1) prepositions in sentences",
        8: "Review of Basic (A1) prepositions in sentences",
        9: "Familiar (B1) prepositions in isolation",
        10: "Familiar (B1) prepositions in sentences",
        11: "Common (B2) prepositions in isolation",
        12: "Common (B2) prepositions in sentences",
    },

    adjektivDeklinationen: {
        1: "Nominative, Accusative, and Dative Adjective Declinations in isolation",
        2: "Nominative Adjective Declinations in sentences",
        3: "Accusative Adjective Declinations in sentences",
        4: "Dative Adjective Declinations in sentences",
        5: "Definite Articles' Adjective Declinations in sentences",
        6: "Indefinite Articles' Adjective Declinations in sentences",
        7: "No Article's Adjective Declinations in sentences",
        8: "Nominative, Accusative, and Dative Adjective Declinations in sentences",
        9: "Genitive, Possessive, Negative, and Demonstrative Adjective Declinations in isolation",
        10: "Genitive Adjective Declinations in sentences",
        11: "Possessive Articles' Adjective Declinations in sentences",
        12: "Demonstrative Articles' Adjective Declinations in sentences",
        13: "Negative Articles' Adjective Declinations in sentences",
        14: "Genitive, Possessive, Negative, and Demonstrative Adjective Declinations in sentences",
        15: "Neutral and Plural Article's Adjective Declinations in isolation",
        16: "Neutral and Plural Article's Adjective Declinations in sentences",
    },

    praesens: {
        1: "Present tense of A1 verbs in isolation",
        2: "Present tense of A1 verbs in isolation",
        3: "Present tense of A1 verbs in isolation",
        4: "Present tense of A1 verbs in isolation",
        5: "Present tense of A1 verbs in isolation",
        6: "Present tense of A2 verbs in isolation",
        7: "Present tense of A2 verbs in isolation",
        8: "Present tense of A2 verbs in isolation",
        9: "Present tense of A2 verbs in isolation",
        10: "Present tense of A2 verbs in isolation",
    },

    praepositionen_konjugation: {
        1: "A1 Verb-Preposition pairs in isolation",
        2: "A1 Verb-Preposition pairs in sentences",
        3: "A2 Verb-Preposition pairs in isolation",
        4: "A2 Verb-Preposition pairs in sentences",
        5: "B1 Verb-Preposition pairs in isolation",
        6: "B1 Verb-Preposition pairs in sentences",
        7: "Da-Words in sentences",
        8: "Wo-Words in sentences",
        9: "B2 Verb-Preposition pairs in isolation",
        10: "B2 Verb-Preposition pairs in sentences",
        11: "Noun-Preposition pairs in isolation",
        12: "Noun-Preposition pairs in sentences",
        13: "Adjective-Preposition pairs in isolation",
        14: "Adjective-Preposition pairs in sentences",
    },

    perfekt: {
        1: "Partizip II of A1 verbs in isolation",
        2: "Partizip II of A1 verbs in sentences",
        3: "Hilfsverb of A2 verbs in sentences",
        4: "Partizip II of A2 verbs in isolation",
        5: "Partizip II of A2 verbs in sentences",
        6: "Hilfsverb of A2 verbs in sentences",
        7: "Partizip II of 75 B1 verbs",
        8: "Partizip II of 75 B1 verbs",
    },

    praeteritum: {
        1: "Präteritum of the most common verbs",
        2: "Präteritum (3rd. Per. Singular) of A1 verbs",
        3: "Präteritum (3rd. Per. Singular) of A2 verbs",
        4: "Präteritum (3rd. Per. Singular) of B1 verbs",
        5: "Präteritum (3rd. Per. Singular) of B1 verbs",
    },

    imperativ: {
        1: "Imperative of A1 verbs",
        2: "Imperative of A1 verbs",
        3: "Imperative of A1 verbs",
        4: "Imperative of A1 verbs",
        5: "Imperative of A1 verbs",
    },

    konjunktiv: {
        1: "Konjunktiv II of the most common verbs",
    },

    adverbien: {
        1: "Basic (A1) Adverbs in isolation",
        2: "Basic (A1) Adverbs in sentences",
        3: "Simple (A2) Adverbs in isolation",
        4: "Simple (A2) Adverbs in sentences",
        5: "Familiar (B1) Adverbs in isolation",
        6: "Familiar (B1) Adverbs in sentences",
        7: "Common (B2) Adverbs in isolation",
        8: "Common (B2) Adverbs in sentences",
    },
}


'''
Basic = A1
Simple = A2
Familiar = B1
Common = B2
'''