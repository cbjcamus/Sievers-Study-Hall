import tkinter as tk

from desktop_app.interface.style import bg_color
from desktop_app.interface.widgets import (create_title, create_section, create_button_back, create_line_menu)
from menus.praepositionen_grammatik.level1 import PraepositionenGrammatikLevel1
from menus.praepositionen_grammatik.level2 import PraepositionenGrammatikLevel2
from menus.praepositionen_grammatik.level3 import PraepositionenGrammatikLevel3
from menus.praepositionen_grammatik.level4 import PraepositionenGrammatikLevel4
from menus.praepositionen_grammatik.level5 import PraepositionenGrammatikLevel5
from menus.praepositionen_grammatik.level6 import PraepositionenGrammatikLevel6
from menus.praepositionen_grammatik.level7 import PraepositionenGrammatikLevel7
from menus.praepositionen_grammatik.level8 import PraepositionenGrammatikLevel8
from menus.praepositionen_grammatik.level9 import PraepositionenGrammatikLevel9
from menus.praepositionen_grammatik.level10 import PraepositionenGrammatikLevel10
from menus.praepositionen_grammatik.level11 import PraepositionenGrammatikLevel11
from menus.praepositionen_grammatik.level12 import PraepositionenGrammatikLevel12


class PraepositionenGrammatik(tk.Frame):
    def __init__(self, parent, controller):
        from menus.startpage import StartPage

        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg=bg_color)

        self.scores = {i: tk.StringVar() for i in range(0, 20)}

        create_title(self, "Präpositionen — Grammatik")

        create_section(self, "A1", 10, 50)

        create_line_menu(self, 110, lambda: controller.show_frame(PraepositionenGrammatikLevel1), 'level',
                         "Level 1", self.scores[1],
                         "A1 prepositions in isolation")

        create_line_menu(self, 140, lambda: controller.show_frame(PraepositionenGrammatikLevel2), 'level',
                         "Level 2", self.scores[2],
                         "Temporal prepositions in sentences")

        create_line_menu(self, 170, lambda: controller.show_frame(PraepositionenGrammatikLevel3), 'level',
                         "Level 3", self.scores[3],
                         "Local (Position) prepositions in sentences")

        create_line_menu(self, 200, lambda: controller.show_frame(PraepositionenGrammatikLevel4), 'level',
                         "Level 4", self.scores[4],
                         "Local (Direction) prepositions in sentences")

        create_line_menu(self, 230, lambda: controller.show_frame(PraepositionenGrammatikLevel5), 'level',
                         "Level 5", self.scores[5],
                         "Modal and Causal prepositions in sentences")

        create_line_menu(self, 260, lambda: controller.show_frame(PraepositionenGrammatikLevel6), 'level',
                         "Level 6", self.scores[6],
                         "Comparative prepositions in sentences")

        create_section(self, "A2", 10, 290)

        create_line_menu(self, 350, lambda: controller.show_frame(PraepositionenGrammatikLevel7), 'level',
                         "Level 7", self.scores[7],
                         "Preposition in sentences")

        create_line_menu(self, 380, lambda: controller.show_frame(PraepositionenGrammatikLevel8), 'level',
                         "Level 8", self.scores[8],
                         "Preposition in sentences")

        create_section(self, "B1", 10, 410)

        create_line_menu(self, 470, lambda: controller.show_frame(PraepositionenGrammatikLevel9), 'level',
                         "Level 9", self.scores[9],
                         "B1 prepositions in isolation")

        create_line_menu(self, 500, lambda: controller.show_frame(PraepositionenGrammatikLevel10), 'level',
                         "Level 10", self.scores[10],
                         "B1 prepositions in sentences")

        create_section(self, "B2", 10, 530)

        create_line_menu(self, 590, lambda: controller.show_frame(PraepositionenGrammatikLevel11), 'level',
                         "Level 11", self.scores[11],
                         "B2 prepositions in isolation")

        create_line_menu(self, 620, lambda: controller.show_frame(PraepositionenGrammatikLevel12), 'level',
                         "Level 12", self.scores[12],
                         "B2 prepositions in sentences")

        create_button_back(self, "Back to Menu", lambda: controller.show_frame(StartPage))

    def update_data(self):
        from utils.exercises import (praepositionen_grammatik)
        from utils.statistics import highest_level_exercise
        from utils.statistics import answered_questions_by_exercise_and_level
        from utils.statistics import total_questions_by_exercise_and_level

        for level in range(1, highest_level_exercise(praepositionen_grammatik) + 1):
            score = (f"{answered_questions_by_exercise_and_level(praepositionen_grammatik, level)} / "
                     f"{total_questions_by_exercise_and_level(praepositionen_grammatik, level)}")
            self.scores[level].set(score)