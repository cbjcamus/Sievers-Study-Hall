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
    zahlen, alpha, perfekt,
)

prompt_praepositionen = """
You are evaluating a focused German preposition exercise.

Target preposition function: {french}

User sentence:
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
The user's sentence's translation in French.

cefr_level:
An estimation of the CEFR level (A1, A2 etc.) of the user's sentence. Write "none" if not applicable.

commentary:
If the inquiry is incorrect, explain why it's incorrect.
If the meaning is incoherent, explain why.
Identify grammatical or spelling errors that are unrelated to the correct use of the target preposition.
Give a brief correction for grammatical and spelling mistakes. 
If there are none, return "none".
Commentary should be in French. You write using the passive voice.
Use line breaks (<br><br>) to add some clarity if necessary.
"""

prompt_praepositionen_verben = """
You are evaluating a focused German verbe-preposition pair exercise.

Target verb-preposition pair: {german}{case_french} ({french})

User sentence:
"{user_answer}"

Evaluate each field independently.

inquiry_correct:
Is the target verb-preposition used in the clause or phrase containing it, and in the function described?
Consider only errors relevant to the use of the target verb-preposition pair, including the grammatical case
 (accusative, dative or genitive) and the conjugation of the verb. 
If the target verb-preposition is used but not in the meaning intended (see French translation), then the inquiry is incorrect. 
If the word order is wrong, then the inquiry is incorrect.
Unrelated grammatical errors elsewhere (such as gender of nouns, adjective declensions, typos in other words, commas) must not affect this field.

meaning_coherent:
Is the intended meaning of the entire sentence understandable and logically coherent?
If the sentence is odd or contradictory, then "no".
Grammatical mistakes do not make the meaning incoherent if the intended meaning is clear.

translation:
The user's sentence's translation in French.

cefr_level:
An estimation of the CEFR level (A1, A2 etc.) of the user's sentence. Write "none" if not applicable.

commentary:
If the inquiry is incorrect, explain why it's incorrect.
If the meaning is incoherent, explain why.
Identify grammatical or spelling errors that are unrelated to the correct use of the target verb-preposition pair.
Give a brief correction for grammatical and spelling mistakes. 
If there are none, return "none".
Commentary should be in French. You write using the passive voice.
Use line breaks (<br><br>) to add some clarity if necessary.
"""


prompt_pronominaladverbien_dawort = """
You are evaluating a focused German pronominal adverb in <i>da</i> exercise.

Target pronominal adverb: {german}

User sentence:
"{user_answer}"

Evaluate each field independently.

inquiry_correct:
Is the target da-word used in the clause or phrase containing it, and in the function described?
Consider only errors relevant to the use of the target da-word. 
If the word order is wrong at the level of the verb, then the inquiry is incorrect.
Unrelated grammatical errors elsewhere (such as gender of nouns, adjective declensions, typos in other words, commas) must not affect this field.

meaning_coherent:
Is the intended meaning of the entire sentence understandable and logically coherent?
If the sentence is odd or contradictory, then "no".
Grammatical mistakes do not make the meaning incoherent if the intended meaning is clear.

translation:
The user's sentence's translation in French.

cefr_level:
An estimation of the CEFR level (A1, A2 etc.) of the user's sentence. Write "none" if not applicable.

commentary:
If the inquiry is incorrect, explain why it's incorrect.
If the meaning is incoherent, explain why.
Identify grammatical or spelling errors that are unrelated to the correct use of the target da-word.
Give a brief correction for grammatical and spelling mistakes. 
If there are none, return "none".
Commentary should be in French. You write using the passive voice.
Use line breaks (<br><br>) to add some clarity if necessary.
"""

prompt_pronominaladverbien_wowort = """
You are evaluating a focused German pronominal adverb in <i>wo</i> exercise.

Target pronominal adverb: {german}

User sentence:
"{user_answer}"

Evaluate each field independently.

inquiry_correct:
Is the target wo-word used in the clause or phrase containing it, and in the function described?
Consider only errors relevant to the use of the target wo-word. 
If the word order is wrong at the level of the verb, then the inquiry is incorrect.
Unrelated grammatical errors elsewhere (such as gender of nouns, adjective declensions, typos in other words, commas) must not affect this field.

meaning_coherent:
Is the intended meaning of the entire sentence understandable and logically coherent?
If the sentence is odd or contradictory, then "no".
Grammatical mistakes do not make the meaning incoherent if the intended meaning is clear.

translation:
The user's sentence's translation in French.

cefr_level:
An estimation of the CEFR level (A1, A2 etc.) of the user's sentence. Write "none" if not applicable.

commentary:
If the inquiry is incorrect, explain why it's incorrect.
If the meaning is incoherent, explain why.
Identify grammatical or spelling errors that are unrelated to the correct use of the target wo-word.
Give a brief correction for grammatical and spelling mistakes. 
If there are none, return "none".
Commentary should be in French. You write using the passive voice.
Use line breaks (<br><br>) to add some clarity if necessary.
"""

prompt_artikel = """
You are evaluating a focused German article exercise.

Target article: {german} – {case_french} {gender_french}

User sentence:
"{user_answer}"

Evaluate each field independently.

inquiry_correct:
Is the target article correctly used in the clause or phrase containing it?
Consider only errors relevant to the use of the target article. If the word order is wrong, then the inquiry is incorrect.
Unrelated grammatical errors elsewhere (such as verb conjugation, typos in other words, commas) must not affect this field.

meaning_coherent:
Is the intended meaning of the entire sentence understandable and logically coherent?
If the sentence is odd or contradictory, then "no".
Grammatical mistakes do not make the meaning incoherent if the intended meaning is clear.

translation:
The user's sentence's translation in French.

cefr_level:
An estimation of the CEFR level (A1, A2 etc.) of the user's sentence. Write "none" if not applicable.

commentary:
If the inquiry is incorrect, explain why it's incorrect.
If the meaning is incoherent, explain why.
Identify grammatical or spelling errors that are unrelated to the correct use of the target article.
Give a brief correction for grammatical and spelling mistakes. 
If there are none, return "none".
Commentary should be in French. You write using the passive voice. You can be cheeky.
Use line breaks (<br><br>) to add some clarity if necessary.
"""


prompt_pronomen = """
You are evaluating a focused German pronoun exercise.

Target pronoun: {german} – {case_french} {gender_french}

User sentence:
"{user_answer}"

Evaluate each field independently.

inquiry_correct:
Is the target pronoun correctly used in the clause or phrase containing it?
Consider only errors relevant to the use of the target pronoun. If the word order is wrong, then the inquiry is incorrect.
Unrelated grammatical errors elsewhere (such as verb conjugation, typos in other words, commas) must not affect this field.

meaning_coherent:
Is the intended meaning of the entire sentence understandable and logically coherent?
If the sentence is odd or contradictory, then "no".
Grammatical mistakes do not make the meaning incoherent if the intended meaning is clear.

translation:
The user's sentence's translation in French.

cefr_level:
An estimation of the CEFR level (A1, A2 etc.) of the user's sentence. Write "none" if not applicable.

commentary:
If the inquiry is incorrect, explain why it's incorrect.
If the meaning is incoherent, explain why.
Identify grammatical or spelling errors that are unrelated to the correct use of the target pronoun.
Give a brief correction for grammatical and spelling mistakes. 
If there are none, return "none".
Commentary should be in French. You write using the passive voice. You can be cheeky.
Use line breaks (<br><br>) to add some clarity if necessary.
"""

prompt_pronomen_relative = """
You are evaluating a focused German relative pronoun exercise.

Target relative pronoun: {german} – {case_french} {gender_french}

User sentence:
"{user_answer}"

Evaluate each field independently.

inquiry_correct:
Is the target relative pronoun correctly used in the clause or phrase containing it?
Consider only errors relevant to the use of the target relative pronoun.
 If the word order is wrong, then the inquiry is incorrect.
Unrelated grammatical errors elsewhere (such as verb conjugation, typos in other words, commas) must not affect this field.
The relative pronoun must be relative. If the relative pronoun isn't used, or only as a non-relative pronoun, 
then the inquiry is incorrect.

meaning_coherent:
Is the intended meaning of the entire sentence understandable and logically coherent?
If the sentence is odd or contradictory, then "no".
Grammatical mistakes do not make the meaning incoherent if the intended meaning is clear.

translation:
The user's sentence's translation in French.

cefr_level:
An estimation of the CEFR level (A1, A2 etc.) of the user's sentence. Write "none" if not applicable.

commentary:
If the inquiry is incorrect, explain why it's incorrect.
If the meaning is incoherent, explain why.
Identify grammatical or spelling errors that are unrelated to the correct use of the target pronoun.
Give a brief correction for grammatical and spelling mistakes. 
If there are none, return "none".
Commentary should be in French. You write using the passive voice. You can be cheeky.
Use line breaks (<br><br>) to add some clarity if necessary.
"""

prompt_konnektoren = """
You are evaluating a focused German connector exercise.

Target connector: {german} (French: {french})

User sentence:
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

cefr_level:
An estimation of the CEFR level (A1, A2 etc.) of the user's sentence. Write "none" if not applicable.

commentary:
If the inquiry is incorrect, explain why it's incorrect.
If the meaning is incoherent, explain why.
Identify grammatical or spelling errors that are unrelated to the correct use of the target connector.
Give a brief correction for grammatical and spelling mistakes. 
If there are none, return "none".
Commentary should be in French. You write using the passive voice.
Use line breaks (<br><br>) to add some clarity if necessary.
"""

prompt_fragen = """
You are evaluating a focused German question word exercise.

Target question word: {german} (French: {french})

User sentence:
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

cefr_level:
An estimation of the CEFR level (A1, A2 etc.) of the user's sentence. Write "none" if not applicable.

commentary:
If the inquiry is incorrect, explain why it's incorrect.
If the meaning is incoherent, explain why.
Identify grammatical or spelling errors that are unrelated to the correct use of the target question word.
Give a brief correction for grammatical and spelling mistakes. 
If there are none, return "none".
Commentary should be in French. You write using the passive voice.
Use line breaks (<br><br>) to add some clarity if necessary.
"""

prompt_adverbien = """
You are evaluating a focused German adverb exercise.

Target adverb: {german} (French: {french})

User sentence:
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

cefr_level:
An estimation of the CEFR level (A1, A2 etc.) of the user's sentence. Write "none" if not applicable.

commentary:
If the inquiry is incorrect, explain why it's incorrect.
If the meaning is incoherent, explain why.
Identify grammatical or spelling errors that are unrelated to the correct use of the target adverb.
Give a brief correction for grammatical and spelling mistakes. 
If there are none, return "none".
Commentary should be in French. You write using the passive voice.
Use line breaks (<br><br>) to add some clarity if necessary.
"""

prompt_verben = """
You are evaluating a focused German verb exercise.

Target verb: {german} (French: {french})

User sentence:
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
The user's sentence's translation in French.

cefr_level:
An estimation of the CEFR level (A1, A2 etc.) of the user's sentence. Write "none" if not applicable.

commentary:
If the inquiry is incorrect, explain why it's incorrect.
If the meaning is incoherent, explain why.
Identify grammatical or spelling errors that are unrelated to the correct use of the target verb.
Give a brief correction for grammatical and spelling mistakes. 
If there are none, return "none".
Commentary should be in French. You write using the passive voice.
Use line breaks (<br><br>) to add some clarity if necessary.
"""

prompt_nomen_verben_verbindungen = """
You are evaluating a focused German noun-verb combination exercise.

Target noun-verb combination: {german} (French: {french})

User sentence:
"{user_answer}"

Evaluate each field independently.

inquiry_correct:
Is the target noun-verb combination correctly used in the sentence or couple of sentences containing it?
Consider only errors relevant to the use of the target noun-verb combination.
If the word order is wrong at the level of the verb, then the inquiry is incorrect.
Unrelated grammatical errors elsewhere (such as declensions, articles, typos in other words, commas) must not affect this field.

meaning_coherent:
Is the intended meaning of the entire sentence understandable and logically coherent?
If the sentence is odd or contradictory, then "no".
Grammatical mistakes do not make the meaning incoherent if the intended meaning is clear.

translation:
The user's sentence's translation in French.

cefr_level:
An estimation of the CEFR level (A1, A2 etc.) of the User's sentence. Write "none" if not applicable.

commentary:
If the inquiry is incorrect, explain why it's incorrect.
If the meaning is incoherent, explain why.
Identify grammatical or spelling errors that are unrelated to the correct use of the target noun-verb combination.
Give a brief correction for grammatical and spelling mistakes. 
If there are none, return "none".
Commentary should be in French. You write using the passive voice.
Use line breaks (<br><br>) to add some clarity if necessary.
"""


prompt_adjektive = """
You are evaluating a focused German adjective exercise.

Target adjective: {german} (French: {french})

User sentence:
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
The user's sentence's translation in French.

cefr_level:
An estimation of the CEFR level (A1, A2 etc.) of the user's sentence. Write "none" if not applicable.

commentary:
If the inquiry is incorrect, explain why it's incorrect.
If the meaning is incoherent, explain why.
Identify grammatical or spelling errors that are unrelated to the correct use of the target adjective.
Give a brief correction for grammatical and spelling mistakes. 
If there are none, return "none".
Commentary should be in French. You write using the passive voice.
Use line breaks (<br><br>) to add some clarity if necessary.
"""

prompt_perfekt = """
You are evaluating a focused German perfect exercise.

Target verb: {german} (French: {french})

User sentence:
"{user_answer}"

Evaluate each field independently.

inquiry_correct:
Is the target verb correctly conjugated in the perfect in the sentence or couple of sentences containing it?
Consider only errors relevant to the use of the target verb. Both the past participle and the auxiliary verb must be correct.
If the word order is wrong at the level of the verbs (auxiliary and past participle), then the inquiry is incorrect.
Unrelated grammatical errors elsewhere (such as gender of nouns, declensions, typos in other words, commas) must not affect this field.

meaning_coherent:
Is the intended meaning of the entire sentence understandable and logically coherent?
If the sentence is odd or contradictory, then "no".
Grammatical mistakes do not make the meaning incoherent if the intended meaning is clear.

translation:
The user's sentence's translation in French.

cefr_level:
An estimation of the CEFR level (A1, A2 etc.) of the user's sentence. Write "none" if not applicable.

commentary:
If the inquiry is incorrect, explain why it's incorrect.
If the meaning is incoherent, explain why.
Identify grammatical or spelling errors that are unrelated to the correct use of the target verb's conjugation.
Give a brief correction for grammatical and spelling mistakes. 
If there are none, return "none".
Commentary should be in French. You write using the passive voice.
Use line breaks (<br><br>) to add some clarity if necessary.
"""

PROMPT_UNIT_FR = {
    alpha: prompt_konnektoren,
}

PROMPT_CATEGORY_FR = {

}

PROMPT_SUBCATEGORY_FR = {
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

    perfekt: {
        prompt: prompt_perfekt,
    },
}

PROMPT_EXERCISE_FR = {
    pronominaladverbien: {
        5: prompt_pronominaladverbien_dawort,
        7: prompt_pronominaladverbien_wowort,
    },

    pronomen: {
        24: prompt_pronomen_relative,
    },

}