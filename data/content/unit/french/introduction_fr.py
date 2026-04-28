from data.data_processing.units import (
    praepositionen, praepositionen_verben, praepositionen_adjektive, praepositionen_nomen, pronominaladverbien,
    artikel, pronomen, praepositionen_artikel, verben_artikel,
    konnektoren, fragen, adverbien, genus_regeln, genus, plural,
    adjektive, komparativ_superlativ, adjektivdeklinationen, adjektive_konjunktionen,
    verben, trennbare_verben, nomen_verben_verbindungen,
    praesens, imperativ, partizip_II, praeteritum, praeteritum_partizip_II, konjunktiv_II, konjunktiv_I, partizip_I,
    nomen_verben_wortstaemme, adjektive_verben_wortstaemme, adjektive_nomen_wortstaemme,
    zahlen,
)

INTRODUCTION_FR = {
    praepositionen:
        "Prépositions Allemandes dans divers contextes. Vous trouverez un guide et un curriculum sur les prépositions allemandes"
        " <a href=\"https://sieversstudyhall.substack.com/p/guide-des-prepositions-allemandes\" target=\"_blank\">ici</a>."
    ,
    praepositionen_verben:
        "Paires Verbe–Préposition, en isolation et en contexte."
        "<br><br>Les adverbes pronominaux en <i>Da</i> et <i>Wo</i> se trouvent "
        "<a href=\"/pronominaladverbien\" target=\"_blank\">ici</a>."
    ,
    praepositionen_adjektive:
        "Paires Adjectif–Préposition, en isolation et en contexte."
    ,
    praepositionen_nomen:
        "Paires Nom–Préposition, en isolation et en contexte."
    ,
    pronominaladverbien:
        "Adverbes pronominaux en <i>Da-</i> et en <i>Wo-</i>."
    ,

    artikel:
        "Articles marinés dans tous les cas grammaticaux."
        "<br><br>Inclut: articles définis, indéfinis, négatifs, possessifs, démonstratifs et bien plus encore."
        "<br><br>Les cas grammaticaux suivant les prépositions et verbes peuvent être pratiquées dans les modules "
        "<a href=\"/praepositionen_artikel\" target=\"_blank\">Präpositionen – Artikel</a> et "
        "<a href=\"/verben_artikel\" target=\"_blank\">Verben – Artikel</a>."
    ,
    pronomen:
        "Pronoms dans tous les cas grammaticaux."
        "<br><br>En fait non, pas de pronoms génitifs. Il y a des pronoms génitifs dans le Latin,"
        " pourquoi pas en Allemand ?"
        "<br><br>Inclut les pronoms réfléchis, relatifs, résolus, réceptifs, récents, récurrents et réconfortants."
    ,
    praepositionen_artikel:
        "Questions venant des autres exercises sur les prépositions pour s'exercer sur les cas grammaticaux suivant les prépositions allemandes."
        "<br><br>Rappel:"
        "<br>&bull; Prépositions suivies par l'Accusatif: bis, durch, für, gegen, ohne, um"
        "<br>&bull; Prépositions suivies par le Datif: aus, bei, mit, nach, seit, von, zu"
        "<br>&bull; Prépositions suivies par l'Accusatif ou le Datif: an, auf, hinter, in, neben, unter, über, vor, zwischen"
        "<br>&bull; Prépositions suivies par le Génitif: anstatt, außerhalb, innerhalb, laut, trotz, während, wegen"
    ,
    verben_artikel:
        "Cas grammaticaux suivant les Verbes."
    ,

    konnektoren:
        "Les connecteurs incluent les conjonction de coordination, les conjonctions de subordination, les conjonctions corrélatives et les adverbes qui relient des phrases entre elles."
        "<br><br>Les conjonctions utilisées avec des adjectifs sont pratiquées dans le module <a href=\"/adjektive_konjunktionen\" target=\"_blank\">Adjektive – Konjunktionen</a>."
        "<br><br>⚠️ Les définitions suivantes sont utilisées:"
        "<br> &nbsp; &bull; Conjonction de coordination:"
        "<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Conjonction de coordination - Sujet - Verbe - COD"
        "<br> &nbsp; &bull; Conjonctions de subordination:"
        "<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Conjonctions de subordination - Sujet - COD - Verbe"
        "<br> &nbsp; &bull; Adverbe:"
        "<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Adverbe - Verbe - Subjet - COD"
        "<br> &nbsp; &bull; Conjonction corrélatives:"
        "<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Set de deux termes ou plus comme <i>um zu</i>, <i>entweder oder</i> ou <i>sowohl als auch</i>"
    ,
    fragen:
        "Mots interrogatifs tels que <i>Wer</i>, <i>Wann</i>, <i>Wo</i>, <i>Wie</i>, <i>Warum</i>, <i>Was</i>."
        "<br><br>Les mots interrogatifs en <i>Wo-</i> sont pratiquées dans le module "
        "<a href=\"/pronominaladverbien\" target=\"_blank\">Pronominaladverbien</a>."
    ,
    adverbien:
        "Adverbes temporels, locaux, et modaux à tous les niveaux."
        "Comprend des adverbes qui n'apparaissent pas dans les modules "
        "<a href=\"/konnektoren\" target=\"_blank\">Konnektoren</a> et "
        "<a href=\"/fragen\" target=\"_blank\">Fragen</a>."
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
        "Combinaisons Nom-Verbe et autres expressions."
    ,

    genus_regeln:
        "Pratiquez le genre des noms communs à l'aide d'heuristiques."
        "<br><br>Un guide énumérant ces heuristiques est disponible "
        "<a href=\"https://sieversstudyhall.substack.com/p/genders-of-german-noun-from-a1-to\" target=\"_blank\">ici</a> (en anglais)."
        "<br><br>Une fois ces exercices terminés, vous pouvez continuer à vous entraîner avec d'autres noms "
        "<a href=\"/genus\" target=\"_blank\">ici</a>."
    ,
    genus:
        "Doux désirs dérivent, dansant dès l’aube claire,"
        "<br>Des doutes disparaissent, le destin se déclare,"
        "<br>Des voix décidées dessinent leurs pas,"
        "<br>Der, Die, Das."
        "<br><br>Je recommande de s'exercer avec le module <a href=\"/genus_regeln\" target=\"_blank\">Genus – Regeln</a> avant de s'attaquer à ces exercices."
    ,
    plural:
        "Forme Plurielle des noms communs allemands les plus utilisés."
    ,

    adjektive:
        "Traductions d'adjectifs en isolation."
    ,
    komparativ_superlativ:
        "Comparatifs et Superlatifs d'Adjectifs."
    ,
    adjektivdeklinationen:
        "Déclinations d'adjectifs dans tous les cas grammaticaux, avec tous les genres et types d'articles."
    ,
    adjektive_konjunktionen:
        "Conjonctions et Constructions pour adjectifs tels que <i>wie</i>, <i>als</i> et <i>so</i>."
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

    nomen_verben_wortstaemme:
        "Paires Nom-Verbe avec la même racine étymologique."
    ,
    adjektive_verben_wortstaemme:
        "Paires Adjectif-Verbe avec la même racine étymologique."
    ,
    adjektive_nomen_wortstaemme:
        "Paires Adjectif-Nom commun avec la même racine étymologique."
    ,

    zahlen:
        "Les nombres sous toutes leurs formes, y compris les nombres cardinaux, ordinaux, séquentiels, adverbiaux, fractionnaires et multiplicateurs."
    ,

}
