from data.data_processing.units import (
    praepositionen_grammatik, praepositionen_verben, praepositionen_adjektive, praepositionen_nomen,
    praepositionen_artikel,
    artikel, pronomen, konnektoren, fragen, adverbien, wortstellung,
    adjektive, adjektivdeklinationen,
    verben, trennbare_verben, nomen_verben_verbindungen,
    praesens, imperativ, partizip_II, praeteritum, praeteritum_partizip_II, konjunktiv_II, konjunktiv_I, partizip_I,
    genus_regeln, genus_routledge, genus_goethe,
)

from webapp.style.icons import STAR_GOLD, STAR_SILVER

STARS = {
    praepositionen_grammatik: f"{STAR_GOLD}",
    praepositionen_verben: f"{STAR_GOLD}",
    praepositionen_adjektive: f"",
    praepositionen_nomen: f"",
    praepositionen_artikel: f"",

    artikel: f"{STAR_GOLD}",
    pronomen: f"",
    konnektoren: f"{STAR_GOLD}",
    fragen: f"",
    adverbien: f"{STAR_GOLD}",
    wortstellung: f"",

    adjektive: f"",
    adjektivdeklinationen: f"",

    verben: f"{STAR_GOLD}",
    trennbare_verben: f"{STAR_GOLD}",
    nomen_verben_verbindungen: f"",

    praesens: f"",
    imperativ: f"",
    partizip_II: f"{STAR_GOLD}",
    praeteritum: f"{STAR_GOLD}",
    praeteritum_partizip_II: f"",
    konjunktiv_II: f"",
    konjunktiv_I: f"",
    partizip_I: f"",

    genus_regeln: f"",
    genus_routledge: f"",
    genus_goethe: f"",
}
