import tkinter as tk

from interface.style import bg_color
from interface.widgets import (create_title, create_section, create_button_back, create_line_menu)
from menus.adverbien.level1 import AdverbienLevel1
from menus.adverbien.level2 import AdverbienLevel2
from menus.adverbien.level3 import AdverbienLevel3
from menus.adverbien.level4 import AdverbienLevel4
from menus.adverbien.level5 import AdverbienLevel5
from menus.adverbien.level6 import AdverbienLevel6
from menus.adverbien.level7 import AdverbienLevel7
from menus.adverbien.level8 import AdverbienLevel8


class Adverbien(tk.Frame):
    def __init__(self, parent, controller):
        from menus.startpage import StartPage

        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg=bg_color)

        self.scores = {i: tk.StringVar() for i in range(0, 20)}

        create_title(self, "Adverbien")

        create_section(self, "A1", 10, 50)

        create_line_menu(self, 110, lambda: controller.show_frame(AdverbienLevel1), 'level',
                         "Level 1", self.scores[1], "Basic Adverbs")

        create_line_menu(self, 140, lambda: controller.show_frame(AdverbienLevel2), 'level',
                         "Level 2", self.scores[2], "Basic Adverbs in sentences")

        create_section(self, "A2", 10, 170)

        create_line_menu(self, 230, lambda: controller.show_frame(AdverbienLevel3), 'level',
                         "Level 3", self.scores[3], "Simple Adverbs")

        create_line_menu(self, 260, lambda: controller.show_frame(AdverbienLevel4), 'level',
                         "Level 4", self.scores[4], "Simple Adverbs in sentences")

        create_section(self, "B1", 10, 290)

        create_line_menu(self, 350, lambda: controller.show_frame(AdverbienLevel5), 'level',
                         "Level 5", self.scores[5], "Familiar Adverbs")

        create_line_menu(self, 380, lambda: controller.show_frame(AdverbienLevel6), 'level',
                         "Level 6", self.scores[6], "Familiar Adverbs in sentences")

        create_section(self, "B2", 10, 410)

        create_line_menu(self, 470, lambda: controller.show_frame(AdverbienLevel7), 'level',
                         "Level 7", self.scores[7], "Common Adverbs")

        create_line_menu(self, 500, lambda: controller.show_frame(AdverbienLevel8), 'level',
                         "Level 8", self.scores[8], "Common Adverbs in sentences")

        create_button_back(self, "Back to Menu", lambda: controller.show_frame(StartPage))

    def update_data(self):
        from utils.exercises import (adverbien)
        from utils.statistics import highest_level_exercise
        from utils.statistics import answered_questions_by_exercise_and_level
        from utils.statistics import total_questions_by_exercise_and_level

        for level in range(1, highest_level_exercise(adverbien)+1):
            score = (f"{answered_questions_by_exercise_and_level(adverbien, level)} / "
                     f"{total_questions_by_exercise_and_level(adverbien, level)}")
            self.scores[level].set(score)