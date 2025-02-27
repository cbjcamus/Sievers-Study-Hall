import tkinter as tk

from interface.style import (bg_color)
from interface.widgets import create_title, create_section, create_line_menu
from menus.imperativ.imperativ import Imperativ
from utils.exercises import konnektoren


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        from menus.artikel.artikel import Artikel
        from menus.pronomen.pronomen import Pronomen
        from menus.praepositionen_grammatik.praepositionen_grammatik import PraepositionenGrammatik
        from menus.konnektoren.konnektoren import Konnektoren
        from menus.adjektivdeklinationen.adjektivdeklinationen import Adjektivdeklinationen
        from menus.relativsaetze.relativsaetze import Relativsaetze

        from menus.praesens.praesens import Praesens
        from menus.praepositionen_konjugation.praepositionen_konjugation import PraepositionenKonjugation
        from menus.perfekt.perfekt import Perfekt
        from menus.praeteritum.praeteritum import Praeteritum
        from menus.konjunktiv.konjunktiv import Konjunktiv

        from menus.verben.verben import Verben
        from menus.adjektive.adjektive import Adjektive
        from menus.adverbien.adverbien import Adverbien

        from utils.exercises import (artikel, pronomen, praepositionen_grammatik, konnektoren, adjektivDeklinationen,
                                     relativSaetze,
                                     praesens, praepositionen_konjugation, imperativ, perfekt, praeteritum, konjunktiv,
                                     verben, adjektive, adverbien, )

        tk.Frame.__init__(self, parent)
        self.configure(bg=bg_color)

        create_title(self, "Deutschtrainer")

        self.scores = {  # Use a dictionary to store StringVar instances
            artikel: tk.StringVar(),
            pronomen: tk.StringVar(),
            praepositionen_grammatik: tk.StringVar(),
            konnektoren: tk.StringVar(),
            adjektivDeklinationen: tk.StringVar(),
            relativSaetze: tk.StringVar(),

            praesens: tk.StringVar(),
            praepositionen_konjugation: tk.StringVar(),
            perfekt: tk.StringVar(),
            praeteritum: tk.StringVar(),
            imperativ: tk.StringVar(),
            konjunktiv: tk.StringVar(),

            verben: tk.StringVar(),
            adjektive: tk.StringVar(),
            adverbien: tk.StringVar(),

        }

        create_section(self, "Grammatik", 10, 50)

        create_line_menu(self, y=110, command=lambda: controller.show_frame(Artikel), page='exercise',
                         text_button="Artikel", text_score=self.scores[artikel], text_info='')

        create_line_menu(self, y=140, command=lambda: controller.show_frame(Pronomen), page='exercise',
                         text_button="Pronomen", text_score=self.scores[pronomen], text_info='')

        create_line_menu(self, y=170, command=lambda: controller.show_frame(PraepositionenGrammatik), page='exercise',
                         text_button="Präpositionen", text_score=self.scores[praepositionen_grammatik], text_info='')

        create_line_menu(self, y=200, command=lambda: controller.show_frame(Konnektoren), page='exercise',
                         text_button="Konnektoren", text_score=self.scores[konnektoren], text_info='')

        create_line_menu(self, y=230, command=lambda: controller.show_frame(Adjektivdeklinationen), page='exercise',
                         text_button="Adjektivdeklinationen", text_score=self.scores[adjektivDeklinationen], text_info='')

        create_line_menu(self, y=260, command=lambda: controller.show_frame(Relativsaetze), page='exercise',
                         text_button="Relativsätze", text_score=self.scores[relativSaetze], text_info='')

        create_section(self, "Konjugation", 10, 290)

        create_line_menu(self, y=350, command=lambda: controller.show_frame(Praesens), page='exercise',
                         text_button="Präsens", text_score=self.scores[praesens], text_info='')

        create_line_menu(self, y=380, command=lambda: controller.show_frame(PraepositionenKonjugation), page='exercise',
                         text_button="Präpositionen", text_score=self.scores[praepositionen_konjugation], text_info='')

        create_line_menu(self, y=410, command=lambda: controller.show_frame(Perfekt), page='exercise',
                         text_button="Perfekt", text_score=self.scores[perfekt], text_info='')

        create_line_menu(self, y=440, command=lambda: controller.show_frame(Praeteritum), page='exercise',
                         text_button="Präteritum", text_score=self.scores[praeteritum], text_info='')

        create_line_menu(self, y=470, command=lambda: controller.show_frame(Imperativ), page='exercise',
                         text_button="Imperativ", text_score=self.scores[imperativ], text_info='')

        create_line_menu(self, y=500, command=lambda: controller.show_frame(Konjunktiv), page='exercise',
                         text_button="Konjunktiv", text_score=self.scores[konjunktiv], text_info='')

        create_section(self, "Wortschatz", 10, 530)

        create_line_menu(self, y=590, command=lambda: controller.show_frame(Verben), page='exercise',
                         text_button="Verben", text_score=self.scores[verben], text_info='')

        create_line_menu(self, y=620, command=lambda: controller.show_frame(Adjektive), page='exercise',
                         text_button="Adjektive", text_score=self.scores[adjektive], text_info='')

        create_line_menu(self, y=650, command=lambda: controller.show_frame(Adverbien), page='exercise',
                         text_button="Adverbien", text_score=self.scores[adverbien], text_info='')


    def update_data(self):
        from utils.exercises import (exercises,
                                     verben, praesens, imperativ, praeteritum, konjunktiv,
                                    )
        from utils.statistics import answered_questions_by_exercise
        from utils.statistics import total_questions_by_exercise

        for exercise in exercises:
            score = (f"{answered_questions_by_exercise(exercise)} / "
                     f"{total_questions_by_exercise(exercise)}")
            self.scores[exercise].set(score)

        score_verben = (f"{answered_questions_by_exercise(verben)} / "
                         "525")
        self.scores[verben].set(score_verben)

        score_praesens = (f"{answered_questions_by_exercise(praesens)} / "
                          f"{total_questions_by_exercise(praesens) * 6}") #f"900")#
        self.scores[praesens].set(score_praesens)

        score_imperativ = (f"{answered_questions_by_exercise(imperativ)} / "
                          f"{total_questions_by_exercise(imperativ) * 3}") #f"900")#
        self.scores[imperativ].set(score_imperativ)

        score_praeteritum = (f"{answered_questions_by_exercise(praeteritum)} / "
                          f"345")# f"{total_questions_by_exercise(praeteritum)}")
        self.scores[praeteritum].set(score_praeteritum)

        score_konjunktiv = (f"{answered_questions_by_exercise(konjunktiv)} / "
                          f"{total_questions_by_exercise(konjunktiv) * 6}") #f"900")#
        self.scores[konjunktiv].set(score_konjunktiv)
