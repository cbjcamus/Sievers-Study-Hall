from data.data_processing.units import (
    praepositionen_grammatik, praepositionen_verben, praepositionen_adjektive, praepositionen_nomen,
    praepositionen_artikel,
    artikel, pronomen, konnektoren, fragen, adverbien,
    adjektive, adjektivdeklinationen,
    trennbare_verben, verben,
    praesens, imperativ, partizip_II, praeteritum, praeteritum_partizip_II, konjunktiv_II, konjunktiv_I, partizip_I,

    deverbale_nomen
)

from webapp.style.icons import ICON_CHECK, ICON_CROSS, ICON_WARN

# bullet point \u25CF

guidance_praepositionen_grammatik_basic = (
    "For each question, you will be provided an incomplete German sentence and its English translation."
    "<br><br>Complete the German sentence with the preposition that fits."
   
    f"<br><br>{ICON_WARN} Only the following prepositions are available at this level: an, auf, aus, bei, bis, durch,"
    f" für, gegen, hinter, in, mit, nach, neben, ohne, seit, über, um, unter, von, vor, zu, zwischen."
    f"<br><br>{ICON_WARN} The correct answer may include an article. In that case, both the form of the prepositional"
    f" contraction (am, ans, vom, zur etc.) or the extended form (an dem etc.) are correct."
    f"<br><br>{ICON_WARN} The absence of preposition may be the correct answer. In that case, leave the input block"
    f" blank and click on the Submit button."
    
    "<h2>Example</h2>"
    "Ich habe _____ Montag Deutschunterricht."
    "<br><br><i>I have German class on Monday.</i>"
    f"<br><br>{ICON_CHECK} am"
    f"<br><br>{ICON_CHECK} an dem"
    f"<br><br>{ICON_CROSS} an"
)

guidance_praepositionen_grammatik_b1_isolation = (
    "For each question, you will be provided the English translation of a German preposition."
    "<br><br>Find the preposition that fits the English translation."

    f"<br><br>{ICON_WARN} Only the following prepositions are available at this level: ab, anstatt, außerhalb, durch,"
    f" gegenüber, innerhalb, laut, trotz, während, wegen, zufolge."
    f"<br><br>{ICON_WARN} Synonyms are available for this exercise. There may be more than one possible answer."
    f"<br><br>{ICON_WARN} Do not write more than one answer, or your answer will be flagged as false."
    
    "<h2>Example</h2>"
    "due to, because of"
    f"<br><br>{ICON_CHECK} wegen"
    f"<br><br>{ICON_CHECK} aufgrund"
    f"<br><br>{ICON_CROSS} wegen, aufgrund"
)

guidance_praepositionen_grammatik_b1_sentences = (
    "For each question, you will be provided an incomplete German sentence and its English translation."
    "<br><br>Complete the German sentence with the preposition that fits."

    f"<br><br>{ICON_WARN} Only the following prepositions are available at this level: ab, anstatt, außerhalb, durch,"
    f" gegenüber, innerhalb, laut, trotz, während, wegen, zufolge."
    f"<br><br>{ICON_WARN} Synonyms are available for this exercise. There may be more than one possible answer."
    f"<br><br>{ICON_WARN} Do not write more than one answer, or your answer will be flagged as false."
    
    "<h2>Example</h2>"
    "Er konnte nicht kommen _____ einer wichtigen Besprechung."
    "<br><br><i>He couldn't come because of an important meeting.</i>"
    f"<br><br>{ICON_CHECK} wegen"
    f"<br><br>{ICON_CHECK} aufgrund"
    f"<br><br>{ICON_CROSS} wegen, aufgrund"
)

guidance_praepositionen_grammatik_b2_isolation = (
    "For each question, you will be provided the English translation of a German preposition."
    "<br><br>Find the preposition that fits the English translation."

    f"<br><br>{ICON_WARN} Only the following prepositions are available at this level: angesichts, anhand, außer, dank,"
    f" entgegen, entlang, infolge, mangels, mithilfe, mittels."
    f"<br><br>{ICON_WARN} Synonyms are available for this exercise. There may be more than one possible answer."
    f"<br><br>{ICON_WARN} Do not write more than one answer, or your answer will be flagged as false."
    
    "<h2>Example</h2>"
    "due to, because of"
    f"<br><br>{ICON_CHECK} wegen"
    f"<br><br>{ICON_CHECK} aufgrund"
    f"<br><br>{ICON_CROSS} wegen, aufgrund"
)

guidance_praepositionen_grammatik_b2_sentences = (
    "For each question, you will be provided an incomplete German sentence and its English translation."
    "<br><br>Complete the German sentence with the preposition that fits."

    f"<br><br>{ICON_WARN} Only the following prepositions are available at this level: angesichts, anhand, außer, dank,"
    f" entgegen, entlang, infolge, mangels, mithilfe, mittels."
    f"<br><br>{ICON_WARN} Synonyms are available for this exercise. There may be more than one possible answer."
    f"<br><br>{ICON_WARN} Do not write more than one answer, or your answer will be flagged as false."
    
    "<h2>Example</h2>"
    "Er konnte nicht kommen _____ einer wichtigen Besprechung."
    "<br><br><i>He couldn't come because of an important meeting.</i>"
    f"<br><br>{ICON_CHECK} wegen"
    f"<br><br>{ICON_CHECK} aufgrund"
    f"<br><br>{ICON_CROSS} wegen, aufgrund"
)

guidance_praepositionen_grammatik_c1_1_isolation = (
    "For each question, you will be provided the English translation of a German preposition."
    "<br><br>Find the preposition that fits the English translation."

    f"<br><br>{ICON_WARN} Only the following prepositions are available at this level: einschließlich, im Gegensatz zu,"
    f" inmitten, je nach, nebst, oberhalb, seitens, unterhalb, zusätzlich zu, zwecks."
    f"<br><br>{ICON_WARN} Synonyms are available for this exercise. There may be more than one possible answer."
    f"<br><br>{ICON_WARN} Do not write more than one answer, or your answer will be flagged as false."
    
    "<h2>Example</h2>"
    "due to, because of"
    f"<br><br>{ICON_CHECK} wegen"
    f"<br><br>{ICON_CHECK} aufgrund"
    f"<br><br>{ICON_CROSS} wegen, aufgrund"
)

guidance_praepositionen_grammatik_c1_1_sentences = (
    "For each question, you will be provided an incomplete German sentence and its English translation."
    "<br><br>Complete the German sentence with the preposition that fits."

    f"<br><br>{ICON_WARN} Only the following prepositions are available at this level: einschließlich, im Gegensatz zu,"
    f" inmitten, je nach, nebst, oberhalb, seitens, unterhalb, zusätzlich zu, zwecks."
    f"<br><br>{ICON_WARN} Synonyms are available for this exercise. There may be more than one possible answer."
    f"<br><br>{ICON_WARN} Do not write more than one answer, or your answer will be flagged as false."
    
    "<h2>Example</h2>"
    "Er konnte nicht kommen _____ einer wichtigen Besprechung."
    "<br><br><i>He couldn't come because of an important meeting.</i>"
    f"<br><br>{ICON_CHECK} wegen"
    f"<br><br>{ICON_CHECK} aufgrund"
    f"<br><br>{ICON_CROSS} wegen, aufgrund"
)

guidance_praepositionen_grammatik_c1_2_isolation = (
    "For each question, you will be provided the English translation of a German preposition."
    "<br><br>Find the preposition that fits the English translation."

    f"<br><br>{ICON_WARN} Only the following prepositions are available at this level: abzüglich, anlässlich,"
    f" beiderseits, bezüglich, diesseits, jenseits, kraft, zugunsten, zuzüglich."
    f"<br><br>{ICON_WARN} Synonyms are available for this exercise. There may be more than one possible answer."
    f"<br><br>{ICON_WARN} Do not write more than one answer, or your answer will be flagged as false."
    
    "<h2>Example</h2>"
    "due to, because of"
    f"<br><br>{ICON_CHECK} wegen"
    f"<br><br>{ICON_CHECK} aufgrund"
    f"<br><br>{ICON_CROSS} wegen, aufgrund"
)

guidance_praepositionen_grammatik_c1_2_sentences = (
    "For each question, you will be provided an incomplete German sentence and its English translation."
    "<br><br>Complete the German sentence with the preposition that fits."

    f"<br><br>{ICON_WARN} Only the following prepositions are available at this level: abzüglich, anlässlich,"
    f" beiderseits, bezüglich, diesseits, jenseits, kraft, zugunsten, zuzüglich."
    f"<br><br>{ICON_WARN} Synonyms are available for this exercise. There may be more than one possible answer."
    f"<br><br>{ICON_WARN} Do not write more than one answer, or your answer will be flagged as false."
    
    "<h2>Example</h2>"
    "Er konnte nicht kommen _____ einer wichtigen Besprechung."
    "<br><br><i>He couldn't come because of an important meeting.</i>"
    f"<br><br>{ICON_CHECK} wegen"
    f"<br><br>{ICON_CHECK} aufgrund"
    f"<br><br>{ICON_CROSS} wegen, aufgrund"
)

guidance_praepositionen_verben_isolation = (
    "For each question, you will be provided an incomplete German Verb-Preposition pair and its English translation."
    "<br><br>Complete the Verb-Preposition pair with the preposition that fits."

    f"<br><br>{ICON_WARN} There is only one correct answer per question."
    
    "<h2>Example</h2>"
    "to think of = denken _____"
    f"<br><br>{ICON_CHECK} an"
)

guidance_praepositionen_verben_sentences = (
    "For each question, you will be provided an incomplete German sentence and its English translation."
    "<br><br>Complete the German sentence with the preposition that fits."

    f"<br><br>{ICON_WARN} There is only one correct answer per question."
    
    "<h2>Example</h2>"
    "Ich denke _____ meine Mutter."
    "<br><br><i>I think about my mother.</i>"
    f"<br><br>{ICON_CHECK} an"
)

guidance_praepositionen_verben_dawort = (
    "For each question, you will be provided an incomplete German sentence and its English translation."
    "<br><br>Complete the German sentence with the Da-Wort that fits."

    f"<br><br>{ICON_WARN} There is only one correct answer per question."

    "<h2>Example</h2>"
    "— Vermissen Sie Ihr Land? <br><bt>— Ja, ich denke oft _____."
    "<br><br><i>— Do you miss your country? <br><bt>— Yes, I often think about it.</i>"
    f"<br><br>{ICON_CHECK} daran"
)

guidance_praepositionen_verben_wowort = (
    "For each question, you will be provided an incomplete German sentence and its English translation."
    "<br><br>Complete the German sentence with the Wo-Wort that fits."

    f"<br><br>{ICON_WARN} There is only one correct answer per question."

    "<h2>Example</h2>"
    "_____ denkst du?"
    "<br><br><i>What are you thinking about?</i>"
    f"<br><br>{ICON_CHECK} Woran"
)

guidance_praepositionen_adjektive_isolation = (
    "For each question, you will be provided an incomplete German Adjective-Preposition pair and its English translation."
    "<br><br>Complete the Adjective-Preposition pair with the preposition that fits." 

    f"<br><br>{ICON_WARN} There is only one correct answer per question."
    
    "<h2>Example</h2>"
    "curious about = neugierig _____"
    f"<br><br>{ICON_CHECK} auf"
)

guidance_praepositionen_adjektive_sentences = (
    "For each question, you will be provided an incomplete German sentence and its English translation."
    "<br><br>Complete the German sentence with the preposition that fits."

    f"<br><br>{ICON_WARN} There is only one correct answer per question."

    "<h2>Example</h2>"
    "Ich bin neugierig _____ die Ergebnisse der Untersuchung."
    "<br><br><i>I am curious about the results of the investigation.</i>"
    f"<br><br>{ICON_CHECK} auf"
)

guidance_praepositionen_nomen_isolation = (
    "For each question, you will be provided an incomplete German Nomun-Preposition pair and its English translation."
    "<br><br>Complete the Noun-Preposition pair with the preposition that fits."

    f"<br><br>{ICON_WARN} There is only one correct answer per question."

    "<h2>Example</h2>"
    "the pride in = der Stolz _____"
    f"<br><br>{ICON_CHECK} auf"
)

guidance_praepositionen_nomen_sentences = (
    "For each question, you will be provided an incomplete German sentence and its English translation."
    "<br><br>Complete the German sentence with the preposition that fits."

    f"<br><br>{ICON_WARN} There is only one correct answer per question."

    "<h2>Example</h2>"
    "Er zeigte Stolz _____ sein Team nach dem Sieg."
    "<br><br><i>He showed pride in his team after the victory.</i>"
    f"<br><br>{ICON_CHECK} auf"
)

guidance_artikel_isolation = (
    "For each question, you will be provided a German article as well as a gender and a case."
    "<br><br>Write the article that corresponds to the gender and case."

    "<h2>Example</h2>"
    "der/die/das \u25CF Feminine, Nominative"
    f"<br><br>{ICON_CHECK} die"
)

guidance_artikel_sentences = (
    "For each question, you will be provided a German sentence and its English translation."
    "<br><br>The German sentence has an article missing. Find the one that fits, taking into account the case and gender."

    "<h2>Example</h2>"
    "_____ Woche hat sieben Tage."
    "<br><br><i>The week has seven days.</i>"
    f"<br><br>{ICON_CHECK} Die"
)

guidance_pronomen_isolation = (
    "For each question, you will be provided a German pronoun as well as a case."
    "<br><br>Write the article that corresponds to the case."

    "<h2>Example</h2>"
    "1st Person Singular \u25CF Nominative"
    f"<br><br>{ICON_CHECK} Ich"
)

guidance_pronomen_sentences = (
    "For each question, you will be provided a German sentence and its English translation."
    "<br><br>The German sentence has a pronoun missing. Find the one that fits, taking into account the grammatical"
    " case (and the gender if applicable)."

    "<h2>Example</h2>"
    "Heute bin _____ sehr müde."
    "<br><br><i>Today I am very tired..</i>"
    f"<br><br>{ICON_CHECK} ich"
)

guidance_konnektoren_isolation = (
    "For each question, you will be provided the English translation of a German connector and its grammatical"
    " type (conjuntion, subjunction, adverb)."
    "<br><br>Find the German connector that corresponds to that translation and grammatical type."

    f"<br><br>{ICON_WARN} Synonyms are available for this exercise. There may be more than one possible answer."
    f"<br><br>{ICON_WARN} Do not write more than one answer, or your answer will be flagged as false."

    "<h2>Example</h2>"
    "therefore, for this reason, because of that \u25CF Adverb"
    f"<br><br>{ICON_CHECK} deshalb"
    f"<br><br>{ICON_CHECK} deswegen"
    f"<br><br>{ICON_CROSS} deshalb, deswegen"
    f"<br><br>{ICON_CROSS} weshalb"
)

guidance_konnektoren_sentences = (
    "For each question, you will be provided a German sentence and its English translation."
    "<br><br>The German sentence has a connector missing. Find the one that fits."

    f"<br><br>{ICON_WARN} Synonyms are available for this exercise. There may be more than one possible answer."
    f"<br><br>{ICON_WARN} Do not write more than one answer, or your answer will be flagged as false."

    "<h2>Example</h2>"
    "Es regnet stark, _____ nehme ich meinen Regenschirm."
    "<br><br><i>It is raining heavily, therefore I take my umbrella.</i>"
    f"<br><br>{ICON_CHECK} deshalb"
    f"<br><br>{ICON_CHECK} deswegen"
    f"<br><br>{ICON_CROSS} deshalb, deswegen"
    f"<br><br>{ICON_CROSS} weshalb"
)

guidance_konnektoren_synonyms = (
    "For each question, you will be provided a German connector and its grammatical type (conjuntion, subjunction,"
    " adverb)."
    "<br><br>Find a synonym of that connector that has the same grammatical type."

    f"<br><br>{ICON_WARN} Do not write more than one synonym, or your answer will be flagged as false."

    "<h2>Example</h2>"
    "darum \u25CF Adverb"
    f"<br><br>{ICON_CHECK} deshalb"
    f"<br><br>{ICON_CHECK} deswegen"
    f"<br><br>{ICON_CROSS} deshalb, deswegen"
    f"<br><br>{ICON_CROSS} darum"
    f"<br><br>{ICON_CROSS} weshalb"
)

guidance_fragen_isolation = (
    "For each question, you will be provided the English translation of a German question-word."
    "<br><br>Find the German question-word that corresponds to that translation."
    
    f"<br><br>{ICON_WARN} Synonyms are available for this exercise. There may be more than one possible answer."
    f"<br><br>{ICON_WARN} Do not write more than one answer, or your answer will be flagged as false."

    "<h2>Example</h2>"
    "Why"
    f"<br><br>{ICON_CHECK} Warum"
    f"<br><br>{ICON_CHECK} Weshalb"
    f"<br><br>{ICON_CROSS} Warum, Weshalb"
)

guidance_fragen_sentences = (
    "For each question, you will be provided a German sentence and its English translation."
    "<br><br>The German sentence has a question-word missing. Find the one that fits."

    f"<br><br>{ICON_WARN} Synonyms are available for this exercise. There may be more than one possible answer."
    f"<br><br>{ICON_WARN} Do not write more than one answer, or your answer will be flagged as false."

    "<h2>Example</h2>"
    "_____ lernst du Deutsch?"
    "<br><br><i>Why are you learning German?</i>"
    f"<br><br>{ICON_CHECK} Warum"
    f"<br><br>{ICON_CHECK} Weshalb"
    f"<br><br>{ICON_CROSS} Warum, Weshalb"
)

guidance_adverbien_isolation = (
    "For each question, you will be provided the English translation of a German adverb."
    "<br><br>Find the German adverb that corresponds to that translation."

    f"<br><br>{ICON_WARN} Synonyms are available for this exercise. There may be more than one possible answer."
    f"<br><br>{ICON_WARN} Do not write more than one answer, or your answer will be flagged as false."

    "<h2>Example</h2>"
    "almost"
    f"<br><br>{ICON_CHECK} fast"
    f"<br><br>{ICON_CHECK} nahezu"
    f"<br><br>{ICON_CROSS} fast, nahezu"
)

guidance_adverbien_sentences = (
    "For each question, you will be provided a German sentence and its English translation."
    "<br><br>The German sentence has an adverb missing. Find the one that fits."

    f"<br><br>{ICON_WARN} Synonyms are available for this exercise. There may be more than one possible answer."
    f"<br><br>{ICON_WARN} Do not write more than one answer, or your answer will be flagged as false."

    "<h2>Example</h2>"
    "Ich bin _____ fertig."
    "<br><br><i>I am almost done.</i>"
    f"<br><br>{ICON_CHECK} fast"
    f"<br><br>{ICON_CHECK} nahezu"
    f"<br><br>{ICON_CROSS} fast, nahezu"
)

guidance_adverbien_hin_her_isolation = (
    "For each question, you will be provided the English translation of a German adverb."
    "<br><br>Find the German adverb in \"hin\" or \"her\" that corresponds to that translation."

    f"<br><br>{ICON_WARN} Synonyms are available for this exercise. There may be more than one possible answer."
    f"<br><br>{ICON_WARN} Do not write more than one answer, or your answer will be flagged as false."

    "<h2>Example</h2>"
    "down, toward the speaker"
    f"<br><br>{ICON_CHECK} herunter"
    f"<br><br>{ICON_CHECK} runter"
    f"<br><br>{ICON_CHECK} herab"
    f"<br><br>{ICON_CROSS} herunter, herab"
    f"<br><br>{ICON_CROSS} hinunter"
)

guidance_adverbien_hin_her_sentences = (
    "For each question, you will be provided a German sentence and its English translation."
    "<br><br>The German sentence has an adverb in \"hin\" or \"her\" missing. Find the one that fits."

    f"<br><br>{ICON_WARN} Synonyms are available for this exercise. There may be more than one possible answer."
    f"<br><br>{ICON_WARN} Do not write more than one answer, or your answer will be flagged as false."

    "<h2>Example</h2>"
    "Er zog vorsichtig die alte Leiter _____, um sie zu reparieren."
    "<br><br><i>He carefully pulled the old ladder down to repair it.</i>"
    f"<br><br>{ICON_CHECK} herunter"
    f"<br><br>{ICON_CHECK} runter"
    f"<br><br>{ICON_CHECK} herab"
    f"<br><br>{ICON_CROSS} herunter, herab"
    f"<br><br>{ICON_CROSS} hinunter"
)

guidance_adverbien_einander_isolation = (
    "For each question, you will be provided the English translation of a German adverb in \"einander\"."
    "<br><br>Find the German adverb that corresponds to that translation."

    f"<br><br>{ICON_WARN} There is only one possible answer per question. Synonyms are not available for this exercise."
    " Read carefully the entire translation."
    
    "<h2>Example</h2>"
    "with each other, jointly"
    f"<br><br>{ICON_CHECK} miteinander"
    f"<br><br>{ICON_CROSS} nebeneinander"
)

guidance_adverbien_einander_sentences = (
    "For each question, you will be provided a German sentence and its English translation."
    "<br><br>The German sentence has an adverb in \"einander\" missing. Find the one that fits."

    f"<br><br>{ICON_WARN} There is only one possible answer per question. Synonyms are not available for this exercise."
    " Read carefully the entire translation."
    
    "<h2>Example</h2>"
    "Wir sollten offener _____ kommunizieren, um Missverständnisse zu vermeiden."
    "<br><br><i>We should communicate more openly with each other to avoid misunderstandings.</i>"
    f"<br><br>{ICON_CHECK} miteinander"
    f"<br><br>{ICON_CROSS} nebeneinander"
)

guidance_adverbien_multiple_choices_english_to_german = (
    "For each question, you will see the English translation of a German adjective and five German adverbs."
    "<br>Select the German adverb that correspond to the English translation."
    
    f"<br><br>{ICON_WARN} Synonyms are available for this exercise. There may be more than one possible answer."

    "<h2>Example</h2>"
    "now and then, occasionally"
    "<br>"
    "<br>bisweilen"
    "<br>ab und zu"
    "<br>wütend"
    "<br>unterwegs"
    "<br>zum Abschluss"
    f"<br><br>{ICON_CHECK} bisweilen"
    f"<br>{ICON_CHECK} ab und zu"
    f"<br>{ICON_CROSS} wütend"
    f"<br>{ICON_CROSS} unterwegs"
    f"<br>{ICON_CROSS} zum Abschluss"
)

guidance_adverbien_multiple_choices_german_to_english = (
    "For each question, you will see a German adverb and five potential English translations."
    "<br>Select the translation that correspond to the German adverb."

    f"<br><br>{ICON_WARN} There is only one possible answer per question. Synonyms are not available for this exercise."
    " Read carefully the entire translation."
    
    "<h2>Example</h2>"
    "wütend"
    "<br>"
    "<br>angrily, furiously"
    "<br>now and then, occasionally"
    "<br>on the way"
    "<br>to conclude, in conclusion"
    "<br>in any case, at least"
    f"<br><br>{ICON_CHECK} angrily, furiously"
)

guidance_adjektive_isolation = (
    "For each question, you will see the English translation of a German adjective."
    "<br>Find the German adjective that correspond to the translation."

    f"<br><br>{ICON_WARN} Synonyms are available for this exercise. There may be more than one possible answer."
    f"<br><br>{ICON_WARN} Do not write more than one answer, or your answer will be flagged as false."

    "<h2>Example</h2>"
    "cheap"
    f"<br><br>{ICON_CHECK} billig"
    f"<br><br>{ICON_CHECK} günstig"
    f"<br><br>{ICON_CROSS} billig, günstig"
)

guidance_adjektive_opposite = (
    "For each question, you will see a German adjective."
    "<br>Write its opposite in German."

    f"<br><br>{ICON_WARN} Synonyms are available for this exercise. There may be more than one possible answer."
    f"<br><br>{ICON_WARN} Do not write more than one answer, or your answer will be flagged as false."

    "<h2>Example</h2>"
    "teuer"
    f"<br><br>{ICON_CHECK} billig"
    f"<br><br>{ICON_CHECK} günstig"
    f"<br><br>{ICON_CROSS} billig, günstig"
)

guidance_adjektive_comparative = (
    "For each question, you will see a German adjective."
    "<br>Write its comparative form."

    "<h2>Example</h2>"
    "alt"
    f"<br><br>{ICON_CHECK} älter"
)

guidance_adjektive_superlative = (
    "For each question, you will see a German adjective."
    "<br>Write its superlative form."

    "<h2>Example</h2>"
    "alt"
    f"<br><br>{ICON_CHECK} am ältesten"
)

guidance_adjektive_comparison_words = (
    "For each question, you will be provided a German sentence and its English translation."
    "<br><br>The German sentence has a comparison word missing. Find the one that fits."

    "<h2>Example</h2>"
    "Peter ist größer _____ sein Bruder."
    "<br><br><i>Peter is taller than his brother.</i>"
    f"<br><br>{ICON_CHECK} als"
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
    f"<br><br>{ICON_CHECK} eigen"
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
    f"<br><br>{ICON_CHECK} own"
)

guidance_adjektivdeklinationen_isolation = (
    "For each question, you will be provided a German phrase with a case and an adjective."
    "<br><br>Complete the phrase with the declined adjective, taking into account the article,"
    " the gender of the noun and the grammatical case."

    "<h2>Example</h2>"
    "ein _____ Vater \u25CF Nominativ \u25CF nett"
    f"<br><br>{ICON_CHECK} netter"
)

guidance_adjektivdeklinationen_sentences = (
    "For each question, you will be provided an incomplete German sentence and an adjective."
    "<br><br>Complete the sentence with the adjective properly declined, taking into account the article,"
    " the gender of the noun and the grammatical case."

    "<h2>Example</h2>"
    "Die _____ Kinder stellen viele Fragen. \u25CF klug"
    f"<br><br>{ICON_CHECK} klugen"
)

guidance_trennbare_verben_root = (
    "For each question, you will be provided the English translation of a German (un)trennbare verb as well as its root."
    "<br><br>Find the German verb that correspond to the translation and root."
    
    f"<br><br>{ICON_WARN} There is only one possible answer per question. Synonyms are not available for this exercise."
    " Read carefully the entire translation."
    f"<br><br>{ICON_WARN} Do not write any reflexive pronoun, even if the verb is usually reflexive."

    "<h2>Example</h2>"
    "to pull, to drag, to move → ziehen"
    "<br><br>to get dressed, to put on, to dress someone, to attract, to pull → _____"
    f"<br><br>{ICON_CHECK} anziehen"
)

guidance_trennbare_verben_prefix = (
    "For each question, you will be provided the English translation of a German (un)trennbare verb as well as its prefix."
    "<br><br>Find the German verb that correspond to the translation and prefix."

    f"<br><br>{ICON_WARN} There is only one possible answer per question. Synonyms are not available for this exercise."
    " Read carefully the entire translation."
    f"<br><br>{ICON_WARN} Do not write any reflexive pronoun, even if the verb is usually reflexive."

    "<h2>Example</h2>"
    "to get dressed, to put on, to dress someone, to attract, to pull \u25CF an"
    f"<br><br>{ICON_CHECK} anziehen"
)

guidance_trennbare_verben_no_help = (
    "For each question, you will be provided the English translation of a German (un)trennbare verb."
    "<br><br>Find the German verb that correspond to the entire translation."

    f"<br><br>{ICON_WARN} There is only one possible answer per question. Synonyms are not available for this exercise."
    " Read carefully the entire translation."
    f"<br><br>{ICON_WARN} Do not write any reflexive pronoun, even if the verb is usually reflexive."

    "<h2>Example</h2>"
    "to get dressed, to put on, to dress someone, to attract, to pull"
    f"<br><br>{ICON_CHECK} anziehen"
)

guidance_verben_translation = (
    "For each question, you will see the English translation of a German verb."
    "<br>Find the German verb that correspond to the entire translation."
    
    f"<br><br>{ICON_WARN} There is only one possible answer per question. Synonyms are not available for this exercise."
    f" Read carefully the entire translation."
    f"<br><br>{ICON_WARN} Do not write any reflexive pronoun, even if the verb is usually reflexive."
    
    "<h2>Example</h2>"
    "to make glad, to be glad (refl.), to look forward (refl.)"
    f"<br><br>{ICON_CHECK} freuen"
    f"<br><br>{ICON_CROSS} sich freuen"
)

guidance_verben_multiple_choices_english_to_german = (
    "For each question, you will see the English translation of a German verb and five German verbs."
    "<br>Select the German verb that correspond to the entire translation."

    f"<br><br>{ICON_WARN} There is only one possible answer per question. Synonyms are not available for this exercise."
    f" Read carefully the entire translation."

    "<h2>Example</h2>"
    "to replace, to substitute, to compensate for"
    "<br><br>ersetzen"
    "<br>leiden"
    "<br>diskutieren"
    "<br>rufen"
    "<br>vorschlagen"
    f"<br><br>{ICON_CHECK} ersetzen"
)

guidance_verben_multiple_choices_german_to_english = (
    "For each question, you will see a German verb and five potential English translations."
    "<br>Select the translation that correspond to the German verb."

    f"<br><br>{ICON_WARN} There is only one possible answer per question. Synonyms are not available for this exercise."
    f" Read carefully the entire translations."

    "<h2>Example</h2>"
    "ersetzen"
    "<br><br>to replace, to substitute, to compensate for"
    "<br>to suffer, to endure, to bear"
    "<br>to discuss, to debate"
    "<br>to call, to shout, to summon"
    "<br>to suggest, to propose"
    f"<br><br>{ICON_CHECK} to replace, to substitute, to compensate for"
)


GUIDANCE_EXERCISE = {

    praepositionen_grammatik: {
        1: guidance_praepositionen_grammatik_basic,
        2: guidance_praepositionen_grammatik_basic,
        3: guidance_praepositionen_grammatik_basic,
        4: guidance_praepositionen_grammatik_basic,

        5: guidance_praepositionen_grammatik_basic,
        6: guidance_praepositionen_grammatik_basic,
        7: guidance_praepositionen_grammatik_basic,
        8: guidance_praepositionen_grammatik_basic,

        9: guidance_praepositionen_grammatik_basic,
        10: guidance_praepositionen_grammatik_basic,
        11: guidance_praepositionen_grammatik_b1_isolation,
        12: guidance_praepositionen_grammatik_b1_sentences,

        13: guidance_praepositionen_grammatik_basic,
        14: guidance_praepositionen_grammatik_basic,
        15: guidance_praepositionen_grammatik_b2_isolation,
        16: guidance_praepositionen_grammatik_b2_sentences,

        17: guidance_praepositionen_grammatik_c1_1_isolation,
        18: guidance_praepositionen_grammatik_c1_1_sentences,
        19: guidance_praepositionen_grammatik_c1_2_isolation,
        20: guidance_praepositionen_grammatik_c1_2_sentences,

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
    },

    praepositionen_adjektive: {
        1: guidance_praepositionen_adjektive_isolation,
        2: guidance_praepositionen_adjektive_sentences,

        3: guidance_praepositionen_adjektive_isolation,
        4: guidance_praepositionen_adjektive_sentences,

        5: guidance_praepositionen_adjektive_isolation,
        6: guidance_praepositionen_adjektive_sentences,
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
        30: guidance_artikel_sentences,
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

        42: guidance_artikel_isolation,
        43: guidance_artikel_sentences,
    },

    pronomen: {
        1: guidance_pronomen_isolation,
        2: guidance_pronomen_sentences,
        3: guidance_pronomen_sentences,
        4: guidance_pronomen_sentences,
        5: guidance_pronomen_sentences,
        6: guidance_pronomen_sentences,

        7: guidance_pronomen_isolation,
        8: guidance_pronomen_sentences,
        9: guidance_pronomen_sentences,
        10: guidance_pronomen_sentences,
        11: guidance_pronomen_isolation,
        12: guidance_pronomen_sentences,
        13: guidance_pronomen_isolation,
        14: guidance_pronomen_sentences,

        15: guidance_pronomen_isolation,
        16: guidance_pronomen_sentences,
        17: guidance_pronomen_sentences,
        18: guidance_pronomen_sentences,
        19: guidance_pronomen_sentences,
        20: guidance_pronomen_sentences,
        21: guidance_pronomen_sentences,
        22: guidance_pronomen_sentences,

        23: guidance_pronomen_sentences,
        24: guidance_pronomen_sentences,
        25: guidance_pronomen_sentences,
    },

    konnektoren: {
        1: guidance_konnektoren_isolation,
        2: guidance_konnektoren_sentences,

        3: guidance_konnektoren_isolation,
        4: guidance_konnektoren_sentences,

        5: guidance_konnektoren_isolation,
        6: guidance_konnektoren_sentences,
        7: guidance_konnektoren_synonyms,

        8: guidance_konnektoren_isolation,
        9: guidance_konnektoren_sentences,
        10: guidance_konnektoren_isolation,
        11: guidance_konnektoren_sentences,
        12: guidance_konnektoren_synonyms,

        13: guidance_konnektoren_isolation,
        14: guidance_konnektoren_sentences,
        15: guidance_konnektoren_synonyms,
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
        9: guidance_adverbien_isolation,
        10: guidance_adverbien_sentences,

        11: guidance_adverbien_isolation,
        12: guidance_adverbien_sentences,
        13: guidance_adverbien_isolation,
        14: guidance_adverbien_sentences,
        15: guidance_adverbien_isolation,
        16: guidance_adverbien_sentences,
        17: guidance_adverbien_isolation,
        18: guidance_adverbien_sentences,

        19: guidance_adverbien_isolation,
        20: guidance_adverbien_sentences,
        21: guidance_adverbien_isolation,
        22: guidance_adverbien_sentences,
        23: guidance_adverbien_isolation,
        24: guidance_adverbien_sentences,
        25: guidance_adverbien_isolation,
        26: guidance_adverbien_sentences,
        27: guidance_adverbien_isolation,
        28: guidance_adverbien_sentences,

        29: guidance_adverbien_hin_her_isolation,
        30: guidance_adverbien_hin_her_sentences,
        31: guidance_adverbien_einander_isolation,
        32: guidance_adverbien_einander_sentences,
        33: guidance_adverbien_multiple_choices_english_to_german,
        34: guidance_adverbien_multiple_choices_german_to_english,
        35: guidance_adverbien_multiple_choices_english_to_german,
        36: guidance_adverbien_multiple_choices_german_to_english,
        37: guidance_adverbien_multiple_choices_english_to_german,
        38: guidance_adverbien_multiple_choices_german_to_english,
        39: guidance_adverbien_multiple_choices_english_to_german,
        40: guidance_adverbien_multiple_choices_german_to_english,
        41: guidance_adverbien_multiple_choices_english_to_german,
        42: guidance_adverbien_multiple_choices_german_to_english,
        43: guidance_adverbien_multiple_choices_english_to_german,
        44: guidance_adverbien_multiple_choices_german_to_english,
    },

    adjektive: {
        1: guidance_adjektive_isolation,
        2: guidance_adjektive_isolation,
        3: guidance_adjektive_isolation,
        4: guidance_adjektive_opposite,
        5: guidance_adjektive_opposite,
        6: guidance_adjektive_comparative,
        7: guidance_adjektive_comparative,
        8: guidance_adjektive_comparative,
        9: guidance_adjektive_superlative,
        10: guidance_adjektive_superlative,
        11: guidance_adjektive_superlative,
        12: guidance_adjektive_comparison_words,

        13: guidance_adjektive_isolation,
        14: guidance_adjektive_isolation,
        15: guidance_adjektive_isolation,
        16: guidance_adjektive_opposite,
        17: guidance_adjektive_opposite,
        18: guidance_adjektive_comparative,
        19: guidance_adjektive_comparative,
        20: guidance_adjektive_comparative,
        21: guidance_adjektive_superlative,
        22: guidance_adjektive_superlative,
        23: guidance_adjektive_superlative,

        24: guidance_adjektive_multiple_choices_german_to_english,
        25: guidance_adjektive_multiple_choices_german_to_english,
        26: guidance_adjektive_multiple_choices_german_to_english,
        27: guidance_adjektive_multiple_choices_english_to_german,
        28: guidance_adjektive_multiple_choices_english_to_german,
        29: guidance_adjektive_multiple_choices_english_to_german,

        30: guidance_adjektive_multiple_choices_german_to_english,
        31: guidance_adjektive_multiple_choices_german_to_english,
        32: guidance_adjektive_multiple_choices_german_to_english,
        33: guidance_adjektive_multiple_choices_english_to_german,
        34: guidance_adjektive_multiple_choices_english_to_german,
        35: guidance_adjektive_multiple_choices_english_to_german,
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
        21: guidance_adjektivdeklinationen_isolation,
        22: guidance_adjektivdeklinationen_sentences,

        23: guidance_adjektivdeklinationen_isolation,
        24: guidance_adjektivdeklinationen_sentences,
        25: guidance_adjektivdeklinationen_isolation,
        26: guidance_adjektivdeklinationen_sentences,
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
        26: guidance_verben_multiple_choices_english_to_german,
        27: guidance_verben_multiple_choices_english_to_german,
        28: guidance_verben_multiple_choices_english_to_german,
        29: guidance_verben_multiple_choices_english_to_german,
        30: guidance_verben_multiple_choices_english_to_german,
        31: guidance_verben_multiple_choices_german_to_english,
        32: guidance_verben_multiple_choices_german_to_english,
        33: guidance_verben_multiple_choices_german_to_english,
        34: guidance_verben_multiple_choices_german_to_english,
        35: guidance_verben_multiple_choices_german_to_english,
        36: guidance_verben_multiple_choices_german_to_english,
        37: guidance_verben_multiple_choices_german_to_english,
        38: guidance_verben_multiple_choices_german_to_english,
        39: guidance_verben_multiple_choices_german_to_english,
        40: guidance_verben_multiple_choices_german_to_english,
    }

}
