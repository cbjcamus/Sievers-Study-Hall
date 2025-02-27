import tkinter as tk

from interface.style import bg_color
from interface.widgets import (create_title, create_section, create_button, create_button_back,
                               create_text_box_scores, create_text_info, create_line_menu)
from menus.praesens.level1 import PraesensLevel1
from menus.praesens.level2 import PraesensLevel2
from menus.praesens.level3 import PraesensLevel3
from menus.praesens.level4 import PraesensLevel4
from menus.praesens.level5 import PraesensLevel5
from menus.praesens.level6 import PraesensLevel6
from menus.praesens.level7 import PraesensLevel7
from menus.praesens.level8 import PraesensLevel8
from menus.praesens.level9 import PraesensLevel9
from menus.praesens.level10 import PraesensLevel10


class Praesens(tk.Frame):
    def __init__(self, parent, controller):
        from menus.startpage import StartPage

        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg=bg_color)

        self.scores = {i: tk.StringVar() for i in range(0, 20)}

        create_title(self, "Präsens")

        create_section(self, "A1", 10, 50)

        create_line_menu(self, 110, lambda: controller.show_frame(PraesensLevel1), 'level',
                         "Level 1", self.scores[1], "Find the present tense of 15 A1 verbs")

        create_line_menu(self, 140, lambda: controller.show_frame(PraesensLevel2), 'level',
                         "Level 2", self.scores[2], "Find the present tense of 15 A1 verbs")

        create_line_menu(self, 170, lambda: controller.show_frame(PraesensLevel3), 'level',
                         "Level 3", self.scores[3], "Find the present tense of 15 A1 verbs")

        create_line_menu(self, 200, lambda: controller.show_frame(PraesensLevel4), 'level',
                         "Level 4", self.scores[4], "Find the present tense of 15 A1 verbs")

        create_line_menu(self, 230, lambda: controller.show_frame(PraesensLevel5), 'level',
                         "Level 5", self.scores[5], "Find the present tense of 15 A1 verbs")

        create_section(self, "A2", 10, 260)

        create_line_menu(self, 320, lambda: controller.show_frame(PraesensLevel6), 'level',
                         "Level 6", self.scores[6], "Find the present tense of 15 A2 verbs")

        create_line_menu(self, 350, lambda: controller.show_frame(PraesensLevel7), 'level',
                         "Level 7", self.scores[7], "Find the present tense of 15 A2 verbs")

        create_line_menu(self, 380, lambda: controller.show_frame(PraesensLevel8), 'level',
                         "Level 8", self.scores[8], "Find the present tense of 15 A2 verbs")

        create_line_menu(self, 410, lambda: controller.show_frame(PraesensLevel9), 'level',
                         "Level 9", self.scores[9], "Find the present tense of 15 A2 verbs")

        create_line_menu(self, 440, lambda: controller.show_frame(PraesensLevel10), 'level',
                         "Level 10", self.scores[10], "Find the present tense of 15 A2 verbs")

        create_button_back(self, "Back to Menu", lambda: controller.show_frame(StartPage))

    def update_data(self):
        from utils.exercises import (praesens)
        from utils.statistics import highest_level_exercise
        from utils.statistics import answered_questions_by_exercise_and_level
        from utils.statistics import total_questions_by_exercise_and_level

        for level in range(1, highest_level_exercise(praesens)+1):
            score = (f"{answered_questions_by_exercise_and_level(praesens, level)} / "
                     f"{total_questions_by_exercise_and_level(praesens, level) * 6}")
            self.scores[level].set(score)