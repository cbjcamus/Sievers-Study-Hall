from data.data_processing.units import (
    praepositionen, praepositionen_verben, praepositionen_adjektive, praepositionen_nomen, pronominaladverbien,
    artikel, pronomen, praepositionen_artikel, verben_artikel,
    konnektoren, fragen, adverbien, wortstellung, genus_regeln, genus, plural,
    adjektive, komparativ_superlativ, adjektivdeklinationen, adjektive_konjunktionen,
    verben, trennbare_verben, nomen_verben_verbindungen,
    praesens, imperativ, partizip_II, praeteritum, konjunktiv_II, konjunktiv_I, partizip_I,
    nomen_verben_wortstaemme, adjektive_verben_wortstaemme, adjektive_nomen_wortstaemme,
    zahlen, alpha,
)

INTRODUCTION_FR = {
    praepositionen:
        "Prépositions allemandes dans divers contextes. Vous trouverez un guide et un curriculum sur les prépositions allemandes"
        " <a href=\"https://sieversstudyhall.substack.com/p/guide-des-prepositions-allemandes\" target=\"_blank\">ici</a>."
    ,
    praepositionen_verben:
        "Paires verbe–préposition, en isolation et en contexte."
        "<br><br>Les adverbes pronominaux en <i>Da</i> et <i>Wo</i> se trouvent "
        "<a href=\"/pronominaladverbien\" target=\"_blank\">ici</a>."
    ,
    praepositionen_adjektive:
        "Paires adjectif–préposition, en isolation et en contexte."
    ,
    praepositionen_nomen:
        "Paires nom–préposition, en isolation et en contexte."
    ,
    pronominaladverbien:
        "Adverbes pronominaux en <i>da-</i> et en <i>wo-</i>."
    ,

    artikel:
        "Articles marinés dans tous les cas grammaticaux."
        "<br><br>Inclut : articles définis, indéfinis, négatifs, possessifs, démonstratifs et bien plus encore."
        "<br><br>Les cas grammaticaux régis par les prépositions et les verbes peuvent être pratiqués dans les modules "
        "<a href=\"/praepositionen_artikel\" target=\"_blank\">Präpositionen – Artikel</a> et "
        "<a href=\"/verben_artikel\" target=\"_blank\">Verben – Artikel</a>."
    ,
    pronomen:
        "Pronoms dans tous les cas grammaticaux."
        "<br><br>En fait non, pas de pronoms génitifs. Il y a des pronoms au génitif en latin,"
        " pourquoi pas en allemand ?"
        "<br><br>Inclut les pronoms réfléchis, relatifs, résolus, réceptifs, récents, récurrents et réconfortants."
    ,
    praepositionen_artikel:
        "Questions venant des autres exercices sur les prépositions pour s'exercer sur les cas grammaticaux régis par les prépositions allemandes."
        "<br><br>Rappel: "
        "<br>&bull; Prépositions suivies de l'accusatif : bis, durch, für, gegen, ohne, um"
        "<br>&bull; Prépositions suivies du datif : aus, bei, mit, nach, seit, von, zu"
        "<br>&bull; Prépositions suivies de l'accusatif ou du datif : an, auf, hinter, in, neben, unter, über, vor, zwischen"
        "<br>&bull; Prépositions suivies du génitif : anstatt, außerhalb, innerhalb, laut, trotz, während, wegen"
    ,
    verben_artikel:
        "Cas grammaticaux régis par les verbes."
    ,

    konnektoren:
        "Les conjonctions (ou éléments de liaison) incluent les conjonctions de coordination, les conjonctions de subordination, les conjonctions corrélatives et les adverbes qui relient des phrases entre elles."
        "<br><br>Les conjonctions utilisées avec des adjectifs sont pratiquées dans le module "
        "<a href=\"/adjektive_konjunktionen\" target=\"_blank\">Adjektive – Konjunktionen</a>, "
        "tandis que les pronoms relatifs sont pratiqués dans "
        "<a href=\"/pronomen\" target=\"_blank\">Pronomen</a>."
        "<br><br>⚠️ Les définitions suivantes sont utilisées :"
        "<br> &nbsp; &bull; Conjonction de coordination :"
        "<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Conjonction de coordination - Sujet - Verbe - COD"
        "<br> &nbsp; &bull; Conjonctions de subordination :"
        "<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Conjonctions de subordination - Sujet - COD - Verbe"
        "<br> &nbsp; &bull; Adverbe :"
        "<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Adverbe - Verbe - Sujet - COD"
        "<br> &nbsp; &bull; Conjonctions corrélatives :"
        "<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Ensemble de deux termes ou plus comme <i>um ... zu</i>, <i>entweder ... oder</i> ou <i>sowohl ... als auch</i>"
    ,
    fragen:
        "Mots interrogatifs tels que <i>Wer</i>, <i>Wann</i>, <i>Wo</i>, <i>Wie</i>, <i>Warum</i>, <i>Was</i>."
        "<br><br>Les mots interrogatifs en <i>Wo-</i> sont pratiqués dans le module "
        "<a href=\"/pronominaladverbien\" target=\"_blank\">Pronominaladverbien</a>."
    ,
    adverbien:
        "Adverbes temporels, locaux, et modaux à tous les niveaux. "
        "<br><br>Comprend des adverbes qui n'apparaissent pas dans les modules "
        "<a href=\"/konnektoren\" target=\"_blank\">Konnektoren</a> et "
        "<a href=\"/fragen\" target=\"_blank\">Fragen</a>."
    ,
    wortstellung:
        "Ordre des mots dans les phrases allemandes."
    ,

    verben:
        "Traduction du français vers l'allemand aux niveaux A1 et A2."
        "<br><br>Questions à choix multiple aux niveaux B1 et B2."
    ,
    trennbare_verben:
        "Verbes séparables et inséparables à traduire avec la racine ou le préfixe comme aide."
        "<br><br>La caractéristique la plus exotique de la langue allemande. La Piña Colada du Rhin. La Caipirinha de l'Elbe."
    ,
    nomen_verben_verbindungen:
        "Combinaisons nom-verbe et autres expressions."
    ,

    genus_regeln:
        "Pratiquez le genre des noms communs à l'aide de règles empiriques."
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
        "Forme plurielle des noms communs allemands les plus utilisés."
    ,

    adjektive:
        "Traductions d'adjectifs en isolation."
    ,
    komparativ_superlativ:
        "Comparatifs et superlatifs d'adjectifs."
    ,
    adjektivdeklinationen:
        "Déclensions d'adjectifs dans tous les cas grammaticaux, avec tous les genres et types d'articles."
    ,
    adjektive_konjunktionen:
        "Conjonctions et constructions pour adjectifs tels que <i>wie</i>, <i>als</i> et <i>so</i>."
    ,

    praesens:
        "Présent de l'indicatif allemand."
    ,
    partizip_II:
        "Participe passé utilisé pour le Perfekt, le Plusquamperfekt, le Futur II et la voix passive."
    ,
    praeteritum:
        "Préterit."
    ,
    imperativ:
        "Impératif pour les trois formes du, ihr et Sie."
    ,
    konjunktiv_II:
        "Le Konjunktiv II est utilisé notamment pour exprimer des situations hypothétiques, des souhaits, des suggestions et des demandes polies."
        "<br><br>Le temps préféré de la politesse."
    ,
    konjunktiv_I:
        "Le Konjunktiv I est utilisé pour exprimer un discours indirect ou rapporté."
        "<br><br>Le temps préféré des journalistes."
    ,
    partizip_I:
        "Le participe présent est utilisé pour exprimer des actions en cours."
        "<br><br>Mais pourquoi utiliser le participe présent alors que vous pourriez utiliser une proposition relative ?"
        "<br><br>De plus, vous devriez le décliner comme un adjectif. Quelle galère."
    ,

    nomen_verben_wortstaemme:
        "Paires nom-verbe avec la même racine étymologique."
    ,
    adjektive_verben_wortstaemme:
        "Paires adjectif-verbe avec la même racine étymologique."
    ,
    adjektive_nomen_wortstaemme:
        "Paires adjectif-nom commun avec la même racine étymologique."
    ,

    zahlen:
        "Les nombres sous toutes leurs formes, y compris les nombres cardinaux, ordinaux, séquentiels, adverbiaux, fractionnaires et multiplicateurs."
    ,
    alpha:
        "Environnement de test."
    ,

}
