from data.data_processing.exercises import prompt

from data.data_processing.units import (
    praepositionen, konnektoren, fragen, adverbien, verben, alpha, praepositionen_verben, adjektive, perfekt,
    pronominaladverbien, artikel, nomen_verben_verbindungen, pronomen, praeteritum, praesens,
)

meaning_coherent = """
meaning_coherent:
Is the intended meaning of the entire sentence understandable and logically coherent?
If the sentence is odd or contradictory, then "no".
Grammatical mistakes do not make the meaning incoherent if the intended meaning is clear.
"""

translation_english = """
translation:
The user's sentence's translation in English.
"""

cefr_level = """
cefr_level:
An estimation of the CEFR level (A1, A2 etc.) of the user's sentence. Write "none" if not applicable.
"""

commentary_english = """
commentary:
If the inquiry is incorrect, explain why it's incorrect.
If the meaning is incoherent, explain why.
Identify grammatical or spelling errors that are unrelated to the correct use of the target word.
Give a brief correction for grammatical and spelling mistakes. 
If there are none, return "none".
Commentary should be in English. You write using the passive voice directly to the student. You can be cheeky.
Use line breaks (<br><br>) to add some clarity if necessary.
"""

prompt_praepositionen = f"""
You are evaluating a focused German preposition exercise.

Target preposition function: {{english}}

User sentence:
"{{user_answer}}"

Evaluate each field independently.

inquiry_correct:
Is the target preposition used in the clause or phrase containing it, and in the function described?
Consider only errors relevant to the use of the target preposition, including the article that follows
 and the grammatical case (accusative, dative or genitive). 
If the target preposition is used correctly but not in the function intended, then the inquiry is incorrect. 
In particular, if the function describes a position but the user's sentence describe a movement or direction,
 then the inquiry is incorrect (and vice-versa).  
If the word order is wrong, then the inquiry is incorrect.
Unrelated grammatical errors elsewhere (such as gender of nouns, adjective declensions, verb conjugation,
 typos in other words, commas) must not affect this field.

{meaning_coherent}
{translation_english}
{cefr_level}
{commentary_english}
"""

prompt_praepositionen_verben = f"""
You are evaluating a focused German verb-preposition pair exercise.

Target verb-preposition pair: {{german}}{{case_english}} ({{english}})

User sentence:
"{{user_answer}}"

Evaluate each field independently.

inquiry_correct:
Is the target verb-preposition used in the clause or phrase containing it, and in the function described?
Consider only errors relevant to the use of the target verb-preposition pair, including the grammatical case
 (accusative, dative or genitive) and the conjugation of the verb. 
If the target verb-preposition is used but not in the meaning intended (see English translation), then the inquiry is incorrect. 
If the word order is wrong, then the inquiry is incorrect.
Unrelated grammatical errors elsewhere (such as gender of nouns, adjective declensions,
 typos in other words, commas) must not affect this field.

{meaning_coherent}
{translation_english}
{cefr_level}
{commentary_english}
"""

prompt_pronominaladverbien_dawort = f"""
You are evaluating a focused German pronominal adverb in <i>da</i> exercise.

Target pronominal adverb: {{german}}

User sentence:
"{{user_answer}}"

Evaluate each field independently.

inquiry_correct:
Is the target da-word used in the clause or phrase containing it, and in the function described?
Consider only errors relevant to the use of the target da-word. 
If the word order is wrong at the level of the verb, then the inquiry is incorrect.
Unrelated grammatical errors elsewhere (such as gender of nouns, adjective declensions,
 typos in other words, commas) must not affect this field.

{meaning_coherent}

{translation_english}

{cefr_level}

{commentary_english}
"""

prompt_pronominaladverbien_wowort = f"""
You are evaluating a focused German pronominal adverb in <i>wo</i> exercise.

Target pronominal adverb: {{german}}

User sentence:
"{{user_answer}}"

Evaluate each field independently.

inquiry_correct:
Is the target wo-word used in the clause or phrase containing it, and in the function described?
Consider only errors relevant to the use of the target wo-word. 
If the word order is wrong at the level of the verb, then the inquiry is incorrect.
Unrelated grammatical errors elsewhere (such as gender of nouns, adjective declensions,
 typos in other words, commas) must not affect this field.

{meaning_coherent}
{translation_english}
{cefr_level}
{commentary_english}
"""

prompt_artikel = f"""
You are evaluating a focused German article exercise.

Target article: {{german}} – {{case_english}} {{gender_english}}

User sentence:
"{{user_answer}}"

Evaluate each field independently.

inquiry_correct:
Is the target article correctly used in the clause or phrase containing it?
Consider only errors relevant to the use of the target article. If the word order is wrong, then the inquiry is incorrect.
Unrelated grammatical errors elsewhere (such as verb conjugation, typos in other words, commas) must not affect this field.

{meaning_coherent}
{translation_english}
{cefr_level}
{commentary_english}
"""

prompt_pronomen = f"""
You are evaluating a focused German pronoun exercise.

Target pronoun: {{german}} – {{case_english}} {{gender_english}}

User sentence:
"{{user_answer}}"

Evaluate each field independently.

inquiry_correct:
Is the target pronoun correctly used in the clause or phrase containing it?
Consider only errors relevant to the use of the target pronoun. If the word order is wrong, then the inquiry is incorrect.
Unrelated grammatical errors elsewhere (such as verb conjugation, typos in other words, commas) must not affect this field.

{meaning_coherent}
{translation_english}
{cefr_level}
{commentary_english}
"""

prompt_pronomen_relative = f"""
You are evaluating a focused German relative pronoun exercise.

Target relative pronoun: {{german}} – {{case_english}} {{gender_english}}

User sentence:
"{{user_answer}}"

Evaluate each field independently.

inquiry_correct:
Is the target relative pronoun correctly used in the clause or phrase containing it?
Consider only errors relevant to the use of the target relative pronoun.
 If the word order is wrong, then the inquiry is incorrect.
Unrelated grammatical errors elsewhere (such as verb conjugation, typos in other words, commas) must not affect this field.
The relative pronoun must be relative. If the relative pronoun isn't used, or only as a non-relative pronoun, 
then the inquiry is incorrect.

{meaning_coherent}
{translation_english}
{cefr_level}
{commentary_english}
"""

prompt_konnektoren = f"""
You are evaluating a focused German connector exercise.

Target connector: {{german}} (English: {{english}})

User sentence:
"{{user_answer}}"

Evaluate each field independently.

inquiry_correct:
Is the target connector correctly used in the clause or phrase containing it?
Consider only errors relevant to the use of the target connector. If the word order is wrong, then the inquiry is incorrect.
Unrelated grammatical errors elsewhere (such as declensions, articles, verb conjugation,
 typos in other words, commas) must not affect this field.

{meaning_coherent}
{translation_english}
{cefr_level}
{commentary_english}
"""

prompt_fragen = f"""
You are evaluating a focused German question word exercise.

Target question word: {{german}} (English: {{english}})

User sentence:
"{{user_answer}}"

Evaluate each field independently.

inquiry_correct:
Is the target question word correctly used in the clause or phrase containing it?
Consider only errors relevant to the use of the target question word. If the word order is wrong, then the inquiry is incorrect.
Unrelated grammatical errors elsewhere (such as declensions, articles, verb conjugation,
 typos in other words, commas) must not affect this field.

{meaning_coherent}
{translation_english}
{cefr_level}
{commentary_english}
"""

prompt_adverbien = f"""
You are evaluating a focused German adverb exercise.

Target adverb: {{german}} (English: {{english}})

User sentence:
"{{user_answer}}"

Evaluate each field independently.

inquiry_correct:
Is the target adverb correctly used in the clause or phrase containing it?
Consider only errors relevant to the use of the target adverb. If the word order is wrong, then the inquiry is incorrect.
Unrelated grammatical errors elsewhere (such as declensions, articles, verb conjugation,
 typos in other words, commas) must not affect this field.

{meaning_coherent}
{translation_english}
{cefr_level}
{commentary_english}
"""

prompt_verben = f"""
You are evaluating a focused German verb exercise.

Target verb: {{german}} (English: {{english}})

User sentence:
"{{user_answer}}"

Evaluate each field independently.

inquiry_correct:
Is the target verb correctly used in the user's sentence(s)?
Consider only errors relevant to the use of the target verb.
 If the word order is wrong at the level of the verb, then the inquiry is incorrect.
Unrelated grammatical errors elsewhere (such as declensions, articles, typos in other words, commas) must not affect this field.

{meaning_coherent}
{translation_english}
{cefr_level}
{commentary_english}
"""

prompt_nomen_verben_verbindungen = f"""
You are evaluating a focused German noun-verb combination exercise.

Target noun-verb combination: {{german}} (English: {{english}})

User sentence:
"{{user_answer}}"

Evaluate each field independently.

inquiry_correct:
Is the target noun-verb combination correctly used in the user's sentence(s)?
Consider only errors relevant to the use of the target noun-verb combination.
If the word order is wrong at the level of the verb, then the inquiry is incorrect.
Unrelated grammatical errors elsewhere (such as declensions, articles, typos in other words, commas) must not affect this field.

{meaning_coherent}
{translation_english}
{cefr_level}
{commentary_english}
"""

prompt_adjektive = f"""
You are evaluating a focused German adjective exercise.

Target adjective: {{german}} (English: {{english}})

User sentence:
"{{user_answer}}"

Evaluate each field independently.

inquiry_correct:
Is the target adjective correctly used in the user's sentence(s)?
Consider only errors relevant to the use of the target adjective. If the declension is incorrect, the inquiry is incorrect.
If the word order is wrong at the level of the verb, then the inquiry is incorrect.
Unrelated grammatical errors elsewhere (such as verb conjugation, articles,
 typos in other words, commas) must not affect this field.

{meaning_coherent}
{translation_english}
{cefr_level}
{commentary_english}
"""

prompt_perfekt = f"""
You are evaluating a focused German perfect exercise.

Target verb: {{german}} (English: {{english}})

User sentence:
"{{user_answer}}"

Evaluate each field independently.

inquiry_correct:
Is the target verb correctly conjugated in the perfect in the user's sentence(s)?
Consider only errors relevant to the use of the target verb. Both the past participle and the auxiliary verb must be correct.
If the word order is wrong at the level of the verbs (auxiliary and past participle), then the inquiry is incorrect.
Unrelated grammatical errors elsewhere (such as gender of nouns, declensions,
 typos in other words, commas) must not affect this field.

{meaning_coherent}
{translation_english}
{cefr_level}
{commentary_english}
"""

prompt_praesens = f"""
You are evaluating a focused German present tense exercise.

Target verb: {{german}} (English: {{english}})

User sentence:
"{{user_answer}}"

Evaluate each field independently.

inquiry_correct:
Is the target verb correctly conjugated in the present tense in the user's sentence(s)?
If the target verb is at the infinitive, then the inquiry is incorrect. 
Consider only errors relevant to the use of the target verb and tense.
If the word order is wrong at the level of the verbs, then the inquiry is incorrect.
Unrelated grammatical errors elsewhere (such as gender of nouns, declensions, typos in other words,
 commas) must not affect this field.

{meaning_coherent}
{translation_english}
{cefr_level}
{commentary_english}
"""

prompt_praeteritum = f"""
You are evaluating a focused German präteritum exercise.

Target verb: {{german}} (English: {{english}})

User sentence:
"{{user_answer}}"

Evaluate each field independently.

inquiry_correct:
Is the target verb correctly conjugated in the simple past (präteritum) in the user's sentence(s)?
Consider only errors relevant to the use of the target verb and tense.
If the word order is wrong at the level of the verbs, then the inquiry is incorrect.
Unrelated grammatical errors elsewhere (such as gender of nouns, declensions, typos in other words,
 commas) must not affect this field.

{meaning_coherent}
{translation_english}
{cefr_level}
{commentary_english}
"""

PROMPT_UNIT_EN = {

}

PROMPT_CATEGORY_EN = {

}

PROMPT_SUBCATEGORY_EN = {
    praepositionen: {
        prompt: prompt_praepositionen,
    },

    praepositionen_verben: {
        prompt: prompt_praepositionen_verben,
    },

    artikel: {
        prompt: prompt_artikel,
    },

    pronomen: {
        prompt: prompt_pronomen,
    },

    konnektoren: {
        prompt: prompt_konnektoren,
    },

    fragen: {
        prompt: prompt_fragen,
    },

    adverbien: {
        prompt: prompt_adverbien,
    },

    verben: {
        prompt: prompt_verben,
    },

    nomen_verben_verbindungen: {
        prompt: prompt_nomen_verben_verbindungen,
    },

    adjektive: {
        prompt: prompt_adjektive,
    },

    praesens: {
        prompt: prompt_praesens,
    },

    perfekt:{
        prompt: prompt_perfekt,
    },

    praeteritum: {
        prompt: prompt_praeteritum,
    },
}

PROMPT_EXERCISE_EN = {
    pronominaladverbien: {
        5: prompt_pronominaladverbien_dawort,
        7: prompt_pronominaladverbien_wowort,
    },

    pronomen:{
        24: prompt_pronomen_relative,
    },

    alpha: {
        1: prompt_konnektoren,
        2: prompt_fragen,
        3: prompt_adverbien,
        4: prompt_adverbien,

        5: prompt_konnektoren,
        6: prompt_fragen,
        7: prompt_adverbien,
        8: prompt_adverbien,
        9: prompt_adverbien,
    }
}