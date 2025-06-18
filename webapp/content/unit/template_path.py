from data.data_processing.units import (
    praepositionen_grammatik, praepositionen_verben, praepositionen_adjektive, praepositionen_nomen, praepositionen_adverbien,
    artikel, pronomen, konnektoren, fragen, adverbien,
    praesens, imperativ, partizip_II, praeteritum, praeteritum_partizip_II, konjunktiv_II, konjunktiv_I, partizip_I,
    adjektive, adjektivdeklinationen,
    trennbare_verben, verben,
    deverbale_nomen
)

TEMPLATE_PATH = {
    praepositionen_grammatik: "praepositionen/praepositionen_grammatik.html",
    praepositionen_verben: "praepositionen/praepositionen_verben.html",
    praepositionen_adjektive: "praepositionen/praepositionen_adjektive.html",
    praepositionen_nomen: "praepositionen/praepositionen_nomen.html",
    praepositionen_adverbien: "praepositionen/praepositionen_adverbien.html",

    artikel: "grammatik/artikel.html",
    pronomen: "grammatik/pronomen.html",
    konnektoren: "grammatik/konnektoren.html",
    fragen: "grammatik/fragen.html",
    adverbien: "grammatik/adverbien.html",

    praesens: "konjugation/praesens.html",
    imperativ: "konjugation/imperativ.html",
    partizip_II: "konjugation/partizip_II.html",
    praeteritum: "konjugation/praeteritum.html",
    praeteritum_partizip_II: "konjugation/praeteritum_partizip_II.html",
    konjunktiv_II: "konjugation/konjunktiv_II.html",
    konjunktiv_I: "konjugation/konjunktiv_I.html",
    partizip_I: "konjugation/partizip_I.html",

    adjektive: "adjektive/adjektive.html",
    adjektivdeklinationen: "adjektive/adjektivdeklinationen.html",

    trennbare_verben: "verben/trennbare_verben.html",
    verben: "verben/verben.html",

    deverbale_nomen: "/deverbale_substantive.html",
}
