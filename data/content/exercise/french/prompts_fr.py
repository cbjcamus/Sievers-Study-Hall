from data.data_processing.exercises import prompt

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

prompt_konnektoren = """
You are evaluating a focused German connector exercise.

Target connector: {german} (French: {french})

Student sentence:
"{user_answer}"

Evaluate each field independently.

inquiry_correct:
Is the target connector correctly used in the clause or phrase containing it?
Consider only errors relevant to the use of the target connector. If the word order is wrong, then the inquiry is incorrect.
Unrelated grammatical errors elsewhere (such as declensions, articles, verb conjugation, typos in other words, commas) must not affect this field.

meaning_coherent:
Is the intended meaning of the entire sentence understandable and logically coherent?
If the sentence is odd or contradictory, then "no".
Grammatical mistakes do not make the meaning incoherent if the intended meaning is clear.

translation:
The user's sentence's translation in French.

commentary:
If the inquiry is incorrect, explain why it's incorrect.
If the meaning is incoherent, explain why.
Identify grammatical or spelling errors that are unrelated to the correct use of the target connector.
Give a brief correction for grammatical and spelling mistakes. 
If there are none, return "none".
Commentary should be in French.
"""

prompt_fragen = """
You are evaluating a focused German question word exercise.

Target question word: {german} (French: {french})

Student sentence:
"{user_answer}"

Evaluate each field independently.

inquiry_correct:
Is the target question word correctly used in the clause or phrase containing it?
Consider only errors relevant to the use of the target question word. If the word order is wrong, then the inquiry is incorrect.
Unrelated grammatical errors elsewhere (such as declensions, articles, verb conjugation, typos in other words, commas) must not affect this field.

meaning_coherent:
Is the intended meaning of the entire sentence understandable and logically coherent?
If the sentence is odd or contradictory, then "no".
Grammatical mistakes do not make the meaning incoherent if the intended meaning is clear.

translation:
The user's sentence's translation in French.

commentary:
If the inquiry is incorrect, explain why it's incorrect.
If the meaning is incoherent, explain why.
Identify grammatical or spelling errors that are unrelated to the correct use of the target question word.
Give a brief correction for grammatical and spelling mistakes. 
If there are none, return "none".
Commentary should be in French.
"""

prompt_adverbien = """
You are evaluating a focused German adverb exercise.

Target adverb: {german} (French: {french})

Student sentence:
"{user_answer}"

Evaluate each field independently.

inquiry_correct:
Is the target adverb correctly used in the clause or phrase containing it?
Consider only errors relevant to the use of the target adverb. If the word order is wrong, then the inquiry is incorrect.
Unrelated grammatical errors elsewhere (such as declensions, articles, verb conjugation, typos in other words, commas) must not affect this field.

meaning_coherent:
Is the intended meaning of the entire sentence understandable and logically coherent?
If the sentence is odd or contradictory, then "no".
Grammatical mistakes do not make the meaning incoherent if the intended meaning is clear.

translation:
The user's sentence's translation in French.

commentary:
If the inquiry is incorrect, explain why it's incorrect.
If the meaning is incoherent, explain why.
Identify grammatical or spelling errors that are unrelated to the correct use of the target adverb.
Give a brief correction for grammatical and spelling mistakes. 
If there are none, return "none".
"""

PROMPT_UNIT_FR = {
    alpha: prompt_konnektoren,
}

PROMPT_CATEGORY_FR = {

}

PROMPT_SUBCATEGORY_FR = {
    konnektoren: {
        prompt: prompt_konnektoren,
    },

    fragen: {
        prompt: prompt_fragen,
    },

    adverbien: {
        prompt: prompt_adverbien,
    },
}

PROMPT_EXERCISE_FR = {

}