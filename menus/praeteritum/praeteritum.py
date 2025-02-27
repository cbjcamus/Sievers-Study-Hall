import tkinter as tk

from interface.style import bg_color
from interface.widgets import (create_title, create_section, create_button_back, create_line_menu)
from menus.praeteritum.level1 import PraeteritumLevel1
from menus.praeteritum.level2 import PraeteritumLevel2
from menus.praeteritum.level3 import PraeteritumLevel3
from menus.praeteritum.level4 import PraeteritumLevel4
from menus.praeteritum.level5 import PraeteritumLevel5


class Praeteritum(tk.Frame):
    def __init__(self, parent, controller):
        from menus.startpage import StartPage

        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg=bg_color)

        self.scores = {i: tk.StringVar() for i in range(0, 20)}

        create_title(self, "Präteritum")

        create_section(self, "A2", 10, 50)

        create_line_menu(self, 110, lambda: controller.show_frame(PraeteritumLevel1), 'level',
                         "Level 1", self.scores[1],
                         "Find the präteritum the most common verbs")

        create_section(self, "B1", 10, 140)

        create_line_menu(self, 200, lambda: controller.show_frame(PraeteritumLevel2), 'level',
                         "Level 2", self.scores[2],
                         "Find the präteritum (3rd. Per. Singular) of A1 verbs")

        create_line_menu(self, 230, lambda: controller.show_frame(PraeteritumLevel3), 'level',
                         "Level 3", self.scores[3],
                         "Find the präteritum (3rd. Per. Singular) of A2 verbs")

        create_section(self, "B2", 10, 260)

        create_line_menu(self, 320, lambda: controller.show_frame(PraeteritumLevel4), 'level',
                         "Level 4", self.scores[4],
                         "Find the präteritum (3rd. Per. Singular) of B1 verbs")

        create_line_menu(self, 350, lambda: controller.show_frame(PraeteritumLevel5), 'level',
                         "Level 5", self.scores[5],
                         "Find the präteritum (3rd. Per. Singular) of B1 verbs")

        create_button_back(self, "Back to Menu", lambda: controller.show_frame(StartPage))

    def update_data(self):
        from utils.exercises import (praeteritum)
        from utils.statistics import highest_level_exercise
        from utils.statistics import answered_questions_by_exercise_and_level
        from utils.statistics import total_questions_by_exercise_and_level

        for level in range(1, 5+1):
            score = (f"{answered_questions_by_exercise_and_level(praeteritum, level)} / "
                     f"{total_questions_by_exercise_and_level(praeteritum, level)}")
            self.scores[level].set(score)

        score_level1 = (f"{answered_questions_by_exercise_and_level(praeteritum, 1)} / "
                        f"{total_questions_by_exercise_and_level(praeteritum, 1) * 6}")
        self.scores[1].set(score_level1)