from data.data_processing.units import (
    praepositionen_grammatik, praepositionen_verben, praepositionen_adjektive, praepositionen_nomen,
    praepositionen_kasus,
    artikel, pronomen, konnektoren, fragen, adverbien,
    adjektive, adjektivdeklinationen,
    verben, trennbare_verben,
    praesens, imperativ, partizip_II, praeteritum, praeteritum_partizip_II, konjunktiv_II, konjunktiv_I, partizip_I,
    deverbale_nomen
)

from webapp.style.icons import STAR_GOLD, STAR_SILVER

STARS = {
    praepositionen_grammatik: f"{STAR_GOLD}",
    praepositionen_verben: f"{STAR_GOLD}",
    praepositionen_adjektive: f"",
    praepositionen_nomen: f"",
    praepositionen_kasus: f"",

    artikel: f"{STAR_GOLD}",
    pronomen: f"",
    konnektoren: f"{STAR_GOLD}",
    fragen: f"",
    adverbien: f"",

    adjektive: f"",
    adjektivdeklinationen: f"",

    trennbare_verben: f"{STAR_GOLD}",
    verben: f"{STAR_GOLD}",

    praesens: f"",
    imperativ: f"",
    partizip_II: f"",
    praeteritum: f"",
    praeteritum_partizip_II: f"",
    konjunktiv_II: f"",
    konjunktiv_I: f"",
    partizip_I: f"",

    deverbale_nomen: "",
    }
