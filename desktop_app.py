import tkinter as tk

from interface.style import size_window

from menus_desktop_app.startpage import StartPage

from menus_desktop_app.artikel.artikel import (Artikel, ArtikelLevel1, ArtikelLevel2, ArtikelLevel3, ArtikelLevel4, ArtikelLevel5,
                                               ArtikelLevel6, ArtikelLevel7, ArtikelLevel8, ArtikelLevel10, ArtikelLevel11,
                                               ArtikelLevel12, ArtikelLevel13)

from menus_desktop_app.pronomen.pronomen import (Pronomen, PronomenLevel1, PronomenLevel2, PronomenLevel3, PronomenLevel4,
                                                 PronomenLevel5, PronomenLevel6)

from menus_desktop_app.praepositionen_grammatik.praepositionen_grammatik import (PraepositionenGrammatik,
                                                                                 PraepositionenGrammatikLevel1,
                                                                                 PraepositionenGrammatikLevel2,
                                                                                 PraepositionenGrammatikLevel3,
                                                                                 PraepositionenGrammatikLevel4,
                                                                                 PraepositionenGrammatikLevel5,
                                                                                 PraepositionenGrammatikLevel6,
                                                                                 PraepositionenGrammatikLevel7,
                                                                                 PraepositionenGrammatikLevel8,
                                                                                 ArtikelLevel9,
                                                                                 PraepositionenGrammatikLevel9,
                                                                                 PraepositionenGrammatikLevel10,
                                                                                 PraepositionenGrammatikLevel11,
                                                                                 PraepositionenGrammatikLevel12)

from menus_desktop_app.konnektoren.konnektoren import (Konnektoren, KonnektorenLevel1, KonnektorenLevel2, KonnektorenLevel3,
                                                       KonnektorenLevel4, KonnektorenLevel5, KonnektorenLevel6, KonnektorenLevel7,
                                                       KonnektorenLevel8)

from menus_desktop_app.adjektivdeklinationen.adjektivdeklinationen import (Adjektivdeklinationen, AdjektivdeklinationenLevel1,
                                                                           AdjektivdeklinationenLevel2, AdjektivdeklinationenLevel3,
                                                                           AdjektivdeklinationenLevel4, AdjektivdeklinationenLevel5,
                                                                           AdjektivdeklinationenLevel6, AdjektivdeklinationenLevel7,
                                                                           AdjektivdeklinationenLevel8, AdjektivdeklinationenLevel9,
                                                                           AdjektivdeklinationenLevel10,
                                                                           AdjektivdeklinationenLevel11,
                                                                           AdjektivdeklinationenLevel12,
                                                                           AdjektivdeklinationenLevel13,
                                                                           AdjektivdeklinationenLevel14,
                                                                           AdjektivdeklinationenLevel15,
                                                                           AdjektivdeklinationenLevel16)

from menus_desktop_app.relativsaetze.relativsaetze import (Relativsaetze, RelativsaetzeLevel1, RelativsaetzeLevel2,
                                                           RelativsaetzeLevel3, RelativsaetzeLevel4, RelativsaetzeLevel5,
                                                           RelativsaetzeLevel6, RelativsaetzeLevel7)

from menus_desktop_app.praesens.praesens import (Praesens, PraesensLevel1, PraesensLevel2, PraesensLevel3, PraesensLevel4,
                                                 PraesensLevel5, PraesensLevel6, PraesensLevel7, PraesensLevel8, PraesensLevel9,
                                                 PraesensLevel10)

from menus_desktop_app.praepositionen_konjugation.praepositionen_konjugation import (PraepositionenKonjugation,
                                                                                     PraepositionenKonjugationLevel1,
                                                                                     PraepositionenKonjugationLevel2,
                                                                                     PraepositionenKonjugationLevel3,
                                                                                     PraepositionenKonjugationLevel4,
                                                                                     PraepositionenKonjugationLevel5,
                                                                                     PraepositionenKonjugationLevel6,
                                                                                     PraepositionenKonjugationLevel7,
                                                                                     PraepositionenKonjugationLevel8,
                                                                                     PraepositionenKonjugationLevel9,
                                                                                     PraepositionenKonjugationLevel10,
                                                                                     PraepositionenKonjugationLevel11,
                                                                                     PraepositionenKonjugationLevel12,
                                                                                     PraepositionenKonjugationLevel13,
                                                                                     PraepositionenKonjugationLevel14)

from menus_desktop_app.imperativ.imperativ import (Imperativ, ImperativLevel1, ImperativLevel2, ImperativLevel3, ImperativLevel4,
                                                   ImperativLevel5)

from menus_desktop_app.perfekt.perfekt import (Perfekt, PerfektLevel1, PerfektLevel2, PerfektLevel3, PerfektLevel4, PerfektLevel5,
                                               PerfektLevel6, PerfektLevel7, PerfektLevel8)

from menus_desktop_app.praeteritum.praeteritum import (Praeteritum, PraeteritumLevel1, PraeteritumLevel2, PraeteritumLevel3,
                                                       PraeteritumLevel4, PraeteritumLevel5)

from menus_desktop_app.konjunktiv.konjunktiv import Konjunktiv, KonjunktivLevel1

from menus_desktop_app.verben.verben import (Verben, VerbenLevel1, VerbenLevel2, VerbenLevel3, VerbenLevel4, VerbenLevel5,
                                             VerbenLevel6, VerbenLevel7, VerbenLevel8)

from menus_desktop_app.adjektive.adjektive import (Adjektive, AdjektiveLevel1)

from menus_desktop_app.adverbien.adverbien import (Adverbien, AdverbienLevel1, AdverbienLevel2, AdverbienLevel3, AdverbienLevel4,
                                                   AdverbienLevel5, AdverbienLevel6, AdverbienLevel7, AdverbienLevel8, )

# TODO Priority
# relativsaetze wo wohin woher

# TODO Exercises
# Wortschatz: adjektives
# Wortschatz: nominalisation verbs
# Wortschatz: nominalisation adjektives
# Wortschatz: trennbare und untrennbare verben
# Wortschatz: formal verben
# Wortschatz: colloquial verben
# Wortschatz: verben that simplify
# Wortschatz: number, ordinal, fractions, double/triple, percent
# Articles: genitive articles
# Possessive pronomen
# Possessive article
# einzige -> adjective instead of adverb


# TODO Format
# add opposite of normalization with list of good answers
# https://en.wikipedia.org/wiki/Eduard_Sievers for logo
# Explanation exercise should be in a format of a skill
# Another color for Correct and Incorrect

# Framework
# Learn & Discover
# Practice & Reinforce / Consolidate
# Apply & Summarize


class AppController(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry(size_window)
        self.frames = {}
        container = tk.Frame(self)
        container.place(x=0, y=0, relwidth=1, relheight=1)

        frames = (StartPage,

                  Artikel, ArtikelLevel1, ArtikelLevel2, ArtikelLevel3, ArtikelLevel4, ArtikelLevel5,
                  ArtikelLevel6, ArtikelLevel7, ArtikelLevel8, ArtikelLevel10, ArtikelLevel11,
                  ArtikelLevel12, ArtikelLevel13,
                  Pronomen, PronomenLevel1, PronomenLevel2, PronomenLevel3, PronomenLevel4, PronomenLevel5,
                  PronomenLevel6,
                  PraepositionenGrammatik, PraepositionenGrammatikLevel1, PraepositionenGrammatikLevel2,
                  PraepositionenGrammatikLevel3, PraepositionenGrammatikLevel4, PraepositionenGrammatikLevel5,
                  PraepositionenGrammatikLevel6, PraepositionenGrammatikLevel7, PraepositionenGrammatikLevel8,
                  PraepositionenGrammatikLevel8, ArtikelLevel9, PraepositionenGrammatikLevel9,
                  PraepositionenGrammatikLevel10, PraepositionenGrammatikLevel11, PraepositionenGrammatikLevel12,
                  Konnektoren, KonnektorenLevel1, KonnektorenLevel2, KonnektorenLevel3,
                  KonnektorenLevel4, KonnektorenLevel5, KonnektorenLevel6, KonnektorenLevel7,
                  KonnektorenLevel8,
                  Adjektivdeklinationen, AdjektivdeklinationenLevel1, AdjektivdeklinationenLevel2,
                  AdjektivdeklinationenLevel3, AdjektivdeklinationenLevel4, AdjektivdeklinationenLevel5,
                  AdjektivdeklinationenLevel6, AdjektivdeklinationenLevel7, AdjektivdeklinationenLevel8,
                  AdjektivdeklinationenLevel9, AdjektivdeklinationenLevel10, AdjektivdeklinationenLevel11,
                  AdjektivdeklinationenLevel12, AdjektivdeklinationenLevel13, AdjektivdeklinationenLevel14,
                  AdjektivdeklinationenLevel15, AdjektivdeklinationenLevel16,
                  Relativsaetze, RelativsaetzeLevel1, RelativsaetzeLevel2, RelativsaetzeLevel3,
                  RelativsaetzeLevel4, RelativsaetzeLevel5, RelativsaetzeLevel6, RelativsaetzeLevel7,

                  Praesens, PraesensLevel1, PraesensLevel2, PraesensLevel3, PraesensLevel4,
                  PraesensLevel5, PraesensLevel6, PraesensLevel7, PraesensLevel8, PraesensLevel9,
                  PraesensLevel10,
                  PraepositionenKonjugation, PraepositionenKonjugationLevel1, PraepositionenKonjugationLevel2,
                  PraepositionenKonjugationLevel3, PraepositionenKonjugationLevel4, PraepositionenKonjugationLevel5,
                  PraepositionenKonjugationLevel6, PraepositionenKonjugationLevel7, PraepositionenKonjugationLevel8,
                  PraepositionenKonjugationLevel9, PraepositionenKonjugationLevel10, PraepositionenKonjugationLevel11,
                  PraepositionenKonjugationLevel12, PraepositionenKonjugationLevel13, PraepositionenKonjugationLevel14,
                  Imperativ, ImperativLevel1, ImperativLevel2, ImperativLevel3, ImperativLevel4,
                  ImperativLevel5,
                  Perfekt, PerfektLevel1, PerfektLevel2, PerfektLevel3, PerfektLevel4, PerfektLevel5, PerfektLevel6,
                  PerfektLevel7, PerfektLevel8,
                  Praeteritum, PraeteritumLevel1, PraeteritumLevel2, PraeteritumLevel3, PraeteritumLevel4,
                  PraeteritumLevel5,
                  Konjunktiv, KonjunktivLevel1,

                  Verben, VerbenLevel1, VerbenLevel2, VerbenLevel3, VerbenLevel4, VerbenLevel5,
                  VerbenLevel6, VerbenLevel7, VerbenLevel8,
                  Adjektive, AdjektiveLevel1,
                  Adverbien, AdverbienLevel1, AdverbienLevel2, AdverbienLevel3, AdverbienLevel4,
                  AdverbienLevel5, AdverbienLevel6, AdverbienLevel7, AdverbienLevel8,
                  )

        for F in frames:
            frame = F(container, self)
            self.frames[F] = frame
            frame.place(x=0, y=0, relwidth=1, relheight=1)

        self.updated_frame = (StartPage, Adjektivdeklinationen)
        self.show_frame(StartPage)


    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.update_data()
        frame.tkraise()
        try:
            frame.post_update()
        except AttributeError:
            pass


app = AppController()
app.title("Deutschtrainer")
app.geometry(size_window)


app.mainloop()