import tkinter as tk

from desktop_app.interface.style import bg_color
from desktop_app.interface.widgets import (create_title, create_section, create_button_back, create_line_menu)
from menus.praepositionen_konjugation.level1 import PraepositionenKonjugationLevel1
from menus.praepositionen_konjugation.level2 import PraepositionenKonjugationLevel2
from menus.praepositionen_konjugation.level3 import PraepositionenKonjugationLevel3
from menus.praepositionen_konjugation.level4 import PraepositionenKonjugationLevel4
from menus.praepositionen_konjugation.level5 import PraepositionenKonjugationLevel5
from menus.praepositionen_konjugation.level6 import PraepositionenKonjugationLevel6
from menus.praepositionen_konjugation.level7 import PraepositionenKonjugationLevel7
from menus.praepositionen_konjugation.level8 import PraepositionenKonjugationLevel8
from menus.praepositionen_konjugation.level9 import PraepositionenKonjugationLevel9
from menus.praepositionen_konjugation.level10 import PraepositionenKonjugationLevel10
from menus.praepositionen_konjugation.level11 import PraepositionenKonjugationLevel11
from menus.praepositionen_konjugation.level12 import PraepositionenKonjugationLevel12
from menus.praepositionen_konjugation.level13 import PraepositionenKonjugationLevel13
from menus.praepositionen_konjugation.level14 import PraepositionenKonjugationLevel14


class PraepositionenKonjugation(tk.Frame):
    def __init__(self, parent, controller):
        from menus.startpage import StartPage

        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg=bg_color)

        self.scores = {i: tk.StringVar() for i in range(0, 30)}

        create_title(self, "Präpositionen — Konjugation")

        create_section(self, "A1", 10, 50)

        create_line_menu(self, 110, lambda: controller.show_frame(PraepositionenKonjugationLevel1), 'level',
                         "Level 1", self.scores[1],
                         "Find the präpositionen attached to the verb in isolation")

        create_line_menu(self, 140, lambda: controller.show_frame(PraepositionenKonjugationLevel2), 'level',
                         "Level 2", self.scores[2],
                         "Find the präpositionen attached to the verb in sentences")

        create_section(self, "A2", 10, 170)

        create_line_menu(self, 230, lambda: controller.show_frame(PraepositionenKonjugationLevel3), 'level',
                         "Level 3", self.scores[3],
                         "Find the präpositionen attached to the verb in isolation")

        create_line_menu(self, 260, lambda: controller.show_frame(PraepositionenKonjugationLevel4), 'level',
                         "Level 4", self.scores[4],
                         "Find the präpositionen attached to the verb in sentences")

        create_section(self, "B1", 10, 290)

        create_line_menu(self, 350, lambda: controller.show_frame(PraepositionenKonjugationLevel5), 'level',
                         "Level 5", self.scores[5],
                         "Find the präpositionen attached to the verb in isolation")

        create_line_menu(self, 380, lambda: controller.show_frame(PraepositionenKonjugationLevel6), 'level',
                         "Level 6", self.scores[6],
                         "Find the präpositionen attached to the verb in sentences")

        create_line_menu(self, 410, lambda: controller.show_frame(PraepositionenKonjugationLevel7), 'level',
                         "Level 7", self.scores[7],
                         "Find the Da-wort in sentences")

        create_line_menu(self, 440, lambda: controller.show_frame(PraepositionenKonjugationLevel8), 'level',
                         "Level 8", self.scores[8],
                         "Find the Wo-wort in sentences")

        create_section(self, "B2", 10, 470)

        create_line_menu(self, 530, lambda: controller.show_frame(PraepositionenKonjugationLevel9), 'level',
                         "Level 9", self.scores[9],
                         "Find the präpositionen attached to the verb in isolation")

        create_line_menu(self, 560, lambda: controller.show_frame(PraepositionenKonjugationLevel10), 'level',
                         "Level 10", self.scores[10],
                         "Find the präpositionen attached to the verb in sentences")

        create_line_menu(self, 590, lambda: controller.show_frame(PraepositionenKonjugationLevel11), 'level',
                         "Level 11", self.scores[11],
                         "Find the präpositionen attached to the noun in isolation")

        create_line_menu(self, 620, lambda: controller.show_frame(PraepositionenKonjugationLevel12), 'level',
                         "Level 12", self.scores[12],
                         "Find the präpositionen attached to the noun in sentences")

        create_line_menu(self, 650, lambda: controller.show_frame(PraepositionenKonjugationLevel13), 'level',
                         "Level 13", self.scores[13],
                         "Find the präpositionen attached to the adjective in isolation")

        create_line_menu(self, 680, lambda: controller.show_frame(PraepositionenKonjugationLevel14), 'level',
                         "Level 14", self.scores[14],
                         "Find the präpositionen attached to the adjective in sentences")

        create_button_back(self, "Back to Menu", lambda: controller.show_frame(StartPage))

    def update_data(self):
        from utils.exercises import praepositionen_konjugation
        from utils.statistics import highest_level_exercise
        from utils.statistics import answered_questions_by_exercise_and_level
        from utils.statistics import total_questions_by_exercise_and_level

        for level in range(1, highest_level_exercise(praepositionen_konjugation) + 1):
            score = (f"{answered_questions_by_exercise_and_level(praepositionen_konjugation, level)} / "
                     f"{total_questions_by_exercise_and_level(praepositionen_konjugation, level)}")
            self.scores[level].set(score)