from data.data_processing.units import (
    praepositionen_grammatik, praepositionen_verben, praepositionen_adjektive, praepositionen_nomen,
    praepositionen_adverbien, praepositionen_artikel,
    artikel, artikel_genus, pronomen, konnektoren, fragen, adverbien, wortstellung,
    adjektive, adjektivdeklinationen,
    verben, trennbare_verben, nomen_verben_verbindungen,
    praesens, imperativ, partizip_II, praeteritum, praeteritum_partizip_II, konjunktiv_II, konjunktiv_I, partizip_I,
)

TEMPLATE_PATH = {
    praepositionen_grammatik: "praepositionen/praepositionen_grammatik.html",
    praepositionen_verben: "praepositionen/praepositionen_verben.html",
    praepositionen_adjektive: "praepositionen/praepositionen_adjektive.html",
    praepositionen_nomen: "praepositionen/praepositionen_nomen.html",
    praepositionen_adverbien: "praepositionen/praepositionen_adverbien.html",
    praepositionen_artikel: "praepositionen/praepositionen_artikel.html",

    artikel: "grammatik/artikel.html",
    artikel_genus: "grammatik/artikel_genus.html",
    pronomen: "grammatik/pronomen.html",
    konnektoren: "grammatik/konnektoren.html",
    fragen: "grammatik/fragen.html",
    adverbien: "grammatik/adverbien.html",
    wortstellung: "grammatik/wortstellung.html",

    adjektive: "adjektive/adjektive.html",
    adjektivdeklinationen: "adjektive/adjektivdeklinationen.html",

    verben: "verben/verben.html",
    trennbare_verben: "verben/trennbare_verben.html",
    nomen_verben_verbindungen: "verben/nomen_verben_verbindungen.html",

    praesens: "konjugation/praesens.html",
    imperativ: "konjugation/imperativ.html",
    partizip_II: "konjugation/partizip_II.html",
    praeteritum: "konjugation/praeteritum.html",
    praeteritum_partizip_II: "konjugation/praeteritum_partizip_II.html",
    konjunktiv_II: "konjugation/konjunktiv_II.html",
    konjunktiv_I: "konjugation/konjunktiv_I.html",
    partizip_I: "konjugation/partizip_I.html",
}
