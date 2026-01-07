from data.data_processing.units import (
    praepositionen_grammatik, praepositionen_verben, praepositionen_adjektive, praepositionen_nomen,
    praepositionen_adverbien, praepositionen_artikel,
    artikel, pronomen, konnektoren, fragen, adverbien,
    adjektive, adjektivdeklinationen, adjektive_konjunktionen,
    verben, trennbare_verben, nomen_verben_verbindungen,
    praesens, imperativ, partizip_II, praeteritum, praeteritum_partizip_II, konjunktiv_II, konjunktiv_I, partizip_I,
    genus_regeln, genus_routledge, genus_goethe,
)

INTRODUCTION_FR = {
    praepositionen_grammatik:
        "Prépositions Allemandes dans divers contextes. Vous trouverez un guide et un curriculum sur les prépositions allemandes"
        " <a href=\"https://sieversstudyhall.substack.com/p/guide-des-prepositions-allemandes\" target=\"_blank\">ici</a>."
    ,
    praepositionen_verben:
        "Paires Verbe–Préposition, en isolation et en contexte."
        "<br><br>Inclu les adverbes pronominaux en <i>Da</i> et <i>Wo</i> au niveau A2."
    ,
    praepositionen_adjektive:
        "Paires Adjectif–Préposition, en isolation et en contexte."
    ,
    praepositionen_nomen:
        "Paires Nom–Préposition, en isolation et en contexte."
    ,
    praepositionen_adverbien:
        "Je plaisante, ça n'existe pas."
    ,
    praepositionen_artikel:
        "Questions venant des autres exercises sur les prépositions pour s'exercer sur les cas grammaticaux suivant les prépositions allemandes."
        "<br><br>Rappel:"
        "<br>&bull; Prépositions suivies par l'Accusatif: Bis, Durch, Für, Ohne, Gegen, Um"
        "<br>&bull; Prépositions suivies par le Datif: Aus, Bei, Mit, Seit, Nach, Von, Zu"
        "<br>&bull; Prépositions suivies par l'Accusatif ou le Datif: An, Auf, In, Hinter, Vor, Über, Unter, Neben, Zwischen"
    ,

    artikel:
        "Articles marinés dans tous les cas grammaticaux."
        "<br><br>Inclu: articles définis, indéfinis, négatifs, possessifs, demonstratifs et bien plus encore."
        "<br><br>Si vous avez des maux de tête, cela signifie que vous apprenez."
    ,
    pronomen:
        "Pronoms dans tous les cas grammaticaux."
        "<br><br>En fait non, pas de pronoms génitifs. Il y a des pronoms génitifs dans le Latin,"
        " pourquoi pas en Allemand ?"
        "<br><br>Inclu les pronoms réflechis, relatifs, résolus, réceptifs, récents, récurrents et réconfortants."
    ,
    konnektoren:
        "Les connecteurs incluent les conjonction de coordination, les conjonctions de subordination, les conjonctions corrélatives et les adverbes qui relient des phrases entre elles."
        "<br><br>⚠️ Les définitions suivantes sont utilisées:"
        "<br> &nbsp; &bull; Conjonction de coordination:"
        "<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Conjonction de coordination – Sujet – Verbe – COD"
        "<br> &nbsp; &bull; Conjonctions de subordination:"
        "<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Conjonctions de subordination – Sujet – COD – Verbe"
        "<br> &nbsp; &bull; Adverbe:"
        "<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Adverbe – Verbe – Subjet – COD"
        "<br> &nbsp; &bull; Conjonction corrélatives:"
        "<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Set de deux termes ou plus comme <i>um zu</i>, <i>entweder oder</i> ou <i>sowohl als auch</i>"
    ,
    fragen:
        "Mots interrogatifs."
        "<br><br>Utiles principalement aux niveaux A1 et A2. Les exercises aux niveaux B1, B2 et C1 ont été créés par exhaustivité."
    ,
    adverbien:
        "Adverbes temporels, locaux, et modaux à tous les niveaux."
    ,

    adjektive:
        "Traductions, antonymes, comparatifs et superlatifs d'adjectifs en isolation."
    ,
    adjektivdeklinationen:
        "Déclinations d'adjectifs dans tous les cas grammaticaux, avec tous les genres et types d'articles."
    ,
    adjektive_konjunktionen:
        "Conjonctions et Constructions pour adjectifs tels que <i>wie</i>, <i>als</i> et <i>so</i>."
    ,

    verben:
        "Traduction du Français vers l'Allemand aux niveaux A1 et A2."
        "<br><br>Questions à Choix-Multiple aux niveaux B1 et B2."
    ,
    trennbare_verben:
        "Verbes séparables et inséparables à traduire avec la racine ou le préfixe comme aide."
        "<br><br>La caractéristique la plus exotique de la langue Allemande. La Piña Colada du Rhin. La Caipirinha de l'Elbe."
    ,
    nomen_verben_verbindungen:
        "Combinaisons nom-verbe commençant au niveau B1."
        "<br><br>Par souci d'exhaustivité, j'utilise une définition large de Nomen-Verben Verbindungen, "
        "qui incluent des combinaisons telles que <i>Lust haben</i> ou <i>Angst haben</i>."
    ,

    praesens:
        "Présent de l'indicatif Allemand."
    ,
    partizip_II:
        "Participe Passé utilisé pour le Perfekt, le Plus-quam-perfekt, le Future II et la forme Passive."
    ,
    praeteritum:
        "Préterit."
    ,
    praeteritum_partizip_II:
        "Exercices pour pratiquer le Participe Passé et le Préterit côte-à-côte."
    ,
    imperativ:
        "Impératif pour les trois personnes grammaticales Du, Ihr et Sie. "
    ,
    konjunktiv_II:
        "Le Konjunktiv II est utilisé pour exprimer le mode subjonctif, les suggestions et les souhaits."
        "<br><br>Le temps préféré de la politesse."
    ,
    konjunktiv_I:
        "Le Konjunktiv I est utilisé pour exprimer un discours indirect ou rapporté."
        "<br><br>Le temps préféré des journalistes."
    ,
    partizip_I:
        "Le participe présent est utilisé pour exprimer des actions en cours."
        "<br><br>Mais pourquoi utiliser le participe présent alors que vous pourriez utiliser une proposition relative ?"
        "<br><br>De plus, vous devriez le décliner comme le reste des adjectifs. Quelle galère."
    ,

    genus_regeln:
        "Practiquez le genre des noms communs à l'aide d'heuristiques."
        "<br><br>Un guide énumérant ces heuristiques est disponible "
        "<a href=\"https://sieversstudyhall.substack.com/p/genders-of-german-noun-from-a1-to\" target=\"_blank\">ici</a> (en anglais)."
    ,
    genus_routledge:
        "Doux désirs dérivent, dansant dès l’aube claire,"
        "<br>Des doutes disparaissent, le destin se déclare,"
        "<br>Des voix décidées dessinent leurs pas,"
        "<br>Der Die Das."
        "<br><br>La liste des noms communs vient de "
        "<a href=\"https://docs.google.com/spreadsheets/d/1r9HwvVpo35MFxnJ_5W6RKlDfx5VzmQVcnpJTgrNUY9I/edit?gid=1814339112#gid=1814339112\" target=\"_blank\">ici</a>."
    ,
    genus_goethe:
        "Une Dance de Der Die Das."
        "<br><br>La liste des noms communs vient du "
        "<a href=\"https://www.goethe.de/pro/relaunch/prf/de/A1_SD1_Wortliste_02.pdf\" target=\"_blank\">Goethe Institut</a>."
    ,
}
