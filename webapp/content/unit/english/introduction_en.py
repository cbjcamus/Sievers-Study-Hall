from data.data_processing.units import (
    praepositionen_grammatik, praepositionen_verben, praepositionen_adjektive, praepositionen_nomen,
    praepositionen_adverbien, praepositionen_artikel,
    artikel, pronomen, konnektoren, fragen, adverbien,
    adjektive, adjektivdeklinationen, adjektive_konjunktionen,
    verben, trennbare_verben, nomen_verben_verbindungen, nomen_verben_wortstaemme,
    praesens, imperativ, partizip_II, praeteritum, praeteritum_partizip_II, konjunktiv_II, konjunktiv_I, partizip_I,
    genus_regeln, genus_routledge, genus_goethe,
)

INTRODUCTION_EN = {
    praepositionen_grammatik:
        "Prepositions in Temporal, Local, Modal and Causal contexts. You can find a guide and curriculum for German preposition <a href=\"https://sieversstudyhall.substack.com/p/basic-german-prepositions-uses-up\" target=\"_blank\">here</a>."
        "<br><br>Happy suffering 🥰😍😘."
    ,
    praepositionen_verben:
        "Verb-Preposition pairs."
        "<br><br>Includes pronominaladverbien in <i>Da</i> and <i>Wo</i> at level A2."
    ,
    praepositionen_adjektive:
        "Adjective-Preposition pairs."
        "<br><br>Think of it as Verb's pretentious sister."
    ,
    praepositionen_nomen:
        "Noun-Preposition pairs."
        "<br><br>Verb's and Adjective's younger brother. The annoying one."
    ,
    praepositionen_adverbien:
        "Just kidding it doesn't exist."
    ,
    praepositionen_artikel:
        "All the questions come from other Präpositionen exercises and updated to practice cases following prepositions."
        "<br><br>Reminder:"
        "<br>&bull; Followed by Accusative: Bis, Durch, Für, Ohne, Gegen, Um"
        "<br>&bull; Followed by Dative: Aus, Bei, Mit, Seit, Nach, Von, Zu"
        "<br>&bull; Followed by Dative or Accusative: An, Auf, In, Hinter, Vor, Über, Unter, Neben, Zwischen"
    ,

    artikel:
        "Articles marinated in every grammatical cases."
        "<br><br>Includes definite, indefinite, negative, possessive, demonstrative articles and much more."
        "<br><br>If you get headaches, it means you're learning."
    ,
    pronomen:
        "Pronouns in every grammatical cases."
        "<br><br>Not genitive though, there are no genitive pronoun in German. Latin does have genitive pronouns,"
        " why not german?"
        "<br><br>Includes reflexive, relative, relentless, reliable, and resolute pronouns."
    ,
    konnektoren:
        "Connectors include coordinating conjunctions, subordinating conjunctions, correlative conjunctions and adverbs that connect two sentences together."
        "<br><br>⚠️ The following definitions are used:"
        "<br> &nbsp; &bull; Coordinating conjunction:"
        "<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Coordinating conjunction – Subject – Verb – Object"
        "<br> &nbsp; &bull; Subordinating conjunction:"
        "<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Subordinating conjunction – Subject – Object – Verb"
        "<br> &nbsp; &bull; Adverb:"
        "<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Adverb – Verb – Subject – Object"
        "<br> &nbsp; &bull; Correlative conjunction:"
        "<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Two or more terms such as <i>um zu</i>, <i>entweder oder</i> or <i>sowohl als auch</i>"
    ,
    fragen:
        "Question words."
        "<br><br>Mostly useful at A1 and A2 level. B1 to C1 levels are here out of exhaustivity."
        "<br><br>Wo means Where and Wer means Who. Hope it makes sense."
    ,
    adverbien:
        "Adverbs, including a mix of Temporal, Local, and Modal ones at each level (Causal adverbs are done in Konnektoren)."
        "<br><br>Features adverbs not seen in Konnektoren and Fragen."
    ,

    adjektive:
        "Adjectives translations, antonyms, comparatives and superlatives in isolation."
    ,
    adjektivdeklinationen:
        "Adjective Declensions in every grammatical cases, persons, and articles."
        "<br><br>I hated that in French as a boy and it's even worse in German."
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
        "Noun-Verb Combinations starting at level B1."
        "<br><br>Out of exhaustivity I'm using the largest definition of Nomen-Verben Verbindungen, "
        "which include combinations such as <i>Lust haben</i> or <i>Angst haben</i>."
    ,
    nomen_verben_wortstaemme:
        "Noun-Verb Pairs with the same etymological root."
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
        "<br><br>Once I spoke to a German teacher about my whereabouts. My level was early B1. "
        "<br>I used the Präteritum instead of the Perfekt because it's easier: you don't have to think about which"
        "hilfsverb to use and you don't have to retain the Partizip II in your head."
        "<br>She cut me off several times and told me to use the Perfekt instead. "
        "<br>And yes I knew the Präteritum is mostly used in writing and not while speaking."
        "<br>That wasn't the point. "
        "My goal was to express myself in German, something I wasn't able to do everyday. "
        "<br>Not every conversation needs to be an oral examination. "
        "There is nothing more frustrating than expressing your thoughts in a new language while someone corrects "
        "every single mistake. "
        "<br>If you're a language teacher be mindful of that. "
        "<br>It's my website I get to rant whenever and wherever I want."
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

    genus_regeln:
        "Practice the gender of nouns based on thumb rules."
        "<br><br>A guide listing these thumb rules is available "
        "<a href=\"https://sieversstudyhall.substack.com/p/genders-of-german-noun-from-a1-to\" target=\"_blank\">here</a>."
    ,
    genus_routledge:
        "Deep dreams drift, daring dusk to dance"
        "<br>Dark doubts dissolve, daylight dares advance:"
        "<br>Determined voices decide, declare, and pass,"
        "<br>Der, Die, Das."
        "<br><br>The list of nouns comes from "
        "<a href=\"https://docs.google.com/spreadsheets/d/1r9HwvVpo35MFxnJ_5W6RKlDfx5VzmQVcnpJTgrNUY9I/edit?gid=1814339112#gid=1814339112\" target=\"_blank\">here</a>."
    ,
    genus_goethe:
        "A Dance of Der Die Das."
        "<br><br>The list of nouns comes from the "
        "<a href=\"https://www.goethe.de/pro/relaunch/prf/de/A1_SD1_Wortliste_02.pdf\" target=\"_blank\">Goethe Institut</a>."
    ,
}
