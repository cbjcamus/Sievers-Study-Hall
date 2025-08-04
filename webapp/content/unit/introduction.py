from data.data_processing.units import (
    praepositionen_grammatik, praepositionen_verben, praepositionen_adjektive, praepositionen_nomen,
    praepositionen_adverbien, praepositionen_kasus,
    artikel, pronomen, konnektoren, fragen, adverbien,
    praesens, imperativ, partizip_II, praeteritum, praeteritum_partizip_II, konjunktiv_II, konjunktiv_I, partizip_I,
    adjektive, adjektivdeklinationen,
    trennbare_verben, verben,
    deverbale_nomen
)

INTRODUCTION = {
    praepositionen_grammatik: "Prepositions in Temporal, Local, Modal and Causal contexts."
                              "<br><br>Basic prepositions are reviewed up to the B2 level."
                              "<br><br>Happy suffering 🥰😍😘.",
    praepositionen_verben: "Verb-Preposition pairs."
                           "<br><br>Includes pronominaladverbien in \"Da\" and \"Wo\" at level A2.",
    praepositionen_adjektive: "Adjective-Preposition pairs."
                              "<br><br>Think of it as Verb's pretentious sister.",
    praepositionen_nomen: "Noun-Preposition pairs."
                          "<br><br>Verb's and Adjective's younger brother. The annoying one.",
    praepositionen_adverbien: "Just kidding it doesn't exist.",
    praepositionen_kasus: "All the questions come from other Präpositionen exercises and updated to practice cases"
                          " following prepositions."
                          "<br><br>Reminder:"
                          "<br>&bull; Followed by Accusative: Bis, Durch, Für, Ohne, Gegen, Um"
                          "<br>&bull; Followed by Dative: Aus, Bei, Mit, Seit, Nach, Von, Zu"
                          "<br>&bull; Followed by Dative or Accusative: An, Auf, In, Hinter, Vor, Über, Unter, Neben, Zwischen",

    artikel: "Articles marinated in every grammatical cases."
             "<br><br>Includes definite, indefinite, negative, possessive, demonstrative articles and much more."
             "<br><br>If you get headaches, it means you're learning.",
    pronomen: "Pronouns in every grammatical cases."
              "<br><br>Not genitive though, there are no genitive pronoun in German. Latin does have genitive pronoun, why not german?"
              "<br><br>Includes reflexive, relative, relentless, reliable, and resolute pronouns.",
    konnektoren: "Connectors include conjunctions, subjunctions, and adverbs that connect two sentences together."
                 "<br><br>I've added levels to learn the different synonyms of each connectors."
                 "<br><br>⚠️ The following definitions are used:"
                 "<br> &nbsp; &nbsp; &nbsp; &nbsp; &bull; Konjunktion: Konjunktion – Subjekt – Verb – Objektkomplement"
                 "<br> &nbsp; &nbsp; &nbsp; &nbsp; &bull; Subjunktion: Subjunktion – Subjekt – Objektkomplement – Verb"
                 "<br> &nbsp; &nbsp; &nbsp; &nbsp; &bull; Adverb: &nbsp; &nbsp; &nbsp; &nbsp; Adverb – Verb – Subjekt – Objektkomplement"
                 "<br> &nbsp; &nbsp; &nbsp; &nbsp; &bull; Zwei Begriffe: Two terms such as \"um zu\" or \"entweder oder\"",
    fragen: "Question words."
            "<br><br>Mostly useful at A1 and A2 level. B1 to C1 levels are here out of exhaustivity."
            "<br><br>Wo means Where and Wer means Who. Hope it makes sense.",
    adverbien: "Adverbs, including a mix of Temporal, Local, Modal, and Causal ones at each level."
               "<br><br>Features adverbs not seen in Konnektoren and Fragen.",

    praesens: "Present tense for each grammatical person."
              "<br><br>⚠️ For Reflexive verbs, do not write the reflexive pronoun, or your answer will be flagged as incorrect. Explanation <a href=https://sieversstudyhall.substack.com/i/165326616/why-are-reflexive-pronouns-missing-in-conjugation-exercises target=\"_blank\">here</a>.",
    partizip_II: "Past Participle used in the Perfekt, Plusquamperfekt, Future II and the Passive voice."
                 "<br><br>I wrote the first script that later became this website to practice the Partizip II. I hold it close to my heart.",
    praeteritum: "Preterit tense."
                 "<br><br>Available for each grammatical person for the most important verbs, then only the 3<sup>rd</sup> singular person is required."
                 "<br><br>⚠️ For Reflexive verbs, do not write the reflexive pronoun, or your answer will be flagged as incorrect. Explanation <a href=https://sieversstudyhall.substack.com/i/165326616/why-are-reflexive-pronouns-missing-in-conjugation-exercises target=\"_blank\">here</a>."
                 "<br><br>Once I spoke to a German teacher about my whereabouts. My level was early B1. "
                 "<br>I used the Präteritum instead of the Perfekt because it's easier: you don't have to think about which hilfsverb to use "
                 "and you don't have to retain the Partizip II in your head."
                 "<br>She cut me off several times and told me to use the Perfekt instead. "
                 "<br>And yes I knew the Präteritum is mostly used in writing and not while speaking."
                 "<br>That wasn't the point. "
                 "My goal was to express myself in German, something I wasn't able to do everyday. "
                 "<br>Not every conversation needs to be an oral examination. "
                 "There is nothing more frustrating than expressing your thoughts in a new language while someone corrects "
                 "every single mistake. "
                 "<br>If you're a language teacher be mindful of that. "
                 "<br>It's my website I get to rant whenever and wherever I want.",
    praeteritum_partizip_II: "Exercise to practice the Präteritum and Partizip II together.",
    imperativ: "Imperative for the three grammatical persons Du, Ihr and Sie."
               "<br><br>Scream at cyclists, the printer that doesn't work, and your toe that hits a piece of furniture the right way."
               "<br><br>⚠️ For Reflexive verbs, do not write the reflexive pronoun, or your answer will be flagged as incorrect. Explanation <a href=https://sieversstudyhall.substack.com/i/165326616/why-are-reflexive-pronouns-missing-in-conjugation-exercises target=\"_blank\">here</a>.",
    konjunktiv_II: "Konjunktiv II is used to express the subjunctive mood, suggestions and wishes."
                   "<br><br>Politeness' favorite tense.",
    konjunktiv_I: "Konjunktiv I is used to express an indirect or reported speech."
                  "<br><br>Journalists' favorite tense."
                  "<br><br>⚠️ For Reflexive verbs, do not write the reflexive pronoun, or your answer will be flagged as incorrect. Explanation <a href=https://sieversstudyhall.substack.com/i/165326616/why-are-reflexive-pronouns-missing-in-conjugation-exercises target=\"_blank\">here</a>.",
    partizip_I: "Partizip I is used to express ongoing actions."
                "<br><br>But why use the Partizip I when you could use a relative clause?"
                "<br><br>Also you would have to decline it as an adjective. What a mess.",

    adjektive: "Adjectives translations, opposites, comparatives and superlatives in isolation.",
    adjektivdeklinationen: "Adjective Declensions in every grammatical cases, persons, and articles."
                           "<br><br>I hated that in French as a boy and it's even worse in German."
                           "<br><br>If it was up to me, Adjective Declensions wouldn't start before C1.",

    trennbare_verben: "Trennbare and Untrennbare verbs to translate from English with either the root or the prefix as an help."
                      "<br><br>⚠️ For Reflexive verbs, do not write the reflexive pronoun, or your answer will be flagged as incorrect. Explanation <a href=https://sieversstudyhall.substack.com/i/165326616/why-are-reflexive-pronouns-missing-in-conjugation-exercises target=\"_blank\">here</a>."
                      "<br><br>The most exotic feature of the German language. The Piña Colada of the Rhine. The Caipirinha of the Elbe.",
    verben: "English to German verb translation exercise."
            "<br><br>⚠️ For Reflexive verbs, do not write the reflexive pronoun, or your answer will be flagged as incorrect. Explanation <a href=https://sieversstudyhall.substack.com/i/165326616/why-are-reflexive-pronouns-missing-in-conjugation-exercises target=\"_blank\">here</a>."
            "<br><br>⚠️ Synonyms are not available for this exercise. Read carefully the entire English translation.",

    deverbale_nomen: "",
    }
