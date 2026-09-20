from data.data_processing.exercises import prompt

from data.data_processing.units import (
    konnektoren, fragen, adverbien, alpha
)

prompt_konnektoren = """
You are evaluating a focused German connector exercise.

Target connector: {german} (English: {english})

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
The user's sentence's translation in English.

commentary:
If the inquiry is incorrect, explain why it's incorrect.
If the meaning is incoherent, explain why.
Identify grammatical or spelling errors that are unrelated to the correct use of the target connector.
Give a brief correction for grammatical and spelling mistakes. 
If there are none, return "none".
"""

prompt_fragen = """
You are evaluating a focused German question word exercise.

Target question word: {german} (English: {english})

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
The user's sentence's translation in English.

commentary:
If the inquiry is incorrect, explain why it's incorrect.
If the meaning is incoherent, explain why.
Identify grammatical or spelling errors that are unrelated to the correct use of the target question word.
Give a brief correction for grammatical and spelling mistakes. 
If there are none, return "none".
"""

prompt_adverbien = """
You are evaluating a focused German adverb exercise.

Target adverb: {german} (English: {english})

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
The user's sentence's translation in English.

commentary:
If the inquiry is incorrect, explain why it's incorrect.
If the meaning is incoherent, explain why.
Identify grammatical or spelling errors that are unrelated to the correct use of the target adverb.
Give a brief correction for grammatical and spelling mistakes. 
If there are none, return "none".
"""


PROMPT_UNIT_EN = {

}

PROMPT_CATEGORY_EN = {

}

PROMPT_SUBCATEGORY_EN = {
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

PROMPT_EXERCISE_EN = {
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