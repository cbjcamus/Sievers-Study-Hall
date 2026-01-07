from data.data_processing.units import (
    praepositionen_grammatik, praepositionen_verben, praepositionen_adjektive, praepositionen_nomen,
    praepositionen_artikel,
    artikel, pronomen, konnektoren, fragen, adverbien, wortstellung,
    adjektive, adjektivdeklinationen, adjektive_konjunktionen,
    trennbare_verben, verben,
    praesens, imperativ, partizip_II, praeteritum, praeteritum_partizip_II, konjunktiv_II, konjunktiv_I, partizip_I,
    genus_regeln, genus_routledge, genus_goethe,
)

from webapp.style.icons import ICON_CHECK, ICON_CROSS, ICON_WARN

# bullet point \u25CF

GUIDANCE_UNIT_EN = {
    wortstellung:
        "Placeholder"
    ,

    praepositionen_artikel:
        "For each question, you will be provided an incomplete German sentence and its English translation."
        "<br><br>Complete the German sentence with the article or pronoun that fits."

        f"<br><br>{ICON_WARN} There is only one correct answer per question."

        "<h2>Example</h2>"
        "Das Bild hängt an _____ Tür."
        "<br><br><i>The picture hangs on the door.</i>"
        f"<br><br>{ICON_CHECK} der"
    ,

    adjektive_konjunktionen:
        "For each question, you will be provided a German sentence and its English translation."
        "<br><br>The German sentence has a conjunction missing. Find the one that fits."

        "<h2>Example</h2>"
        "Peter ist größer _____ sein Bruder."
        "<br><br><i>Peter is taller than his brother.</i>"
        f"<br><br>{ICON_CHECK} als"
    ,

    praesens:
        "For each question, you will see a German verb with a personal pronoun."
        "<br>Conjugate the verb in the Present tense for that pronoun."
        
        f"<br><br>{ICON_WARN} Do not write the personal pronoun, or your answer will be flagged as incorrect."
        f"<br><br>{ICON_WARN} Do not write any reflexive pronoun, even if the verb is usually reflexive."
        
        "<h2>Example</h2>"
        "freuen \u25CF Ich _____"
        f"<br><br>{ICON_CHECK} freue"
        f"<br><br>{ICON_CROSS} Ich freue"
        f"<br><br>{ICON_CROSS} freue mich"
    ,

    partizip_II:
        "For each question, you will see a German verb."
        "<br>Provide the Partizip II (Past Participle) of the given verb."
        
        f"<br><br>{ICON_WARN} Do not write any Hilfsverb, or your answer will be flagged as incorrect."
        f"<br><br>{ICON_WARN} Do not write any reflexive pronoun, even if the verb is usually reflexive."
        
        "<h2>Example</h2>"
        "freuen"
        f"<br><br>{ICON_CHECK} gefreut"
        f"<br><br>{ICON_CROSS} sich gefreut"
        f"<br><br>{ICON_CROSS} hat gefreut"
    ,

    praeteritum:
        "For each question, you will see a German verb."
        "<br>Conjugate the verb in the Präteritum tense (Preterit) at the 3rd person Singular (Er/Sie/Es) of the given verb."
        
        f"<br><br>{ICON_WARN} Do not write the personal pronoun, or your answer will be flagged as incorrect."
        f"<br><br>{ICON_WARN} Do not write any reflexive pronoun, even if the verb is usually reflexive."
        
        "<h2>Example</h2>"
        "freuen"
        f"<br><br>{ICON_CHECK} freute"
        f"<br><br>{ICON_CROSS} freute sich"
        f"<br><br>{ICON_CROSS} er freute"
    ,

    praeteritum_partizip_II:
        "For each question, you will see a German verb."
        "<br>Provide the 3rd person Singular (Er/Sie/Es) Präteritum and the Partizip II the of the given verb."
        
        f"<br><br>{ICON_WARN} Separate the Präteritum and the Partizip II with a space or a comma and a space."
        f"<br><br>{ICON_WARN} Do not write the personal pronoun, or your answer will be flagged as incorrect."
        f"<br><br>{ICON_WARN} Do not write any Hilfsverb, or your answer will be flagged as incorrect."
        f"<br><br>{ICON_WARN} Do not write any reflexive pronoun, even if the verb is usually reflexive."
        
        "<h2>Example</h2>"
        "freuen"
        f"<br><br>{ICON_CHECK} freute, gefreut"
        f"<br><br>{ICON_CHECK} freute gefreut"
        f"<br><br>{ICON_CROSS} freute, hat gefreut"
        f"<br><br>{ICON_CROSS} er freute, gefreut"
        f"<br><br>{ICON_CROSS} freute sich, sich gefreut"
    ,

    imperativ:
        "For each question, you will see a German verb with a personal pronoun."
        "<br>Conjugate the verb in the Imperative tense for that pronoun."
        
        f"<br><br>{ICON_WARN} Write personal pronouns only in the case of the 3rd Plural."
        f"<br><br>{ICON_WARN} Do not write any reflexive pronoun, even if the verb is usually reflexive."
        
        "<h2>Example</h2>"
        "freuen \u25CF Du"
        f"<br><br>{ICON_CHECK} freu"
        f"<br><br>{ICON_CROSS} Du freu"
        f"<br><br>{ICON_CROSS} freu dich"
        "<br><br>freuen \u25CF Sie"
        f"<br><br>{ICON_CHECK} freuen Sie"
        f"<br><br>{ICON_CROSS} freuen"
        f"<br><br>{ICON_CROSS} freuen sich"
    ,

    konjunktiv_II:
        "For each question, you will see a German verb with a personal pronoun."
        "<br>Conjugate the verb in the Conjunctive II tense for that pronoun."
        
        f"<br><br>{ICON_WARN} Do not write the personal pronoun, or your answer will be flagged as incorrect."
        
        "<h2>Example</h2>"
        "sein \u25CF Du"
        f"<br><br>{ICON_CHECK} wärest"
        f"<br><br>{ICON_CROSS} Du wärest"
    ,

    konjunktiv_I:
        "For each question, you will see a German verb with a personal pronoun."
        "<br>Conjugate the verb in the Conjunctive I tense for that pronoun."
        
        f"<br><br>{ICON_WARN} Do not write the personal pronoun, or your answer will be flagged as incorrect."
        
        "<h2>Example</h2>"
        "sein \u25CF Du"
        f"<br><br>{ICON_CHECK} seiest"
        f"<br><br>{ICON_CROSS} Du seiest"
    ,

    partizip_I:
        "For each question, you will see a German verb."
        "<br>Provide the Partizip I (Present Participle) of the given verb."
        
        f"<br><br>{ICON_WARN} Do not write any reflexive pronoun, even if the verb is usually reflexive."
        
        "<h2>Example</h2>"
        "freuen"
        f"<br><br>{ICON_CHECK} freuend"
        f"<br><br>{ICON_CROSS} sich freuend"
    ,

    genus_regeln:
        "For each question, you will be provided a German noun and its English translation."
        "<br><br>Find the definite article (Der, Die or Das) that fits the noun."

        "<br><br>→ A guide explaining the gender of nouns is available "
        "<a href=\"https://sieversstudyhall.substack.com/p/genders-of-german-noun-from-a1-to\" target=\"_blank\">here</a>."
        
        f"<br><br>{ICON_WARN} There is only one correct answer per question."

        "<h2>Example</h2>"
        "_____ Abend"
        "<br><br><i>The evening</i>"
        f"<br><br>{ICON_CHECK} Der"
        f"<br><br>{ICON_CHECK} der"
        f"<br><br>{ICON_CROSS} Die"
    ,

    genus_routledge:
        "For each question, you will be provided a German noun and its English translation."
        "<br><br>Find the definite article (Der, Die or Das) that fits the noun."
        
        "<br><br>→ A guide explaining the gender of nouns is available "
        "<a href=\"https://sieversstudyhall.substack.com/p/genders-of-german-noun-from-a1-to\" target=\"_blank\">here</a>."

        f"<br><br>{ICON_WARN} There is only one correct answer per question."

        "<h2>Example</h2>"
        "_____ Abend"
        "<br><br><i>The evening</i>"
        f"<br><br>{ICON_CHECK} Der"
        f"<br><br>{ICON_CHECK} der"
        f"<br><br>{ICON_CROSS} Die"
    ,

    genus_goethe:
        "For each question, you will be provided a German noun and its English translation."
        "<br><br>Find the definite article (Der, Die or Das) that fits the noun."
        
        "<br><br>→ A guide explaining the gender of nouns is available "
        "<a href=\"https://sieversstudyhall.substack.com/p/genders-of-german-noun-from-a1-to\" target=\"_blank\">here</a>."

        f"<br><br>{ICON_WARN} There is only one correct answer per question."

        "<h2>Example</h2>"
        "_____ Abend"
        "<br><br><i>The evening</i>"
        f"<br><br>{ICON_CHECK} Der"
        f"<br><br>{ICON_CHECK} der"
        f"<br><br>{ICON_CROSS} Die"
    ,
}
