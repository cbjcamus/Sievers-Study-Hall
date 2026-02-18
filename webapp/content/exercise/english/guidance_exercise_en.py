from data.data_processing.units import (
    praepositionen_grammatik, praepositionen_verben, praepositionen_adjektive, praepositionen_nomen,
    praepositionen_artikel, praepositionen_adverbien,
    artikel, pronomen, konnektoren, fragen, adverbien,
    adjektive, adjektivdeklinationen,
    verben, trennbare_verben, nomen_verben_verbindungen, nomen_verben_wortstaemme,
    praesens, imperativ, partizip_II, praeteritum, praeteritum_partizip_II, konjunktiv_II, konjunktiv_I, partizip_I,
    zahlen,
)

from webapp.style.icons import ICON_CHECK, ICON_CROSS, ICON_WARN

# bullet point \u25CF

guidance_praepositionen_grammatik_isolation = (
    "For each question, you will be provided the English translation of a German preposition."
    "<br><br>Find the preposition that fits the English translation."

    f"<br><br> &nbsp; {ICON_WARN} Synonyms are available for this exercise. There may be more than one possible answer."
    f"<br><br> &nbsp; {ICON_WARN} Do not write more than one answer, or your answer will be flagged as false."
    
    "<h2>Example</h2>"
    "due to, because of"
    f"<br><br> &nbsp; {ICON_CHECK} wegen"
    f"<br><br> &nbsp; {ICON_CHECK} aufgrund"
    f"<br><br> &nbsp; {ICON_CROSS} wegen, aufgrund"
)

guidance_praepositionen_grammatik_sentences = (
    "For each question, you will be provided an incomplete German sentence and its English translation."
    "<br><br>Complete the German sentence with the preposition that fits."

    f"<br><br> &nbsp; {ICON_WARN} Synonyms are available for this exercise. There may be more than one possible answer."
    f"<br><br> &nbsp; {ICON_WARN} Do not write more than one answer, or your answer will be flagged as false."
    f"<br><br> &nbsp; {ICON_WARN} The correct answer may be an absence of preposition. In that case, leave the input box empty."
    f"<br><br> &nbsp; {ICON_WARN} The correct answer may include an article. In that case, both the form of the prepositional"
    f" contraction (am, ans, vom, zur etc.) or the extended form (an dem etc.) are correct."
    
    f"<br><br>➡️ You can find a guide to German preposition <a href=\"https://sieversstudyhall.substack.com/p/basic-german-prepositions-uses-up\" target=\"_blank\">here</a>."
    
    "<h2>Examples</h2>"
    "Ich habe _____ Montag Deutschunterricht."
    "<br><br><i>I have German class on Monday.</i>"
    f"<br><br> &nbsp; {ICON_CHECK} am"
    f"<br><br> &nbsp; {ICON_CHECK} an dem"
    f"<br><br> &nbsp; {ICON_CROSS} an"

    "<br><br>Ich trinke eine Tasse _____ Kaffee."
    "<br><br><i>I drink a cup of coffee.</i>"
    f"<br><br> &nbsp; {ICON_CHECK} "
    f"<br><br> &nbsp; {ICON_CROSS} von"
)

guidance_praepositionen_grammatik_synonyms = (
    "For each question, you will be provided a German preposition."
    "<br><br>Find a synonym of that preposition."

    f"<br><br> &nbsp; {ICON_WARN} There may be more than one possible answer."
    f"<br><br> &nbsp; {ICON_WARN} Do not write more than one synonym, or your answer will be flagged as false."

    "<h2>Example</h2>"
    "wegen"
    f"<br><br> &nbsp; {ICON_CHECK} aufgrund"
    f"<br><br> &nbsp; {ICON_CHECK} auf Grund"
    f"<br><br> &nbsp; {ICON_CROSS} aufgrund, auf Grund"
)

guidance_praepositionen_grammatik_antonym = (
    "For each question, you will see a German preposition."
    "<br>Write its antonym in German."

    f"<br><br> &nbsp; {ICON_WARN} Synonyms are available for this exercise. There may be more than one possible answer."
    f"<br><br> &nbsp; {ICON_WARN} Do not write more than one answer, or your answer will be flagged as false."

    "<h2>Example</h2>"
    "trotz"
    f"<br><br> &nbsp; {ICON_CHECK} wegen"
    f"<br><br> &nbsp; {ICON_CHECK} aufgrund"
    f"<br><br> &nbsp; {ICON_CROSS} wegen, aufgrund"
)

guidance_praepositionen_verben_isolation = (
    "For each question, you will be provided an incomplete German Verb-Preposition pair and its English translation."
    "<br><br>Complete the Verb-Preposition pair with the preposition that fits."

    f"<br><br> &nbsp; {ICON_WARN} There is only one correct answer per question."
    
    "<h2>Example</h2>"
    "to think of = denken _____"
    f"<br><br> &nbsp; {ICON_CHECK} an"
)

guidance_praepositionen_verben_sentences = (
    "For each question, you will be provided an incomplete German sentence and its English translation."
    "<br><br>Complete the German sentence with the preposition that fits."

    f"<br><br> &nbsp; {ICON_WARN} There is only one correct answer per question."
    
    "<h2>Example</h2>"
    "Ich denke _____ meine Mutter."
    "<br><br><i>I think about my mother.</i>"
    f"<br><br> &nbsp; {ICON_CHECK} an"
)

guidance_praepositionen_verben_dawort = (
    "For each question, you will be provided an incomplete German sentence and its English translation."
    "<br><br>Complete the German sentence with the Da-Wort that fits."

    f"<br><br> &nbsp; {ICON_WARN} There is only one correct answer per question."

    "<h2>Example</h2>"
    "— Vermissen Sie Ihr Land? <br><bt>— Ja, ich denke oft _____."
    "<br><br><i>— Do you miss your country? <br><bt>— Yes, I often think about it.</i>"
    f"<br><br> &nbsp; {ICON_CHECK} daran"
)

guidance_praepositionen_verben_wowort = (
    "For each question, you will be provided an incomplete German sentence and its English translation."
    "<br><br>Complete the German sentence with the Wo-Wort that fits."

    f"<br><br> &nbsp; {ICON_WARN} There is only one correct answer per question."

    "<h2>Example</h2>"
    "_____ denkst du?"
    "<br><br><i>What are you thinking about?</i>"
    f"<br><br> &nbsp; {ICON_CHECK} Woran"
)

guidance_praepositionen_adjektive_isolation = (
    "For each question, you will be provided an incomplete German Adjective-Preposition pair and its English translation."
    "<br><br>Complete the Adjective-Preposition pair with the preposition that fits." 

    f"<br><br> &nbsp; {ICON_WARN} There is only one correct answer per question."
    
    "<h2>Example</h2>"
    "curious about = neugierig _____"
    f"<br><br> &nbsp; {ICON_CHECK} auf"
)

guidance_praepositionen_adjektive_sentences = (
    "For each question, you will be provided an incomplete German sentence and its English translation."
    "<br><br>Complete the German sentence with the preposition that fits."

    f"<br><br> &nbsp; {ICON_WARN} There is only one correct answer per question."

    "<h2>Example</h2>"
    "Ich bin neugierig _____ die Ergebnisse der Untersuchung."
    "<br><br><i>I am curious about the results of the investigation.</i>"
    f"<br><br> &nbsp; {ICON_CHECK} auf"
)

guidance_praepositionen_nomen_isolation = (
    "For each question, you will be provided an incomplete German Noun-Preposition pair and its English translation."
    "<br><br>Complete the Noun-Preposition pair with the preposition that fits."

    f"<br><br> &nbsp; {ICON_WARN} There is only one correct answer per question."

    "<h2>Example</h2>"
    "the pride in = der Stolz _____"
    f"<br><br> &nbsp; {ICON_CHECK} auf"
)

guidance_praepositionen_nomen_sentences = (
    "For each question, you will be provided an incomplete German sentence and its English translation."
    "<br><br>Complete the German sentence with the preposition that fits."

    f"<br><br> &nbsp; {ICON_WARN} There is only one correct answer per question."

    "<h2>Example</h2>"
    "Er zeigte Stolz _____ sein Team nach dem Sieg."
    "<br><br><i>He showed pride in his team after the victory.</i>"
    f"<br><br> &nbsp; {ICON_CHECK} auf"
)

guidance_artikel_isolation = (
    "For each question, you will be provided a German article as well as a gender and a case."
    "<br><br>Write the article that corresponds to the gender and case."

    "<h2>Example</h2>"
    "der/die/das \u25CF Feminine, Nominative"
    f"<br><br> &nbsp; {ICON_CHECK} die"
)

guidance_artikel_sentences = (
    "For each question, you will be provided a German sentence and its English translation."
    "<br><br>The German sentence has an article missing. Find the one that fits, taking into account the case and gender."

    f"<br><br>➡️ If you need help on the gender of the noun, click on the m/f/n/pl button."

    "<h2>Example</h2>"
    "_____ Woche hat sieben Tage."
    "<br><br><i>The week has seven days.</i>"
    f"<br><br> &nbsp; {ICON_CHECK} Die"
)

guidance_pronomen_isolation = (
    "For each question, you will be provided a German pronoun as well as a case."
    "<br><br>Write the article that corresponds to the case."

    "<h2>Example</h2>"
    "1st Person Singular \u25CF Nominative"
    f"<br><br> &nbsp; {ICON_CHECK} Ich"
)

guidance_pronomen_sentences = (
    "For each question, you will be provided a German sentence and its English translation."
    "<br><br>The German sentence has a pronoun missing. Find the one that fits, taking into account the grammatical"
    " case (and the gender if applicable)."

    f"<br><br>➡️ If you need help on the gender of a noun, click on the m/f/n/pl button."

    "<h2>Example</h2>"
    "Heute bin _____ sehr müde."
    "<br><br><i>Today I am very tired.</i>"
    f"<br><br> &nbsp; {ICON_CHECK} ich"
)

guidance_pronomen_replacing = (
    "For each question, you will be provided a German sentence, its English translation, and an object."
    "<br><br>Replace the object with the pronoun that fits, taking into account the grammatical case and the gender if applicable."

    "<h2>Example</h2>"
    "Wir besuchen die Schule jeden Tag. \u25CF die Schule"
    "<br><br><i>We visit the school every day.</i>"
    f"<br><br> &nbsp; {ICON_CHECK} sie"
    f"<br><br> &nbsp; {ICON_CROSS} es"
    f"<br><br> &nbsp; {ICON_CROSS} ihr"
)

guidance_konnektoren_isolation = (
    "For each question, you will be provided the English translation of a German connector and its grammatical"
    " category (coordinating conjunction, subordinating conjunction, adverb, correlative conjunction)."
    "<br><br>Find the German connector that corresponds to that translation and grammatical type."

    f"<br><br> &nbsp; {ICON_WARN} Synonyms are available for this exercise. There may be more than one possible answer."
    f"<br><br> &nbsp; {ICON_WARN} Take the connector's grammatical category into account. If your answer is a correct literal translation, "
    f"but the grammatical category is incorrect, your answer will be flagged as false"
    f"<br><br> &nbsp; {ICON_WARN} Do not write more than one answer, or your answer will be flagged as false."

    "<h2>Examples</h2>"
    "because, for \u25CF Coordinating conjunction"
    f"<br><br> &nbsp; {ICON_CHECK} denn"
    f"<br><br> &nbsp; {ICON_CROSS} weil (It's a subordinating conjunction, not a coordinating conjunction)"
    f"<br><br>"
    
    "therefore, for this reason, because of that \u25CF Adverb"
    f"<br><br> &nbsp; {ICON_CHECK} deshalb"
    f"<br><br> &nbsp; {ICON_CHECK} deswegen"
    f"<br><br> &nbsp; {ICON_CROSS} deshalb, deswegen"
    f"<br><br> &nbsp; {ICON_CROSS} weshalb (It's a subordinating conjunction, not an adverb)"
    f"<br><br>"
    
    "both and \u25CF Correlative conjunction"
    f"<br><br> &nbsp; {ICON_CHECK} sowohl als auch"
    f"<br><br> &nbsp; {ICON_CHECK} sowohl ... als auch"
    f"<br><br> &nbsp; {ICON_CROSS} sowie (It's a coordinating conjunction, not a correlative conjunction)"
)

guidance_konnektoren_sentences = (
    "For each question, you will be provided a German sentence and its English translation."
    "<br><br>The German sentence has a connector missing. Find the one that fits."

    f"<br><br> &nbsp; {ICON_WARN} Synonyms are available for this exercise. There may be more than one possible answer."
    f"<br><br> &nbsp; {ICON_WARN} Do not write more than one answer, or your answer will be flagged as false."

    "<h2>Example</h2>"
    "Es regnet stark, _____ nehme ich meinen Regenschirm."
    "<br><br><i>It is raining heavily, therefore I take my umbrella.</i>"
    f"<br><br> &nbsp; {ICON_CHECK} deshalb"
    f"<br><br> &nbsp; {ICON_CHECK} deswegen"
    f"<br><br> &nbsp; {ICON_CROSS} deshalb, deswegen"
    f"<br><br> &nbsp; {ICON_CROSS} weshalb"
)

guidance_konnektoren_synonyms = (
    "For each question, you will be provided a German connector and its grammatical type (conjuntion, subjunction,"
    " adverb)."
    "<br><br>Find a synonym of that connector that has the same grammatical type."

    f"<br><br> &nbsp; {ICON_WARN} Do not write more than one synonym, or your answer will be flagged as false."

    "<h2>Example</h2>"
    "darum \u25CF Adverb"
    f"<br><br> &nbsp; {ICON_CHECK} deshalb"
    f"<br><br> &nbsp; {ICON_CHECK} deswegen"
    f"<br><br> &nbsp; {ICON_CROSS} deshalb, deswegen"
    f"<br><br> &nbsp; {ICON_CROSS} darum"
    f"<br><br> &nbsp; {ICON_CROSS} weshalb"
)

guidance_fragen_isolation = (
    "For each question, you will be provided the English translation of a German question-word."
    "<br><br>Find the German question-word that corresponds to that translation."
    
    f"<br><br> &nbsp; {ICON_WARN} Synonyms are available for this exercise. There may be more than one possible answer."
    f"<br><br> &nbsp; {ICON_WARN} Do not write more than one answer, or your answer will be flagged as false."

    "<h2>Example</h2>"
    "Why"
    f"<br><br> &nbsp; {ICON_CHECK} Warum"
    f"<br><br> &nbsp; {ICON_CHECK} Weshalb"
    f"<br><br> &nbsp; {ICON_CROSS} Warum, Weshalb"
)

guidance_fragen_sentences = (
    "For each question, you will be provided a German sentence and its English translation."
    "<br><br>The German sentence has a question-word missing. Find the one that fits."

    f"<br><br> &nbsp; {ICON_WARN} Synonyms are available for this exercise. There may be more than one possible answer."
    f"<br><br> &nbsp; {ICON_WARN} Do not write more than one answer, or your answer will be flagged as false."

    f"<br><br>➡️ If you need help on the gender of the noun, click on the m/f/n/pl button."

    "<h2>Example</h2>"
    "_____ lernst du Deutsch?"
    "<br><br><i>Why are you learning German?</i>"
    f"<br><br> &nbsp; {ICON_CHECK} Warum"
    f"<br><br> &nbsp; {ICON_CHECK} Weshalb"
    f"<br><br> &nbsp; {ICON_CROSS} Warum, Weshalb"
)

guidance_adverbien_isolation = (
    "For each question, you will be provided the English translation of a German adverb."
    "<br><br>Find the German adverb that corresponds to that translation."

    f"<br><br> &nbsp; {ICON_WARN} Synonyms are available for this exercise. There may be more than one possible answer."
    f"<br><br> &nbsp; {ICON_WARN} Do not write more than one answer, or your answer will be flagged as false."

    "<h2>Example</h2>"
    "almost"
    f"<br><br> &nbsp; {ICON_CHECK} fast"
    f"<br><br> &nbsp; {ICON_CHECK} nahezu"
    f"<br><br> &nbsp; {ICON_CROSS} fast, nahezu"
)

guidance_adverbien_sentences = (
    "For each question, you will be provided a German sentence and its English translation."
    "<br><br>The German sentence has an adverb missing. Find the one that fits."

    f"<br><br> &nbsp; {ICON_WARN} Synonyms are available for this exercise. There may be more than one possible answer."
    f"<br><br> &nbsp; {ICON_WARN} Do not write more than one answer, or your answer will be flagged as false."

    "<h2>Example</h2>"
    "Ich bin _____ fertig."
    "<br><br><i>I am almost done.</i>"
    f"<br><br> &nbsp; {ICON_CHECK} fast"
    f"<br><br> &nbsp; {ICON_CHECK} nahezu"
    f"<br><br> &nbsp; {ICON_CROSS} fast, nahezu"
)

guidance_adverbien_synonyms = (
    "For each question, you will be provided a German adverb."
    "<br><br>Find a synonym of that adverb."

    f"<br><br> &nbsp; {ICON_WARN} There may be more than one possible answer."
    f"<br><br> &nbsp; {ICON_WARN} Do not write more than one synonym, or your answer will be flagged as false."

    "<h2>Example</h2>"
    "mindestens"
    f"<br><br> &nbsp; {ICON_CHECK} wenigstens"
    f"<br><br> &nbsp; {ICON_CHECK} zumindest"
    f"<br><br> &nbsp; {ICON_CROSS} wenigstens, zumindest"
)

guidance_adverbien_antonym = (
    "For each question, you will see a German adverb."
    "<br>Write its antonym in German."

    f"<br><br> &nbsp; {ICON_WARN} Synonyms are available for this exercise. There may be more than one possible answer."
    f"<br><br> &nbsp; {ICON_WARN} Do not write more than one answer, or your answer will be flagged as false."

    "<h2>Example</h2>"
    "immer"
    f"<br><br> &nbsp; {ICON_CHECK} nie"
    f"<br><br> &nbsp; {ICON_CHECK} nimmer"
    f"<br><br> &nbsp; {ICON_CROSS} nie, nimmer"
)

guidance_adverbien_hin_her_isolation = (
    "For each question, you will be provided the English translation of a German adverb."
    "<br><br>Find the German adverb in \"hin\" or \"her\" that corresponds to that translation."

    f"<br><br> &nbsp; {ICON_WARN} Synonyms are available for this exercise. There may be more than one possible answer."
    f"<br><br> &nbsp; {ICON_WARN} Do not write more than one answer, or your answer will be flagged as false."

    "<h2>Example</h2>"
    "down, toward the speaker"
    f"<br><br> &nbsp; {ICON_CHECK} herunter"
    f"<br><br> &nbsp; {ICON_CHECK} runter"
    f"<br><br> &nbsp; {ICON_CHECK} herab"
    f"<br><br> &nbsp; {ICON_CROSS} herunter, herab"
    f"<br><br> &nbsp; {ICON_CROSS} hinunter"
)

guidance_adverbien_hin_her_sentences = (
    "For each question, you will be provided a German sentence and its English translation."
    "<br><br>The German sentence has an adverb in \"hin\" or \"her\" missing. Find the one that fits."

    f"<br><br> &nbsp; {ICON_WARN} Synonyms are available for this exercise. There may be more than one possible answer."
    f"<br><br> &nbsp; {ICON_WARN} Do not write more than one answer, or your answer will be flagged as false."

    "<h2>Example</h2>"
    "Er zog vorsichtig die alte Leiter _____, um sie zu reparieren."
    "<br><br><i>He carefully pulled the old ladder down to repair it.</i>"
    f"<br><br> &nbsp; {ICON_CHECK} herunter"
    f"<br><br> &nbsp; {ICON_CHECK} runter"
    f"<br><br> &nbsp; {ICON_CHECK} herab"
    f"<br><br> &nbsp; {ICON_CROSS} herunter, herab"
    f"<br><br> &nbsp; {ICON_CROSS} hinunter"
)

guidance_adverbien_einander_isolation = (
    "For each question, you will be provided the English translation of a German adverb in \"einander\"."
    "<br><br>Find the German adverb that corresponds to that translation."

    f"<br><br> &nbsp; {ICON_WARN} There is only one possible answer per question. Synonyms are not available for this exercise."
    " Read carefully the entire translation."
    
    "<h2>Example</h2>"
    "with each other, jointly"
    f"<br><br> &nbsp; {ICON_CHECK} miteinander"
    f"<br><br> &nbsp; {ICON_CROSS} nebeneinander"
)

guidance_adverbien_einander_sentences = (
    "For each question, you will be provided a German sentence and its English translation."
    "<br><br>The German sentence has an adverb in \"einander\" missing. Find the one that fits."

    f"<br><br> &nbsp; {ICON_WARN} There is only one possible answer per question. Synonyms are not available for this exercise."
    " Read carefully the entire translation."
    
    "<h2>Example</h2>"
    "Wir sollten offener _____ kommunizieren, um Missverständnisse zu vermeiden."
    "<br><br><i>We should communicate more openly with each other to avoid misunderstandings.</i>"
    f"<br><br> &nbsp; {ICON_CHECK} miteinander"
    f"<br><br> &nbsp; {ICON_CROSS} nebeneinander"
)

guidance_adverbien_multiple_choices_english_to_german = (
    "For each question, you will see the English translation of a German adjective and five German adverbs."
    "<br>Select the German adverb that correspond to the English translation."
    
    f"<br><br> &nbsp; {ICON_WARN} Synonyms are available for this exercise. There may be more than one possible answer."

    "<h2>Example</h2>"
    "now and then, occasionally"
    "<br>"
    "<br>bisweilen"
    "<br>ab und zu"
    "<br>wütend"
    "<br>unterwegs"
    "<br>zum Abschluss"
    f"<br><br> &nbsp; {ICON_CHECK} bisweilen"
    f"<br> &nbsp; {ICON_CHECK} ab und zu"
    f"<br> &nbsp; {ICON_CROSS} wütend"
    f"<br> &nbsp; {ICON_CROSS} unterwegs"
    f"<br> &nbsp; {ICON_CROSS} zum Abschluss"
)

guidance_adverbien_multiple_choices_german_to_english = (
    "For each question, you will see a German adverb and five potential English translations."
    "<br>Select the translation that correspond to the German adverb."

    f"<br><br> &nbsp; {ICON_WARN} There is only one possible answer per question. Synonyms are not available for this exercise."
    " Read carefully the entire translation."
    
    "<h2>Example</h2>"
    "wütend"
    "<br>"
    "<br>angrily, furiously"
    "<br>now and then, occasionally"
    "<br>on the way"
    "<br>to conclude, in conclusion"
    "<br>in any case, at least"
    f"<br><br> &nbsp; {ICON_CHECK} angrily, furiously"
)

guidance_adjektive_isolation = (
    "For each question, you will see the English translation of a German adjective."
    "<br>Find the German adjective that correspond to the translation."

    f"<br><br> &nbsp; {ICON_WARN} Synonyms are available for this exercise. There may be more than one possible answer."
    f"<br><br> &nbsp; {ICON_WARN} Do not write more than one answer, or your answer will be flagged as false."

    "<h2>Example</h2>"
    "cheap"
    f"<br><br> &nbsp; {ICON_CHECK} billig"
    f"<br><br> &nbsp; {ICON_CHECK} günstig"
    f"<br><br> &nbsp; {ICON_CROSS} billig, günstig"
)

guidance_adjektive_antonym = (
    "For each question, you will see a German adjective."
    "<br>Write its antonym in German."

    f"<br><br> &nbsp; {ICON_WARN} Synonyms are available for this exercise. There may be more than one possible answer."
    f"<br><br> &nbsp; {ICON_WARN} Do not write more than one answer, or your answer will be flagged as false."

    "<h2>Example</h2>"
    "teuer"
    f"<br><br> &nbsp; {ICON_CHECK} billig"
    f"<br><br> &nbsp; {ICON_CHECK} günstig"
    f"<br><br> &nbsp; {ICON_CROSS} billig, günstig"
)

guidance_adjektive_comparative = (
    "For each question, you will see a German adjective."
    "<br>Write its comparative form."

    "<h2>Example</h2>"
    "alt"
    f"<br><br> &nbsp; {ICON_CHECK} älter"
)

guidance_adjektive_superlative = (
    "For each question, you will see a German adjective."
    "<br>Write its superlative form."

    "<h2>Example</h2>"
    "alt"
    f"<br><br> &nbsp; {ICON_CHECK} am ältesten"
)

guidance_adjektive_comparison_words = (
    "For each question, you will be provided a German sentence and its English translation."
    "<br><br>The German sentence has a comparison word missing. Find the one that fits."

    "<h2>Example</h2>"
    "Peter ist größer _____ sein Bruder."
    "<br><br><i>Peter is taller than his brother.</i>"
    f"<br><br> &nbsp; {ICON_CHECK} als"
)

guidance_adjektive_multiple_choices_english_to_german = (
    "For each question, you will see the English translation of a German adjective and five German adjectives."
    "<br>Select the German adjective that correspond to the English translation."

    "<h2>Example</h2>"
    "own"
    "<br><br>eigen"
    "<br>international"
    "<br>europäisch"
    "<br>tot"
    "<br>einzeln"
    f"<br><br> &nbsp; {ICON_CHECK} eigen"
)

guidance_adjektive_multiple_choices_german_to_english = (
    "For each question, you will see a German adjective and five potential English translations."
    "<br>Select the translation that correspond to the German adjective."

    "<h2>Example</h2>"
    "eigen"
    "<br><br>own"
    "<br>international"
    "<br>European"
    "<br>dead"
    "<br>single, only"
    f"<br><br> &nbsp; {ICON_CHECK} own"
)

guidance_adjektivdeklinationen_isolation = (
    "For each question, you will be provided a German phrase with a case and an adjective."
    "<br><br>Complete the phrase with the declined adjective, taking into account the article,"
    " the gender of the noun and the grammatical case."

    "<h2>Example</h2>"
    "ein _____ Vater \u25CF Nominativ \u25CF nett"
    f"<br><br> &nbsp; {ICON_CHECK} netter"
)

guidance_adjektivdeklinationen_sentences = (
    "For each question, you will be provided an incomplete German sentence and an adjective."
    "<br><br>Complete the sentence with the adjective properly declined, taking into account the article,"
    " the gender of the noun and the grammatical case."

    "<h2>Example</h2>"
    "Die _____ Kinder stellen viele Fragen. \u25CF klug"
    f"<br><br> &nbsp; {ICON_CHECK} klugen"
)

guidance_adjektivdeklinationen_comparative_isolation = (
    "For each question, you will be provided a German phrase with a case and an adjective."
    "<br><br>Complete the phrase with the declined <b>comparative</b> adjective, taking into account the article,"
    " the gender of the noun and the grammatical case."

    "<h2>Example</h2>"
    "ein _____ Vater \u25CF Nominativ \u25CF nett"
    f"<br><br> &nbsp; {ICON_CHECK} netterer"
)

guidance_adjektivdeklinationen_comparative_sentences = (
    "For each question, you will be provided an incomplete German sentence and an adjective."
    "<br><br>Complete the sentence with the <b>comparative</b> adjective properly declined, taking into account the article,"
    " the gender of the noun and the grammatical case."

    "<h2>Example</h2>"
    "Der _____ Hund läuft im Garten. \u25CF groß"
    f"<br><br> &nbsp; {ICON_CHECK} größere"
)

guidance_adjektivdeklinationen_superlative_isolation = (
    "For each question, you will be provided a German phrase with a case and an adjective."
    "<br><br>Complete the phrase with the declined <b>superlative</b> adjective, taking into account the article,"
    " the gender of the noun and the grammatical case."

    "<h2>Example</h2>"
    "der _____ Vater \u25CF Nominativ \u25CF nett"
    f"<br><br> &nbsp; {ICON_CHECK} netteste"
)

guidance_adjektivdeklinationen_superlative_sentences = (
    "For each question, you will be provided an incomplete German sentence and an adjective."
    "<br><br>Complete the sentence with the <b>superlative</b> adjective properly declined, taking into account the article,"
    " the gender of the noun and the grammatical case."

    "<h2>Example</h2>"
    "Die _____ Blume steht auf dem Tisch. \u25CF schön"
    f"<br><br> &nbsp; {ICON_CHECK} schönste"
)

guidance_verben_translation = (
    "For each question, you will see the English translation of a German verb."
    "<br>Find the German verb that correspond to the entire translation."

    f"<br><br> &nbsp; {ICON_WARN} There is only one possible answer per question. Synonyms are not available for this exercise."
    f" Read carefully the entire translation."
    f"<br><br> &nbsp; {ICON_WARN} Do not write any reflexive pronoun, even if the verb is usually reflexive."

    "<h2>Example</h2>"
    "to make glad, to be glad (refl.), to look forward (refl.)"
    f"<br><br> &nbsp; {ICON_CHECK} freuen"
    f"<br><br> &nbsp; {ICON_CROSS} sich freuen"
)

guidance_verben_multiple_choices_english_to_german = (
    "For each question, you will see the English translation of a German verb and five German verbs."
    "<br>Select the German verb that correspond to the entire translation."

    f"<br><br> &nbsp; {ICON_WARN} There is only one possible answer per question. Synonyms are not available for this exercise."
    f" Read carefully the entire translation."

    "<h2>Example</h2>"
    "to replace, to substitute, to compensate for"
    "<br><br>ersetzen"
    "<br>leiden"
    "<br>diskutieren"
    "<br>rufen"
    "<br>vorschlagen"
    f"<br><br> &nbsp; {ICON_CHECK} ersetzen"
)

guidance_verben_multiple_choices_german_to_english = (
    "For each question, you will see a German verb and five potential English translations."
    "<br>Select the translation that correspond to the German verb."

    f"<br><br> &nbsp; {ICON_WARN} There is only one possible answer per question. Synonyms are not available for this exercise."
    f" Read carefully the entire translations."

    "<h2>Example</h2>"
    "ersetzen"
    "<br><br>to replace, to substitute, to compensate for"
    "<br>to suffer, to endure, to bear"
    "<br>to discuss, to debate"
    "<br>to call, to shout, to summon"
    "<br>to suggest, to propose"
    f"<br><br> &nbsp; {ICON_CHECK} to replace, to substitute, to compensate for"
)

guidance_trennbare_verben_root = (
    "For each question, you will be provided the English translation of a German (un)trennbare verb as well as its root."
    "<br><br>Find the German verb that correspond to the translation and root."
    
    f"<br><br> &nbsp; {ICON_WARN} There is only one possible answer per question. Synonyms are not available for this exercise."
    " Read carefully the entire translation."
    f"<br><br> &nbsp; {ICON_WARN} Do not write any reflexive pronoun, even if the verb is usually reflexive."

    "<h2>Example</h2>"
    "to pull, to drag, to move → ziehen"
    "<br><br>to get dressed, to put on, to dress someone, to attract, to pull → _____"
    f"<br><br> &nbsp; {ICON_CHECK} anziehen"
)

guidance_trennbare_verben_prefix = (
    "For each question, you will be provided the English translation of a German (un)trennbare verb as well as its prefix."
    "<br><br>Find the German verb that correspond to the translation and prefix."

    f"<br><br> &nbsp; {ICON_WARN} There is only one possible answer per question. Synonyms are not available for this exercise."
    " Read carefully the entire translation."
    f"<br><br> &nbsp; {ICON_WARN} Do not write any reflexive pronoun, even if the verb is usually reflexive."

    "<h2>Example</h2>"
    "to get dressed, to put on, to dress someone, to attract, to pull \u25CF an"
    f"<br><br> &nbsp; {ICON_CHECK} anziehen"
)

guidance_trennbare_verben_no_help = (
    "For each question, you will be provided the English translation of a German (un)trennbare verb."
    "<br><br>Find the German verb that correspond to the entire translation."

    f"<br><br> &nbsp; {ICON_WARN} There is only one possible answer per question. Synonyms are not available for this exercise."
    " Read carefully the entire translation."
    f"<br><br> &nbsp; {ICON_WARN} Do not write any reflexive pronoun, even if the verb is usually reflexive."

    "<h2>Example</h2>"
    "to get dressed, to put on, to dress someone, to attract, to pull"
    f"<br><br> &nbsp; {ICON_CHECK} anziehen"
)

guidance_nomen_verben_verbindungen_nomen_isolation = (
    "For each question, you will be provided an incomplete German Noun-Verb Combination and its English translation."
    "<br><br>Find the German noun that completes the combination."

    f"<br><br> &nbsp; {ICON_WARN} There may be more than one possible answer."
    f"<br><br> &nbsp; {ICON_WARN} Do not write more than one answer, or your answer will be flagged as false."
    f"<br><br> &nbsp; {ICON_WARN} The answer may require an article and/or a preposition."
    
    f"<br><br>➡️ If you need help on the gender of the noun, click on the m/f/n/pl button."

    "<h2>Examples</h2>"
    "_____ haben"
    "<br><br><i>to have an opinion</i>"
    f"<br><br> &nbsp; {ICON_CHECK} eine Meinung"
    f"<br><br> &nbsp; {ICON_CHECK} eine Ansicht"
    f"<br><br> &nbsp; {ICON_CROSS} eine Meinung, eine Ansicht"
    f"<br><br> &nbsp; {ICON_CROSS} Meinung"
    f"<br><br> &nbsp; {ICON_CROSS} ein Meinung"

    "<br><br>_____ nehmen"
    "<br><br><i>to accept, to take the risk</i>"
    f"<br><br> &nbsp; {ICON_CHECK} in Kauf"
    f"<br><br> &nbsp; {ICON_CROSS} Kauf"
)

guidance_nomen_verben_verbindungen_verben_isolation = (
    "For each question, you will be provided an incomplete German Noun-Verb Combination and its English translation."
    "<br><br>Find the German verb that completes the combination."

    f"<br><br> &nbsp; {ICON_WARN} There may be more than one possible answer."
    f"<br><br> &nbsp; {ICON_WARN} Do not write more than one answer, or your answer will be flagged as false."

    "<h2>Example</h2>"
    "eine Meinung _____"
    "<br><br><i>to have an opinion, to think</i>"
    f"<br><br> &nbsp; {ICON_CHECK} haben"
    f"<br><br> &nbsp; {ICON_CHECK} vertreten"
    f"<br><br> &nbsp; {ICON_CROSS} haben, vertreten"
)

guidance_nomen_verben_verbindungen_nomen_sentences = (
    "For each question, you will be provided an incomplete German sentence and its English translation."
    "<br><br>Find the German noun that completes the sentence."

    f"<br><br> &nbsp; {ICON_WARN} There may be more than one possible answer."
    f"<br><br> &nbsp; {ICON_WARN} Do not write more than one answer, or your answer will be flagged as false."
    f"<br><br> &nbsp; {ICON_WARN} The answer may require a preposition."

    "<h2>Examples</h2>"
    "Ich habe eine andere _____ als du."
    "<br><br><i>I have a different opinion than you.</i>"
    f"<br><br> &nbsp; {ICON_CHECK} Meinung"
    f"<br><br> &nbsp; {ICON_CHECK} Ansicht"
    f"<br><br> &nbsp; {ICON_CROSS} Meinung, Ansicht"

    "<br><br>Ich will dieses Projekt unbedingt _____ bringen, bevor ich in den Urlaub fahre."
    "<br><br><i>I absolutely want to finish this project before I go on vacation.</i>"
    f"<br><br> &nbsp; {ICON_CHECK} zu Ende"
    f"<br><br> &nbsp; {ICON_CHECK} zum Abschluss"
    f"<br><br> &nbsp; {ICON_CROSS} Ende"
    f"<br><br> &nbsp; {ICON_CROSS} Abschluss"
    f"<br><br> &nbsp; {ICON_CROSS} zu Ende, zum Abschluss"
)

guidance_nomen_verben_verbindungen_verben_sentences = (
    "For each question, you will be provided an incomplete German sentence and its English translation."
    "<br><br>Find the German verb that completes the sentence."

    f"<br><br> &nbsp; {ICON_WARN} There may be more than one possible answer."
    f"<br><br> &nbsp; {ICON_WARN} Do not write more than one answer, or your answer will be flagged as false."
    f"<br><br> &nbsp; {ICON_WARN} The verb must be conjugated in the proper tense and the proper grammatical person."

    "<h2>Example</h2>"
    "Sie _____ den Vorschlag, gemeinsam zu reisen."
    "<br><br><i>She made the suggestion to travel together.</i>"
    f"<br><br> &nbsp; {ICON_CHECK} machte"
    f"<br><br> &nbsp; {ICON_CHECK} unterbreitete"
    f"<br><br> &nbsp; {ICON_CROSS} machte, unterbreitete"
    f"<br><br> &nbsp; {ICON_CROSS} macht"
    f"<br><br> &nbsp; {ICON_CROSS} machen"
)

guidance_nomen_verben_wortstaemme_verben = (
    "For each question, you will be provided an incomplete German Noun-Verb Pair and its English translation."
    "<br><br>Find the German verb that completes the pair."

    f"<br><br> &nbsp; {ICON_WARN} There is only one possible answer per question. Synonyms are not available for this exercise."
    " Read carefully the entire translation."
    f"<br><br> &nbsp; {ICON_WARN} Do not write any reflexive pronoun, even if the verb is usually reflexive."

    "<h2>Example</h2>"
    "the language, the speech → die Sprache"
    "<br><br>to speak → _____"
    f"<br><br> &nbsp; {ICON_CHECK} sprechen"
)

guidance_nomen_verben_wortstaemme_nomen = (
    "For each question, you will be provided an incomplete German Noun-Verb Pair and its English translation."
    "<br><br>Find the German noun that completes the pair."

    f"<br><br> &nbsp; {ICON_WARN} There may be more than one possible answer."
    f"<br><br> &nbsp; {ICON_WARN} Do not write more than one answer, or your answer will be flagged as false."

    f"<br><br>➡️ If you need help on the gender of the noun, click on the m/f/n/pl button."

    "<h2>Example</h2>"
    "to speak → sprechen"
    "<br><br>the language, the speech → _____"
    f"<br><br> &nbsp; {ICON_CHECK} die Sprache"
)

guidance_zahlen_number = (
    "For each question, you will be provided a Number."
    "<br><br>Write the German spelled form of that Number."
    
    "<h2>Examples</h2>"
    "2"
    f"<br><br> &nbsp; {ICON_CHECK} zwei"
    
    "<br><br>1,23"
    f"<br><br> &nbsp; {ICON_CHECK} eins Komma zwei drei"
    f"<br><br> &nbsp; {ICON_CROSS} eins Punkt zwei drei"
)

guidance_zahlen_time_spelled = (
    "For each question, you will be provided a time of the day."
    "<br><br>Write the German spelled form of that time."

    "<h2>Examples</h2>"
    "8:00"
    f"<br><br> &nbsp; {ICON_CHECK} acht Uhr"
    f"<br><br> &nbsp; {ICON_CHECK} acht Uhr null"

    "<br><br>17:50"
    f"<br><br> &nbsp; {ICON_CHECK} siebzehn Uhr fünfzig"
    f"<br><br> &nbsp; {ICON_CHECK} zehn vor sechs"
)

guidance_zahlen_time_digital = (
    "For each question, you will be provided a time of the day."
    "<br><br>Write the digital version of that time."

    "<h2>Example</h2>"
    "Viertel vor neun"
    f"<br><br> &nbsp; {ICON_CHECK} 8:45"
    f"<br><br> &nbsp; {ICON_CHECK} 08:45"
)

guidance_zahlen_ordinal_isolation = (
    "For each question, you will be provided an English ordinal number."
    "<br><br>Translate this ordinal number in German."
    
    f"<br><br> &nbsp; {ICON_WARN} The ordinal number should be declined in the <i>-e</i> form."

    "<h2>Example</h2>"
    "first"
    f"<br><br> &nbsp; {ICON_CHECK} erste"
    f"<br><br> &nbsp; {ICON_CROSS} ersten"
)

guidance_zahlen_ordinal_sentence = (
    "For each question, you will be provided a German sentence and its English translation."
    "<br><br>The German sentence has an ordinal number missing. Find the one that fits."
    
    f"<br><br> &nbsp; {ICON_WARN} The ordinal number should be declined based on the context."

    "<h2>Example</h2>"
    "Sie wohnt im _____ Stock."
    "<br><br><i>She lives on the second floor.</i>"
    f"<br><br> &nbsp; {ICON_CHECK} zweiten"
    f"<br><br> &nbsp; {ICON_CROSS} zweite"
)

guidance_zahlen_adverb_isolation = (
    "For each question, you will be provided an English adverb."
    "<br><br>Translate this adverb in German."

    "<h2>Example</h2>"
    "thirdly"
    f"<br><br> &nbsp; {ICON_CHECK} drittens"
)

guidance_zahlen_adverb_sentence = (
    "For each question, you will be provided a German sentence and its English translation."
    "<br><br>The German sentence has an adverb missing. Find the one that fits."

    "<h2>Example</h2>"
    "_____ fehlt uns im Moment das nötige Budget."
    "<br><br><i>Thirdly, we currently lack the necessary budget.</i>"
    f"<br><br> &nbsp; {ICON_CHECK} Drittens"
)

guidance_zahlen_fraction_isolation = (
    "For each question, you will be provided an English fraction."
    "<br><br>Translate this fraction in German."

    "<h2>Example</h2>"
    "a third"
    f"<br><br> &nbsp; {ICON_CHECK} ein Drittel"
)

guidance_zahlen_fraction_sentence = (
    "For each question, you will be provided a German sentence and its English translation."
    "<br><br>The German sentence has a fraction missing. Find the one that fits."

    "<h2>Example</h2>"
    "_____ der Teilnehmenden hat den Kurs vorzeitig beendet."
    "<br><br><i>Half of the participants dropped out of the course early.</i>"
    f"<br><br> &nbsp; {ICON_CHECK} Die Hälfte"
)

guidance_zahlen_genitive_isolation = (
    "For each question, you will be provided a number."
    "<br><br>Provide the genitive form of this number."

    "<h2>Example</h2>"
    "3"
    f"<br><br> &nbsp; {ICON_CHECK} dreier"
)

guidance_zahlen_genitive_sentence = (
    "For each question, you will be provided a German sentence and its English translation."
    "<br><br>The German sentence has the genitive form of a number missing. Find the one that fits."

    "<h2>Examples</h2>"
    "Der Ausschuss einigte sich nach intensiver Debatte auf einen Kompromiss _____ Parteien."
    "<br><br><i>After intense debate, the committee agreed on a compromise involving seven parties.</i>"
    f"<br><br> &nbsp; {ICON_CHECK} siebener"
    f"<br><br> &nbsp; {ICON_CHECK} von sieben"

    "<br><br>Die Lösung ergibt sich aus der Kombination _____ voneinander abhängiger Faktoren."
    "<br><br><i>The solution emerges from the combination of four interdependent factors.</i>"
    f"<br><br> &nbsp; {ICON_CHECK} vierer"
    f"<br><br> &nbsp; {ICON_CROSS} von vier (adjective declension doesn't correspond)"
)

guidance_zahlen_multiplier_isolation = (
    "For each question, you will be provided an English multiplier."
    "<br><br>Translate this multiplier in German."

    "<h2>Example</h2>"
    "fourfold"
    f"<br><br> &nbsp; {ICON_CHECK} vierfach"
)

guidance_zahlen_multiplier_sentence = (
    "For each question, you will be provided a German sentence and its English translation."
    "<br><br>The German sentence has a multiplier missing. Find the one that fits."

    f"<br><br> &nbsp; {ICON_WARN} The multiplier should be declined based on the context."

    "<h2>Example</h2>"
    "Das Risiko ist _____: finanziell und reputationsbezogen."
    "<br><br><i>The risk is twofold: financial and reputational.</i>"
    f"<br><br> &nbsp; {ICON_CHECK} zweifach"
)

GUIDANCE_EXERCISE_EN = {

    praepositionen_grammatik: {
        1: guidance_praepositionen_grammatik_sentences,
        2: guidance_praepositionen_grammatik_sentences,
        3: guidance_praepositionen_grammatik_sentences,
        4: guidance_praepositionen_grammatik_sentences,

        5: guidance_praepositionen_grammatik_sentences,
        6: guidance_praepositionen_grammatik_sentences,
        7: guidance_praepositionen_grammatik_sentences,
        8: guidance_praepositionen_grammatik_sentences,

        9: guidance_praepositionen_grammatik_sentences,
        10: guidance_praepositionen_grammatik_sentences,
        11: guidance_praepositionen_grammatik_isolation,
        12: guidance_praepositionen_grammatik_sentences,

        13: guidance_praepositionen_grammatik_sentences,
        14: guidance_praepositionen_grammatik_sentences,
        15: guidance_praepositionen_grammatik_isolation,
        16: guidance_praepositionen_grammatik_sentences,

        17: guidance_praepositionen_grammatik_sentences,
        18: guidance_praepositionen_grammatik_sentences,
        19: guidance_praepositionen_grammatik_isolation,
        20: guidance_praepositionen_grammatik_sentences,
        21: guidance_praepositionen_grammatik_isolation,
        22: guidance_praepositionen_grammatik_sentences,
        23: guidance_praepositionen_grammatik_isolation,
        24: guidance_praepositionen_grammatik_sentences,
        25: guidance_praepositionen_grammatik_isolation,
        26: guidance_praepositionen_grammatik_sentences,
        27: guidance_praepositionen_grammatik_synonyms,
        28: guidance_praepositionen_grammatik_antonym,

        29: guidance_praepositionen_grammatik_sentences,
    },

    praepositionen_verben: {
        1: guidance_praepositionen_verben_isolation,
        2: guidance_praepositionen_verben_sentences,
        3: guidance_praepositionen_verben_isolation,
        4: guidance_praepositionen_verben_sentences,

        5: guidance_praepositionen_verben_isolation,
        6: guidance_praepositionen_verben_sentences,
        7: guidance_praepositionen_verben_isolation,
        8: guidance_praepositionen_verben_sentences,
        9: guidance_praepositionen_verben_dawort,
        10: guidance_praepositionen_verben_wowort,

        11: guidance_praepositionen_verben_isolation,
        12: guidance_praepositionen_verben_sentences,
        13: guidance_praepositionen_verben_isolation,
        14: guidance_praepositionen_verben_sentences,
        15: guidance_praepositionen_verben_isolation,
        16: guidance_praepositionen_verben_sentences,
        17: guidance_praepositionen_verben_isolation,
        18: guidance_praepositionen_verben_sentences,

        19: guidance_praepositionen_verben_isolation,
        20: guidance_praepositionen_verben_sentences,
        21: guidance_praepositionen_verben_isolation,
        22: guidance_praepositionen_verben_sentences,
        23: guidance_praepositionen_verben_isolation,
        24: guidance_praepositionen_verben_sentences,
        25: guidance_praepositionen_verben_isolation,
        26: guidance_praepositionen_verben_sentences,

        27: guidance_praepositionen_verben_isolation,
        28: guidance_praepositionen_verben_sentences,
        29: guidance_praepositionen_verben_isolation,
        30: guidance_praepositionen_verben_sentences,
        31: guidance_praepositionen_verben_isolation,
        32: guidance_praepositionen_verben_sentences,
        33: guidance_praepositionen_verben_isolation,
        34: guidance_praepositionen_verben_sentences,

        35: guidance_praepositionen_verben_isolation,
        36: guidance_praepositionen_verben_sentences,
        37: guidance_praepositionen_verben_isolation,
        38: guidance_praepositionen_verben_sentences,
        39: guidance_praepositionen_verben_isolation,
        40: guidance_praepositionen_verben_sentences,
        41: guidance_praepositionen_verben_isolation,
        42: guidance_praepositionen_verben_sentences,
    },

    praepositionen_adjektive: {
        1: guidance_praepositionen_adjektive_isolation,
        2: guidance_praepositionen_adjektive_sentences,
        3: guidance_praepositionen_adjektive_isolation,
        4: guidance_praepositionen_adjektive_sentences,

        5: guidance_praepositionen_adjektive_isolation,
        6: guidance_praepositionen_adjektive_sentences,
        7: guidance_praepositionen_adjektive_isolation,
        8: guidance_praepositionen_adjektive_sentences,
        9: guidance_praepositionen_adjektive_isolation,
        10: guidance_praepositionen_adjektive_sentences,

        11: guidance_praepositionen_adjektive_isolation,
        12: guidance_praepositionen_adjektive_sentences,
        13: guidance_praepositionen_adjektive_isolation,
        14: guidance_praepositionen_adjektive_sentences,
        15: guidance_praepositionen_adjektive_isolation,
        16: guidance_praepositionen_adjektive_sentences,
        17: guidance_praepositionen_adjektive_isolation,
        18: guidance_praepositionen_adjektive_sentences,
    },

    praepositionen_nomen: {
        1: guidance_praepositionen_nomen_isolation,
        2: guidance_praepositionen_nomen_sentences,
        3: guidance_praepositionen_nomen_isolation,
        4: guidance_praepositionen_nomen_sentences,
        5: guidance_praepositionen_nomen_isolation,
        6: guidance_praepositionen_nomen_sentences,

        7: guidance_praepositionen_nomen_isolation,
        8: guidance_praepositionen_nomen_sentences,
        9: guidance_praepositionen_nomen_isolation,
        10: guidance_praepositionen_nomen_sentences,
        11: guidance_praepositionen_nomen_isolation,
        12: guidance_praepositionen_nomen_sentences,
        13: guidance_praepositionen_nomen_isolation,
        14: guidance_praepositionen_nomen_sentences,
        15: guidance_praepositionen_nomen_isolation,
        16: guidance_praepositionen_nomen_sentences,

        17: guidance_praepositionen_nomen_isolation,
        18: guidance_praepositionen_nomen_sentences,
        19: guidance_praepositionen_nomen_isolation,
        20: guidance_praepositionen_nomen_sentences,
        21: guidance_praepositionen_nomen_isolation,
        22: guidance_praepositionen_nomen_sentences,
        23: guidance_praepositionen_nomen_isolation,
        24: guidance_praepositionen_nomen_sentences,
        25: guidance_praepositionen_nomen_isolation,
        26: guidance_praepositionen_nomen_sentences,
    },

    artikel: {
        1: guidance_artikel_isolation,
        2: guidance_artikel_sentences,
        3: guidance_artikel_sentences,
        4: guidance_artikel_sentences,
        5: guidance_artikel_sentences,
        6: guidance_artikel_sentences,
        7: guidance_artikel_sentences,
        8: guidance_artikel_sentences,
        9: guidance_artikel_sentences,
        10: guidance_artikel_sentences,
        11: guidance_artikel_isolation,
        12: guidance_artikel_sentences,
        13: guidance_artikel_sentences,
        14: guidance_artikel_sentences,
        15: guidance_artikel_sentences,
        16: guidance_artikel_sentences,
        17: guidance_artikel_sentences,
        18: guidance_artikel_sentences,
        19: guidance_artikel_sentences,
        20: guidance_artikel_isolation,
        21: guidance_artikel_sentences,
        22: guidance_artikel_isolation,
        23: guidance_artikel_sentences,
        24: guidance_artikel_isolation,
        25: guidance_artikel_sentences,

        26: guidance_artikel_isolation,
        27: guidance_artikel_sentences,
        28: guidance_artikel_isolation,
        29: guidance_artikel_sentences,
        30: guidance_artikel_isolation,
        31: guidance_artikel_sentences,

        32: guidance_artikel_isolation,
        33: guidance_artikel_sentences,
        34: guidance_artikel_isolation,
        35: guidance_artikel_sentences,
        36: guidance_artikel_isolation,
        37: guidance_artikel_sentences,

        38: guidance_artikel_isolation,
        39: guidance_artikel_sentences,

        40: guidance_artikel_isolation,
        41: guidance_artikel_sentences,
        42: guidance_artikel_sentences,
        43: guidance_artikel_sentences,
    },

    pronomen: {
        1: guidance_pronomen_isolation,
        2: guidance_pronomen_sentences,
        3: guidance_pronomen_isolation,
        4: guidance_pronomen_sentences,
        5: guidance_pronomen_isolation,
        6: guidance_pronomen_sentences,
        7: guidance_pronomen_sentences,
        8: guidance_pronomen_sentences,
        9: guidance_pronomen_replacing,
        10: guidance_pronomen_replacing,

        11: guidance_pronomen_isolation,
        12: guidance_pronomen_sentences,
        13: guidance_pronomen_sentences,
        14: guidance_pronomen_sentences,

        15: guidance_pronomen_isolation,
        16: guidance_pronomen_sentences,
        17: guidance_pronomen_isolation,
        18: guidance_pronomen_sentences,
        19: guidance_pronomen_isolation,
        20: guidance_pronomen_sentences,
        21: guidance_pronomen_sentences,
        22: guidance_pronomen_sentences,

        23: guidance_pronomen_sentences,
        24: guidance_pronomen_sentences,
        25: guidance_pronomen_sentences,
        26: guidance_pronomen_isolation,
        27: guidance_pronomen_sentences,
        28: guidance_pronomen_isolation,
        29: guidance_pronomen_sentences,

        30: guidance_pronomen_sentences,
    },

    konnektoren: {
        1: guidance_konnektoren_isolation,
        2: guidance_konnektoren_sentences,

        3: guidance_konnektoren_isolation,
        4: guidance_konnektoren_sentences,

        5: guidance_konnektoren_isolation,
        6: guidance_konnektoren_sentences,
        7: guidance_konnektoren_isolation,
        8: guidance_konnektoren_sentences,
        9: guidance_konnektoren_isolation,
        10: guidance_konnektoren_sentences,
        11: guidance_konnektoren_synonyms,

        12: guidance_konnektoren_isolation,
        13: guidance_konnektoren_sentences,
        14: guidance_konnektoren_isolation,
        15: guidance_konnektoren_sentences,
        16: guidance_konnektoren_isolation,
        17: guidance_konnektoren_sentences,
        18: guidance_konnektoren_synonyms,

        19: guidance_konnektoren_isolation,
        20: guidance_konnektoren_sentences,
        21: guidance_konnektoren_isolation,
        22: guidance_konnektoren_sentences,
        23: guidance_konnektoren_isolation,
        24: guidance_konnektoren_sentences,
        25: guidance_konnektoren_isolation,
        26: guidance_konnektoren_sentences,
        27: guidance_konnektoren_isolation,
        28: guidance_konnektoren_sentences,
        29: guidance_konnektoren_synonyms,
        30: guidance_konnektoren_synonyms,
        31: guidance_konnektoren_synonyms,
        32: guidance_konnektoren_synonyms,
    },

    fragen: {
        1: guidance_fragen_isolation,
        2: guidance_fragen_sentences,

        3: guidance_fragen_isolation,
        4: guidance_fragen_sentences,

        5: guidance_fragen_isolation,
        6: guidance_fragen_sentences,

        7: guidance_fragen_isolation,
        8: guidance_fragen_sentences,
        9: guidance_fragen_isolation,
        10: guidance_fragen_sentences,

        11: guidance_fragen_isolation,
        12: guidance_fragen_sentences,

        13: guidance_fragen_isolation,
        14: guidance_fragen_sentences,
    },

    adverbien: {
        1: guidance_adverbien_isolation,
        2: guidance_adverbien_sentences,
        3: guidance_adverbien_isolation,
        4: guidance_adverbien_sentences,

        5: guidance_adverbien_isolation,
        6: guidance_adverbien_sentences,
        7: guidance_adverbien_isolation,
        8: guidance_adverbien_sentences,
        9: guidance_adverbien_synonyms,
        10: guidance_adverbien_antonym,

        11: guidance_adverbien_isolation,
        12: guidance_adverbien_sentences,
        13: guidance_adverbien_isolation,
        14: guidance_adverbien_sentences,
        15: guidance_adverbien_isolation,
        16: guidance_adverbien_sentences,
        17: guidance_adverbien_isolation,
        18: guidance_adverbien_sentences,
        19: guidance_adverbien_synonyms,
        20: guidance_adverbien_antonym,

        21: guidance_adverbien_isolation,
        22: guidance_adverbien_sentences,
        23: guidance_adverbien_isolation,
        24: guidance_adverbien_sentences,
        25: guidance_adverbien_isolation,
        26: guidance_adverbien_sentences,
        27: guidance_adverbien_isolation,
        28: guidance_adverbien_sentences,
        29: guidance_adverbien_synonyms,
        30: guidance_adverbien_antonym,

        31: guidance_adverbien_isolation,
        32: guidance_adverbien_sentences,
        33: guidance_adverbien_isolation,
        34: guidance_adverbien_sentences,
        35: guidance_adverbien_isolation,
        36: guidance_adverbien_sentences,
        37: guidance_adverbien_isolation,
        38: guidance_adverbien_sentences,
        39: guidance_adverbien_synonyms,
        40: guidance_adverbien_antonym,

        41: guidance_adverbien_isolation,
        42: guidance_adverbien_sentences,
        43: guidance_adverbien_isolation,
        44: guidance_adverbien_sentences,
        45: guidance_adverbien_isolation,
        46: guidance_adverbien_sentences,
        47: guidance_adverbien_isolation,
        48: guidance_adverbien_sentences,
        49: guidance_adverbien_synonyms,
        50: guidance_adverbien_antonym,

        51: guidance_adverbien_isolation,
        52: guidance_adverbien_sentences,
        53: guidance_adverbien_isolation,
        54: guidance_adverbien_sentences,
        55: guidance_adverbien_isolation,
        56: guidance_adverbien_sentences,
        57: guidance_adverbien_isolation,
        58: guidance_adverbien_sentences,
        59: guidance_adverbien_synonyms,
        60: guidance_adverbien_antonym,

        61: guidance_adverbien_isolation,
        62: guidance_adverbien_sentences,
        63: guidance_adverbien_isolation,
        64: guidance_adverbien_sentences,
        65: guidance_adverbien_isolation,
        66: guidance_adverbien_sentences,
        67: guidance_adverbien_isolation,
        68: guidance_adverbien_sentences,
        69: guidance_adverbien_synonyms,
        70: guidance_adverbien_antonym,

        71: guidance_adverbien_isolation,
        72: guidance_adverbien_sentences,
        73: guidance_adverbien_isolation,
        74: guidance_adverbien_sentences,
        75: guidance_adverbien_isolation,
        76: guidance_adverbien_sentences,
        77: guidance_adverbien_isolation,
        78: guidance_adverbien_sentences,
        79: guidance_adverbien_synonyms,
        80: guidance_adverbien_antonym,
    },

    adjektive: {
        1: guidance_adjektive_isolation,
        2: guidance_adjektive_isolation,
        3: guidance_adjektive_isolation,
        4: guidance_adjektive_antonym,
        5: guidance_adjektive_antonym,
        6: guidance_adjektive_comparative,
        7: guidance_adjektive_comparative,
        8: guidance_adjektive_comparative,
        9: guidance_adjektive_superlative,
        10: guidance_adjektive_superlative,
        11: guidance_adjektive_superlative,

        12: guidance_adjektive_isolation,
        13: guidance_adjektive_isolation,
        14: guidance_adjektive_isolation,
        15: guidance_adjektive_antonym,
        16: guidance_adjektive_antonym,
        17: guidance_adjektive_comparative,
        18: guidance_adjektive_comparative,
        19: guidance_adjektive_comparative,
        20: guidance_adjektive_superlative,
        21: guidance_adjektive_superlative,
        22: guidance_adjektive_superlative,

        23: guidance_adjektive_multiple_choices_english_to_german,
        24: guidance_adjektive_multiple_choices_english_to_german,
        25: guidance_adjektive_multiple_choices_english_to_german,
        26: guidance_adjektive_multiple_choices_german_to_english,
        27: guidance_adjektive_multiple_choices_german_to_english,
        28: guidance_adjektive_multiple_choices_german_to_english,

        29: guidance_adjektive_multiple_choices_german_to_english,
        30: guidance_adjektive_multiple_choices_german_to_english,
        31: guidance_adjektive_multiple_choices_german_to_english,
        32: guidance_adjektive_multiple_choices_english_to_german,
        33: guidance_adjektive_multiple_choices_english_to_german,
        34: guidance_adjektive_multiple_choices_english_to_german,
    },

    adjektivdeklinationen: {
        1: guidance_adjektivdeklinationen_isolation,
        2: guidance_adjektivdeklinationen_sentences,
        3: guidance_adjektivdeklinationen_isolation,
        4: guidance_adjektivdeklinationen_sentences,
        5: guidance_adjektivdeklinationen_isolation,
        6: guidance_adjektivdeklinationen_sentences,
        7: guidance_adjektivdeklinationen_isolation,
        8: guidance_adjektivdeklinationen_sentences,
        9: guidance_adjektivdeklinationen_isolation,
        10: guidance_adjektivdeklinationen_sentences,
        11: guidance_adjektivdeklinationen_sentences,
        12: guidance_adjektivdeklinationen_sentences,
        13: guidance_adjektivdeklinationen_isolation,
        14: guidance_adjektivdeklinationen_sentences,

        15: guidance_adjektivdeklinationen_isolation,
        16: guidance_adjektivdeklinationen_sentences,
        17: guidance_adjektivdeklinationen_isolation,
        18: guidance_adjektivdeklinationen_sentences,
        19: guidance_adjektivdeklinationen_isolation,
        20: guidance_adjektivdeklinationen_sentences,
        21: guidance_adjektivdeklinationen_comparative_isolation,
        22: guidance_adjektivdeklinationen_comparative_sentences,
        23: guidance_adjektivdeklinationen_superlative_isolation,
        24: guidance_adjektivdeklinationen_superlative_sentences,

        25: guidance_adjektivdeklinationen_isolation,
        26: guidance_adjektivdeklinationen_sentences,

        27: guidance_adjektivdeklinationen_isolation,
        28: guidance_adjektivdeklinationen_sentences,
        29: guidance_adjektivdeklinationen_isolation,
        30: guidance_adjektivdeklinationen_sentences,
    },

    verben: {
        1: guidance_verben_translation,
        2: guidance_verben_translation,
        3: guidance_verben_translation,
        4: guidance_verben_translation,
        5: guidance_verben_translation,

        6: guidance_verben_translation,
        7: guidance_verben_translation,
        8: guidance_verben_translation,
        9: guidance_verben_translation,
        10: guidance_verben_translation,

        11: guidance_verben_multiple_choices_english_to_german,
        12: guidance_verben_multiple_choices_english_to_german,
        13: guidance_verben_multiple_choices_english_to_german,
        14: guidance_verben_multiple_choices_english_to_german,
        15: guidance_verben_multiple_choices_english_to_german,
        16: guidance_verben_multiple_choices_german_to_english,
        17: guidance_verben_multiple_choices_german_to_english,
        18: guidance_verben_multiple_choices_german_to_english,
        19: guidance_verben_multiple_choices_german_to_english,
        20: guidance_verben_multiple_choices_german_to_english,

        21: guidance_verben_multiple_choices_english_to_german,
        22: guidance_verben_multiple_choices_english_to_german,
        23: guidance_verben_multiple_choices_english_to_german,
        24: guidance_verben_multiple_choices_english_to_german,
        25: guidance_verben_multiple_choices_english_to_german,
        26: guidance_verben_multiple_choices_german_to_english,
        27: guidance_verben_multiple_choices_german_to_english,
        28: guidance_verben_multiple_choices_german_to_english,
        29: guidance_verben_multiple_choices_german_to_english,
        30: guidance_verben_multiple_choices_german_to_english,

        31: guidance_verben_multiple_choices_english_to_german,
        32: guidance_verben_multiple_choices_english_to_german,
        33: guidance_verben_multiple_choices_english_to_german,
        34: guidance_verben_multiple_choices_english_to_german,
        35: guidance_verben_multiple_choices_english_to_german,
        36: guidance_verben_multiple_choices_english_to_german,
        37: guidance_verben_multiple_choices_english_to_german,
        38: guidance_verben_multiple_choices_english_to_german,
        39: guidance_verben_multiple_choices_english_to_german,
        40: guidance_verben_multiple_choices_english_to_german,

        41: guidance_verben_multiple_choices_german_to_english,
        42: guidance_verben_multiple_choices_german_to_english,
        43: guidance_verben_multiple_choices_german_to_english,
        44: guidance_verben_multiple_choices_german_to_english,
        45: guidance_verben_multiple_choices_german_to_english,
        46: guidance_verben_multiple_choices_german_to_english,
        47: guidance_verben_multiple_choices_german_to_english,
        48: guidance_verben_multiple_choices_german_to_english,
        49: guidance_verben_multiple_choices_german_to_english,
        50: guidance_verben_multiple_choices_german_to_english,
    },

    trennbare_verben: {
        1: guidance_trennbare_verben_root,
        2: guidance_trennbare_verben_prefix,
        3: guidance_trennbare_verben_no_help,

        4: guidance_trennbare_verben_root,
        5: guidance_trennbare_verben_prefix,
        6: guidance_trennbare_verben_no_help,

        7: guidance_trennbare_verben_root,
        8: guidance_trennbare_verben_root,
        9: guidance_trennbare_verben_root,
        10: guidance_trennbare_verben_root,
        11: guidance_trennbare_verben_prefix,
        12: guidance_trennbare_verben_prefix,
        13: guidance_trennbare_verben_prefix,
        14: guidance_trennbare_verben_prefix,
        15: guidance_trennbare_verben_no_help,
        16: guidance_trennbare_verben_no_help,
        17: guidance_trennbare_verben_no_help,
        18: guidance_trennbare_verben_no_help,

        19: guidance_trennbare_verben_root,
        20: guidance_trennbare_verben_root,
        21: guidance_trennbare_verben_root,
        22: guidance_trennbare_verben_root,
        23: guidance_trennbare_verben_prefix,
        24: guidance_trennbare_verben_prefix,
        25: guidance_trennbare_verben_prefix,
        26: guidance_trennbare_verben_prefix,
        27: guidance_trennbare_verben_no_help,
        28: guidance_trennbare_verben_no_help,
        29: guidance_trennbare_verben_no_help,
        30: guidance_trennbare_verben_no_help,

        31: guidance_trennbare_verben_root,
        32: guidance_trennbare_verben_root,
        33: guidance_trennbare_verben_root,
        34: guidance_trennbare_verben_root,
        35: guidance_trennbare_verben_root,
        36: guidance_trennbare_verben_root,
        37: guidance_trennbare_verben_root,
        38: guidance_trennbare_verben_root,
        39: guidance_trennbare_verben_root,
        40: guidance_trennbare_verben_root,
        41: guidance_trennbare_verben_root,
        42: guidance_trennbare_verben_root,
        43: guidance_trennbare_verben_root,
        44: guidance_trennbare_verben_root,
        45: guidance_trennbare_verben_root,
        46: guidance_trennbare_verben_root,
        47: guidance_trennbare_verben_root,
        48: guidance_trennbare_verben_root,
        49: guidance_trennbare_verben_root,
        50: guidance_trennbare_verben_root,
        51: guidance_trennbare_verben_root,
        52: guidance_trennbare_verben_root,
        53: guidance_trennbare_verben_root,
        54: guidance_trennbare_verben_root,
        55: guidance_trennbare_verben_prefix,
        56: guidance_trennbare_verben_prefix,
        57: guidance_trennbare_verben_prefix,
        58: guidance_trennbare_verben_prefix,
        59: guidance_trennbare_verben_prefix,
        60: guidance_trennbare_verben_prefix,
        61: guidance_trennbare_verben_prefix,
        62: guidance_trennbare_verben_prefix,
        63: guidance_verben_multiple_choices_english_to_german,
        64: guidance_verben_multiple_choices_english_to_german,
        65: guidance_verben_multiple_choices_english_to_german,
        66: guidance_verben_multiple_choices_english_to_german,
        67: guidance_verben_multiple_choices_english_to_german,
        68: guidance_verben_multiple_choices_english_to_german,
        69: guidance_verben_multiple_choices_english_to_german,
        70: guidance_verben_multiple_choices_english_to_german,
    },

    nomen_verben_verbindungen: {
        1: guidance_nomen_verben_verbindungen_nomen_isolation,
        2: guidance_nomen_verben_verbindungen_verben_isolation,
        3: guidance_nomen_verben_verbindungen_nomen_sentences,
        4: guidance_nomen_verben_verbindungen_verben_sentences,

        5: guidance_nomen_verben_verbindungen_nomen_isolation,
        6: guidance_nomen_verben_verbindungen_verben_isolation,
        7: guidance_nomen_verben_verbindungen_nomen_sentences,
        8: guidance_nomen_verben_verbindungen_verben_sentences,
        9: guidance_nomen_verben_verbindungen_nomen_isolation,
        10: guidance_nomen_verben_verbindungen_verben_isolation,
        11: guidance_nomen_verben_verbindungen_nomen_sentences,
        12: guidance_nomen_verben_verbindungen_verben_sentences,
        13: guidance_nomen_verben_verbindungen_nomen_isolation,
        14: guidance_nomen_verben_verbindungen_verben_isolation,
        15: guidance_nomen_verben_verbindungen_nomen_sentences,
        16: guidance_nomen_verben_verbindungen_verben_sentences,

        17: guidance_nomen_verben_verbindungen_nomen_isolation,
        18: guidance_nomen_verben_verbindungen_verben_isolation,
        19: guidance_nomen_verben_verbindungen_nomen_sentences,
        20: guidance_nomen_verben_verbindungen_verben_sentences,
        21: guidance_nomen_verben_verbindungen_nomen_isolation,
        22: guidance_nomen_verben_verbindungen_verben_isolation,
        23: guidance_nomen_verben_verbindungen_nomen_sentences,
        24: guidance_nomen_verben_verbindungen_verben_sentences,
        25: guidance_nomen_verben_verbindungen_nomen_isolation,
        26: guidance_nomen_verben_verbindungen_verben_isolation,
        27: guidance_nomen_verben_verbindungen_nomen_sentences,
        28: guidance_nomen_verben_verbindungen_verben_sentences,
        29: guidance_nomen_verben_verbindungen_nomen_isolation,
        30: guidance_nomen_verben_verbindungen_verben_isolation,
        31: guidance_nomen_verben_verbindungen_nomen_sentences,
        32: guidance_nomen_verben_verbindungen_verben_sentences,
    },

    nomen_verben_wortstaemme: {
        1: guidance_nomen_verben_wortstaemme_verben,
        2: guidance_nomen_verben_wortstaemme_nomen,

        3: guidance_nomen_verben_wortstaemme_verben,
        4: guidance_nomen_verben_wortstaemme_nomen,
        5: guidance_nomen_verben_wortstaemme_verben,
        6: guidance_nomen_verben_wortstaemme_nomen,
        7: guidance_nomen_verben_wortstaemme_verben,
        8: guidance_nomen_verben_wortstaemme_nomen,

        9: guidance_nomen_verben_wortstaemme_verben,
        10: guidance_nomen_verben_wortstaemme_nomen,
        11: guidance_nomen_verben_wortstaemme_verben,
        12: guidance_nomen_verben_wortstaemme_nomen,
        13: guidance_nomen_verben_wortstaemme_verben,
        14: guidance_nomen_verben_wortstaemme_nomen,
        15: guidance_nomen_verben_wortstaemme_verben,
        16: guidance_nomen_verben_wortstaemme_nomen,
        17: guidance_nomen_verben_wortstaemme_verben,
        18: guidance_nomen_verben_wortstaemme_nomen,
        19: guidance_nomen_verben_wortstaemme_verben,
        20: guidance_nomen_verben_wortstaemme_nomen,
        21: guidance_nomen_verben_wortstaemme_verben,
        22: guidance_nomen_verben_wortstaemme_nomen,
        23: guidance_nomen_verben_wortstaemme_verben,
        24: guidance_nomen_verben_wortstaemme_nomen,
        25: guidance_nomen_verben_wortstaemme_verben,
        26: guidance_nomen_verben_wortstaemme_nomen,
        27: guidance_nomen_verben_wortstaemme_verben,
        28: guidance_nomen_verben_wortstaemme_nomen,

        29: guidance_nomen_verben_wortstaemme_verben,
        30: guidance_nomen_verben_wortstaemme_nomen,
        31: guidance_nomen_verben_wortstaemme_verben,
        32: guidance_nomen_verben_wortstaemme_nomen,
        33: guidance_nomen_verben_wortstaemme_verben,
        34: guidance_nomen_verben_wortstaemme_nomen,
        35: guidance_nomen_verben_wortstaemme_verben,
        36: guidance_nomen_verben_wortstaemme_nomen,
        37: guidance_nomen_verben_wortstaemme_verben,
        38: guidance_nomen_verben_wortstaemme_nomen,
        39: guidance_nomen_verben_wortstaemme_verben,
        40: guidance_nomen_verben_wortstaemme_nomen,
        41: guidance_nomen_verben_wortstaemme_verben,
        42: guidance_nomen_verben_wortstaemme_nomen,
        43: guidance_nomen_verben_wortstaemme_verben,
        44: guidance_nomen_verben_wortstaemme_nomen,
        45: guidance_nomen_verben_wortstaemme_verben,
        46: guidance_nomen_verben_wortstaemme_nomen,
        47: guidance_nomen_verben_wortstaemme_verben,
        48: guidance_nomen_verben_wortstaemme_nomen,
        49: guidance_nomen_verben_wortstaemme_verben,
        50: guidance_nomen_verben_wortstaemme_nomen,
        51: guidance_nomen_verben_wortstaemme_verben,
        52: guidance_nomen_verben_wortstaemme_nomen,
        53: guidance_nomen_verben_wortstaemme_verben,
        54: guidance_nomen_verben_wortstaemme_nomen,
        55: guidance_nomen_verben_wortstaemme_verben,
        56: guidance_nomen_verben_wortstaemme_nomen,
        57: guidance_nomen_verben_wortstaemme_verben,
        58: guidance_nomen_verben_wortstaemme_nomen,

        59: guidance_nomen_verben_wortstaemme_verben,
        60: guidance_nomen_verben_wortstaemme_nomen,
        61: guidance_nomen_verben_wortstaemme_verben,
        62: guidance_nomen_verben_wortstaemme_nomen,
        63: guidance_nomen_verben_wortstaemme_verben,
        64: guidance_nomen_verben_wortstaemme_nomen,
        65: guidance_nomen_verben_wortstaemme_verben,
        66: guidance_nomen_verben_wortstaemme_nomen,
        67: guidance_nomen_verben_wortstaemme_verben,
        68: guidance_nomen_verben_wortstaemme_nomen,
        69: guidance_nomen_verben_wortstaemme_verben,
        70: guidance_nomen_verben_wortstaemme_nomen,
        71: guidance_nomen_verben_wortstaemme_verben,
        72: guidance_nomen_verben_wortstaemme_nomen,
        73: guidance_nomen_verben_wortstaemme_verben,
        74: guidance_nomen_verben_wortstaemme_nomen,
        75: guidance_nomen_verben_wortstaemme_verben,
        76: guidance_nomen_verben_wortstaemme_nomen,
        77: guidance_nomen_verben_wortstaemme_verben,
        78: guidance_nomen_verben_wortstaemme_nomen,
        79: guidance_nomen_verben_wortstaemme_verben,
        80: guidance_nomen_verben_wortstaemme_nomen,
        81: guidance_nomen_verben_wortstaemme_verben,
        82: guidance_nomen_verben_wortstaemme_nomen,
        83: guidance_nomen_verben_wortstaemme_verben,
        84: guidance_nomen_verben_wortstaemme_nomen,
        85: guidance_nomen_verben_wortstaemme_verben,
        86: guidance_nomen_verben_wortstaemme_nomen,
        87: guidance_nomen_verben_wortstaemme_verben,
        88: guidance_nomen_verben_wortstaemme_nomen,
        89: guidance_nomen_verben_wortstaemme_verben,
        90: guidance_nomen_verben_wortstaemme_nomen,
        91: guidance_nomen_verben_wortstaemme_verben,
        92: guidance_nomen_verben_wortstaemme_nomen,
    },

    zahlen: {
        1: guidance_zahlen_number,
        2: guidance_zahlen_number,
        3: guidance_zahlen_number,
        4: guidance_zahlen_number,
        5: guidance_zahlen_number,
        6: guidance_zahlen_number,
        7: guidance_zahlen_number,
        8: guidance_zahlen_number,
        9: guidance_zahlen_time_spelled,
        10: guidance_zahlen_time_digital,

        11: guidance_zahlen_number,
        12: guidance_zahlen_number,
        13: guidance_zahlen_ordinal_isolation,
        14: guidance_zahlen_ordinal_isolation,
        15: guidance_zahlen_ordinal_isolation,
        16: guidance_zahlen_ordinal_sentence,

        17: guidance_zahlen_adverb_isolation,
        18: guidance_zahlen_adverb_sentence,
        19: guidance_zahlen_adverb_isolation,
        20: guidance_zahlen_adverb_sentence,
        21: guidance_zahlen_fraction_isolation,
        22: guidance_zahlen_fraction_sentence,

        23: guidance_zahlen_genitive_isolation,
        24: guidance_zahlen_genitive_sentence,
    },
}
