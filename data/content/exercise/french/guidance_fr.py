from data.data_processing.exercises import isolation, context, synonym, multiple_choice_native, multiple_choice_target, \
    antonym, prompt
from data.data_processing.units import (
    praepositionen, praepositionen_verben, praepositionen_adjektive, praepositionen_nomen, pronominaladverbien,
    artikel, pronomen, konnektoren, fragen, adverbien, adjektive, komparativ_superlativ, adjektivdeklinationen, verben,
    trennbare_verben, nomen_verben_verbindungen,
    nomen_verben_wortstaemme, adjektive_verben_wortstaemme, adjektive_nomen_wortstaemme,
    praepositionen_artikel, verben_artikel, wortstellung, genus_regeln, genus, plural,
    adjektive_konjunktionen, praesens, partizip_II, praeteritum, imperativ, konjunktiv_II,
    konjunktiv_I, partizip_I,
    zahlen, alpha,
)

from webapp.style.icons import ICON_CHECK, ICON_CROSS, ICON_WARN

GUIDANCE_UNIT_FR = {
    alpha:
        "Pour chaque question, une conjonction allemande, sa traduction en français et sa catégorie grammaticale "
        " (conjonction de coordination, conjonction de subordination, adverbe, conjonction corrélative) seront présentés."
        "<br><br>Écrivez une phrase en allemand en utilisant cette conjonction."
    
        f"<br><br> {ICON_WARN} Tenez compte de la catégorie grammaticale de la conjonction."
        f" La proposition contenant la conjonction doit respecter l'ordre correct des mots."
        f"<br><br> {ICON_WARN} La phrase en allemand doit être cohérente."
        f"<br><br> {ICON_WARN} Les erreurs secondaires, telles que les cas et les fautes d'orthographe,"
        f" sont acceptables tant que la phrase reste compréhensible."
        f"<br><br> {ICON_WARN} L'évaluation, la correction et les commentaires sont fournis par un modèle de langage (LLM)."
        f" Les modèles de langage peuvent commettre des erreurs. Vérifiez les informations importantes."
    
        "<h2>Exemples</h2>"
        f"deshalb"
        f"<br><br><i>pour cette raison, à cause de cela \u25CF Adverbe</i>"
        f"<br><br> &nbsp; {ICON_CHECK} Ich habe Durst, deshalb trinke ich ein Glas Wasser."
        f"<br><br> &nbsp; {ICON_CROSS} Ich habe Durst, deshalb ich trinke ein Glas Wasser. (L'ordre des mots est incorrect)"
        f"<br><br> &nbsp; {ICON_CHECK} Ich habe Durst, deshalb trinke ich eine Glas Wasser. (Erreur acceptable)"
        f"<br><br> &nbsp; {ICON_CROSS} Ich trinke ein Glas Wasser, deshalb habe ich Durst. (La phrase est incohérente)"
,

    praepositionen_artikel:
        "Pour chaque question, une phrase allemande incomplète, sa traduction en français, "
        "une préposition et un article ou un pronom seront présentés."

        "<br><br>Complétez la phrase allemande avec la préposition et l’article ou le pronom appropriés."

        f"<br><br>➡️ Si vous avez besoin d'aide pour déterminer le genre du nom, cliquez sur le bouton m/f/n/pl."

        "<h2>Exemple</h2>"
        "Ein Zettel klebt _____ Schrank. \u25CF an \u25CF der/die/das"
        "<br><br><i>Ein Zettel klebt am Schrank.</i>"
        f"<br><br> &nbsp; {ICON_CHECK} am"
        f"<br><br> &nbsp; {ICON_CHECK} an dem"
        f"<br><br> &nbsp; {ICON_CROSS} dem"
        f"<br><br> &nbsp; {ICON_CROSS} an"
    ,

    verben_artikel:
        "Pour chaque question, une phrase allemande incomplète, sa traduction en français et un article "
        "ou un pronom seront présentés."

        "<br><br>Complétez la phrase allemande avec l’article ou le pronom approprié."

        f"<br><br>➡️ Si vous avez besoin d'aide pour déterminer le genre du nom, cliquez sur le bouton m/f/n/pl."

        "<h2>Exemples</h2>"
        "Ich danke _____ für deine Hilfe. \u25CF du"
        "<br><br><i>Je te remercie pour ton aide.</i>"
        f"<br><br> &nbsp; {ICON_CHECK} dir"
        f"<br><br> &nbsp; {ICON_CROSS} du"
        f"<br><br> &nbsp; {ICON_CROSS} dich"

        "<br><br>Ich trinke _____ Kaffee. \u25CF ein"
        "<br><br><i>Je bois un café.</i>"
        f"<br><br> &nbsp; {ICON_CHECK} einen"
        f"<br><br> &nbsp; {ICON_CROSS} ein"
        f"<br><br> &nbsp; {ICON_CROSS} eine"
        f"<br><br> &nbsp; {ICON_CROSS} den"
    ,

    wortstellung:
        "Pour chaque question, une phrase en français et une série de mots en allemand seront présentées."
        "<br><br>Construisez une phrase allemande grammaticalement correcte qui traduit la phrase française"
        " et respecte les éventuelles indications."

        f"<br><br> {ICON_WARN} Tous les mots proposés doivent être utilisés."
        f"<br><br> {ICON_WARN} Il peut y avoir plusieurs réponses possibles."
        f"<br><br> {ICON_WARN} Le premier mot ou groupe formant la phrase en allemand peut être indiqué."
        f"<br><br> {ICON_WARN} Dans les propositions principales déclaratives, en l'absence d'indication contraire, commencez par le sujet."

        "<h2>Exemples</h2>"
        "<i>Je prends mes gants</i>"
        "<br><br>nehme Handschuhe ich meine"
        f"<br><br> &nbsp; {ICON_CHECK} ich nehme meine Handschuhe"

        "<br><br><br><i>Le soir je regarde un film.</i>"
        "<br><br>En première position : expression temporelle"
        "<br><br>sehe am Film ich Abend einen"
        f"<br><br> &nbsp; {ICON_CHECK} Am Abend sehe ich einen Film."
        f"<br><br> &nbsp; {ICON_CROSS} Ich sehe am Abend einen Film."
        f" (ne respecte pas l'indication du mot en première position)"

        "<br><br><br><i>Il doit travailler aujourd’hui.</i>"
        "<br><br>arbeiten er heute muss"
        f"<br><br> &nbsp; {ICON_CHECK} Er muss heute arbeiten."
        f"<br><br> &nbsp; {ICON_CROSS} Heute muss er arbeiten."
        f" (à défaut d'indication contraire, le premier mot doit être le sujet)"
    ,

    genus_regeln:
        "Pour chaque question, un nom allemand et sa traduction en français seront présentés."
        "<br><br>Donnez l’article défini (Der, Die ou Das) correspondant au nom."

        "<br><br>→ Un guide expliquant le genre des noms communs est disponible (en anglais) "
        "<a href=\"https://sieversstudyhall.substack.com/p/genders-of-german-noun-from-a1-to\" target=\"_blank\">ici</a>."

        f"<br><br> {ICON_WARN} Il n’y a qu’une seule bonne réponse par question."

        "<h2>Exemple</h2>"
        "_____ Abend"
        "<br><br><i>Le soir</i>"
        f"<br><br> &nbsp; {ICON_CHECK} Der"
        f"<br><br> &nbsp; {ICON_CHECK} der"
    ,

    genus:
        "Pour chaque question, un nom allemand et sa traduction en français seront présentés."
        "<br><br>Donnez l’article défini (Der, Die ou Das) correspondant au nom."

        "<br><br>→ Un guide expliquant le genre des noms communs est disponible (en anglais) "
        "<a href=\"https://sieversstudyhall.substack.com/p/genders-of-german-noun-from-a1-to\" target=\"_blank\">ici</a>."

        f"<br><br> {ICON_WARN} Il n’y a qu’une seule bonne réponse par question."

        "<h2>Exemple</h2>"
        "_____ Abend"
        "<br><br><i>Le soir</i>"
        f"<br><br> &nbsp; {ICON_CHECK} Der"
        f"<br><br> &nbsp; {ICON_CHECK} der"
    ,

    plural:
        "Pour chaque question, un nom commun allemand et sa traduction en français seront présentés."
        "<br><br>Trouvez la forme plurielle de ce nom."

        f"<br><br> {ICON_WARN} Il n'y a qu'une seule bonne réponse par question."

        "<h2>Exemple</h2>"
        "Singulier : die Stunde (<i>l'heure</i>)"
        "<br><br>Pluriel : die _____"
        f"<br><br> &nbsp; {ICON_CHECK} Stunden"
        f"<br><br> &nbsp; {ICON_CHECK} stunden"
        f"<br><br> &nbsp; {ICON_CROSS} Stunde"
    ,

    adjektive_konjunktionen:
        "Pour chaque question, une phrase allemande et sa traduction française seront présentées."

        "<br><br>Il manque une mot dans la phrase allemande. Trouvez celui qui convient."

        "<h2>Exemple</h2>"
        "Peter ist größer _____ sein Bruder."
        "<br><br><i>Peter est plus grand que son frère.</i>"
        f"<br><br> &nbsp; {ICON_CHECK} als"
    ,

    praesens:
        "Pour chaque question, un verbe allemand et un pronom personnel seront présentés."
        "<br>Conjuguez le verbe au présent pour ce pronom."

        f"<br><br> {ICON_WARN} N’écrivez pas le pronom personnel, sinon votre réponse sera considérée comme incorrecte."
        f"<br><br> {ICON_WARN} La réponse peut nécessiter un pronom réfléchi si le verbe est toujours réfléchi."

        "<h2>Exemples</h2>"
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
        "Pour chaque question, un verbe allemand sera présenté."
        "<br>Indiquez le Partizip II (participe passé) du verbe donné."

        f"<br><br> {ICON_WARN} N’écrivez pas d’auxiliaire, sinon votre réponse sera considérée comme incorrecte."
        f"<br><br> {ICON_WARN} La réponse peut nécessiter un pronom réfléchi si le verbe est toujours réfléchi."

        "<h2>Exemples</h2>"
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
        "Pour chaque question, un verbe allemand sera présenté."
        "<br>Conjuguez le verbe au Präteritum (prétérit) à la personne indiquée."

        f"<br><br> {ICON_WARN} N’écrivez pas le pronom personnel, sinon votre réponse sera considérée comme incorrecte."
        f"<br><br> {ICON_WARN} La réponse peut nécessiter un pronom réfléchi si le verbe est toujours réfléchi."

        "<h2>Exemples</h2>"
        "erinnern"
        f"<br><br> &nbsp; {ICON_CHECK} erinnerte"
        f"<br><br> &nbsp; {ICON_CHECK} erinnerte sich"
        f"<br><br> &nbsp; {ICON_CROSS} er erinnerte"

        "<br><br>sich freuen"
        f"<br><br> &nbsp; {ICON_CHECK} freute sich"
        f"<br><br> &nbsp; {ICON_CROSS} freute"
        f"<br><br> &nbsp; {ICON_CROSS} er freute sich"
    ,

    imperativ:
        "Pour chaque question, un verbe allemand et un pronom personnel seront présentés."
        "<br>Conjuguez le verbe à l’impératif pour ce pronom."

        f"<br><br> {ICON_WARN} Écrivez le pronom personnel uniquement pour l'impératif de politesse avec Sie."
        f"<br><br> {ICON_WARN} La réponse peut nécessiter un pronom réfléchi si le verbe est toujours réfléchi."

        "<h2>Exemple</h2>"
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
        "Pour chaque question, un verbe allemand et un pronom personnel seront présentés."
        "<br>Conjuguez le verbe au Konjunktiv II pour ce pronom."

        f"<br><br> {ICON_WARN} N’écrivez pas le pronom personnel, sinon votre réponse sera considérée comme incorrecte."

        "<h2>Exemples</h2>"
        "sein \u25CF Du"
        f"<br><br> &nbsp; {ICON_CHECK} wärest"
        f"<br><br> &nbsp; {ICON_CROSS} Du wärest"

        "<br><br>geben \u25CF du"
        f"<br><br> &nbsp; {ICON_CHECK} gäbest"
        f"<br><br> &nbsp; {ICON_CHECK} gäbst"
        f"<br><br> &nbsp; {ICON_CROSS} würdest geben"
    ,

    konjunktiv_I:
        "Pour chaque question, un verbe allemand et un pronom personnel seront présentés."
        "<br>Conjuguez le verbe au Konjunktiv I pour ce pronom."

        f"<br><br> {ICON_WARN} N’écrivez pas le pronom personnel, sinon votre réponse sera considérée comme incorrecte."

        "<h2>Exemple</h2>"
        "sein \u25CF Du"
        f"<br><br> &nbsp; {ICON_CHECK} seiest"
        f"<br><br> &nbsp; {ICON_CROSS} Du seiest"
    ,

    partizip_I:
        "Pour chaque question, un verbe allemand sera présenté."
        "<br>Indiquez le Partizip I (participe présent) du verbe donné."

        f"<br><br> {ICON_WARN} La réponse peut nécessiter un pronom réfléchi si le verbe est toujours réfléchi."

        "<h2>Exemple</h2>"
        "sich freuen"
        f"<br><br> &nbsp; {ICON_CHECK} sich freuend"
        f"<br><br> &nbsp; {ICON_CROSS} freuend"
    ,
}

guidance_praepositionen_isolation = (
    "Pour chaque question, la traduction française d'une préposition allemande sera présentée."
    "<br><br>Trouvez la préposition allemande qui convient."

    f"<br><br> {ICON_WARN} Des synonymes sont disponibles pour cet exercice. Il peut y avoir plusieurs réponses possibles."
    f"<br><br> {ICON_WARN} N'écrivez pas plus d'une réponse, sinon votre réponse sera signalée comme fausse."

    "<h2>Exemple</h2>"
    "à cause de, dû à"
    f"<br><br> &nbsp; {ICON_CHECK} wegen"
    f"<br><br> &nbsp; {ICON_CHECK} aufgrund"
    f"<br><br> &nbsp; {ICON_CROSS} wegen, aufgrund"
)

guidance_praepositionen_sentences = (
    "Pour chaque question, une phrase allemande incomplète et sa traduction française seront présentées."
    "<br><br>Complétez la phrase allemande avec la préposition qui convient."
    
    f"<br><br> {ICON_WARN} Des synonymes sont disponibles pour cet exercice. Il peut y avoir plusieurs réponses possibles."
    f"<br><br> {ICON_WARN} N'écrivez pas plus d'une réponse, sinon votre réponse sera signalée comme fausse."
    f"<br><br> {ICON_WARN} La bonne réponse peut être l'absence de préposition. Dans ce cas, laissez le champ de saisie vide."
    f"<br><br> {ICON_WARN} La bonne réponse peut inclure un article. Dans ce cas, la forme"
    f" contractée (am, ans, vom, zur etc.) comme la forme développée (an dem etc.) sont acceptées."
    
    "<h2>Exemples</h2>"
    "Ich habe _____ Montag Deutschunterricht."
    "<br><br><i>J'ai un cours d'allemand lundi.</i>"
    f"<br><br> &nbsp; {ICON_CHECK} am"
    f"<br><br> &nbsp; {ICON_CHECK} an dem"
    f"<br><br> &nbsp; {ICON_CROSS} an"

    "<br><br>Ich trinke eine Tasse _____ Kaffee."
    "<br><br><i>Je bois une tasse de café.</i>"
    f"<br><br> &nbsp; {ICON_CHECK} "
    f"<br><br> &nbsp; {ICON_CROSS} von"
)

guidance_praepositionen_synonyms = (
    "Pour chaque question, une préposition allemande sera présentée."
    "<br><br>Trouvez un synonyme de cette préposition."

    f"<br><br> {ICON_WARN} N'écrivez pas plus d'un synonyme, sinon votre réponse sera considérée comme fausse."

    "<h2>Exemple</h2>"
    "wegen"
    f"<br><br> &nbsp; {ICON_CHECK} aufgrund"
    f"<br><br> &nbsp; {ICON_CHECK} auf Grund"
    f"<br><br> &nbsp; {ICON_CROSS} aufgrund, auf Grund"
)

guidance_praepositionen_antonym = (
    "Pour chaque question, une préposition allemande sera présentée."
    "<br>Trouvez un antonyme de cette préposition."

    f"<br><br> {ICON_WARN} Des synonymes sont disponibles pour cet exercice. Il peut y avoir plusieurs réponses possibles."
    f"<br><br> {ICON_WARN} N'écrivez pas plus d'une réponse, sinon votre réponse sera signalée comme fausse."

    "<h2>Exemple</h2>"
    "trotz"
    f"<br><br> &nbsp; {ICON_CHECK} aufgrund"
    f"<br><br> &nbsp; {ICON_CHECK} auf Grund"
    f"<br><br> &nbsp; {ICON_CROSS} aufgrund, auf Grund"
)

guidance_praepositionen_prompt = (
    "Pour chaque question, une préposition allemande et une de ses fonctions seront présentées."
    "<br><br>Rédigez une phrase en allemand en utilisant cette préposition dans cette fonction précise."

    f"<br><br> {ICON_WARN} La phrase allemande doit respecter l'ordre des mots correct."
    f"<br><br> {ICON_WARN} La phrase allemande doit être cohérente."
    f"<br><br> {ICON_WARN} Les erreurs secondaires, telles que les erreurs de conjugaison ou d'orthographe,"
    f" sont acceptées tant que la phrase reste compréhensible et cohérente."
    f"<br><br> {ICON_WARN} L'évaluation, les corrections et les retours sont générés par un grand modèle de langage (LLM)."
    f" Les LLM peuvent faire des erreurs, inventer des informations ou fournir des conseils non vérifiés."
    f" Veuillez vérifier les informations importantes."
    f"<br><br> {ICON_WARN} Ne fournissez aucune information personnelle telle que votre nom de famille,"
    f" votre date de naissance, votre adresse précise ou votre numéro d'identité."

    "<h2>Exemple</h2>"
    f"to indicate a specific time → um + Acc."
    f"<br><br> &nbsp; {ICON_CHECK} Um 4 Uhr musst du gehen."
    f"<br><br> &nbsp; {ICON_CROSS} Um 4 Uhr du musst gehen. (Ordre des mots incorrect)"
    f"<br><br> &nbsp; {ICON_CHECK} Um 4 Uhr musst ich gehen. (Erreur de conjugaison acceptable)"
    f"<br><br> &nbsp; {ICON_CROSS} Der Hund rennt um den Block. (Phrase correcte mais n'utilisant pas la fonction de <i>um</i> présentée.)"
)

guidance_praepositionen_verben_isolation = (
    "Pour chaque question, une paire verbe-préposition allemande incomplète et sa traduction française seront présentées."
    "<br><br>Complétez le couple verbe-préposition avec la préposition qui convient."
    
    f"<br><br> {ICON_WARN} Il n'y a qu'une seule bonne réponse par question."
    
    "<h2>Exemple</h2>"
    "penser à = denken _____"
    f"<br><br> &nbsp; {ICON_CHECK} an"
)

guidance_praepositionen_verben_sentences = (
    "Pour chaque question, une phrase allemande incomplète et sa traduction française seront présentées."
    "<br><br>Complétez la phrase allemande avec la préposition qui convient."
    
    f"<br><br> {ICON_WARN} Il n'y a qu'une seule bonne réponse par question."
    
    "<h2>Exemple</h2>"
    "Ich denke _____ meine Mutter."
    "<br><br><i>Je pense à ma mère.</i>"
    f"<br><br> &nbsp; {ICON_CHECK} an"
)

guidance_praepositionen_adjektive_isolation = (
    "Pour chaque question, une paire adjectif-préposition allemande incomplète et sa traduction française seront présentées."

    "<br><br>Complétez le couple adjectif-préposition avec la préposition qui convient."
    
    f"<br><br> {ICON_WARN} Il n'y a qu'une seule bonne réponse par question."
    
    "<h2>Exemple</h2>"
    "curieux de = neugierig _____"
    f"<br><br> &nbsp; {ICON_CHECK} auf"
)

guidance_praepositionen_adjektive_sentences = (
    "Pour chaque question, une phrase allemande incomplète et sa traduction française seront présentées."
    "<br><br>Complétez la phrase allemande avec la préposition qui convient."
    
    f"<br><br> {ICON_WARN} Il n'y a qu'une seule bonne réponse par question."
    
    "<h2>Exemple</h2>"
    "Ich bin neugierig _____ die Ergebnisse der Untersuchung."
    "<br><br><i>Je suis curieux de connaître les résultats de l'enquête.</i>"
    f"<br><br> &nbsp; {ICON_CHECK} auf"
)

guidance_praepositionen_nomen_isolation = (
    "Pour chaque question, une paire nom-préposition allemande incomplète et sa traduction française seront présentées."
    "<br><br>Complétez le couple nom-préposition avec la préposition qui convient."
    
    f"<br><br> {ICON_WARN} Il n'y a qu'une seule bonne réponse par question."
    
    "<h2>Exemple</h2>"
    "la fierté de = der Stolz _____"
    f"<br><br> &nbsp; {ICON_CHECK} auf"
)

guidance_praepositionen_nomen_sentences = (
    "Pour chaque question, une phrase allemande incomplète et sa traduction française seront présentées."
    "<br><br>Complétez la phrase allemande avec la préposition qui convient."
    
    f"<br><br> {ICON_WARN} Il n'y a qu'une seule bonne réponse par question."
    
    "<h2>Exemple</h2>"
    "Er zeigte Stolz _____ sein Team nach dem Sieg."
    "<br><br><i>Il a montré sa fierté envers son équipe après la victoire.</i>"
    f"<br><br> &nbsp; {ICON_CHECK} auf"
)

guidance_pronominaladverbien_dawort = (
    "Pour chaque question, une phrase allemande incomplète et sa traduction française seront présentées."
    "<br><br>Complétez la phrase allemande avec l'adverbe pronominal en Da- qui convient."

    f"<br><br> {ICON_WARN} Il n'y a qu'une seule bonne réponse par question."

    "<h2>Exemple</h2>"
    "Ich habe lange gearbeitet und wurde _____ gelobt."
    f"<br><br>J’ai travaillé longtemps et j’ai été félicité pour cela."
    f"<br><br> &nbsp; {ICON_CHECK} dafür"
)

guidance_pronominaladverbien_wowort = (
    "Pour chaque question, une phrase allemande incomplète et sa traduction française seront présentées."
    "<br><br>Complétez la phrase allemande avec l'adverbe pronominal en Wo- qui convient."

    f"<br><br> {ICON_WARN} Il n'y a qu'une seule bonne réponse par question."

    "<h2>Exemple</h2>"
    "_____ denkst du?"
    "<br><br><i>À quoi pensez-vous?</i>"
    f"<br><br> &nbsp; {ICON_CHECK} Woran"
)

guidance_artikel_isolation = (
    "Pour chaque question, un article en allemand, ainsi qu'un genre et un cas seront présentés."

    "<br><br>Donnez l'article correspondant au genre et au cas."
    
    "<h2>Exemple</h2>"
    "der/die/das \u25CF Féminin, Nominatif"
    f"<br><br> &nbsp; {ICON_CHECK} die"
)

guidance_artikel_sentences = (
    "Pour chaque question, une phrase en allemand et sa traduction française seront présentées."
    "<br><br>Il manque un article dans la phrase allemande. Trouvez celui qui convient, en tenant compte du cas et du genre."

    f"<br><br>➡️ Si vous avez besoin d'aide pour le genre du nom commun, cliquez sur le bouton m/f/n/pl."

    "<h2>Exemple</h2>"
    "_____ Woche hat sieben Tage."
    "<br><br><i>La semaine compte sept jours.</i>"
    f"<br><br> &nbsp; {ICON_CHECK} Die"
)

guidance_pronomen_isolation = (
    "Pour chaque question, un pronom ainsi qu'un cas grammatical seront présentés."
    "<br><br>Donnez le pronom allemand correspondant au cas grammatical."

    "<h2>Exemple</h2>"
    "1re personne du singulier \u25CF Nominatif"
    f"<br><br> &nbsp; {ICON_CHECK} Ich"
)

guidance_pronomen_sentences = (
    "Pour chaque question, une phrase en allemand et sa traduction française seront présentées."
    "<br><br>Il manque un pronom dans la phrase allemande. Trouvez celui qui convient, en tenant compte du cas grammatical"
    " (et du genre, le cas échéant)."

    "<h2>Exemple</h2>"
    "Heute bin _____ sehr müde."
    "<br><br><i>Aujourd'hui, je suis très fatigué.</i>"
    f"<br><br> &nbsp; {ICON_CHECK} ich"
)

guidance_pronomen_replacing = (
    "Pour chaque question, une phrase en allemand, sa traduction française et un objet seront présentés."
    "<br><br>Remplacez l'objet avec le pronom qui convient, en tenant compte du cas grammatical (et du genre, le cas échéant)."

    "<h2>Exemple</h2>"
    "Wir besuchen die Schule jeden Tag. \u25CF die Schule"
    "<br><br><i>Nous visitons l'école tous les jours.</i>"
    f"<br><br> &nbsp; {ICON_CHECK} sie"
    f"<br><br> &nbsp; {ICON_CROSS} es"
    f"<br><br> &nbsp; {ICON_CROSS} ihr"
)

guidance_pronomen_relative_isolation = (
    "Pour chaque question, un genre et un cas grammatical seront présentés."
    "<br><br>Donnez le pronom relatif allemand correspondant au genre et au cas grammatical."

    "<h2>Exemple</h2>"
    "Féminin \u25CF Nominatif"
    f"<br><br> &nbsp; {ICON_CHECK} die"
)

guidance_pronomen_relative_sentences = (
    "Pour chaque question, une phrase en allemand et sa traduction française seront présentées."
    "<br><br>Il manque un pronom relatif dans la phrase allemande. Trouvez celui qui convient,"
    " en tenant compte du cas grammatical et du genre."

    "<h2>Exemple</h2>"
    "Der Mann, _____ hier steht, ist mein Lehrer."
    "<br><br><i>L’homme qui se tient ici est mon professeur.</i>"
    f"<br><br> &nbsp; {ICON_CHECK} der"
)

guidance_konnektoren_isolation = (
    "Pour chaque question, la traduction française d'un connecteur allemand et sa catégorie grammaticale "
    " (conjonction de coordination, conjonction de subordination, adverbe, conjonction corrélative) seront présentées."
    "<br><br>Trouvez celui correspondant à cette traduction et à cette catégorie grammaticale."

    f"<br><br> {ICON_WARN} Des synonymes sont disponibles pour cet exercice. Il peut y avoir plusieurs réponses possibles."
    f"<br><br> {ICON_WARN} Tenez compte de la catégorie grammaticale du connecteur."
    f" Si votre réponse est une traduction littérale correcte, "
    f" mais que la catégorie grammaticale est incorrecte, votre réponse sera signalée comme fausse."
    f"<br><br> {ICON_WARN} Ne donnez pas plusieurs réponses, sinon votre réponse sera considérée comme fausse."
    f"<br><br> {ICON_WARN} Avec une conjonction de coordination, l'ordre des mots est le même que dans la proposition principale. "
    f"<br><br> {ICON_WARN} Avec une conjonction de subordination, le verbe se place à la fin de la proposition."
    f"<br><br> {ICON_WARN} Avec un adverbe, le verbe vient en deuxième position."
    f"<br><br> {ICON_WARN} Une conjonction corrélative comporte deux parties qui ne sont pas directement contiguës."

    "<h2>Exemple</h2>"
    "parce que, car \u25CF Conjonction de coordination"
    f"<br><br> &nbsp; {ICON_CHECK} denn"
    f"<br><br> &nbsp; {ICON_CROSS} weil (C'est une conjonction de subordination, pas une conjonction de coordination)"
    f"<br><br>"
    
    "pour cette raison, à cause de cela \u25CF Adverbe"
    f"<br><br> &nbsp; {ICON_CHECK} deshalb"
    f"<br><br> &nbsp; {ICON_CHECK} deswegen"
    f"<br><br> &nbsp; {ICON_CROSS} deshalb, deswegen"
    f"<br><br> &nbsp; {ICON_CROSS} weshalb (C'est une conjonction de subordination, pas un adverbe)"
    f"<br><br>"
    
    "à la fois ... et \u25CF Conjonction corrélative"
    f"<br><br> &nbsp; {ICON_CHECK} sowohl als auch"
    f"<br><br> &nbsp; {ICON_CHECK} sowohl ... als auch"
    f"<br><br> &nbsp; {ICON_CROSS} sowie (C'est une conjonction de coordination, pas une conjonction corrélative)"
)

guidance_konnektoren_sentences = (
    "Pour chaque question, une phrase en allemand et sa traduction française seront présentées."
    "<br><br>Il manque un connecteur dans la phrase allemande. Trouvez celui qui convient."

    f"<br><br> {ICON_WARN} Des synonymes sont disponibles pour cet exercice. Il peut y avoir plusieurs réponses possibles."
    f"<br><br> {ICON_WARN} N'écrivez pas plus d'une réponse, sinon votre réponse sera considérée comme fausse."

    "<h2>Exemple</h2>"
    "Es regnet stark, _____ nehme ich meinen Regenschirm."
    "<br><br><i>Il pleut fort, donc je prends mon parapluie.</i>"
    f"<br><br> &nbsp; {ICON_CHECK} deshalb"
    f"<br><br> &nbsp; {ICON_CHECK} deswegen"
    f"<br><br> &nbsp; {ICON_CROSS} deshalb, deswegen"
    f"<br><br> &nbsp; {ICON_CROSS} weshalb"
)

guidance_konnektoren_synonyms = (
    "Pour chaque question, un connecteur allemand et une phrase d'exemple seront présentés."
    "<br><br>Trouvez un synonyme du connecteur qui convient dans le même contexte."

    f"<br><br> {ICON_WARN} N'écrivez pas plus d'un synonyme, sinon votre réponse sera considérée comme fausse."

    "<h2>Exemple</h2>"
    "darum \u25CF Adverbe"
    f"<br><br> &nbsp; {ICON_CHECK} deshalb"
    f"<br><br> &nbsp; {ICON_CHECK} deswegen"
    f"<br><br> &nbsp; {ICON_CROSS} deshalb, deswegen"
    f"<br><br> &nbsp; {ICON_CROSS} darum"
    f"<br><br> &nbsp; {ICON_CROSS} weshalb"
)

guidance_konnektoren_prompt = (
    "Pour chaque question, un connecteur allemand, sa traduction française et sa catégorie grammaticale "
    "(conjonction de coordination, conjonction de subordination, adverbe, conjonction corrélative) seront présentés."
    "<br><br>Écrivez une phrase en allemand utilisant ce connecteur."

    f"<br><br> {ICON_WARN} Tenez compte de la catégorie grammaticale du connecteur. La proposition contenant le connecteur "
    f"doit respecter l'ordre des mots correspondant."
    f"<br><br> {ICON_WARN} La phrase allemande doit être cohérente."
    f"<br><br> {ICON_WARN} Les erreurs secondaires, telles que les erreurs de cas ou d'orthographe,"
    f" sont acceptées tant que la phrase reste compréhensible et cohérente."
    f"<br><br> {ICON_WARN} L'évaluation, les corrections et les retours sont générés par un grand modèle de langage (LLM)."
    f" Les LLM peuvent faire des erreurs, inventer des informations ou fournir des conseils non vérifiés."
    f" Veuillez vérifier les informations importantes."
    f"<br><br> {ICON_WARN} Ne fournissez aucune information personnelle telle que votre nom de famille,"
    f" votre date de naissance, votre adresse précise ou votre numéro d'identité."

    "<h2>Exemples</h2>"
    f"deshalb"
    f"<br><br><i>donc, c'est pourquoi, pour cette raison ● Adverbe</i>"
    f"<br><br> &nbsp; {ICON_CHECK} Ich habe Durst, deshalb trinke ich ein Glas Wasser."
    f"<br><br> &nbsp; {ICON_CROSS} Ich habe Durst, deshalb ich trinke ein Glas Wasser. (Ordre des mots incorrect)"
    f"<br><br> &nbsp; {ICON_CHECK} Ich habe Durst, deshalb trinke ich eine Glas Wasser. (Erreur acceptable)"
    f"<br><br> &nbsp; {ICON_CROSS} Ich trinke ein Glas Wasser, deshalb habe ich Durst. (Phrase incohérente)"
)

guidance_fragen_isolation = (
    "Pour chaque question, la traduction française d'un mot interrogatif allemand sera présentée."
    "<br><br>Trouvez le mot interrogatif allemand correspondant à cette traduction."
    
    f"<br><br> {ICON_WARN} Des synonymes sont disponibles pour cet exercice. Il peut y avoir plusieurs réponses possibles."
    f"<br><br> {ICON_WARN} N'écrivez pas plus d'une réponse, sinon votre réponse sera considérée comme fausse."

    "<h2>Exemple</h2>"
    "Pourquoi"
    f"<br><br> &nbsp; {ICON_CHECK} Warum"
    f"<br><br> &nbsp; {ICON_CHECK} Weshalb"
    f"<br><br> &nbsp; {ICON_CROSS} Warum, Weshalb"
)

guidance_fragen_sentences = (
    "Pour chaque question, une phrase allemande et sa traduction française seront présentées."

    "<br><br>Il manque un mot interrogatif dans la phrase allemande. Trouvez celui qui convient."
    
    f"<br><br> {ICON_WARN} Des synonymes sont disponibles pour cet exercice. Il peut y avoir plusieurs réponses possibles."
    f"<br><br> {ICON_WARN} N'écrivez pas plus d'une réponse, sinon votre réponse sera signalée comme fausse."
    
    f"<br><br>➡️ Si vous avez besoin d'aide pour le genre du nom commun, cliquez sur le bouton m/f/n/pl."

    "<h2>Exemple</h2>"
    "_____ lernst du Deutsch?"
    "<br><br><i>Pourquoi apprenez-vous l'allemand?</i>"
    f"<br><br> &nbsp; {ICON_CHECK} Warum"
    f"<br><br> &nbsp; {ICON_CHECK} Weshalb"
    f"<br><br> &nbsp; {ICON_CROSS} Warum, Weshalb"
)

guidance_fragen_prompt = (
    "Pour chaque question, un mot interrogatif allemand et sa traduction française seront présentés."
    "<br><br>Écrivez une phrase en allemand utilisant ce mot interrogatif."

    f"<br><br> {ICON_WARN} La phrase allemande doit respecter l'ordre des mots correct."
    f"<br><br> {ICON_WARN} La phrase allemande doit être cohérente."
    f"<br><br> {ICON_WARN} Les erreurs secondaires, telles que les erreurs de cas ou d'orthographe,"
    f" sont acceptées tant que la phrase reste compréhensible et cohérente."
    f"<br><br> {ICON_WARN} L'évaluation, les corrections et les retours sont générés par un grand modèle de langage (LLM)."
    f" Les LLM peuvent faire des erreurs, inventer des informations ou fournir des conseils non vérifiés."
    f" Veuillez vérifier les informations importantes."
    f"<br><br> {ICON_WARN} Ne fournissez aucune information personnelle telle que votre nom de famille,"
    f" votre date de naissance, votre adresse précise ou votre numéro d'identité."

    "<h2>Exemples</h2>"
    f"Wo"
    f"<br><br><i>Où</i>"
    f"<br><br> &nbsp; {ICON_CHECK} Wo ist der Stuhl?"
    f"<br><br> &nbsp; {ICON_CROSS} Wo der Stuhl ist? (Ordre des mots incorrect)"
    f"<br><br> &nbsp; {ICON_CHECK} Wo ist das Stuhl? (Erreur acceptable)"
    f"<br><br> &nbsp; {ICON_CROSS} Wer ist der Stuhl? (Phrase incohérente)"
)

guidance_adverbien_isolation = (
    "Pour chaque question, la traduction française d'un adverbe allemand sera présentée."

    "<br><br>Trouvez l'adverbe allemand correspondant à cette traduction."
    
    f"<br><br> {ICON_WARN} Des synonymes sont disponibles pour cet exercice. Il peut y avoir plusieurs réponses possibles."
    f"<br><br> {ICON_WARN} N'écrivez pas plus d'une réponse, sinon votre réponse sera signalée comme fausse."
    
    "<h2>Exemple</h2>"
    "presque"
    f"<br><br> &nbsp; {ICON_CHECK} fast"
    f"<br><br> &nbsp; {ICON_CHECK} nahezu"
    f"<br><br> &nbsp; {ICON_CROSS} fast, nahezu"
)

guidance_adverbien_sentences = (
    "Pour chaque question, une phrase allemande et sa traduction française seront présentées."
    "<br><br>Il manque un adverbe dans la phrase allemande. Trouvez celui qui convient."

    f"<br><br> {ICON_WARN} Des synonymes sont disponibles pour cet exercice. Il peut y avoir plusieurs réponses possibles."
    f"<br><br> {ICON_WARN} N'écrivez pas plus d'une réponse, sinon votre réponse sera signalée comme fausse."
    
    "<h2>Exemple</h2>"
    "Ich bin _____ fertig."
    "<br><br><i>J'ai presque fini.</i>"
    f"<br><br> &nbsp; {ICON_CHECK} fast"
    f"<br><br> &nbsp; {ICON_CHECK} nahezu"
    f"<br><br> &nbsp; {ICON_CROSS} fast, nahezu"
)

guidance_adverbien_synonyms = (
    "Pour chaque question, un adverbe allemand sera présenté."
    "<br><br>Trouvez un synonyme de cet adverbe."

    f"<br><br> {ICON_WARN} N'écrivez pas plus d'un synonyme, sinon votre réponse sera considérée comme fausse."

    "<h2>Exemple</h2>"
    "mindestens"
    f"<br><br> &nbsp; {ICON_CHECK} wenigstens"
    f"<br><br> &nbsp; {ICON_CHECK} zumindest"
    f"<br><br> &nbsp; {ICON_CROSS} wenigstens, zumindest"
)

guidance_adverbien_antonym = (
    "Pour chaque question, un adverbe allemand sera présenté."
    "<br>Donnez son antonyme en allemand."

    f"<br><br> {ICON_WARN} Des synonymes sont disponibles pour cet exercice. Il peut y avoir plusieurs réponses possibles."
    f"<br><br> {ICON_WARN} N'écrivez pas plus d'une réponse, sinon votre réponse sera signalée comme fausse."

    "<h2>Exemple</h2>"
    "immer"
    f"<br><br> &nbsp; {ICON_CHECK} nie"
    f"<br><br> &nbsp; {ICON_CHECK} nimmer"
    f"<br><br> &nbsp; {ICON_CROSS} nie, nimmer"
)

guidance_adverbien_prompt = (
    "Pour chaque question, un adverbe allemand et sa traduction française seront présentés."
    "<br><br>Écrivez une phrase en allemand utilisant cet adverbe."

    f"<br><br> {ICON_WARN} La phrase allemande doit respecter l'ordre des mots correct."
    f"<br><br> {ICON_WARN} La phrase allemande doit être cohérente."
    f"<br><br> {ICON_WARN} Les erreurs secondaires, telles que les erreurs de cas ou d'orthographe,"
    f" sont acceptées tant que la phrase reste compréhensible et cohérente."
    f"<br><br> {ICON_WARN} L'évaluation, les corrections et les retours sont générés par un grand modèle de langage (LLM)."
    f" Les LLM peuvent faire des erreurs, inventer des informations ou fournir des conseils non vérifiés."
    f" Veuillez vérifier les informations importantes."
    f"<br><br> {ICON_WARN} Ne fournissez aucune information personnelle telle que votre nom de famille,"
    f" votre date de naissance, votre adresse précise ou votre numéro d'identité."

    "<h2>Exemples</h2>"
    f"heute"
    f"<br><br><i>aujourd'hui</i>"
    f"<br><br> &nbsp; {ICON_CHECK} Heute esse ich ein Sandwich."
    f"<br><br> &nbsp; {ICON_CROSS} Heute ich esse ein Sandwich. (Ordre des mots incorrect)"
    f"<br><br> &nbsp; {ICON_CHECK} Heute esse ich eine Sandwich. (Erreur acceptable)"
    f"<br><br> &nbsp; {ICON_CROSS} Heute esse ich Wasser. (Phrase incohérente)"
)

guidance_adjektive_isolation = (
    "Pour chaque question, la traduction française d'un adjectif allemand sera présentée."
    "<br>Trouvez l'adjectif allemand correspondant à la traduction."

    f"<br><br> {ICON_WARN} Des synonymes sont disponibles pour cet exercice. Il peut y avoir plusieurs réponses possibles."
    f"<br><br> {ICON_WARN} N'écrivez pas plus d'une réponse, sinon votre réponse sera signalée comme fausse."
    
    "<h2>Exemple</h2>"
    "bon marché"
    f"<br><br> &nbsp; {ICON_CHECK} billig"
    f"<br><br> &nbsp; {ICON_CHECK} günstig"
    f"<br><br> &nbsp; {ICON_CROSS} billig, günstig"
)

guidance_adjektive_synonym = (
    "Pour chaque question, un adjectif allemand sera présenté."
    "<br><br>Trouvez un synonyme de cet adjectif."

    f"<br><br> {ICON_WARN} Il peut y avoir plus d'une réponse possible."
    f"<br><br> {ICON_WARN} N'écrivez pas plus d'un synonyme, sinon votre réponse sera considérée comme fausse."

    "<h2>Exemple</h2>"
    "schlecht"
    f"<br><br> &nbsp; {ICON_CHECK} böse"
    f"<br><br> &nbsp; {ICON_CHECK} schlimm"
    f"<br><br> &nbsp; {ICON_CROSS} böse, schlimm"
)

guidance_adjektive_antonym = (
    "Pour chaque question, un adjectif allemand sera présenté."
    "<br>Donnez son contraire en allemand."
    
    f"<br><br> {ICON_WARN} Des synonymes sont disponibles pour cet exercice. Il peut y avoir plusieurs réponses possibles."
    f"<br><br> {ICON_WARN} N'écrivez pas plus d'une réponse, sinon votre réponse sera signalée comme fausse."
    
    "<h2>Exemple</h2>"
    "teuer"
    f"<br><br> &nbsp; {ICON_CHECK} billig"
    f"<br><br> &nbsp; {ICON_CHECK} günstig"
    f"<br><br> &nbsp; {ICON_CROSS} billig, günstig"
)

guidance_adjektive_comparative = (
    "Pour chaque question, un adjectif allemand sera présenté."
    "<br>Donnez sa forme comparative."

    "<h2>Exemple</h2>"
    "alt"
    "<br><br>vieux"
    f"<br><br> &nbsp; {ICON_CHECK} älter"
)

guidance_adjektive_superlative = (
    "Pour chaque question, un adjectif allemand sera présenté."
    "<br>Donnez son superlatif."
    
    f"<br><br>{ICON_WARN} Donnez la forme superlative avec \"am\"."

    "<h2>Exemple</h2>"
    "alt"
    "<br><br>vieux"
    f"<br><br> &nbsp; {ICON_CHECK} am ältesten"
    f"<br><br> &nbsp; {ICON_CROSS} älteste"
)

guidance_adjektive_comparison_words = (
    "Pour chaque question, une phrase allemande et sa traduction française seront présentées."

    "<br><br>Il manque un mot de comparaison dans la phrase allemande. Trouvez celui qui convient."
    
    "<h2>Exemple</h2>"
    "Peter ist größer _____ sein Bruder."
    "<br><br><i>Peter est plus grand que son frère."
    f"<br><br> &nbsp; {ICON_CHECK} als"
)

guidance_adjektivdeklinationen_isolation = (
    "Pour chaque question, une phrase allemande, un adjectif et un cas grammatical seront présentés."
    
    "<br><br>Complétez la phrase avec l’adjectif décliné, en tenant compte de l’article,"
    " du genre du nom et du cas grammatical."

    "<h2>Exemple</h2>"
    "ein _____ Vater \u25CF Nominativ \u25CF nett"
    f"<br><br> &nbsp; {ICON_CHECK} netter"
)

guidance_adjektivdeklinationen_sentences = (
    "Pour chaque question, une phrase allemande incomplète et un adjectif seront présentés."
    
    "<br><br>Complétez la phrase avec l’adjectif correctement décliné, en tenant compte de l’article,"
    " du genre du nom et du cas grammatical."

    "<h2>Exemple</h2>"
    "Die _____ Kinder stellen viele Fragen. \u25CF klug"
    f"<br><br> &nbsp; {ICON_CHECK} klugen"
)

guidance_adjektivdeklinationen_comparative_isolation = (
    "Pour chaque question, une phrase allemande, un adjectif et un cas grammatical seront présentés."
    
    "<br><br>Complétez la phrase avec l’adjectif <b>comparatif</b> décliné, en tenant compte de l’article,"
    " du genre du nom et du cas grammatical."

    "<h2>Exemple</h2>"
    "ein _____ Vater \u25CF Nominativ \u25CF nett"
    f"<br><br> &nbsp; {ICON_CHECK} netterer"
)

guidance_adjektivdeklinationen_comparative_sentences = (
    "Pour chaque question, une phrase allemande incomplète et un adjectif seront présentés."
    
    "<br><br>Complétez la phrase avec l’adjectif <b>comparatif</b> correctement décliné, en tenant compte de l’article,"
    " du genre du nom et du cas grammatical."

    "<h2>Exemple</h2>"
    "Der _____ Hund läuft im Garten. \u25CF groß"
    f"<br><br> &nbsp; {ICON_CHECK} größere"
)

guidance_adjektivdeklinationen_superlative_isolation = (
    "Pour chaque question, une phrase allemande, un adjectif et un cas grammatical seront présentés."
    
    "<br><br>Complétez la phrase avec l’adjectif <b>superlatif</b> décliné, en tenant compte de l’article,"
    " du genre du nom et du cas grammatical."

    "<h2>Exemple</h2>"
    "der _____ Vater \u25CF Nominatif \u25CF nett"
    f"<br><br> &nbsp; {ICON_CHECK} netteste"
)

guidance_adjektivdeklinationen_superlative_sentences = (
    "Pour chaque question, une phrase allemande incomplète et un adjectif seront présentés."
    
    "<br><br>Complétez la phrase avec l’adjectif <b>superlatif</b> correctement décliné, en tenant compte de l’article,"
    " du genre du nom et du cas grammatical."

    "<h2>Exemple</h2>"
    "Die _____ Blume steht auf dem Tisch. \u25CF schön"
    f"<br><br> &nbsp; {ICON_CHECK} schönste"
)

guidance_verben_translation = (
    "Pour chaque question, la traduction française d’un verbe allemand sera présentée."
    "<br>Donnez le verbe allemand correspondant à l’ensemble de la traduction."

    f"<br><br> {ICON_WARN} Il n’y a qu’une seule réponse possible par question."
    f" Les synonymes ne sont pas acceptés pour cet exercice. Lisez attentivement toute la traduction."
    f"<br><br> {ICON_WARN} La réponse peut nécessiter un pronom réfléchi si le verbe est toujours réfléchi."

    "<h2>Exemple</h2>"
    "rendre heureux, être heureux (réfl.), attendre avec impatience (réfl.)"
    f"<br><br> &nbsp; {ICON_CHECK} sich freuen"
    f"<br><br> &nbsp; {ICON_CROSS} freuen"
)

guidance_verben_multiple_choices_french_to_german = (
    "Pour chaque question, la traduction française d’un verbe allemand et cinq verbes allemands seront présentés."
    "<br>Sélectionnez le verbe allemand correspondant à l’ensemble de la traduction."

    f"<br><br> {ICON_WARN} Il n’y a qu’une seule réponse possible par question."
    f" Les synonymes ne sont pas acceptés pour cet exercice. Lisez attentivement toute la traduction."

    "<h2>Exemple</h2>"
    "remplacer, substituer, compenser"
    "<br><br>ersetzen"
    "<br>leiden"
    "<br>diskutieren"
    "<br>rufen"
    "<br>vorschlagen"
    f"<br><br> &nbsp; {ICON_CHECK} ersetzen"
)

guidance_verben_multiple_choices_german_to_french = (
    "Pour chaque question, un verbe allemand et cinq traductions françaises possibles seront présentés."
    "<br>Sélectionnez la traduction qui correspond au verbe allemand."

    f"<br><br> {ICON_WARN} Il n’y a qu’une seule réponse possible par question."
    f" Les synonymes ne sont pas acceptés pour cet exercice. Lisez attentivement l'ensemble de la traduction."

    "<h2>Exemple</h2>"
    "ersetzen"
    "<br><br>remplacer, substituer, compenser"
    "<br>souffrir, endurer, supporter"
    "<br>discuter, débattre"
    "<br>appeler, crier, convoquer"
    "<br>suggérer, proposer"
    f"<br><br> &nbsp; {ICON_CHECK} remplacer, substituer, compenser"
)

guidance_trennbare_verben_root = (
    "Pour chaque question, la traduction française d’un verbe allemand (séparable ou inséparable)"
    " ainsi que sa racine seront présentées."
    "<br><br>Trouvez le verbe allemand correspondant à la traduction et à la racine."

    f"<br><br> {ICON_WARN} Il n’y a qu’une seule réponse possible par question."
    f" Les synonymes ne sont pas acceptés pour cet exercice. Lisez attentivement l'ensemble de la traduction."
    f"<br><br> {ICON_WARN} La réponse peut nécessiter un pronom réfléchi si le verbe est toujours réfléchi."

    "<h2>Exemple</h2>"
    "tirer, traîner, déplacer → ziehen"
    "<br><br>s'habiller, mettre, habiller quelqu'un, attirer, tirer → _____"
    f"<br><br> &nbsp; {ICON_CHECK} anziehen"
)

guidance_trennbare_verben_prefix = (
    "Pour chaque question, la traduction française d’un verbe allemand (séparable ou inséparable)"
    " ainsi que son préfixe seront présentés."
    "<br><br>Donnez le verbe allemand correspondant à la traduction et au préfixe."

    f"<br><br> {ICON_WARN} Il n’y a qu’une seule réponse possible par question."
    f" Les synonymes ne sont pas acceptés pour cet exercice. Lisez attentivement l'ensemble de la traduction."
    f"<br><br> {ICON_WARN} La réponse peut nécessiter un pronom réfléchi si le verbe est toujours réfléchi."

    "<h2>Exemple</h2>"
    "s'habiller, mettre, habiller quelqu'un, attirer, tirer \u25CF an"
    f"<br><br> &nbsp; {ICON_CHECK} anziehen"
)

guidance_trennbare_verben_no_help = (
    "Pour chaque question, la traduction française d’un verbe allemand (séparable ou inséparable) sera présentée."
    "<br><br>Trouvez le verbe allemand correspondant à l’ensemble de la traduction."

    f"<br><br> {ICON_WARN} Il n’y a qu’une seule réponse possible par question."
    f" Les synonymes ne sont pas acceptés pour cet exercice. Lisez attentivement l'ensemble de la traduction."
    f"<br><br> {ICON_WARN} La réponse peut nécessiter un pronom réfléchi si le verbe est toujours réfléchi."

    "<h2>Exemple</h2>"
    "s'habiller, mettre, habiller quelqu'un, attirer, tirer"
    f"<br><br> &nbsp; {ICON_CHECK} anziehen"
)

guidance_nomen_verben_verbindungen_nomen_isolation = (
    "Pour chaque question, une combinaison nom-verbe allemande incomplète et sa traduction française seront présentées."
    "<br><br>Trouvez le nom allemand qui complète cette combinaison."

    f"<br><br> {ICON_WARN} Il peut y avoir plusieurs réponses possibles."
    f"<br><br> {ICON_WARN} N'écrivez pas plus d'une réponse, sinon votre réponse sera signalée comme fausse."
    f"<br><br> {ICON_WARN} La réponse peut nécessiter un article et/ou une préposition."

    f"<br><br>➡️ Si vous avez besoin d'aide pour le genre du nom commun, cliquez sur le bouton m/f/n/pl."
    
    "<h2>Exemples</h2>"
    "_____ haben"
    "<br><br><i>avoir une opinion, penser</i>"
    f"<br><br> &nbsp; {ICON_CHECK} eine Meinung"
    f"<br><br> &nbsp; {ICON_CHECK} eine Ansicht"
    f"<br><br> &nbsp; {ICON_CROSS} eine Meinung, eine Ansicht"
    f"<br><br> &nbsp; {ICON_CROSS} Meinung"
    f"<br><br> &nbsp; {ICON_CROSS} ein Meinung"

    "<br><br>_____ nehmen"
    "<br><br><i>accepter</i>"
    f"<br><br> &nbsp; {ICON_CHECK} in Kauf"
    f"<br><br> &nbsp; {ICON_CROSS} Kauf"
)

guidance_nomen_verben_verbindungen_verben_isolation = (
    "Pour chaque question, une combinaison nom-verbe allemande incomplète et sa traduction française seront présentées."
    "<br><br>Trouvez le verbe allemand qui complète cette combinaison."

    f"<br><br> {ICON_WARN} Il peut y avoir plusieurs réponses possibles."
    f"<br><br> {ICON_WARN} N'écrivez pas plus d'une réponse, sinon votre réponse sera signalée comme fausse."

    "<h2>Exemple</h2>"
    "eine Meinung _____"
    "<br><br><i>avoir une opinion, penser</i>"
    f"<br><br> &nbsp; {ICON_CHECK} haben"
    f"<br><br> &nbsp; {ICON_CHECK} vertreten"
    f"<br><br> &nbsp; {ICON_CROSS} haben, vertreten"
)

guidance_nomen_verben_verbindungen_nomen_sentences = (
    "Pour chaque question, une phrase allemande incomplète et sa traduction française seront présentées."
    "<br><br>Trouvez le nom allemand qui complète cette phrase."

    f"<br><br> {ICON_WARN} Il peut y avoir plusieurs réponses possibles."
    f"<br><br> {ICON_WARN} N'écrivez pas plus d'une réponse, sinon votre réponse sera signalée comme fausse."
    f"<br><br> {ICON_WARN} La réponse peut nécessiter une préposition."

    "<h2>Exemples</h2>"
    "Ich habe eine andere _____ als du."
    "<br><br><i>J’ai une opinion différente de la tienne.</i>"
    f"<br><br> &nbsp; {ICON_CHECK} Meinung"
    f"<br><br> &nbsp; {ICON_CHECK} Ansicht"
    f"<br><br> &nbsp; {ICON_CROSS} Meinung, Ansicht"

    "<br><br>Ich will dieses Projekt unbedingt _____ bringen, bevor ich in den Urlaub fahre."
    "<br><br><i>Je veux absolument terminer ce projet avant de partir en vacances.</i>"
    f"<br><br> &nbsp; {ICON_CHECK} zu Ende"
    f"<br><br> &nbsp; {ICON_CHECK} zum Abschluss"
    f"<br><br> &nbsp; {ICON_CROSS} Ende"
    f"<br><br> &nbsp; {ICON_CROSS} Abschluss"
    f"<br><br> &nbsp; {ICON_CROSS} zu Ende, zum Abschluss"
)

guidance_nomen_verben_verbindungen_verben_sentences = (
    "Pour chaque question, une phrase allemande incomplète et sa traduction française seront présentées."
    "<br><br>Trouvez le verbe allemand qui complète cette phrase."

    f"<br><br> {ICON_WARN} Il peut y avoir plusieurs réponses possibles."
    f"<br><br> {ICON_WARN} N'écrivez pas plus d'une réponse, sinon votre réponse sera signalée comme fausse."
    f"<br><br> {ICON_WARN} Le verbe doit être conjugué au temps et à la personne appropriés."

    "<h2>Exemple</h2>"
    "Sie _____ den Vorschlag, gemeinsam zu reisen."
    "<br><br><i>Elle a fait la proposition de voyager ensemble.</i>"
    f"<br><br> &nbsp; {ICON_CHECK} machte"
    f"<br><br> &nbsp; {ICON_CHECK} unterbreitete"
    f"<br><br> &nbsp; {ICON_CROSS} machte, unterbreitete"
    f"<br><br> &nbsp; {ICON_CROSS} macht"
    f"<br><br> &nbsp; {ICON_CROSS} machen"
)

guidance_nomen_verben_wortstaemme_verben = (
    "Pour chaque question, une paire nom-verbe allemande incomplète sera présentée, accompagnée de sa traduction française."
    "<br><br>Trouvez le verbe allemand qui complète cette paire."

    f"<br><br> {ICON_WARN} Il n’y a qu’une seule réponse possible par question."
    f" Les synonymes ne sont pas acceptés pour cet exercice. Lisez attentivement l'ensemble de la traduction."
    f"<br><br> {ICON_WARN} La réponse peut nécessiter un pronom réfléchi si le verbe est toujours réfléchi."

    "<h2>Exemple</h2>"
    "le travail → die Arbeit"
    "<br><br>travailler → _____"
    f"<br><br> &nbsp; {ICON_CHECK} arbeiten"
)

guidance_nomen_verben_wortstaemme_nomen = (
    "Pour chaque question, une paire nom-verbe allemande incomplète sera présentée, accompagnée de sa traduction française."
    "<br><br>Trouvez le nom allemand qui complète cette paire."

    f"<br><br> {ICON_WARN} Il peut y avoir plusieurs réponses possibles."
    f"<br><br> {ICON_WARN} N'écrivez pas plus d'une réponse, sinon votre réponse sera signalée comme fausse."

    f"<br><br>➡️ Si vous avez besoin d'aide pour le genre du nom commun, cliquez sur le bouton m/f/n/pl."
    
    "<h2>Exemple</h2>"
    "travailler → arbeiten"
    "<br><br>le travail → _____"
    f"<br><br> &nbsp; {ICON_CHECK} die Arbeit"
)

guidance_adjektive_verben_wortstaemme_adjektive = (
    "Pour chaque question, une paire adjectif-verbe allemande incomplète sera présentée, accompagnée de sa traduction française."
    "<br><br>Trouvez l'adjectif allemand qui complète cette paire."

    f"<br><br> {ICON_WARN} Il peut y avoir plusieurs réponses possibles."
    f"<br><br> {ICON_WARN} N'écrivez pas plus d'une réponse, sinon votre réponse sera signalée comme fausse."

    "<h2>Exemple</h2>"
    "aimer, apprécier → mögen"
    "<br><br>possible → _____"
    f"<br><br> &nbsp; {ICON_CHECK} möglich"
)

guidance_adjektive_verben_wortstaemme_verben = (
    "Pour chaque question, une paire adjectif-verbe allemande incomplète sera présentée, accompagnée de sa traduction française."
    "<br><br>Trouvez le verbe allemand qui complète cette paire."

    f"<br><br> {ICON_WARN} Il peut y avoir plusieurs réponses possibles."
    f"<br><br> {ICON_WARN} N'écrivez pas plus d'une réponse, sinon votre réponse sera signalée comme fausse."

    "<h2>Exemple</h2>"
    "possible → möglich"
    "<br><br>aimer, apprécier → _____"
    f"<br><br> &nbsp; {ICON_CHECK} mögen"
)

guidance_adjektive_nomen_wortstaemme_adjektive = (
    "Pour chaque question, une paire nom-adjectif allemande incomplète sera présentée, accompagnée de sa traduction française."
    "<br><br>Trouvez l'adjectif allemand qui complète cette paire."

    f"<br><br> {ICON_WARN} Il peut y avoir plusieurs réponses possibles."
    f"<br><br> {ICON_WARN} N'écrivez pas plus d'une réponse, sinon votre réponse sera signalée comme fausse."

    "<h2>Exemple</h2>"
    "la direction → die Richtung"
    "<br><br>correct, juste → _____"
    f"<br><br> &nbsp; {ICON_CHECK} richtig"
)

guidance_adjektive_nomen_wortstaemme_nomen = (
    "Pour chaque question, une paire nom-adjectif allemande incomplète sera présentée, accompagnée de sa traduction française."
    "<br><br>Trouvez le nom allemand qui complète cette paire."

    f"<br><br> {ICON_WARN} Il peut y avoir plusieurs réponses possibles."
    f"<br><br> {ICON_WARN} N'écrivez pas plus d'une réponse, sinon votre réponse sera signalée comme fausse."

    f"<br><br>➡️ Si vous avez besoin d'aide pour le genre du nom commun, cliquez sur le bouton m/f/n/pl."

    "<h2>Exemple</h2>"
    "correct, juste → richtig"
    "<br><br>la direction → _____"
    f"<br><br> &nbsp; {ICON_CHECK} die Richtung"
)

guidance_zahlen_number = (
    "Pour chaque question, un nombre sera présenté."
    "<br><br>Écrivez ce nombre en toutes lettres en allemand."

    "<h2>Exemples</h2>"
    "2"
    f"<br><br> &nbsp; {ICON_CHECK} zwei"
    
    "<br><br>1,23"
    f"<br><br> &nbsp; {ICON_CHECK} eins Komma zwei drei"
    f"<br><br> &nbsp; {ICON_CROSS} eins Punkt zwei drei"
)

guidance_zahlen_time_spelled = (
    "Pour chaque question, une heure de la journée sera présentée."
    "<br><br>Écrivez cette heure en toutes lettres en allemand."

    "<h2>Exemples</h2>"
    "8h"
    f"<br><br> &nbsp; {ICON_CHECK} acht Uhr"
    f"<br><br> &nbsp; {ICON_CHECK} acht Uhr null"

    "<br><br>17:50"
    f"<br><br> &nbsp; {ICON_CHECK} siebzehn Uhr fünfzig"
    f"<br><br> &nbsp; {ICON_CHECK} zehn vor sechs"
)

guidance_zahlen_time_digital = (
    "Pour chaque question, une heure de la journée sera présentée."
    "<br><br>Écrivez cette heure sous forme numérique."

    "<h2>Exemple</h2>"
    "Viertel vor neun"
    f"<br><br> &nbsp; {ICON_CHECK} 8:45"
    f"<br><br> &nbsp; {ICON_CHECK} 08:45"
)

guidance_zahlen_ordinal_isolation = (
    "Pour chaque question, un nombre ordinal sera présenté en français."
    "<br><br>Traduisez ce nombre ordinal en allemand."

    f"<br><br> {ICON_WARN} Le nombre ordinal doit être décliné sous la forme <i>-e</i>."

    "<h2>Exemple</h2>"
    "premier"
    f"<br><br> &nbsp; {ICON_CHECK} erste"
    f"<br><br> &nbsp; {ICON_CROSS} ersten"
)

guidance_zahlen_ordinal_sentence = (
    "Pour chaque question, une phrase en allemand et sa traduction française seront présentées."
    "<br><br>Il manque un nombre ordinal dans la phrase allemande. Trouvez celui qui convient."

    f"<br><br> {ICON_WARN} Le nombre ordinal doit être décliné en fonction du contexte."

    "<h2>Exemple</h2>"
    "Sie wohnt im _____ Stock."
    "<br><br><i>Elle habite au deuxième étage.</i>"
    f"<br><br> &nbsp; {ICON_CHECK} zweiten"
    f"<br><br> &nbsp; {ICON_CROSS} zweite"
)

guidance_zahlen_adverb_isolation = (
    "Pour chaque question, un adverbe français sera présenté."
    "<br><br>Traduisez cet adverbe en allemand."

    "<h2>Exemple</h2>"
    "troisièmement"
    f"<br><br> &nbsp; {ICON_CHECK} drittens"
)

guidance_zahlen_adverb_sentence = (
    "Pour chaque question, une phrase en allemand et sa traduction française seront présentées."
    "<br><br>Il manque un adverbe dans la phrase allemande. Trouvez celui qui convient."

    "<h2>Exemple</h2>"
    "_____ fehlt uns im Moment das nötige Budget."
    "<br><br><i>Troisièmement, il nous manque actuellement le budget nécessaire.</i>"
    f"<br><br> &nbsp; {ICON_CHECK} Drittens"
)

guidance_zahlen_fraction_isolation = (
    "Pour chaque question, une fraction en français sera présentée."
    "<br><br>Traduisez cette fraction en allemand."

    "<h2>Exemple</h2>"
    "un tiers"
    f"<br><br> &nbsp; {ICON_CHECK} ein Drittel"
)

guidance_zahlen_fraction_sentence = (
    "Pour chaque question, une phrase en allemand et sa traduction française seront présentées."
    "<br><br>Il manque une fraction dans la phrase allemande. Trouvez celle qui convient."

    "<h2>Exemple</h2>"
    "_____ der Teilnehmenden hat den Kurs vorzeitig beendet."
    "<br><br><i>La moitié des participants a quitté le cours prématurément.</i>"
    f"<br><br> &nbsp; {ICON_CHECK} Die Hälfte"
)

guidance_zahlen_multiplier_isolation = (
    "Pour chaque question, un multiplicateur sera présenté en français."
    "<br><br>Traduisez ce multiplicateur en allemand."

    "<h2>Exemple</h2>"
    "quadruple"
    f"<br><br> &nbsp; {ICON_CHECK} vierfach"
)

guidance_zahlen_multiplier_sentence = (
    "Pour chaque question, une phrase en allemand et sa traduction française seront présentées."
    "<br><br> Il manque un multiplicateur dans la phrase allemande. Trouvez celui qui convient."

    f"<br><br>{ICON_WARN} Le multiplicateur doit être choisi en fonction du contexte."

    "<h2>Exemple</h2>"
    "Das Risiko ist _____: finanziell und reputationsbezogen."
    "<br><br><i>Le risque est double : financier et de réputation.</i>"
    f"<br><br>&nbsp; {ICON_CHECK} zweifach"
)

guidance_zahlen_genitive_isolation = (
    "Pour chaque question, un nombre sera présenté."
    "<br><br>Donnez la forme génitive de ce nombre."

    "<h2>Exemple</h2>"
    "3"
    f"<br><br> &nbsp; {ICON_CHECK} dreier"
)

guidance_zahlen_genitive_sentence = (
    "Pour chaque question, une phrase en allemand et sa traduction française seront présentées."
    "<br><br>Il manque la forme génitive d'un nombre dans la phrase allemande. Trouvez celle qui convient."

    "<h2>Exemples</h2>"
    "Der Ausschuss einigte sich nach intensiver Debatte auf einen Kompromiss _____ Parteien."
    "<br><br><i>Après un débat intense, la commission s’est accordée sur un compromis entre sept partis.</i>"
    f"<br><br> &nbsp; {ICON_CHECK} siebener"
    f"<br><br> &nbsp; {ICON_CHECK} von sieben"

    "<br><br>Die Lösung ergibt sich aus der Kombination _____ voneinander abhängiger Faktoren."
    "<br><br><i>La solution résulte de la combinaison de quatre facteurs interdépendants.</i>"
    f"<br><br> &nbsp; {ICON_CHECK} vierer"
    f"<br><br> &nbsp; {ICON_CROSS} von vier (la déclinaison de l'adjectif ne correspond pas)"
)

GUIDANCE_SUBCATEGORY_FR = {
    praepositionen: {
        isolation: guidance_praepositionen_isolation,
        context: guidance_praepositionen_sentences,
        synonym: guidance_praepositionen_synonyms,
        antonym: guidance_praepositionen_antonym,
        prompt: guidance_praepositionen_prompt,
    },

    praepositionen_verben: {
        isolation: guidance_praepositionen_verben_isolation,
        context: guidance_praepositionen_verben_sentences,
    },

    praepositionen_adjektive: {
        isolation: guidance_praepositionen_adjektive_isolation,
        context: guidance_praepositionen_adjektive_sentences,
    },

    praepositionen_nomen: {
        isolation: guidance_praepositionen_nomen_isolation,
        context: guidance_praepositionen_nomen_sentences,
    },

    konnektoren: {
        isolation: guidance_konnektoren_isolation,
        context: guidance_konnektoren_sentences,
        synonym: guidance_konnektoren_synonyms,
        prompt: guidance_konnektoren_prompt,
    },

    fragen: {
        isolation: guidance_fragen_isolation,
        context: guidance_fragen_sentences,
        prompt: guidance_fragen_prompt,
    },

    adverbien: {
        isolation: guidance_adverbien_isolation,
        context: guidance_adverbien_sentences,
        synonym: guidance_adverbien_synonyms,
        antonym: guidance_adverbien_antonym,
        prompt: guidance_adverbien_prompt,
    },

    adjektive: {
        isolation: guidance_adjektive_isolation,
        synonym: guidance_adjektive_synonym,
    },

    verben: {
        isolation: guidance_verben_translation,
        multiple_choice_native: guidance_verben_multiple_choices_german_to_french,
        multiple_choice_target: guidance_verben_multiple_choices_french_to_german,
    },

}

GUIDANCE_CATEGORY_FR = {

}

GUIDANCE_EXERCISE_FR = {

    pronominaladverbien: {
        1: guidance_pronominaladverbien_dawort,

        2: guidance_pronominaladverbien_dawort,
        3: guidance_pronominaladverbien_dawort,
        4: guidance_pronominaladverbien_wowort,

        5: guidance_pronominaladverbien_wowort,
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
        11: guidance_artikel_sentences,
        12: guidance_artikel_isolation,
        13: guidance_artikel_sentences,
        14: guidance_artikel_sentences,
        15: guidance_artikel_sentences,
        16: guidance_artikel_sentences,
        17: guidance_artikel_sentences,
        18: guidance_artikel_sentences,
        19: guidance_artikel_sentences,
        20: guidance_artikel_sentences,
        21: guidance_artikel_isolation,
        22: guidance_artikel_sentences,
        23: guidance_artikel_isolation,
        24: guidance_artikel_sentences,
        25: guidance_artikel_isolation,
        26: guidance_artikel_sentences,

        27: guidance_artikel_isolation,
        28: guidance_artikel_sentences,
        29: guidance_artikel_isolation,
        30: guidance_artikel_sentences,
        31: guidance_artikel_isolation,
        32: guidance_artikel_sentences,

        33: guidance_artikel_isolation,
        34: guidance_artikel_sentences,
        35: guidance_artikel_isolation,
        36: guidance_artikel_sentences,
        37: guidance_artikel_isolation,
        38: guidance_artikel_sentences,

        39: guidance_artikel_isolation,
        40: guidance_artikel_sentences,

        41: guidance_artikel_isolation,
        42: guidance_artikel_sentences,
        43: guidance_artikel_sentences,
        44: guidance_artikel_sentences,

        45: guidance_artikel_isolation,
        46: guidance_artikel_sentences,
        47: guidance_artikel_isolation,
        48: guidance_artikel_sentences,
        49: guidance_artikel_isolation,
        50: guidance_artikel_sentences,
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
        17: guidance_pronomen_relative_isolation,
        18: guidance_pronomen_relative_sentences,
        19: guidance_pronomen_relative_sentences,
        20: guidance_pronomen_relative_sentences,
        21: guidance_pronomen_relative_sentences,
        22: guidance_pronomen_relative_sentences,
        23: guidance_pronomen_relative_sentences,

        24: guidance_pronomen_isolation,
        25: guidance_pronomen_sentences,
        26: guidance_pronomen_isolation,
        27: guidance_pronomen_sentences,
        28: guidance_pronomen_relative_sentences,
        29: guidance_pronomen_relative_sentences,
        30: guidance_pronomen_relative_sentences,

        31: guidance_pronomen_isolation,
        32: guidance_pronomen_sentences,
        33: guidance_pronomen_isolation,
        34: guidance_pronomen_sentences,
        35: guidance_pronomen_isolation,
        36: guidance_pronomen_sentences,
        37: guidance_pronomen_relative_sentences,
        38: guidance_pronomen_sentences,

        39: guidance_pronomen_isolation,
        40: guidance_pronomen_sentences,
        41: guidance_pronomen_isolation,
        42: guidance_pronomen_sentences
    },

    komparativ_superlativ: {
        1: guidance_adjektive_comparative,
        2: guidance_adjektive_comparative,
        3: guidance_adjektive_comparative,
        4: guidance_adjektive_superlative,
        5: guidance_adjektive_superlative,
        6: guidance_adjektive_superlative,

        7: guidance_adjektive_comparative,
        8: guidance_adjektive_comparative,
        9: guidance_adjektive_comparative,
        10: guidance_adjektive_superlative,
        11: guidance_adjektive_superlative,
        12: guidance_adjektive_superlative,
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
        19: guidance_adjektivdeklinationen_comparative_isolation,
        20: guidance_adjektivdeklinationen_comparative_sentences,
        21: guidance_adjektivdeklinationen_superlative_isolation,
        22: guidance_adjektivdeklinationen_superlative_sentences,

        23: guidance_adjektivdeklinationen_isolation,
        24: guidance_adjektivdeklinationen_sentences,
        25: guidance_adjektivdeklinationen_isolation,
        26: guidance_adjektivdeklinationen_sentences,
        27: guidance_adjektivdeklinationen_isolation,
        28: guidance_adjektivdeklinationen_sentences,

        29: guidance_adjektivdeklinationen_isolation,
        30: guidance_adjektivdeklinationen_sentences,
        31: guidance_adjektivdeklinationen_isolation,
        32: guidance_adjektivdeklinationen_sentences,
    },

    adjektive_verben_wortstaemme: {
        1: guidance_adjektive_verben_wortstaemme_adjektive,
        2: guidance_adjektive_verben_wortstaemme_verben,
        3: guidance_adjektive_verben_wortstaemme_adjektive,
        4: guidance_adjektive_verben_wortstaemme_verben,

        5: guidance_adjektive_verben_wortstaemme_adjektive,
        6: guidance_adjektive_verben_wortstaemme_verben,
        7: guidance_adjektive_verben_wortstaemme_adjektive,
        8: guidance_adjektive_verben_wortstaemme_verben,
        9: guidance_adjektive_verben_wortstaemme_adjektive,
        10: guidance_adjektive_verben_wortstaemme_verben,

        11: guidance_adjektive_verben_wortstaemme_adjektive,
        12: guidance_adjektive_verben_wortstaemme_verben,
        13: guidance_adjektive_verben_wortstaemme_adjektive,
        14: guidance_adjektive_verben_wortstaemme_verben,
        15: guidance_adjektive_verben_wortstaemme_adjektive,
        16: guidance_adjektive_verben_wortstaemme_verben,
        17: guidance_adjektive_verben_wortstaemme_adjektive,
        18: guidance_adjektive_verben_wortstaemme_verben,
        19: guidance_adjektive_verben_wortstaemme_adjektive,
        20: guidance_adjektive_verben_wortstaemme_verben,
    },

    adjektive_nomen_wortstaemme: {
        1: guidance_adjektive_nomen_wortstaemme_adjektive,
        2: guidance_adjektive_nomen_wortstaemme_nomen,
        3: guidance_adjektive_nomen_wortstaemme_adjektive,
        4: guidance_adjektive_nomen_wortstaemme_nomen,

        5: guidance_adjektive_nomen_wortstaemme_adjektive,
        6: guidance_adjektive_nomen_wortstaemme_nomen,
        7: guidance_adjektive_nomen_wortstaemme_adjektive,
        8: guidance_adjektive_nomen_wortstaemme_nomen,

        9: guidance_adjektive_nomen_wortstaemme_adjektive,
        10: guidance_adjektive_nomen_wortstaemme_nomen,
        11: guidance_adjektive_nomen_wortstaemme_adjektive,
        12: guidance_adjektive_nomen_wortstaemme_nomen,
        13: guidance_adjektive_nomen_wortstaemme_adjektive,
        14: guidance_adjektive_nomen_wortstaemme_nomen,
        15: guidance_adjektive_nomen_wortstaemme_adjektive,
        16: guidance_adjektive_nomen_wortstaemme_nomen,
        17: guidance_adjektive_nomen_wortstaemme_adjektive,
        18: guidance_adjektive_nomen_wortstaemme_nomen,
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
        23: guidance_trennbare_verben_root,
        24: guidance_trennbare_verben_root,
        25: guidance_trennbare_verben_prefix,
        26: guidance_trennbare_verben_prefix,
        27: guidance_trennbare_verben_prefix,
        28: guidance_trennbare_verben_prefix,
        29: guidance_trennbare_verben_prefix,
        30: guidance_trennbare_verben_prefix,
        31: guidance_trennbare_verben_no_help,
        32: guidance_trennbare_verben_no_help,
        33: guidance_trennbare_verben_no_help,
        34: guidance_trennbare_verben_no_help,
        35: guidance_trennbare_verben_no_help,
        36: guidance_trennbare_verben_no_help,

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
        55: guidance_trennbare_verben_root,
        56: guidance_trennbare_verben_root,
        57: guidance_trennbare_verben_root,
        58: guidance_trennbare_verben_root,
        59: guidance_trennbare_verben_root,
        60: guidance_trennbare_verben_root,
        61: guidance_trennbare_verben_root,
        62: guidance_trennbare_verben_root,
        63: guidance_trennbare_verben_root,
        64: guidance_trennbare_verben_root,
        65: guidance_trennbare_verben_root,
        66: guidance_trennbare_verben_root,
        67: guidance_trennbare_verben_root,
        68: guidance_trennbare_verben_root,
        69: guidance_trennbare_verben_root,
        70: guidance_trennbare_verben_prefix,
        71: guidance_trennbare_verben_prefix,
        72: guidance_trennbare_verben_prefix,
        73: guidance_trennbare_verben_prefix,
        74: guidance_trennbare_verben_prefix,
        75: guidance_trennbare_verben_prefix,
        76: guidance_trennbare_verben_prefix,
        77: guidance_trennbare_verben_prefix,
        78: guidance_trennbare_verben_prefix,
        79: guidance_trennbare_verben_prefix,
        80: guidance_trennbare_verben_prefix,
        81: guidance_trennbare_verben_prefix,
        82: guidance_trennbare_verben_prefix,
        83: guidance_trennbare_verben_prefix,
        84: guidance_trennbare_verben_prefix,
        85: guidance_trennbare_verben_prefix,
        86: guidance_trennbare_verben_prefix,
        87: guidance_verben_multiple_choices_french_to_german,
        88: guidance_verben_multiple_choices_french_to_german,
        89: guidance_verben_multiple_choices_french_to_german,
        90: guidance_verben_multiple_choices_french_to_german,
        91: guidance_verben_multiple_choices_french_to_german,
        92: guidance_verben_multiple_choices_french_to_german,
        93: guidance_verben_multiple_choices_french_to_german,
        94: guidance_verben_multiple_choices_french_to_german,
        95: guidance_verben_multiple_choices_french_to_german,
        96: guidance_verben_multiple_choices_french_to_german,
        97: guidance_verben_multiple_choices_french_to_german,
        98: guidance_verben_multiple_choices_french_to_german,
        99: guidance_verben_multiple_choices_french_to_german,
        100: guidance_verben_multiple_choices_french_to_german,
        101: guidance_verben_multiple_choices_french_to_german,
        102: guidance_verben_multiple_choices_french_to_german,
        103: guidance_verben_multiple_choices_french_to_german,
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

'''
    praepositionen: {
        1: guidance_praepositionen_sentences,
        2: guidance_praepositionen_sentences,
        3: guidance_praepositionen_sentences,
        4: guidance_praepositionen_sentences,
        5: guidance_praepositionen_sentences,

        6: guidance_praepositionen_sentences,
        7: guidance_praepositionen_sentences,
        8: guidance_praepositionen_sentences,
        9: guidance_praepositionen_sentences,
        10: guidance_praepositionen_sentences,

        11: guidance_praepositionen_sentences,
        12: guidance_praepositionen_sentences,
        13: guidance_praepositionen_isolation,
        14: guidance_praepositionen_sentences,

        15: guidance_praepositionen_sentences,
        16: guidance_praepositionen_sentences,
        17: guidance_praepositionen_sentences,
        18: guidance_praepositionen_sentences,
        19: guidance_praepositionen_isolation,
        20: guidance_praepositionen_sentences,

        21: guidance_praepositionen_sentences,
        22: guidance_praepositionen_sentences,
        23: guidance_praepositionen_sentences,
        24: guidance_praepositionen_sentences,
        25: guidance_praepositionen_isolation,
        26: guidance_praepositionen_sentences,
        27: guidance_praepositionen_isolation,
        28: guidance_praepositionen_sentences,
        29: guidance_praepositionen_synonyms,
        30: guidance_praepositionen_antonym,

        31: guidance_praepositionen_isolation,
        32: guidance_praepositionen_sentences,
        33: guidance_praepositionen_isolation,
        34: guidance_praepositionen_sentences,
    },

'''