from data.data_processing.units import (
    praepositionen_grammatik, praepositionen_verben, praepositionen_adjektive, praepositionen_nomen,
    praepositionen_adverbien, praepositionen_artikel,
    artikel, pronomen, konnektoren, fragen, adverbien, wortstellung,
    adjektive, adjektivdeklinationen, adjektive_konjunktionen,
    verben, trennbare_verben, nomen_verben_verbindungen, nomen_verben_wortstaemme,
    praesens, imperativ, partizip_II, praeteritum, praeteritum_partizip_II, konjunktiv_II, konjunktiv_I, partizip_I,
    genus_regeln, genus_routledge, genus_goethe,
)

TEMPLATE_PATH = {
    praepositionen_grammatik: "units/praepositionen/praepositionen_grammatik.html",
    praepositionen_verben: "units/praepositionen/praepositionen_verben.html",
    praepositionen_adjektive: "units/praepositionen/praepositionen_adjektive.html",
    praepositionen_nomen: "units/praepositionen/praepositionen_nomen.html",
    praepositionen_adverbien: "units/praepositionen/praepositionen_adverbien.html",
    praepositionen_artikel: "units/praepositionen/praepositionen_artikel.html",

    artikel: "units/grammatik/artikel.html",
    pronomen: "units/grammatik/pronomen.html",
    konnektoren: "units/grammatik/konnektoren.html",
    fragen: "units/grammatik/fragen.html",
    adverbien: "units/grammatik/adverbien.html",
    wortstellung: "units/grammatik/wortstellung.html",

    adjektive: "units/adjektive/adjektive.html",
    adjektivdeklinationen: "units/adjektive/adjektivdeklinationen.html",
    adjektive_konjunktionen: "units/adjektive/adjektive_konjunktionen.html",

    verben: "units/verben/verben.html",
    trennbare_verben: "units/verben/trennbare_verben.html",
    nomen_verben_verbindungen: "units/verben/nomen_verben_verbindungen.html",
    nomen_verben_wortstaemme: "units/verben/nomen_verben_wortstaemme.html",

    praesens: "units/konjugation/praesens.html",
    imperativ: "units/konjugation/imperativ.html",
    partizip_II: "units/konjugation/partizip_II.html",
    praeteritum: "units/konjugation/praeteritum.html",
    praeteritum_partizip_II: "units/konjugation/praeteritum_partizip_II.html",
    konjunktiv_II: "units/konjugation/konjunktiv_II.html",
    konjunktiv_I: "units/konjugation/konjunktiv_I.html",
    partizip_I: "units/konjugation/partizip_I.html",

    genus_regeln: "units/genus/genus_regeln.html",
    genus_routledge: "units/genus/genus_routledge.html",
    genus_goethe: "units/genus/genus_goethe.html",
}
