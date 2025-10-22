from data.data_processing.units import (
    praepositionen_grammatik, praepositionen_verben, praepositionen_adjektive, praepositionen_nomen,
    praepositionen_artikel,
    artikel, artikel_genus, pronomen, konnektoren, fragen, adverbien,
    adjektive, adjektivdeklinationen,
    trennbare_verben, verben,
    praesens, imperativ, partizip_II, praeteritum, praeteritum_partizip_II, konjunktiv_II, konjunktiv_I, partizip_I,
)

from webapp.style.icons import ICON_CHECK, ICON_CROSS, ICON_WARN

# bullet point \u25CF

GUIDANCE_UNIT_FR = {
    artikel_genus:
        "Pour chaque question, un nom allemand et sa traduction anglaise vous seront proposés."
        "<br><br>Trouvez l’article défini (Der, Die ou Das) qui correspond au nom."

        f"<br><br>{ICON_WARN} Il n’y a qu’une seule bonne réponse par question."

        "<h2>Exemple</h2>"
        "_____ Abend"
        "<br><br><i>Le soir</i>"
        f"<br><br>{ICON_CHECK} Der"
        f"<br><br>{ICON_CHECK} der"
    ,

    praepositionen_artikel:
        "Pour chaque question, une phrase allemande incomplète et sa traduction anglaise vous seront proposées."
        "<br><br>Complétez la phrase allemande avec l’article ou le pronom approprié."

        f"<br><br>{ICON_WARN} Il n’y a qu’une seule bonne réponse par question."

        "<h2>Exemple</h2>"
        "Das Bild hängt an _____ Tür."
        "<br><br><i>Le tableau est accroché à la porte.</i>"
        f"<br><br>{ICON_CHECK} der"
    ,

    praesens:
        "Pour chaque question, vous verrez un verbe allemand accompagné d’un pronom personnel."
        "<br>Conjuguez le verbe au présent pour ce pronom."

        f"<br><br>{ICON_WARN} N’écrivez pas le pronom personnel, sinon votre réponse sera considérée comme incorrecte."
        f"<br><br>{ICON_WARN} N’écrivez pas de pronom réfléchi, même si le verbe est habituellement réfléchi."

        "<h2>Exemple</h2>"
        "freuen \u25CF Ich"
        f"<br><br>{ICON_CHECK} freue"
        f"<br><br>{ICON_CROSS} Ich freue"
        f"<br><br>{ICON_CROSS} freue mich"
    ,

    partizip_II:
        "Pour chaque question, vous verrez un verbe allemand."
        "<br>Indiquez le Partizip II (participe passé) du verbe donné."

        f"<br><br>{ICON_WARN} N’écrivez pas d’auxiliaire, sinon votre réponse sera considérée comme incorrecte."
        f"<br><br>{ICON_WARN} N’écrivez pas de pronom réfléchi, même si le verbe est habituellement réfléchi."

        "<h2>Exemple</h2>"
        "freuen"
        f"<br><br>{ICON_CHECK} gefreut"
        f"<br><br>{ICON_CROSS} sich gefreut"
        f"<br><br>{ICON_CROSS} hat gefreut"
    ,

    praeteritum:
        "Pour chaque question, vous verrez un verbe allemand."
        "<br>Conjuguez le verbe au Präteritum (prétérit) à la 3ᵉ personne du singulier (Er/Sie/Es) du verbe donné."

        f"<br><br>{ICON_WARN} N’écrivez pas le pronom personnel, sinon votre réponse sera considérée comme incorrecte."
        f"<br><br>{ICON_WARN} N’écrivez pas de pronom réfléchi, même si le verbe est habituellement réfléchi."

        "<h2>Exemple</h2>"
        "freuen"
        f"<br><br>{ICON_CHECK} freute"
        f"<br><br>{ICON_CROSS} freute sich"
        f"<br><br>{ICON_CROSS} er freute"
    ,

    praeteritum_partizip_II:
        "Pour chaque question, vous verrez un verbe allemand."
        "<br>Indiquez le Präteritum (prétérit) à la 3ᵉ personne du singulier (Er/Sie/Es) ainsi que le Partizip II (participe passé) du verbe donné."

        f"<br><br>{ICON_WARN} Séparez le Präteritum et le Partizip II par un espace ou par une virgule suivie d’un espace."
        f"<br><br>{ICON_WARN} N’écrivez pas le pronom personnel, sinon votre réponse sera considérée comme incorrecte."
        f"<br><br>{ICON_WARN} N’écrivez pas d’auxiliaire, sinon votre réponse sera considérée comme incorrecte."
        f"<br><br>{ICON_WARN} N’écrivez pas de pronom réfléchi, même si le verbe est habituellement réfléchi."

        "<h2>Exemple</h2>"
        "freuen"
        f"<br><br>{ICON_CHECK} freute, gefreut"
        f"<br><br>{ICON_CHECK} freute gefreut"
        f"<br><br>{ICON_CROSS} freute, hat gefreut"
        f"<br><br>{ICON_CROSS} er freute, gefreut"
        f"<br><br>{ICON_CROSS} freute sich, sich gefreut"
    ,

    imperativ:
        "Pour chaque question, vous verrez un verbe allemand accompagné d’un pronom personnel."
        "<br>Conjuguez le verbe à l’impératif pour ce pronom."

        f"<br><br>{ICON_WARN} Écrivez les pronoms personnels uniquement dans le cas de la 3ᵉ personne du pluriel."
        f"<br><br>{ICON_WARN} N’écrivez pas de pronom réfléchi, même si le verbe est habituellement réfléchi."

        "<h2>Exemple</h2>"
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
        "Pour chaque question, vous verrez un verbe allemand accompagné d’un pronom personnel."
        "<br>Conjuguez le verbe au Konjunktiv II (subjonctif II) pour ce pronom."

        f"<br><br>{ICON_WARN} N’écrivez pas le pronom personnel, sinon votre réponse sera considérée comme incorrecte."

        "<h2>Exemple</h2>"
        "sein \u25CF Du"
        f"<br><br>{ICON_CHECK} wärest"
        f"<br><br>{ICON_CROSS} Du wärest"
    ,

    konjunktiv_I:
        "Pour chaque question, vous verrez un verbe allemand accompagné d’un pronom personnel."
        "<br>Conjuguez le verbe au Konjunktiv I (subjonctif I) pour ce pronom."

        f"<br><br>{ICON_WARN} N’écrivez pas le pronom personnel, sinon votre réponse sera considérée comme incorrecte."

        "<h2>Exemple</h2>"
        "sein \u25CF Du"
        f"<br><br>{ICON_CHECK} seiest"
        f"<br><br>{ICON_CROSS} Du seiest"
    ,

    partizip_I:
        "Pour chaque question, vous verrez un verbe allemand."
        "<br>Indiquez le Partizip I (participe présent) du verbe donné."

        f"<br><br>{ICON_WARN} N’écrivez pas de pronom réfléchi, même si le verbe est habituellement réfléchi."

        "<h2>Exemple</h2>"
        "freuen"
        f"<br><br>{ICON_CHECK} freuend"
        f"<br><br>{ICON_CROSS} sich freuend"
    ,
}
