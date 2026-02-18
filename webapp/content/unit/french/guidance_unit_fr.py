from data.data_processing.units import (
    praepositionen_grammatik, praepositionen_verben, praepositionen_adjektive, praepositionen_nomen,
    praepositionen_artikel,
    artikel, pronomen, konnektoren, fragen, adverbien, wortstellung,
    adjektive, adjektivdeklinationen, adjektive_konjunktionen,
    trennbare_verben, verben,
    praesens, imperativ, partizip_II, praeteritum, praeteritum_partizip_II, konjunktiv_II, konjunktiv_I, partizip_I,
    genus_regeln, genus_routledge, genus_goethe
)

from webapp.style.icons import ICON_CHECK, ICON_CROSS, ICON_WARN

# bullet point \u25CF

GUIDANCE_UNIT_FR = {
    wortstellung:
        "Placeholder"
    ,

    praepositionen_artikel:
        "Pour chaque question, une phrase allemande incomplète, sa traduction anglaise, "
        "une préposition et un article ou un pronom vous seront présentées."
        
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

    adjektive_konjunktionen:
    "Pour chaque question, vous recevrez une phrase allemande et sa traduction française"

    "<br><br>Il manque une conjunction dans la phrase allemande. Trouvez celui qui convient."

    "<h2>Exemple</h2>"
    "Peter ist größer _____ sein Bruder."
    "<br><br><i>Peter est plus grand que son frère."
    f"<br><br> &nbsp; {ICON_CHECK} als"
    ,

    praesens:
        "Pour chaque question, vous verrez un verbe allemand accompagné d’un pronom personnel."
        "<br>Conjuguez le verbe au présent pour ce pronom."

        f"<br><br> &nbsp; {ICON_WARN} N’écrivez pas le pronom personnel, sinon votre réponse sera considérée comme incorrecte."
        f"<br><br> &nbsp; {ICON_WARN} N’écrivez pas de pronom réfléchi, même si le verbe est habituellement réfléchi."

        "<h2>Exemple</h2>"
        "freuen \u25CF Ich _____"
        f"<br><br> &nbsp; {ICON_CHECK} freue"
        f"<br><br> &nbsp; {ICON_CROSS} Ich freue"
        f"<br><br> &nbsp; {ICON_CROSS} freue mich"
    ,

    partizip_II:
        "Pour chaque question, vous verrez un verbe allemand."
        "<br>Indiquez le Partizip II (participe passé) du verbe donné."

        f"<br><br> &nbsp; {ICON_WARN} N’écrivez pas d’auxiliaire, sinon votre réponse sera considérée comme incorrecte."
        f"<br><br> &nbsp; {ICON_WARN} N’écrivez pas de pronom réfléchi, même si le verbe est habituellement réfléchi."

        "<h2>Exemple</h2>"
        "freuen"
        f"<br><br> &nbsp; {ICON_CHECK} gefreut"
        f"<br><br> &nbsp; {ICON_CROSS} sich gefreut"
        f"<br><br> &nbsp; {ICON_CROSS} hat gefreut"
    ,

    praeteritum:
        "Pour chaque question, vous verrez un verbe allemand."
        "<br>Conjuguez le verbe au Präteritum (prétérit) à la 3ᵉ personne du singulier (Er/Sie/Es) du verbe donné."

        f"<br><br> &nbsp; {ICON_WARN} N’écrivez pas le pronom personnel, sinon votre réponse sera considérée comme incorrecte."
        f"<br><br> &nbsp; {ICON_WARN} N’écrivez pas de pronom réfléchi, même si le verbe est habituellement réfléchi."

        "<h2>Exemple</h2>"
        "freuen"
        f"<br><br> &nbsp; {ICON_CHECK} freute"
        f"<br><br> &nbsp; {ICON_CROSS} freute sich"
        f"<br><br> &nbsp; {ICON_CROSS} er freute"
    ,

    praeteritum_partizip_II:
        "Pour chaque question, vous verrez un verbe allemand."
        "<br>Indiquez le Präteritum (prétérit) à la 3ᵉ personne du singulier (Er/Sie/Es) ainsi que le Partizip II (participe passé) du verbe donné."

        f"<br><br> &nbsp; {ICON_WARN} N’écrivez pas le pronom personnel, sinon votre réponse sera considérée comme incorrecte."
        f"<br><br> &nbsp; {ICON_WARN} N’écrivez pas d’auxiliaire, sinon votre réponse sera considérée comme incorrecte."
        f"<br><br> &nbsp; {ICON_WARN} N’écrivez pas de pronom réfléchi, même si le verbe est habituellement réfléchi."

        "<h2>Exemple</h2>"
        "freuen"
        f"<br><br> &nbsp; {ICON_CHECK} freute, gefreut"
        f"<br><br> &nbsp; {ICON_CHECK} freute gefreut"
        f"<br><br> &nbsp; {ICON_CHECK} freute /       gefreut"
        f"<br><br> &nbsp; {ICON_CROSS} freute, hat gefreut"
        f"<br><br> &nbsp; {ICON_CROSS} er freute, gefreut"
        f"<br><br> &nbsp; {ICON_CROSS} freute sich, sich gefreut"
    ,

    imperativ:
        "Pour chaque question, vous verrez un verbe allemand accompagné d’un pronom personnel."
        "<br>Conjuguez le verbe à l’impératif pour ce pronom."

        f"<br><br> &nbsp; {ICON_WARN} Écrivez les pronoms personnels uniquement dans le cas de la 3ᵉ personne du pluriel."
        f"<br><br> &nbsp; {ICON_WARN} N’écrivez pas de pronom réfléchi, même si le verbe est habituellement réfléchi."

        "<h2>Exemple</h2>"
        "freuen \u25CF Du"
        f"<br><br> &nbsp; {ICON_CHECK} freu"
        f"<br><br> &nbsp; {ICON_CROSS} Du freu"
        f"<br><br> &nbsp; {ICON_CROSS} freu dich"
        "<br><br>freuen \u25CF Sie"
        f"<br><br> &nbsp; {ICON_CHECK} freuen Sie"
        f"<br><br> &nbsp; {ICON_CROSS} freuen"
        f"<br><br> &nbsp; {ICON_CROSS} freuen sich"
    ,

    konjunktiv_II:
        "Pour chaque question, vous verrez un verbe allemand accompagné d’un pronom personnel."
        "<br>Conjuguez le verbe au Konjunktiv II (subjonctif II) pour ce pronom."

        f"<br><br> &nbsp; {ICON_WARN} N’écrivez pas le pronom personnel, sinon votre réponse sera considérée comme incorrecte."

        "<h2>Exemple</h2>"
        "sein \u25CF Du"
        f"<br><br> &nbsp; {ICON_CHECK} wärest"
        f"<br><br> &nbsp; {ICON_CROSS} Du wärest"
    ,

    konjunktiv_I:
        "Pour chaque question, vous verrez un verbe allemand accompagné d’un pronom personnel."
        "<br>Conjuguez le verbe au Konjunktiv I (subjonctif I) pour ce pronom."

        f"<br><br> &nbsp; {ICON_WARN} N’écrivez pas le pronom personnel, sinon votre réponse sera considérée comme incorrecte."

        "<h2>Exemple</h2>"
        "sein \u25CF Du"
        f"<br><br> &nbsp; {ICON_CHECK} seiest"
        f"<br><br> &nbsp; {ICON_CROSS} Du seiest"
    ,

    partizip_I:
        "Pour chaque question, vous verrez un verbe allemand."
        "<br>Indiquez le Partizip I (participe présent) du verbe donné."

        f"<br><br> &nbsp; {ICON_WARN} N’écrivez pas de pronom réfléchi, même si le verbe est habituellement réfléchi."

        "<h2>Exemple</h2>"
        "freuen"
        f"<br><br> &nbsp; {ICON_CHECK} freuend"
        f"<br><br> &nbsp; {ICON_CROSS} sich freuend"
    ,

    genus_regeln:
        "Pour chaque question, un nom allemand et sa traduction anglaise vous seront proposés."
        "<br><br>Trouvez l’article défini (Der, Die ou Das) qui correspond au nom."
        
        "<br><br>→ Un guide expliquant le genre des noms communs est disponible (en anglais) "
        "<a href=\"https://sieversstudyhall.substack.com/p/genders-of-german-noun-from-a1-to\" target=\"_blank\">ici</a>."

        f"<br><br> &nbsp; {ICON_WARN} Il n’y a qu’une seule bonne réponse par question."

        "<h2>Exemple</h2>"
        "_____ Abend"
        "<br><br><i>Le soir</i>"
        f"<br><br> &nbsp; {ICON_CHECK} Der"
        f"<br><br> &nbsp; {ICON_CHECK} der"
    ,

    genus_routledge:
        "Pour chaque question, un nom allemand et sa traduction anglaise vous seront proposés."
        "<br><br>Trouvez l’article défini (Der, Die ou Das) qui correspond au nom."
        
        "<br><br>→ Un guide expliquant le genre des noms communs est disponible (en anglais) "
        "<a href=\"https://sieversstudyhall.substack.com/p/genders-of-german-noun-from-a1-to\" target=\"_blank\">ici</a>."

        f"<br><br> &nbsp; {ICON_WARN} Il n’y a qu’une seule bonne réponse par question."

        "<h2>Exemple</h2>"
        "_____ Abend"
        "<br><br><i>Le soir</i>"
        f"<br><br> &nbsp; {ICON_CHECK} Der"
        f"<br><br> &nbsp; {ICON_CHECK} der"
    ,

    genus_goethe:
        "Pour chaque question, un nom allemand et sa traduction anglaise vous seront proposés."
        "<br><br>Trouvez l’article défini (Der, Die ou Das) qui correspond au nom."
        
        "<br><br>→ Un guide expliquant le genre des noms communs est disponible (en anglais) "
        "<a href=\"https://sieversstudyhall.substack.com/p/genders-of-german-noun-from-a1-to\" target=\"_blank\">ici</a>."

        f"<br><br> &nbsp; {ICON_WARN} Il n’y a qu’une seule bonne réponse par question."

        "<h2>Exemple</h2>"
        "_____ Abend"
        "<br><br><i>Le soir</i>"
        f"<br><br> &nbsp; {ICON_CHECK} Der"
        f"<br><br> &nbsp; {ICON_CHECK} der"
    ,

}
