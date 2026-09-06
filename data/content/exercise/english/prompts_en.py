from data.data_processing.units import (
    praepositionen, praepositionen_verben, praepositionen_adjektive, praepositionen_nomen, pronominaladverbien,
    artikel, pronomen, praepositionen_artikel, verben_artikel,
    konnektoren, fragen, adverbien, wortstellung,
    genus_regeln, genus, plural,
    adjektive, komparativ_superlativ, adjektivdeklinationen, adjektive_konjunktionen,
    verben, trennbare_verben, nomen_verben_verbindungen,
    praesens, imperativ, partizip_II, praeteritum, praeteritum_partizip_II, konjunktiv_II, konjunktiv_I, partizip_I,
    nomen_verben_wortstaemme, adjektive_verben_wortstaemme, adjektive_nomen_wortstaemme,
    zahlen, alpha
)

prompt_konnektoren = """
You are evaluating a focused German connector exercise.

Target connector: {german}

Student sentence:
"{user_answer}"

Evaluate each field independently.

inquiry_correct:
Is the target connector correctly used in the clause or phrase containing it?
Consider only errors relevant to the use of the target connector. 
Unrelated grammatical errors elsewhere must not affect this field.

meaning_coherent:
Is the intended meaning of the entire sentence understandable and logically coherent?
Grammatical mistakes do not make the meaning incoherent if the intended meaning is clear.

other_errors:
Identify grammatical or spelling errors that are unrelated to the correct use of the target connector.
Give a brief correction for grammatical and spelling mistakes. 
Do not provide a correction when the meaning is incoherent, 
only say that the sentence is incoherent. If there are none, return "none".

Return ONLY a valid JSON object with exactly these keys:
{{
  "inquiry_correct": "yes" or "no",
  "meaning_coherent": "yes" or "no",
  "german_sentence": "exact student sentence",
  "translation": "English translation of the intended meaning",
  "other_errors": "a brief description and correction or let it blank"
}}
"""


PROMPT_UNIT_EN = {
    alpha: prompt_konnektoren,
}

PROMPT_EXERCISE_EN = {

}