from data.data_processing.units import (
    praepositionen, praepositionen_verben, praepositionen_adjektive, praepositionen_nomen, pronominaladverbien,
    artikel, pronomen, praepositionen_artikel, verben_artikel,
    konnektoren, fragen, adverbien, wortstellung,
    genus_regeln, genus, plural,
    adjektive, komparativ_superlativ, adjektivdeklinationen, adjektive_konjunktionen,
    verben, trennbare_verben, nomen_verben_verbindungen,
    praesens, imperativ, partizip_II, praeteritum, konjunktiv_II, konjunktiv_I, partizip_I,
    nomen_verben_wortstaemme, adjektive_verben_wortstaemme, adjektive_nomen_wortstaemme,
    zahlen, alpha,
)

INTRODUCTION_EN = {
    praepositionen:
        "Prepositions in temporal, local, modal and causal contexts. You can find a guide and curriculum for German prepositions <a href=\"https://sieversstudyhall.substack.com/p/basic-german-prepositions-uses-up\" target=\"_blank\">here</a>."
        "<br><br>Happy suffering 🥰😍😘."
    ,
    praepositionen_verben:
        "Verb-Preposition pairs."
        "<br><br>Exercises for pronominal adverbs in <i>Da</i> and <i>Wo</i> can be found "
        "<a href=\"/pronominaladverbien\" target=\"_blank\">here</a>."
    ,
    praepositionen_adjektive:
        "Adjective-Preposition pairs."
        "<br><br>Think of it as the verb's pretentious sister."
    ,
    praepositionen_nomen:
        "Noun-Preposition pairs."
        "<br><br>The verb's and adjective's younger brother. The annoying one."
    ,
    pronominaladverbien:
        "Pronominal adverbs in <i>Da-</i> and in <i>Wo-</i>."
        "<br><br>Feel free to check the following guides for "
        "<a href=\"https://yourdailygerman.com/da-words-meaning-german/\" target=\"_blank\">Da-words</a> and "
        "<a href=\"https://yourdailygerman.com/german-wo-comounds-explained/\" target=\"_blank\">Wo-words</a> written by Emanuel from "
        "<a href=\"https://yourdailygerman.com/\" target=\"_blank\">YourDailyGerman</a>."
    ,

    artikel:
        "Articles marinated in every grammatical case."
        "<br><br>Includes definite, indefinite, negative, possessive, demonstrative articles and much more."
        "<br><br>You can practice the grammatical cases that follow prepositions and verbs in the modules "
        "<a href=\"/praepositionen_artikel\" target=\"_blank\">Präpositionen – Artikel</a> and "
        "<a href=\"/verben_artikel\" target=\"_blank\">Verben – Artikel</a>."
        "<br><br>If you get headaches, it means you're learning."
    ,
    pronomen:
        "Pronouns in every grammatical case."
        "<br><br>Not genitive though, there are no genitive pronouns in German. Latin does have genitive pronouns,"
        " why not German?"
        "<br><br>Includes reflexive, relative, relentless, reliable, and resolute pronouns."
    ,
    praepositionen_artikel:
        "All the questions come from other Präpositionen exercises and have been updated to practice cases following prepositions."
        "<br><br>Reminder:"
        "<br>&bull; Followed by the Accusative case: bis, durch, für, gegen, ohne, um"
        "<br>&bull; Followed by the Dative case: aus, bei, mit, nach, seit, von, zu"
        "<br>&bull; Followed by the Dative or the Accusative case: an, auf, hinter, in, neben, unter, über, vor, zwischen"
        "<br>&bull; Followed by the Genitive case: anstatt, außerhalb, innerhalb, laut, trotz, während, wegen"
    ,
    verben_artikel:
        "Cases following verbs."
    ,

    konnektoren:
        "Connectors include coordinating conjunctions, subordinating conjunctions, correlative conjunctions and adverbs that connect two sentences."
        "<br><br>Conjunctions used with adjectives are covered in "
        "<a href=\"/adjektive_konjunktionen\" target=\"_blank\">Adjektive – Konjunktionen</a>, "
        "while relative pronouns are done in <a href=\"/pronomen\" target=\"_blank\">Pronomen</a>."
        "<br><br>⚠️ The following definitions are used:"
        "<br> &nbsp; &bull; Coordinating conjunction:"
        "<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Coordinating conjunction - Subject - Verb - Object"
        "<br> &nbsp; &bull; Subordinating conjunction:"
        "<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Subordinating conjunction - Subject - Object - Verb"
        "<br> &nbsp; &bull; Adverb:"
        "<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Adverb - Verb - Subject - Object"
        "<br> &nbsp; &bull; Correlative conjunction:"
        "<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Two or more terms such as <i>um ... zu</i>, <i>entweder ... oder</i> or <i>sowohl ... als auch</i>"
    ,
    fragen:
        "Question words such as <i>Wer</i>, <i>Wann</i>, <i>Wo</i>, <i>Wie</i>, <i>Warum</i>, <i>Was</i>."
        "<br><br>Question words in <i>Wo-</i> are done in "
        "<a href=\"/pronominaladverbien\" target=\"_blank\">Pronominaladverbien</a>."
        "<br><br>Wo means \"where\" and Wer means \"who\". Hope it makes sense."
    ,
    adverbien:
        "Adverbs, including a mix of temporal, local, and modal ones at each level – causal adverbs are done in Konnektoren."
        "<br><br>Features adverbs not seen in "
        "<a href=\"/konnektoren\" target=\"_blank\">Konnektoren</a> and "
        "<a href=\"/fragen\" target=\"_blank\">Fragen</a>."
    ,
    wortstellung:
        "Word Order in German sentences."
        "<br><br>You can check my guide to German word order <a href=\"https://sieversstudyhall.substack.com/p/guide-to-german-word-order-draft\" target=\"_blank\">here</a> (currently a draft)."
    ,

    genus_regeln:
        "Practice the gender of nouns based on rules of thumb."
        "<br><br>A guide listing these rules of thumb is available "
        "<a href=\"https://sieversstudyhall.substack.com/p/genders-of-german-noun-from-a1-to\" target=\"_blank\">here</a>."
        "<br><br>Once you have finished these exercises, you can continue practicing with more nouns "
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
        "Adjective translations in isolation."
    ,
    komparativ_superlativ:
        "Adjectives' comparative and superlative forms."
    ,
    adjektivdeklinationen:
        "Adjective declensions across grammatical cases, genders and article types."
        "<br><br>I hated that in French when I was a kid and it's even worse in German."
        "<br><br>If it was up to me, Adjective Declensions wouldn't start before level C1."
    ,
    adjektive_konjunktionen:
        "Conjunctions and Constructions for adjectives such as <i>wie</i>, <i>als</i> and <i>so</i>."
    ,

    verben:
        "English to German verb translation exercises at A1 and A2."
        "<br><br>Multiple-choice questions at B1 and B2, with both English to German and German to English translations."
    ,
    trennbare_verben:
        "Separable and inseparable verbs to translate from English, with either the root or the prefix as a hint."
        "<br><br>The most exotic feature of the German language. The Piña Colada of the Rhine. The Caipirinha of the Elbe."
    ,
    nomen_verben_verbindungen:
        "Noun-Verb Combinations and other idioms."
    ,

    praesens:
        "Present tense for each grammatical person."
    ,
    partizip_II:
        "Past participle used in the Perfekt, Plusquamperfekt, Futur II and passive voice."
        "<br><br>I wrote the first script that later became this website to practice the Partizip II."
    ,
    praeteritum:
        "Preterit tense."
        "<br><br>Available for each grammatical person for the most important verbs, "
        "then only the 3<sup>rd</sup>-person singular is required."
    ,
    imperativ:
        "Imperative for the three forms du, ihr and Sie."
        "<br><br>Scream at cyclists, the printer that doesn't work,"
        " and your toe that hits a piece of furniture the right way."
    ,
    konjunktiv_II:
        "Konjunktiv II is used for hypothetical situations, wishes, suggestions and polite requests."
        "<br><br>Politeness's favorite mood."
    ,
    konjunktiv_I:
        "Konjunktiv I is used primarily for indirect or reported speech."
        "<br><br>Journalists' favorite mood."
    ,
    partizip_I:
        "Partizip I is used to express ongoing actions."
        "<br><br>But why use the Partizip I when you could use a relative clause?"
        "<br><br>Also you would have to decline it like an adjective. What a mess."
    ,

    nomen_verben_wortstaemme:
        "Noun–verb pairs sharing the same root."
    ,
    adjektive_verben_wortstaemme:
        "Adjective-verb Pairs sharing the same root."
    ,
    adjektive_nomen_wortstaemme:
        "Adjective-Noun Pairs sharing the same root."
    ,

    zahlen:
        "Numbers in all their forms, including cardinal, ordinal, sequential, adverbial, fractional and multiplicative forms."
    ,
    alpha:
        "This is to test stuff"
    ,
}
