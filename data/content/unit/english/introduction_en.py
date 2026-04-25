from data.data_processing.units import (
    praepositionen, praepositionen_verben, praepositionen_adjektive, praepositionen_nomen, pronominaladverbien,
    artikel, pronomen, praepositionen_artikel, verben_artikel,
    konnektoren, fragen, adverbien, wortstellung,
    genus_regeln, genus, plural,
    adjektive, komparativ_superlativ, adjektivdeklinationen, adjektive_konjunktionen,
    verben, trennbare_verben, nomen_verben_verbindungen,
    praesens, imperativ, partizip_II, praeteritum, praeteritum_partizip_II, konjunktiv_II, konjunktiv_I, partizip_I,
    nomen_verben_wortstaemme, adjektive_verben_wortstaemme, adjektive_nomen_wortstaemme,
    zahlen,
)

INTRODUCTION_EN = {
    praepositionen:
        "Prepositions in Temporal, Local, Modal and Causal contexts. You can find a guide and curriculum for German preposition <a href=\"https://sieversstudyhall.substack.com/p/basic-german-prepositions-uses-up\" target=\"_blank\">here</a>."
        "<br><br>Happy suffering 🥰😍😘."
    ,
    praepositionen_verben:
        "Verb-Preposition pairs."
        "<br><br>Exercises for pronominal adverbs in <i>Da</i> and <i>Wo</i> can be found "
        "<a href=\"/pronominaladverbien\" target=\"_blank\">here</a>."
    ,
    praepositionen_adjektive:
        "Adjective-Preposition pairs."
        "<br><br>Think of it as Verb's pretentious sister."
    ,
    praepositionen_nomen:
        "Noun-Preposition pairs."
        "<br><br>Verb's and Adjective's younger brother. The annoying one."
    ,
    pronominaladverbien:
        "Pronominal adverbs in <i>Da-</i> and in <i>Wo-</i>."
        "<br><br>Feel free to check the following guides for "
        "<a href=\"https://yourdailygerman.com/da-words-meaning-german/\" target=\"_blank\">Da-words</a> and "
        "<a href=\"https://yourdailygerman.com/german-wo-comounds-explained/\" target=\"_blank\">Wo-words</a> written by Emanuel from "
        "<a href=\"https://yourdailygerman.com/\" target=\"_blank\">YourDailyGerman</a>."
    ,

    artikel:
        "Articles marinated in every grammatical cases."
        "<br><br>Includes definite, indefinite, negative, possessive, demonstrative articles and much more."
        "<br><br>You can practice the grammatical cases that follow prepositions and verbs in the modules "
        "<a href=\"/praepositionen_artikel\" target=\"_blank\">Präpositionen – Artikel</a> and "
        "<a href=\"/verben_artikel\" target=\"_blank\">Verben – Artikel</a>."
        "<br><br>If you get headaches, it means you're learning."
    ,
    pronomen:
        "Pronouns in every grammatical cases."
        "<br><br>Not genitive though, there are no genitive pronoun in German. Latin does have genitive pronouns,"
        " why not german?"
        "<br><br>Includes reflexive, relative, relentless, reliable, and resolute pronouns."
    ,
    praepositionen_artikel:
        "All the questions come from other Präpositionen exercises and updated to practice cases following prepositions."
        "<br><br>Reminder:"
        "<br>&bull; Followed by the Accusative case: bis, durch, für, gegen, ohne, um"
        "<br>&bull; Followed by the Dative case: aus, bei, mit, nach, seit, von, zu"
        "<br>&bull; Followed by the Dative or the Accusative case: an, auf, hinter, in, neben, unter, über, vor, zwischen"
        "<br>&bull; Followed by the Genitive case: anstatt, außerhalb, innerhalb, laut, trotz, während, wegen"
    ,
    verben_artikel:
        "Cases following Verbs."
    ,

    konnektoren:
        "Connectors include coordinating conjunctions, subordinating conjunctions, correlative conjunctions and adverbs that connect two sentences together."
        "<br><br>Conjunctions used with adjectives are done in <a href=\"/adjektive_konjunktionen\" target=\"_blank\">Adjektive – Konjunktionen</a>."
        "<br><br>⚠️ The following definitions are used:"
        "<br> &nbsp; &bull; Coordinating conjunction:"
        "<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Coordinating conjunction - Subject - Verb - Object"
        "<br> &nbsp; &bull; Subordinating conjunction:"
        "<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Subordinating conjunction - Subject - Object - Verb"
        "<br> &nbsp; &bull; Adverb:"
        "<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Adverb - Verb - Subject - Object"
        "<br> &nbsp; &bull; Correlative conjunction:"
        "<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Two or more terms such as <i>um zu</i>, <i>entweder oder</i> or <i>sowohl als auch</i>"
    ,
    fragen:
        "Question words such as <i>Wer</i>, <i>Wann</i>, <i>Wo</i>, <i>Wie</i>, <i>Warum</i>, <i>Was</i>."
        "<br><br>Question words in <i>Wo-</i> are done in "
        "<a href=\"/pronominaladverbien\" target=\"_blank\">Pronominaladverbien</a>."
        "<br><br>Wo means Where and Wer means Who. Hope it makes sense."
    ,
    adverbien:
        "Adverbs, including a mix of Temporal, Local, and Modal ones at each level – Causal adverbs are done in Konnektoren."
        "<br><br>Features adverbs not seen in "
        "<a href=\"/konnektoren\" target=\"_blank\">Konnektoren</a> and "
        "<a href=\"/fragen\" target=\"_blank\">Fragen</a>."
    ,
    wortstellung:
        ""
    ,

    genus_regeln:
        "Practice the gender of nouns based on thumb rules."
        "<br><br>A guide listing these thumb rules is available "
        "<a href=\"https://sieversstudyhall.substack.com/p/genders-of-german-noun-from-a1-to\" target=\"_blank\">here</a>."
        "<br><br>Once you've finished these exercises, you can continue practicing with more nouns "
        "<a href=\"/genus\" target=\"_blank\">here</a>."
    ,
    genus:
        "Deep dreams drift, daring dusk to dance"
        "<br>Dark doubts dissolve, daylight dares advance:"
        "<br>Determined voices decide, declare, and pass,"
        "<br>Der, Die, Das."
        "<br><br> I recommend practicing with the module <a href=\"/genus_regeln\" target=\"_blank\">Genus – Regeln</a> before tackling these exercises."
    ,
    plural:
        "Plurals of common German nouns."
    ,

    adjektive:
        "Adjectives translations in isolation."
    ,
    komparativ_superlativ:
        "Adjectives' comparative and superlative forms."
    ,
    adjektivdeklinationen:
        "Adjective Declensions in every grammatical cases, persons, and articles."
        "<br><br>I hated that in French when I was a kid and it's even worse in German."
        "<br><br>If it was up to me, Adjective Declensions wouldn't start before C1."
    ,
    adjektive_konjunktionen:
        "Conjunctions and Constructions for adjectives such as <i>wie</i>, <i>als</i> and <i>so</i>."
    ,

    verben:
        "English to German verb translation exercises at A1 and A2."
        "<br><br>Multiple-choice questions at B1 and B2, with both English to German and German to English translations."
    ,
    trennbare_verben:
        "Separable and Inseparable verbs to translate from English with either the root or the prefix as an help."
        "<br><br>The most exotic feature of the German language. The Piña Colada of the Rhine. The Caipirinha of the Elbe."
    ,
    nomen_verben_verbindungen:
        "Noun-Verb Combinations and other idioms."
    ,

    praesens:
        "Present tense for each grammatical person."
    ,
    partizip_II:
        "Past Participle used in the Perfekt, Plusquamperfekt, Future II and the Passive voice."
        "<br><br>I wrote the first script that later became this website to practice the Partizip II."
    ,
    praeteritum:
        "Preterit tense."
        "<br><br>Available for each grammatical person for the most important verbs, "
        "then only the 3<sup>rd</sup> singular person is required."
    ,
    praeteritum_partizip_II:
        "Exercise to practice the Präteritum and Partizip II together."
    ,
    imperativ:
        "Imperative for the three grammatical persons Du, Ihr and Sie."
        "<br><br>Scream at cyclists, the printer that doesn't work,"
        " and your toe that hits a piece of furniture the right way."
    ,
    konjunktiv_II:
        "Konjunktiv II is used to express the subjunctive mood, suggestions and wishes."
        "<br><br>Politeness' favorite tense."
    ,
    konjunktiv_I:
        "Konjunktiv I is used to express an indirect or reported speech."
        "<br><br>Journalists' favorite tense."
    ,
    partizip_I:
        "Partizip I is used to express ongoing actions."
        "<br><br>But why use the Partizip I when you could use a relative clause?"
        "<br><br>Also you would have to decline it as an adjective. What a mess."
    ,

    nomen_verben_wortstaemme:
        "Noun-Verb Pairs with the same etymological root."
    ,
    adjektive_verben_wortstaemme:
        "Adjective-Verb Pairs with the same etymological root."
    ,
    adjektive_nomen_wortstaemme:
        "Adjective-Noun Pairs with the same etymological root."
    ,

    zahlen:
        "Numbers in all their forms, including cardinal, ordinal, sequential, adverbial, fractional and multiplier."
    ,
}
