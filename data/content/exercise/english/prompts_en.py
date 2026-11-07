from data.data_processing.exercises import prompt

from data.data_processing.units import (
    praepositionen, konnektoren, fragen, adverbien, verben, alpha, praepositionen_verben, adjektive,
)

prompt_praepositionen = """
You are evaluating a focused German preposition exercise.

Target preposition function: {english}

Student sentence:
"{user_answer}"

Evaluate each field independently.

inquiry_correct:
Is the target preposition used in the clause or phrase containing it, and in the function described?
Consider only errors relevant to the use of the target preposition, including the article that follows and the grammatical case (accusative, dative or genitive). 
If the target preposition is used correctly but not in the function intended, then the inquiry is incorrect. 
In particular, if the function describes a position but the user's sentence describe a movement or direction, then the inquiry is incorrect (and vice-versa).  
If the word order is wrong, then the inquiry is incorrect.
Unrelated grammatical errors elsewhere (such as gender of nouns, adjective declensions, verb conjugation, typos in other words, commas) must not affect this field.

meaning_coherent:
Is the intended meaning of the entire sentence understandable and logically coherent?
If the sentence is odd or contradictory, then "no".
Grammatical mistakes do not make the meaning incoherent if the intended meaning is clear.

translation:
The user's sentence's translation in English.

cefr_level:
An estimation of the CEFR level (A1, A2 etc.) of the student's sentence. Write "none" if not applicable.

commentary:
If the inquiry is incorrect, explain why it's incorrect.
If the meaning is incoherent, explain why.
Identify grammatical or spelling errors that are unrelated to the correct use of the target preposition.
Give a brief correction for grammatical and spelling mistakes. 
If there are none, return "none".
Commentary should be in English. Use line breaks (<br>) to add some clarity if necessary.
"""

prompt_praepositionen_verben = """
You are evaluating a focused German verbe-preposition pair exercise.

Target verb-preposition pair: {german}{case_english} ({english})

Student sentence:
"{user_answer}"

Evaluate each field independently.

inquiry_correct:
Is the target verb-preposition used in the clause or phrase containing it, and in the function described?
Consider only errors relevant to the use of the target verb-preposition pair, including the grammatical case
 (accusative, dative or genitive) and the conjugation of the verb. 
If the target verb-preposition is used but not in the meaning intended (see English translation), then the inquiry is incorrect. 
If the word order is wrong, then the inquiry is incorrect.
Unrelated grammatical errors elsewhere (such as gender of nouns, adjective declensions, typos in other words, commas) must not affect this field.

meaning_coherent:
Is the intended meaning of the entire sentence understandable and logically coherent?
If the sentence is odd or contradictory, then "no".
Grammatical mistakes do not make the meaning incoherent if the intended meaning is clear.

translation:
The user's sentence's translation in English.

cefr_level:
An estimation of the CEFR level (A1, A2 etc.) of the student's sentence. Write "none" if not applicable.

commentary:
If the inquiry is incorrect, explain why it's incorrect.
If the meaning is incoherent, explain why.
Identify grammatical or spelling errors that are unrelated to the correct use of the target verb-preposition pair.
Give a brief correction for grammatical and spelling mistakes. 
If there are none, return "none".
Commentary should be in English. Use line breaks (<br>) to add some clarity if necessary.
"""

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

cefr_level:
An estimation of the CEFR level (A1, A2 etc.) of the student's sentence. Write "none" if not applicable.

commentary:
If the inquiry is incorrect, explain why it's incorrect.
If the meaning is incoherent, explain why.
Identify grammatical or spelling errors that are unrelated to the correct use of the target connector.
Give a brief correction for grammatical and spelling mistakes. 
If there are none, return "none".
Commentary should be in English. Use line breaks (<br>) to add some clarity if necessary.
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

cefr_level:
An estimation of the CEFR level (A1, A2 etc.) of the student's sentence. Write "none" if not applicable.

commentary:
If the inquiry is incorrect, explain why it's incorrect.
If the meaning is incoherent, explain why.
Identify grammatical or spelling errors that are unrelated to the correct use of the target question word.
Give a brief correction for grammatical and spelling mistakes. 
If there are none, return "none".
Commentary should be in English. Use line breaks (<br>) to add some clarity if necessary.
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

cefr_level:
An estimation of the CEFR level (A1, A2 etc.) of the student's sentence. Write "none" if not applicable.

commentary:
If the inquiry is incorrect, explain why it's incorrect.
If the meaning is incoherent, explain why.
Identify grammatical or spelling errors that are unrelated to the correct use of the target adverb.
Give a brief correction for grammatical and spelling mistakes. 
If there are none, return "none".
Commentary should be in English. Use line breaks (<br>) to add some clarity if necessary.
"""

prompt_verben = """
You are evaluating a focused German verb exercise.

Target verb: {german} (English: {english})

Student sentence:
"{user_answer}"

Evaluate each field independently.

inquiry_correct:
Is the target verb correctly used in the sentence or couple of sentences containing it?
Consider only errors relevant to the use of the target verb. If the word order is wrong at the level of the verb, then the inquiry is incorrect.
Unrelated grammatical errors elsewhere (such as declensions, articles, typos in other words, commas) must not affect this field.

meaning_coherent:
Is the intended meaning of the entire sentence understandable and logically coherent?
If the sentence is odd or contradictory, then "no".
Grammatical mistakes do not make the meaning incoherent if the intended meaning is clear.

translation:
The user's sentence's translation in English.

cefr_level:
An estimation of the CEFR level (A1, A2 etc.) of the student's sentence. Write "none" if not applicable.

commentary:
If the inquiry is incorrect, explain why it's incorrect.
If the meaning is incoherent, explain why.
Identify grammatical or spelling errors that are unrelated to the correct use of the target verb.
Give a brief correction for grammatical and spelling mistakes. 
If there are none, return "none".
Commentary should be in English. Use line breaks (<br>) to add some clarity if necessary.
"""

prompt_adjektive = """
You are evaluating a focused German adjective exercise.

Target adjective: {german} (English: {english})

Student sentence:
"{user_answer}"

Evaluate each field independently.

inquiry_correct:
Is the target adjective correctly used in the sentence or couple of sentences containing it?
Consider only errors relevant to the use of the target adjective. If the declension is incorrect, the inquiry is incorrect.
If the word order is wrong at the level of the verb, then the inquiry is incorrect.
Unrelated grammatical errors elsewhere (such as verb conjugation, articles, typos in other words, commas) must not affect this field.

meaning_coherent:
Is the intended meaning of the entire sentence understandable and logically coherent?
If the sentence is odd or contradictory, then "no".
Grammatical mistakes do not make the meaning incoherent if the intended meaning is clear.

translation:
The user's sentence's translation in English.

cefr_level:
An estimation of the CEFR level (A1, A2 etc.) of the student's sentence. Write "none" if not applicable.

commentary:
If the inquiry is incorrect, explain why it's incorrect.
If the meaning is incoherent, explain why.
Identify grammatical or spelling errors that are unrelated to the correct use of the target adjective.
Give a brief correction for grammatical and spelling mistakes. 
If there are none, return "none".
Commentary should be in English. Use line breaks (<br>) to add some clarity if necessary.
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
        prompt: prompt_praepositionen,
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

    adjektive: {
        prompt: prompt_adjektive,
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