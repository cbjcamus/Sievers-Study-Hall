from data.data_processing.units import (
    praepositionen, praepositionen_verben, praepositionen_adjektive, praepositionen_nomen,
    praepositionen_adverbien, praepositionen_artikel, verben_artikel,
    artikel, pronomen, konnektoren, fragen, adverbien, wortstellung,
    genus_regeln, genus, plural,
    adjektive, komparativ_superlativ, adjektivdeklinationen, adjektive_konjunktionen,
    verben, trennbare_verben, nomen_verben_verbindungen,
    praesens, imperativ, partizip_II, praeteritum, praeteritum_partizip_II, konjunktiv_II, konjunktiv_I, partizip_I,
    nomen_verben_wortstaemme, adjektive_verben_wortstaemme, adjektive_nomen_wortstaemme,
    zahlen,
)

from webapp.style.icons import ICON_CHECK, ICON_CROSS, ICON_WARN

# bullet point \u25CF

GUIDANCE_UNIT_EN = {
    wortstellung:
        "Placeholder"
    ,

    praepositionen_artikel:
        "For each question, you will be provided an incomplete German sentence, its English translation, "
        "a preposition and an article or a pronoun."
        "<br><br>Complete the German sentence with the preposition and the article or pronoun that fits."

        f"<br><br>➡️ If you need help on the gender of the noun, click on the m/f/n/pl button."

        "<h2>Example</h2>"
        "Ein Zettel klebt _____ Schrank. \u25CF an \u25CF der/die/das"
        "<br><br><i>A note is stuck to the closet.</i>"
        f"<br><br> &nbsp; {ICON_CHECK} am"
        f"<br><br> &nbsp; {ICON_CHECK} an dem"
        f"<br><br> &nbsp; {ICON_CROSS} dem"
        f"<br><br> &nbsp; {ICON_CROSS} an"
    ,

    verben_artikel:
        "For each question, you will be provided an incomplete German sentence, its English translation, "
        "and an article or a pronoun."
        "<br><br>Complete the German sentence with the article or pronoun that fits."

        f"<br><br>➡️ If you need help on the gender of the noun, click on the m/f/n/pl button."

        "<h2>Examples</h2>"
        "Ich danke _____ für deine Hilfe. \u25CF du"
        "<br><br><i>I thank you for your help.</i>"
        f"<br><br> &nbsp; {ICON_CHECK} dir"
        f"<br><br> &nbsp; {ICON_CROSS} du"
        f"<br><br> &nbsp; {ICON_CROSS} dich"

        "<br><br>Ich trinke _____ Kaffee. \u25CF ein"
        "<br><br><i>I drink a coffee.</i>"
        f"<br><br> &nbsp; {ICON_CHECK} einen"
        f"<br><br> &nbsp; {ICON_CROSS} ein"
        f"<br><br> &nbsp; {ICON_CROSS} eine"
        f"<br><br> &nbsp; {ICON_CROSS} den"
    ,

    adjektive_konjunktionen:
        "For each question, you will be provided a German sentence and its English translation."
        "<br><br>The German sentence has a conjunction missing. Find the one that fits."

        "<h2>Example</h2>"
        "Peter ist größer _____ sein Bruder."
        "<br><br><i>Peter is taller than his brother.</i>"
        f"<br><br> &nbsp; {ICON_CHECK} als"
    ,

    praesens:
        "For each question, you will see a German verb with a personal pronoun."
        "<br>Conjugate the verb in the Present tense for that pronoun."
        
        f"<br><br> {ICON_WARN} Do not write the personal pronoun, or your answer will be flagged as incorrect."
        f"<br><br> {ICON_WARN} The answer may require a reflexive pronoun if the verb is always reflexive."
        
        "<h2>Examples</h2>"
        "haben \u25CF Ich _____"
        f"<br><br> &nbsp; {ICON_CHECK} habe"
        f"<br><br> &nbsp; {ICON_CROSS} Ich habe"
        f"<br><br> &nbsp; {ICON_CROSS} ich habe"
        
        "<br><br>sich freuen \u25CF Ich _____"
        f"<br><br> &nbsp; {ICON_CHECK} freue mich"
        f"<br><br> &nbsp; {ICON_CROSS} Ich freue mich"
        f"<br><br> &nbsp; {ICON_CROSS} freue"
    ,

    partizip_II:
        "For each question, you will see a German verb."
        "<br>Provide the Partizip II (Past Participle) of the given verb."
        
        f"<br><br> {ICON_WARN} Do not write any Hilfsverb, or your answer will be flagged as incorrect."
        f"<br><br> {ICON_WARN} The answer may require a reflexive pronoun if the verb is always reflexive."
        
        "<h2>Examples</h2>"
        "erinnern"
        f"<br><br> &nbsp; {ICON_CHECK} erinnert"
        f"<br><br> &nbsp; {ICON_CHECK} sich erinnert"
        f"<br><br> &nbsp; {ICON_CROSS} hat erinnert"
        
        "<br><br>sich freuen"
        f"<br><br> &nbsp; {ICON_CHECK} sich gefreut"
        f"<br><br> &nbsp; {ICON_CROSS} gefreute"
        f"<br><br> &nbsp; {ICON_CROSS} hat sich gefreut"
    ,

    praeteritum:
        "For each question, you will see a German verb."
        "<br>Conjugate the verb in the Präteritum tense (Preterit) using the indicated person."
        
        f"<br><br> {ICON_WARN} Do not write the personal pronoun, or your answer will be flagged as incorrect."
        f"<br><br> {ICON_WARN} The answer may require a reflexive pronoun if the verb is always reflexive."
        
        "<h2>Examples</h2>"
        "erinnern"
        f"<br><br> &nbsp; {ICON_CHECK} erinnerte"
        f"<br><br> &nbsp; {ICON_CHECK} erinnerte sich"
        f"<br><br> &nbsp; {ICON_CROSS} er erinnerte"
        
        "<br><br>sich freuen"
        f"<br><br> &nbsp; {ICON_CHECK} freute sich"
        f"<br><br> &nbsp; {ICON_CROSS} freute"
        f"<br><br> &nbsp; {ICON_CROSS} er freute sich"
    ,

    praeteritum_partizip_II:
        "For each question, you will see a German verb."
        "<br>Provide the 3rd person Singular (Er/Sie/Es) Präteritum and the Partizip II the of the given verb."
        
        f"<br><br> {ICON_WARN} Do not write the personal pronoun, or your answer will be flagged as incorrect."
        f"<br><br> {ICON_WARN} Do not write any Hilfsverb, or your answer will be flagged as incorrect."
        f"<br><br> {ICON_WARN} Do not write any reflexive pronoun, even if the verb is usually reflexive."
        
        "<h2>Example</h2>"
        "freuen"
        f"<br><br> &nbsp; {ICON_CHECK} freute, gefreut"
        f"<br><br> &nbsp; {ICON_CHECK} freute gefreut"
        f"<br><br> &nbsp; {ICON_CHECK} freute /       gefreut"
        f"<br><br> &nbsp; {ICON_CROSS} freute, hat gefreut"
        f"<br><br> &nbsp; {ICON_CROSS} er freute, gefreut"
        f"<br><br> &nbsp; {ICON_CROSS} freute sich, sich gefreut"
    ,

    imperativ:
        "For each question, you will see a German verb with a personal pronoun."
        "<br>Conjugate the verb in the Imperative tense for that pronoun."
        
        f"<br><br> {ICON_WARN} Write personal pronouns only in the case of the 3rd Plural."
        f"<br><br> {ICON_WARN} The answer may require a reflexive pronoun if the verb is always reflexive."
        
        "<h2>Example</h2>"
        "sich freuen \u25CF Du"
        f"<br><br> &nbsp; {ICON_CHECK} freu dich"
        f"<br><br> &nbsp; {ICON_CHECK} freue dich"
        f"<br><br> &nbsp; {ICON_CROSS} Du freu dich"

        "<br><br>sich freuen \u25CF Sie"
        f"<br><br> &nbsp; {ICON_CHECK} freuen Sie sich"
        f"<br><br> &nbsp; {ICON_CROSS} freuen Sie"
        f"<br><br> &nbsp; {ICON_CROSS} freuen sich"
    ,

    konjunktiv_II:
        "For each question, you will see a German verb with a personal pronoun."
        "<br>Conjugate the verb in the Conjunctive II tense for that pronoun."
        
        f"<br><br> {ICON_WARN} Do not write the personal pronoun, or your answer will be flagged as incorrect."
        
        "<h2>Example</h2>"
        "sein \u25CF Du"
        f"<br><br> &nbsp; {ICON_CHECK} wärest"
        f"<br><br> &nbsp; {ICON_CROSS} Du wärest"
    ,

    konjunktiv_I:
        "For each question, you will see a German verb with a personal pronoun."
        "<br>Conjugate the verb in the Conjunctive I tense for that pronoun."
        
        f"<br><br> {ICON_WARN} Do not write the personal pronoun, or your answer will be flagged as incorrect."
        
        "<h2>Example</h2>"
        "sein \u25CF Du"
        f"<br><br> &nbsp; {ICON_CHECK} seiest"
        f"<br><br> &nbsp; {ICON_CROSS} Du seiest"
    ,

    partizip_I:
        "For each question, you will see a German verb."
        "<br>Provide the Partizip I (Present Participle) of the given verb."
        
        f"<br><br> {ICON_WARN} The answer may require a reflexive pronoun if the verb is always reflexive."
        
        "<h2>Example</h2>"
        "sich freuen"
        f"<br><br> &nbsp; {ICON_CHECK} sich freuend"
        f"<br><br> &nbsp; {ICON_CROSS} freuend"
    ,

    genus_regeln:
        "For each question, you will be provided a German noun and its English translation."
        "<br><br>Find the definite article (<i>Der</i>, <i>Die</i> or <i>Das</i>) that fits the noun."

        "<br><br>➡️ A guide explaining the gender of nouns is available "
        "<a href=\"https://sieversstudyhall.substack.com/p/genders-of-german-noun-from-a1-to\" target=\"_blank\">here</a>."
        
        f"<br><br> {ICON_WARN} There is only one correct answer per question."

        "<h2>Example</h2>"
        "_____ Abend"
        "<br><br><i>The evening</i>"
        f"<br><br> &nbsp; {ICON_CHECK} Der"
        f"<br><br> &nbsp; {ICON_CHECK} der"
        f"<br><br> &nbsp; {ICON_CROSS} Die"
    ,

    genus:
        "For each question, you will be provided a German noun and its English translation."
        "<br><br>Find the definite article (<i>Der</i>, <i>Die</i> or <i>Das</i>) that fits the noun."
        
        "<br><br>➡️ A guide explaining the gender of nouns is available "
        "<a href=\"https://sieversstudyhall.substack.com/p/genders-of-german-noun-from-a1-to\" target=\"_blank\">here</a>."

        f"<br><br> {ICON_WARN} There is only one correct answer per question."

        "<h2>Example</h2>"
        "_____ Abend"
        "<br><br><i>The evening</i>"
        f"<br><br> &nbsp; {ICON_CHECK} Der"
        f"<br><br> &nbsp; {ICON_CHECK} der"
        f"<br><br> &nbsp; {ICON_CROSS} Die"
    ,

    plural:
        "For each question, you will be provided a German noun and its English translation."
        "<br><br>Find the plural form of this noun."

        f"<br><br> {ICON_WARN} There is only one correct answer per question."

        "<h2>Example</h2>"
        "Singular: die Stunde (<i>the hour</i>)"
        "<br><br>Plural: die _____"
        f"<br><br> &nbsp; {ICON_CHECK} Stunden"
        f"<br><br> &nbsp; {ICON_CHECK} stunden"
        f"<br><br> &nbsp; {ICON_CROSS} Stunde"
    ,
}
