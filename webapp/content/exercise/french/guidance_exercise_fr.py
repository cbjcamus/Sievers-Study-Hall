from data.data_processing.units import (
    praepositionen_grammatik, praepositionen_verben, praepositionen_adjektive, praepositionen_nomen,
    praepositionen_artikel,
    artikel, pronomen, konnektoren, fragen, adverbien,
    adjektive, adjektivdeklinationen,
    verben, trennbare_verben, nomen_verben_verbindungen,
    praesens, imperativ, partizip_II, praeteritum, praeteritum_partizip_II, konjunktiv_II, konjunktiv_I, partizip_I,
)

from webapp.style.icons import ICON_CHECK, ICON_CROSS, ICON_WARN

# bullet point \u25CF

guidance_praepositionen_grammatik_isolation = (
    "Pour chaque question, vous recevrez la traduction française d'une préposition allemande."
    "<br><br>Trouvez la préposition qui correspond à la traduction française."

    f"<br><br>{ICON_WARN} Des synonymes sont disponibles pour cet exercice. Il peut y avoir plusieurs réponses possibles."
    f"<br><br>{ICON_WARN} N'écrivez pas plus d'une réponse, sinon votre réponse sera signalée comme fausse."

    "<h2>Exemple</h2>"
    "à cause de, dû à"
    f"<br><br>{ICON_CHECK} wegen"
    f"<br><br>{ICON_CHECK} aufgrund"
    f"<br><br>{ICON_CROSS} wegen, aufgrund"
)

guidance_praepositionen_grammatik_sentences = (
    "Pour chaque question, vous recevrez une phrase allemande incomplète et sa traduction française."
    "<br><br>Complétez la phrase allemande avec la préposition qui convient."
    
    f"<br><br>{ICON_WARN} Des synonymes sont disponibles pour cet exercice. Il peut y avoir plusieurs réponses possibles."
    f"<br><br>{ICON_WARN} N'écrivez pas plus d'une réponse, sinon votre réponse sera signalée comme fausse."
    f"<br><br>{ICON_WARN} La bonne réponse peut inclure un article. Dans ce cas, la forme de la prépositionnelle"
    f" contraction (am, ans, vom, zur etc.) ou la forme étendue (an dem etc.) sont correctes."
    
    "<h2>Exemple</h2>"
    "Ich habe _____ Montag Deutschunterricht."
    "<br><br><i>J'ai un cours d'allemand lundi.</i>"
    f"<br><br>{ICON_CHECK} am"
    f"<br><br>{ICON_CHECK} an dem"
    f"<br><br>{ICON_CROSS} an"
)

guidance_praepositionen_verben_isolation = (
    "Pour chaque question, vous recevrez un couple verbe-préposition allemand incomplet et sa traduction française."
    "<br><br>Complétez le couple verbe-préposition avec la préposition qui convient."
    
    f"<br><br>{ICON_WARN} Il n'y a qu'une seule bonne réponse par question."
    
    "<h2>Exemple</h2>"
    "penser à = denken _____"
    f"<br><br>{ICON_CHECK} an"
)

guidance_praepositionen_verben_sentences = (
    "Pour chaque question, vous recevrez une phrase allemande incomplète et sa traduction française."
    "<br><br>Complétez la phrase allemande avec la préposition qui convient."
    
    f"<br><br>{ICON_WARN} Il n'y a qu'une seule bonne réponse par question."
    
    "<h2>Exemple</h2>"
    "Ich denke _____ meine Mutter.</i>"
    "<br><br><i>Je pense à ma mère.</i>"
    f"<br><br>{ICON_CHECK} an"
)

guidance_praepositionen_verben_dawort = (
    "Pour chaque question, vous recevrez une phrase allemande incomplète et sa traduction française."
    "<br><br>Complétez la phrase allemande avec l'adverbe pronominal en Da- qui convient."
    
    f"<br><br>{ICON_WARN} Il n'y a qu'une seule bonne réponse par question."
    
    "<h2>Exemple</h2>"
    "— Vermissen Sie Ihr Land? <br><bt>— Ja, ich denke oft _____."
    "<br><br><i>— Votre pays vous manque-t-il? <br><bt>— Oui, j'y pense souvent.</i>"
    f"<br><br>{ICON_CHECK} daran"
)

guidance_praepositionen_verben_wowort = (
    "Pour chaque question, vous recevrez une phrase allemande incomplète et sa traduction française."
    "<br><br>Complétez la phrase allemande avec l'adverbe pronominal en Wo- qui convient."
    
    f"<br><br>{ICON_WARN} Il n'y a qu'une seule bonne réponse par question."
    
    "<h2>Exemple</h2>"
    "_____ denkst du?"
    "<br><br><i>À quoi pensez-vous?</i>"
    f"<br><br>{ICON_CHECK} Woran"
)

guidance_praepositionen_adjektive_isolation = (
    "Pour chaque question, vous recevrez un couple adjectif-préposition allemand incomplet et sa traduction française."

    "<br><br>Complétez le couple adjectif-préposition avec la préposition qui convient."
    
    f"<br><br>{ICON_WARN} Il n'y a qu'une seule bonne réponse par question."
    
    "<h2>Exemple</h2>"
    "curieux de = neugierig _____"
    f"<br><br>{ICON_CHECK} auf"
)

guidance_praepositionen_adjektive_sentences = (
    "Pour chaque question, vous recevrez une phrase allemande incomplète et sa traduction française."
    "<br><br>Complétez la phrase allemande avec la préposition qui convient."
    
    f"<br><br>{ICON_WARN} Il n'y a qu'une seule bonne réponse par question."
    
    "<h2>Exemple</h2>"
    "Ich bin neugierig _____ die Ergebnisse der Untersuchung."
    "<br><br><i>Je suis curieux de connaître les résultats de l'enquête.</i>"
    f"<br><br>{ICON_CHECK} auf"
)

guidance_praepositionen_nomen_isolation = (
    "Pour chaque question, vous recevrez un couple nom-préposition allemand incomplet et sa traduction française."
    "<br><br>Complétez le couple nom-préposition avec la préposition qui convient."
    
    f"<br><br>{ICON_WARN} Il n'y a qu'une seule bonne réponse par question."
    
    "<h2>Exemple</h2>"
    "la fierté de = der Stolz _____"
    f"<br><br>{ICON_CHECK} auf"
)

guidance_praepositionen_nomen_sentences = (
    "Pour chaque question, vous recevrez une phrase allemande incomplète et sa traduction française."
    "<br><br>Complétez la phrase allemande avec la préposition qui convient."
    
    f"<br><br>{ICON_WARN} Il n'y a qu'une seule bonne réponse par question."
    
    "<h2>Exemple</h2>"
    "Er zeigte Stolz _____ sein Team nach dem Sieg."
    "<br><br><i>Il a montré sa fierté envers son équipe après la victoire.</i>"
    f"<br><br>{ICON_CHECK} auf"
)

guidance_artikel_isolation = (
    "Pour chaque question, vous recevrez un article en allemand, ainsi qu'un genre et un cas."

    "<br><br>Rédigez l'article correspondant au genre et au cas."
    
    "<h2>Exemple</h2>"
    "der/die/das \u25CF Féminin, Nominatif"
    f"<br><br>{ICON_CHECK} die"
)

guidance_artikel_sentences = (
    "Pour chaque question, vous recevrez une phrase en allemand et sa traduction en anglais."
    "<br><br>Il manque un article dans la phrase allemande. Trouvez celui qui convient, en tenant compte du cas et du genre."

    "<h2>Exemple</h2>"
    "_____ Woche hat sieben Tage."
    "<br><br><i>La semaine compte sept jours.</i>"
    f"<br><br>{ICON_CHECK} Die"
)

guidance_pronomen_isolation = (
    "Pour chaque question, vous recevrez un pronom allemand ainsi qu'un cas."
    "<br><br>Écrivez l'article qui correspond au cas."

    "<h2>Exemple</h2>"
    "1re personne du singulier \u25CF Nominatif"
    f"<br><br>{ICON_CHECK} Ich"
)

guidance_pronomen_sentences = (
    "Pour chaque question, vous recevrez une phrase en allemand et sa traduction en anglais."
    "<br><br>Il manque un pronom dans la phrase allemande. Trouvez celui qui convient, en tenant compte du cas grammatical"
    " (et du genre, le cas échéant)."

    "<h2>Exemple</h2>"
    "Heute bin _____ sehr müde."
    "<br><br><i>Aujourd'hui, je suis très fatigué.</i>"
    f"<br><br>{ICON_CHECK} ich"
)

guidance_pronomen_replacing = (
    "Pour chaque question, vous recevrez une phrase en allemand, sa traduction en anglais, et un objet."
    "<br><br>Remplacez l'objet avec le pronom qui convient, en tenant compte du cas grammatical (et du genre, le cas échéant)."

    "<h2>Exemple</h2>"
    "Wir besuchen die Schule jeden Tag. \u25CF die Schule"
    "<br><br><i>Nous visitons l'école tous les jours.</i>"
    f"<br><br>{ICON_CHECK} sie"
    f"<br><br>{ICON_CROSS} es"
    f"<br><br>{ICON_CROSS} ihr"
)

guidance_konnektoren_isolation = (
    "Pour chaque question, vous recevrez la traduction française d'un connecteur allemand et son type grammatical "
    " (conjonction, subjonction, adverbe)."
    "<br><br>Trouvez le connecteur allemand qui correspond à cette traduction et à ce type grammatical."

    f"<br><br>{ICON_WARN} Synonymes sont disponibles pour cet exercice. Il peut y avoir plusieurs réponses possibles."
    f"<br><br>{ICON_WARN} Ne donnez pas plusieurs réponses, sinon votre réponse sera considérée comme fausse."

    "<h2>Exemple</h2>"
    "par conséquent, pour cette raison, à cause de cela \u25CF Adverbe"
    f"<br><br>{ICON_CHECK} deshalb"
    f"<br><br>{ICON_CHECK} deswegen"
    f"<br><br>{ICON_CROSS} deshalb, deswegen"
    f"<br><br>{ICON_CROSS} weshalb"
    f"<br><br>"
    
    "ainsi que \u25CF Conjonction corrélative"
    f"<br><br>{ICON_CHECK} sowohl als auch"
    f"<br><br>{ICON_CROSS} sowohl ... als auch"
)

guidance_konnektoren_sentences = (
    "Pour chaque question, vous recevrez une phrase en allemand et sa traduction en anglais."
    "<br><br>Il manque un connecteur dans la phrase allemande. Trouvez celui qui convient."

    f"<br><br>{ICON_WARN} Des synonymes sont disponibles pour cet exercice. Il peut y avoir plusieurs réponses possibles."
    f"<br><br>{ICON_WARN} N'écrivez pas plus d'une réponse, sinon votre réponse sera considérée comme fausse."

    "<h2>Exemple</h2>"
    "Es regnet stark, _____ nehme ich meinen Regenschirm."
    "<br><br><i>Il pleut fort, donc je prends mon parapluie.</i>"
    f"<br><br>{ICON_CHECK} deshalb"
    f"<br><br>{ICON_CHECK} deswegen"
    f"<br><br>{ICON_CROSS} deshalb, deswegen"
    f"<br><br>{ICON_CROSS} weshalb"
)

guidance_konnektoren_synonyms = (
    "Pour chaque question, vous recevrez un connecteur allemand et son type grammatical (conjonction, subjonction, adverbe)."
    "<br><br>Trouvez un synonyme de ce connecteur qui a le même type grammatical."

    f"<br><br>{ICON_WARN} N'écrivez pas plus d'un synonyme, sinon votre réponse sera considérée comme fausse."

    "<h2>Example</h2>"
    "darum \u25CF Adverbe"
    f"<br><br>{ICON_CHECK} deshalb"
    f"<br><br>{ICON_CHECK} deswegen"
    f"<br><br>{ICON_CROSS} deshalb, deswegen"
    f"<br><br>{ICON_CROSS} darum"
    f"<br><br>{ICON_CROSS} weshalb"
)

guidance_fragen_isolation = (
    "Pour chaque question, vous recevrez la traduction française d'un mot interrogatif allemand."
    "<br><br>Trouvez le mot interrogatif allemand qui correspond à cette traduction."
    
    f"<br><br>{ICON_WARN} Synonymes sont disponibles pour cet exercice. Il peut y avoir plusieurs réponses possibles."
    f"<br><br>{ICON_WARN} N'écrivez pas plus d'une réponse, sinon votre réponse sera considérée comme fausse."

    "<h2>Exemple</h2>"
    "Pourquoi"
    f"<br><br>{ICON_CHECK} Warum"
    f"<br><br>{ICON_CHECK} Weshalb"
    f"<br><br>{ICON_CROSS} Warum, Weshalb"
)

guidance_fragen_sentences = (
    "Pour chaque question, vous recevrez une phrase allemande et sa traduction française"

    "<br><br>Il manque un mot interrogatif dans la phrase allemande. Trouvez celui qui convient."
    
    f"<br><br>{ICON_WARN} Des synonymes sont disponibles pour cet exercice. Il peut y avoir plusieurs réponses possibles."
    f"<br><br>{ICON_WARN} N'écrivez pas plus d'une réponse, sinon votre réponse sera signalée comme fausse."
    
    "<h2>Exemple</h2>"
    "_____ lernst du Deutsch?"
    "<br><br><i>Pourquoi apprenez-vous l'allemand?</i>"
    f"<br><br>{ICON_CHECK} Warum"
    f"<br><br>{ICON_CHECK} Weshalb"
    f"<br><br>{ICON_CROSS} Warum, Weshalb"
)

guidance_adverbien_isolation = (
    "Pour chaque question, vous recevrez la traduction française d'un adverbe allemand."

    "<br><br>Trouvez l'adverbe allemand correspondant à cette traduction."
    
    f"<br><br>{ICON_WARN} Des synonymes sont disponibles pour cet exercice. Il peut y avoir plusieurs réponses possibles."
    f"<br><br>{ICON_WARN} N'écrivez pas plus d'une réponse, sinon votre réponse sera signalée comme fausse."
    
    "<h2>Exemple</h2>"
    "almost"
    f"<br><br>{ICON_CHECK} fast"
    f"<br><br>{ICON_CHECK} nahezu"
    f"<br><br>{ICON_CROSS} fast, nahezu"
)

guidance_adverbien_sentences = (
    "Pour chaque question, vous recevrez une phrase allemande et sa traduction française."
    "<br><br>Il manque un adverbe dans la phrase allemande. Trouvez celui qui convient."

    f"<br><br>{ICON_WARN} Des synonymes sont disponibles pour cet exercice. Il peut y avoir plusieurs réponses possibles."
    f"<br><br>{ICON_WARN} N'écrivez pas plus d'une réponse, sinon votre réponse sera signalée comme fausse."
    
    "<h2>Exemple</h2>"
    "Ich bin _____ fertig."
    "<br><br><i>J'ai presque fini.</i>"
    f"<br><br>{ICON_CHECK} fast"
    f"<br><br>{ICON_CHECK} nahezu"
    f"<br><br>{ICON_CROSS} fast, nahezu"
)

guidance_adverbien_hin_her_isolation = (
    "Pour chaque question, vous recevrez la traduction française d'un adverbe allemand."
    "<br><br>Trouvez l'adverbe allemand dans «hin» ou «her» correspondant à cette traduction."
    
    f"<br><br>{ICON_WARN} Des synonymes sont disponibles pour cet exercice. Il peut y avoir plusieurs réponses possibles."
    f"<br><br>{ICON_WARN} N'écrivez pas plus d'une réponse, sinon votre réponse sera signalée comme fausse."
    
    "<h2>Exemple</h2>"
    "down, towards the speaker"
    f"<br><br>{ICON_CHECK} herunter"
    f"<br><br>{ICON_CHECK} runter"
    f"<br><br>{ICON_CHECK} herab"
    f"<br><br>{ICON_CROSS} herunter, herab"
    f"<br><br>{ICON_CROSS} hinunter"
)

guidance_adverbien_hin_her_sentences = (
    "Pour chaque question, vous recevrez une phrase allemande et sa traduction française"
    "<br><br>La phrase allemande manque un adverbe dans «hin» ou «her». Trouvez celui qui convient."
    
    f"<br><br>{ICON_WARN} Des synonymes sont disponibles pour cet exercice. Il peut y avoir plusieurs réponses possibles."
    f"<br><br>{ICON_WARN} N'écrivez pas plus d'une réponse, sinon votre réponse sera signalée comme fausse."
    
    "<h2>Exemple</h2>"
    "Er zog vorsichtig die alte Leiter _____, um sie zu reparieren."
    "<br><br><i>Il a soigneusement descendu la vieille échelle pour la réparer.</i>"
    f"<br><br>{ICON_CHECK} herunter"
    f"<br><br>{ICON_CHECK} runter"
    f"<br><br>{ICON_CHECK} herab"
    f"<br><br>{ICON_CROSS} herunter, herab"
    f"<br><br>{ICON_CROSS} hinunter"
)

guidance_adverbien_einander_isolation = (
    "Pour chaque question, vous recevrez la traduction française d'un adverbe allemand dans «einander»."
    "<br><br>Trouvez l'adverbe allemand correspondant à cette traduction."

    f"<br><br>{ICON_WARN} Il n'y a qu'une seule réponse possible par question. Les synonymes ne sont pas disponibles pour cet exercice. "
    "Lisez attentivement la traduction complète."

    "<h2>Exemple</h2>"
    "avec l'autre, conjointement"
    f"<br><br>{ICON_CHECK} miteinander"
    f"<br><br>{ICON_CROSS} nebeneinander"
)

guidance_adverbien_einander_sentences = (
    "Pour chaque question, vous recevrez une phrase allemande et sa traduction française."
    "<br><br>Il manque un adverbe dans «einander» dans la phrase allemande. Trouvez celui qui convient."

    f"<br><br>{ICON_WARN} Il n'y a qu'une seule réponse possible par question. Aucun synonyme n'est disponible pour cet exercice."
    "Lisez attentivement la traduction complète."
    
    "<h2>Exemple</h2>"
    "Wir sollten offener _____ kommunizieren, um Missverständnisse zu vermeiden."
    "<br><br><i>Nous devrions communiquer plus ouvertement les uns avec les autres pour éviter les malentendus.</i>"
    f"<br><br>{ICON_CHECK} miteinander"
    f"<br><br>{ICON_CROSS} nebeneinander"
)

guidance_adverbien_multiple_choices_english_to_german = (
    "Pour chaque question, vous verrez la traduction française d'un adjectif et de cinq adverbes allemands."
    "<br>Sélectionnez l'adverbe allemand correspondant à la traduction française"
    
    f"<br><br>{ICON_WARN} Des synonymes sont disponibles pour cet exercice. Il peut y avoir plusieurs réponses possibles."
    
    "<h2>Exemple</h2>"
    "de temps en temps, de temps en temps"
    "<br>"
    "<br>bisweilen"
    "<br>ab et zu"
    "<br>wütend"
    "<br>Unterwegs"
    "<br>zum Abschluss"
    f"<br><br>{ICON_CHECK} bisweilen"
    f"<br>{ICON_CHECK} ab et zu"
    f"<br>{ICON_CROSS} wütend"
    f"<br>{ICON_CROSS} chemins de fer"
    f"<br>{ICON_CROSS} pour un Abschluss"
)

guidance_adverbien_multiple_choices_german_to_english = (
    "Pour chaque question, vous verrez un adverbe allemand et cinq traductions française possibles."
    "<br>Sélectionnez la traduction correspondant à l'adverbe allemand."
    
    f"<br><br>{ICON_WARN} Il n'y a qu'une seule réponse possible par question. Les synonymes ne sont pas disponibles pour cet exercice."
    "Lisez attentivement la traduction complète."
    
    "<h2>Exemple</h2>"
    "wütend"
    "<br>"
    "<br>avec colère, furieusement"
    "<br>de temps en temps, occasionnellement"
    "<br>en chemin"
    "<br>pour conclure, en conclusion"
    "<br>en tout cas, au moins"
    f"<br><br>{ICON_CHECK} avec colère, furieusement"
)

guidance_adjektive_isolation = (
    "Pour chaque question, vous verrez la traduction française d'un adjectif allemand."
    "<br>Trouvez l'adjectif allemand correspondant à la traduction."

    f"<br><br>{ICON_WARN} Des synonymes sont disponibles pour cet exercice. Il peut y avoir plusieurs réponses possibles."
    f"<br><br>{ICON_WARN} N'écrivez pas plus d'une réponse, sinon votre réponse sera signalée comme fausse."
    
    "<h2>Exemple</h2>"
    "bon marché"
    f"<br><br>{ICON_CHECK} billig"
    f"<br><br>{ICON_CHECK} günstig"
    f"<br><br>{ICON_CROSS} billig, günstig"
)

guidance_adjektive_opposite = (
    "Pour chaque question, vous verrez un adjectif allemand."
    "<br>Écrivez son contraire en allemand."
    
    f"<br><br>{ICON_WARN} Des synonymes sont disponibles pour cet exercice. Il peut y avoir plusieurs réponses possibles."
    f"<br><br>{ICON_WARN} N'écrivez pas plus d'une réponse, sinon votre réponse sera signalée comme fausse."
    
    "<h2>Exemple</h2>"
    "teuer"
    f"<br><br>{ICON_CHECK} billig"
    f"<br><br>{ICON_CHECK} günstig"
    f"<br><br>{ICON_CROSS} billig, günstig"
)

guidance_adjektive_comparative = (
    "Pour chaque question, vous verrez un adjectif allemand."
    "<br>Écrivez sa forme comparative."

    "<h2>Exemple</h2>"
    "alt"
    f"<br><br>{ICON_CHECK} älter"
)

guidance_adjektive_superlative = (
    "Pour chaque question, vous verrez un adjectif allemand."
    "<br>Écrivez son superlatif."
    
    "<h2>Exemple</h2>"
    "alt"
    f"<br><br>{ICON_CHECK} am ältesten"
)

guidance_adjektive_comparison_words = (
    "Pour chaque question, vous recevrez une phrase allemande et sa traduction française"

    "<br><br>Il manque un mot de comparaison dans la phrase allemande. Trouvez celui qui convient."
    
    "<h2>Exemple</h2>"
    "Peter ist größer _____ sein Bruder."
    "<br><br><i>Peter est plus grand que son frère."
    f"<br><br>{ICON_CHECK} als"
)

guidance_adjektive_multiple_choices_english_to_german = (
    "Pour chaque question, vous verrez la traduction française d’un adjectif allemand et cinq adjectifs allemands."
    "<br>Sélectionnez l’adjectif allemand qui correspond à la traduction française"

    "<h2>Example</h2>"
    "propre (\"le sien\")"
    "<br><br>eigen"
    "<br>international"
    "<br>europäisch"
    "<br>tot"
    "<br>einzeln"
    f"<br><br>{ICON_CHECK} eigen"
)

guidance_adjektive_multiple_choices_german_to_english = (
    "Pour chaque question, vous verrez un adjectif allemand et cinq traductions française possibles."
    "<br>Sélectionnez la traduction qui correspond à l’adjectif allemand."

    "<h2>Exemple</h2>"
    "eigen"
    "<br><br>propre (\"le sien\")"
    "<br>international"
    "<br>européen"
    "<br>mort"
    "<br>célibataire"
    f"<br><br>{ICON_CHECK} own"
)

guidance_adjektivdeklinationen_isolation = (
    "Pour chaque question, une phrase allemande vous sera proposée avec un cas et un adjectif."
    
    "<br><br>Complétez la phrase avec l’adjectif décliné, en tenant compte de l’article,"
    " du genre du nom et du cas grammatical."

    "<h2>Exemple</h2>"
    "ein _____ Vater \u25CF Nominativ \u25CF nett"
    f"<br><br>{ICON_CHECK} netter"
)

guidance_adjektivdeklinationen_sentences = (
    "Pour chaque question, une phrase allemande incomplète et un adjectif vous seront proposés."
    
    "<br><br>Complétez la phrase avec l’adjectif correctement décliné, en tenant compte de l’article,"
    " du genre du nom et du cas grammatical."

    "<h2>Exemple</h2>"
    "Die _____ Kinder stellen viele Fragen. \u25CF klug"
    f"<br><br>{ICON_CHECK} klugen"
)

guidance_adjektivdeklinationen_comparative_isolation = (
    "Pour chaque question, une phrase allemande vous sera proposée avec un cas et un adjectif."
    
    "<br><br>Complétez la phrase avec l’adjectif <b>comparatif</b> décliné, en tenant compte de l’article,"
    " du genre du nom et du cas grammatical."

    "<h2>Exemple</h2>"
    "ein _____ Vater \u25CF Nominativ \u25CF nett"
    f"<br><br>{ICON_CHECK} netterer"
)

guidance_adjektivdeklinationen_comparative_sentences = (
    "Pour chaque question, une phrase allemande incomplète et un adjectif vous seront proposés."
    
    "<br><br>Complétez la phrase avec l’adjectif <b>comparatif</b> correctement décliné, en tenant compte de l’article,"
    " du genre du nom et du cas grammatical."

    "<h2>Exemple</h2>"
    "Der _____ Hund läuft im Garten. \u25CF groß"
    f"<br><br>{ICON_CHECK} größere"
)

guidance_adjektivdeklinationen_superlative_isolation = (
    "Pour chaque question, une phrase allemande vous sera proposée avec un cas et un adjectif."
    
    "<br><br>Complétez la phrase avec l’adjectif <b>superlatif</b> décliné, en tenant compte de l’article,"
    " du genre du nom et du cas grammatical."

    "<h2>Exemple</h2>"
    "der _____ Vater \u25CF Nominatif \u25CF nett"
    f"<br><br>{ICON_CHECK} netteste"
)

guidance_adjektivdeklinationen_superlative_sentences = (
    "Pour chaque question, une phrase allemande incomplète et un adjectif vous seront proposés."
    
    "<br><br>Complétez la phrase avec l’adjectif <b>superlatif</b> correctement décliné, en tenant compte de l’article,"
    " du genre du nom et du cas grammatical."

    "<h2>Exemple</h2>"
    "Die _____ Blume steht auf dem Tisch. \u25CF schön"
    f"<br><br>{ICON_CHECK} schönste"
)

guidance_verben_translation = (
    "Pour chaque question, vous verrez la traduction française d’un verbe allemand."
    "<br>Trouvez le verbe allemand qui correspond à l’ensemble de la traduction."

    f"<br><br>{ICON_WARN} Il n’y a qu’une seule réponse possible par question. Les synonymes ne sont pas acceptés pour cet exercice."
    f" Lisez attentivement toute la traduction."
    f"<br><br>{ICON_WARN} N’écrivez pas de pronom réfléchi, même si le verbe est habituellement réfléchi."

    "<h2>Exemple</h2>"
    "rendre heureux, être heureux (réfl.), attendre avec impatience (réfl.)"
    f"<br><br>{ICON_CHECK} freuen"
    f"<br><br>{ICON_CROSS} sich freuen"
)

guidance_verben_multiple_choices_english_to_german = (
    "Pour chaque question, vous verrez la traduction française d’un verbe allemand et cinq verbes allemands."
    "<br>Sélectionnez le verbe allemand qui correspond à l’ensemble de la traduction."

    f"<br><br>{ICON_WARN} Il n’y a qu’une seule réponse possible par question. Les synonymes ne sont pas acceptés pour cet exercice."
    f" Lisez attentivement toute la traduction."

    "<h2>Exemple</h2>"
    "remplacer, substituer, compenser"
    "<br><br>ersetzen"
    "<br>leiden"
    "<br>diskutieren"
    "<br>rufen"
    "<br>vorschlagen"
    f"<br><br>{ICON_CHECK} ersetzen"
)

guidance_verben_multiple_choices_german_to_english = (
    "Pour chaque question, vous verrez un verbe allemand et cinq traductions française possibles."
    "<br>Sélectionnez la traduction qui correspond au verbe allemand."

    f"<br><br>{ICON_WARN} Il n’y a qu’une seule réponse possible par question. Les synonymes ne sont pas acceptés pour cet exercice."
    f" Lisez attentivement toutes les traductions."

    "<h2>Exemple</h2>"
    "ersetzen"
    "<br><br>remplacer, substituer, compenser"
    "<br>souffrir, endurer, supporter"
    "<br>discuter, débattre"
    "<br>appeler, crier, convoquer"
    "<br>suggérer, proposer"
    f"<br><br>{ICON_CHECK} remplacer, substituer, compenser"
)

guidance_trennbare_verben_root = (
    "Pour chaque question, vous recevrez la traduction française d’un verbe allemand (séparable ou inséparable) ainsi que sa racine."
    
    "<br><br>Trouvez le verbe allemand qui correspond à la traduction et à la racine."

    f"<br><br>{ICON_WARN} Il n’y a qu’une seule réponse possible par question. Les synonymes ne sont pas acceptés pour cet exercice."
    " Lisez attentivement toute la traduction."
    f"<br><br>{ICON_WARN} N’écrivez pas de pronom réfléchi, même si le verbe est habituellement réfléchi."

    "<h2>Exemple</h2>"
    "tirer, traîner, déplacer → ziehen"
    "<br><br>s'habiller, mettre, habiller quelqu'un, attirer, tirer → _____"
    f"<br><br>{ICON_CHECK} anziehen"
)

guidance_trennbare_verben_prefix = (
    "Pour chaque question, vous recevrez la traduction française d’un verbe allemand (séparable ou inséparable) ainsi que son préfixe."
    "<br><br>Trouvez le verbe allemand qui correspond à la traduction et au préfixe."

    f"<br><br>{ICON_WARN} Il n’y a qu’une seule réponse possible par question. Les synonymes ne sont pas acceptés pour cet exercice."
    " Lisez attentivement toute la traduction."
    f"<br><br>{ICON_WARN} N’écrivez pas de pronom réfléchi, même si le verbe est habituellement réfléchi."

    "<h2>Exemple</h2>"
    "s'habiller, mettre, habiller quelqu'un, attirer, tirer \u25CF an"
    f"<br><br>{ICON_CHECK} anziehen"
)

guidance_trennbare_verben_no_help = (
    "Pour chaque question, vous recevrez la traduction française d’un verbe allemand (séparable ou inséparable)."
    "<br><br>Trouvez le verbe allemand qui correspond à l’ensemble de la traduction."

    f"<br><br>{ICON_WARN} Il n’y a qu’une seule réponse possible par question. Les synonymes ne sont pas acceptés pour cet exercice."
    " Lisez attentivement toute la traduction."
    f"<br><br>{ICON_WARN} N’écrivez pas de pronom réfléchi, même si le verbe est habituellement réfléchi."

    "<h2>Exemple</h2>"
    "s'habiller, mettre, habiller quelqu'un, attirer, tirer"
    f"<br><br>{ICON_CHECK} anziehen"
)

guidance_nomen_verben_verbindungen_nomen_isolation = (
    "Pour chaque question, vous recevrez une combination Nom-Verbe allemande incomplète et sa traduction française."
    "<br><br>Trouvez le nom allemand qui complète cette combination."

    f"<br><br>{ICON_WARN} Il peut y avoir plusieurs réponses possibles."
    f"<br><br>{ICON_WARN} N'écrivez pas plus d'une réponse, sinon votre réponse sera signalée comme fausse."
    f"<br><br>{ICON_WARN} La réponse peut nécessiter un article."

    "<h2>Exemple</h2>"
    "_____ haben"
    "<br><br><i>avoir une opinion, penser</i>"
    f"<br><br>{ICON_CHECK} eine Meinung"
    f"<br><br>{ICON_CHECK} eine Ansicht"
    f"<br><br>{ICON_CROSS} eine Meinung, eine Ansicht"
    f"<br><br>{ICON_CROSS} Meinung"
    f"<br><br>{ICON_CROSS} ein Meinung"
)

guidance_nomen_verben_verbindungen_verben_isolation = (
    "Pour chaque question, vous recevrez une combination Nom-Verbe allemande incomplète et sa traduction française."
    "<br><br>Trouvez le verb allemand qui complète cette combination."

    f"<br><br>{ICON_WARN} Il peut y avoir plusieurs réponses possibles."
    f"<br><br>{ICON_WARN} N'écrivez pas plus d'une réponse, sinon votre réponse sera signalée comme fausse."

    "<h2>Exemple</h2>"
    "eine Meinung _____"
    "<br><br><i>avoir une opinion, penser</i>"
    f"<br><br>{ICON_CHECK} haben"
    f"<br><br>{ICON_CHECK} vertreten"
    f"<br><br>{ICON_CROSS} haben, vertreten"
)

guidance_nomen_verben_verbindungen_nomen_sentences = (
    "Pour chaque question, vous recevrez une phrase allemande incomplète et sa traduction française."
    "<br><br>Trouvez le nom allemand qui complète cette phrase."

    f"<br><br>{ICON_WARN} Il peut y avoir plusieurs réponses possibles."
    f"<br><br>{ICON_WARN} N'écrivez pas plus d'une réponse, sinon votre réponse sera signalée comme fausse."
    f"<br><br>{ICON_WARN} La réponse ne nécessite PAS d'article."

    "<h2>Exemple</h2>"
    "Ich habe eine andere _____ als du."
    "<br><br><i>J’ai une opinion différente de la tienne.</i>"
    f"<br><br>{ICON_CHECK} Meinung"
    f"<br><br>{ICON_CHECK} Ansicht"
    f"<br><br>{ICON_CROSS} Meinung, Ansicht"
)

guidance_nomen_verben_verbindungen_verben_sentences = (
    "Pour chaque question, vous recevrez une phrase allemande incomplète et sa traduction française."
    "<br><br>Trouvez le verb allemand qui complète cette phrase."

    f"<br><br>{ICON_WARN} Il peut y avoir plusieurs réponses possibles."
    f"<br><br>{ICON_WARN} N'écrivez pas plus d'une réponse, sinon votre réponse sera signalée comme fausse."
    f"<br><br>{ICON_WARN} Le verbe doit être conjugué au temps et la personne correcte."

    "<h2>Exemple</h2>"
    "Sie _____ den Vorschlag, gemeinsam zu reisen."
    "<br><br><i>Elle a fait la proposition de voyager ensemble.</i>"
    f"<br><br>{ICON_CHECK} machte"
    f"<br><br>{ICON_CHECK} unterbreitete"
    f"<br><br>{ICON_CROSS} machte, unterbreitete"
    f"<br><br>{ICON_CROSS} macht"
    f"<br><br>{ICON_CROSS} machen"
)


GUIDANCE_EXERCISE_FR = {

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
        3: guidance_pronomen_isolation,
        4: guidance_pronomen_sentences,
        5: guidance_pronomen_isolation,
        6: guidance_pronomen_sentences,
        7: guidance_pronomen_sentences,
        8: guidance_pronomen_sentences,

        9: guidance_pronomen_isolation,
        10: guidance_pronomen_sentences,
        11: guidance_pronomen_replacing,
        12: guidance_pronomen_replacing,

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
        26: guidance_pronomen_sentences,

        27: guidance_pronomen_sentences,
        28: guidance_pronomen_sentences,
        29: guidance_pronomen_sentences,
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
        27: guidance_adjektivdeklinationen_comparative_isolation,
        28: guidance_adjektivdeklinationen_comparative_sentences,
        29: guidance_adjektivdeklinationen_superlative_isolation,
        30: guidance_adjektivdeklinationen_superlative_sentences,
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

    nomen_verben_verbindungen: {
        1: guidance_nomen_verben_verbindungen_nomen_isolation,
        2: guidance_nomen_verben_verbindungen_verben_isolation,
        3: guidance_nomen_verben_verbindungen_nomen_sentences,
        4: guidance_nomen_verben_verbindungen_verben_sentences,

        5: guidance_nomen_verben_verbindungen_nomen_isolation,
        6: guidance_nomen_verben_verbindungen_verben_isolation,
        7: guidance_nomen_verben_verbindungen_nomen_sentences,
        8: guidance_nomen_verben_verbindungen_verben_sentences,
    }

}
