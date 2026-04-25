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

TEMPLATE_PATH = {
    praepositionen: "units/praepositionen/praepositionen.html",
    praepositionen_verben: "units/praepositionen/praepositionen_verben.html",
    praepositionen_adjektive: "units/praepositionen/praepositionen_adjektive.html",
    praepositionen_nomen: "units/praepositionen/praepositionen_nomen.html",
    pronominaladverbien: "units/praepositionen/pronominaladverbien.html",

    artikel: "units/artikel_pronomen_kasus/artikel.html",
    pronomen: "units/artikel_pronomen_kasus/pronomen.html",
    praepositionen_artikel: "units/artikel_pronomen_kasus/praepositionen_artikel.html",
    verben_artikel: "units/artikel_pronomen_kasus/verben_artikel.html",

    konnektoren: "units/satzbildung/konnektoren.html",
    fragen: "units/satzbildung/fragen.html",
    adverbien: "units/satzbildung/adverbien.html",
    wortstellung: "units/satzbildung/wortstellung.html",

    genus_regeln: "units/genus/genus_regeln.html",
    genus: "units/genus/genus.html",
    plural: "units/genus/plural.html",

    verben: "units/verben/verben.html",
    trennbare_verben: "units/verben/trennbare_verben.html",
    nomen_verben_verbindungen: "units/verben/nomen_verben_verbindungen.html",

    adjektive: "units/adjektive/adjektive.html",
    komparativ_superlativ: "units/adjektive/komparativ_superlativ.html",
    adjektivdeklinationen: "units/adjektive/adjektivdeklinationen.html",
    adjektive_konjunktionen: "units/adjektive/adjektive_konjunktionen.html",

    praesens: "units/konjugation/praesens.html",
    imperativ: "units/konjugation/imperativ.html",
    partizip_II: "units/konjugation/partizip_II.html",
    praeteritum: "units/konjugation/praeteritum.html",
    praeteritum_partizip_II: "units/konjugation/praeteritum_partizip_II.html",
    konjunktiv_II: "units/konjugation/konjunktiv_II.html",
    konjunktiv_I: "units/konjugation/konjunktiv_I.html",
    partizip_I: "units/konjugation/partizip_I.html",

    nomen_verben_wortstaemme: "units/wortstaemme/nomen_verben_wortstaemme.html",
    adjektive_verben_wortstaemme: "units/wortstaemme/adjektive_verben_wortstaemme.html",
    adjektive_nomen_wortstaemme: "units/wortstaemme/adjektive_nomen_wortstaemme.html",

    zahlen: "units/sonstige/zahlen.html",
}
