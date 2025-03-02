import tkinter as tk

from desktop_app.interface.style import bg_color
from desktop_app.interface.widgets import (create_title, create_section, create_button_back,
                                           create_line_menu)
from menus.pronomen.level1 import PronomenLevel1
from menus.pronomen.level2 import PronomenLevel2
from menus.pronomen.level3 import PronomenLevel3
from menus.pronomen.level4 import PronomenLevel4
from menus.pronomen.level5 import PronomenLevel5
from menus.pronomen.level6 import PronomenLevel6


class Pronomen(tk.Frame):
    def __init__(self, parent, controller):
        from menus.startpage import StartPage

        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg=bg_color)

        self.scores = {i: tk.StringVar() for i in range(0, 20)}

        create_title(self, "Pronomen")

        create_section(self, "A1", 10, 50)

        create_line_menu(self, 110, lambda: controller.show_frame(PronomenLevel1), 'level',
                         "Level 1", self.scores[1],
                         "Nominative pronouns in sentences")

        create_line_menu(self, 140, lambda: controller.show_frame(PronomenLevel2), 'level',
                         "Level 2", self.scores[2],
                         "Accusative pronouns in sentences")

        create_line_menu(self, 170, lambda: controller.show_frame(PronomenLevel3), 'level',
                         "Level 3", self.scores[3],
                         "Dative pronouns in sentences")

        create_line_menu(self, 200, lambda: controller.show_frame(PronomenLevel4), 'level',
                         "Level 4", self.scores[4],
                         "Accusative and Dative pronouns in sentences")

        create_section(self, "A2", 10, 230)

        create_line_menu(self, 290, lambda: controller.show_frame(PronomenLevel5), 'level',
                         "Level 5", self.scores[5],
                         "Reflexive pronouns in sentences")

        create_line_menu(self, 320, lambda: controller.show_frame(PronomenLevel6), 'level',
                         "Level 6", self.scores[6],
                         "Accusative, Dative, and Reflexive pronouns in sentences")

        create_button_back(self, "Back to Menu", lambda: controller.show_frame(StartPage))

    def update_data(self):
        from utils.exercises import (pronomen)
        from utils.statistics import highest_level_exercise
        from utils.statistics import answered_questions_by_exercise_and_level
        from utils.statistics import total_questions_by_exercise_and_level

        for level in range(1, highest_level_exercise(pronomen)+1):
            score = (f"{answered_questions_by_exercise_and_level(pronomen, level)} / "
                     f"{total_questions_by_exercise_and_level(pronomen, level)}")
            self.scores[level].set(score)