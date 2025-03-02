import tkinter as tk

from desktop_app.interface.style import bg_color
from desktop_app.interface.widgets import (create_title, create_section, create_line_menu, create_button_back)
from menus.perfekt.level1 import PerfektLevel1
from menus.perfekt.level2 import PerfektLevel2
from menus.perfekt.level3 import PerfektLevel3
from menus.perfekt.level4 import PerfektLevel4
from menus.perfekt.level5 import PerfektLevel5
from menus.perfekt.level6 import PerfektLevel6
from menus.perfekt.level7 import PerfektLevel7
from menus.perfekt.level8 import PerfektLevel8


class Perfekt(tk.Frame):
    def __init__(self, parent, controller):
        from menus.startpage import StartPage

        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg=bg_color)

        self.scores = {i: tk.StringVar() for i in range(0, 20)}

        create_title(self, "Perfekt")

        create_section(self, "A1", 10, 50)

        create_line_menu(self, 110, lambda: controller.show_frame(PerfektLevel1), 'level',
                         "Level 1", self.scores[1],
                         "Find the Partizip II of A1 verbs in isolation")

        create_line_menu(self, 140, lambda: controller.show_frame(PerfektLevel2), 'level',
                         "Level 2", self.scores[2],
                         "Find the Partizip II of A1 verbs in sentences")

        create_line_menu(self, 170, lambda: controller.show_frame(PerfektLevel3), 'level',
                         "Level 3", self.scores[3],
                         "Find the Hilfsverb of A1 verbs in sentences")

        create_section(self, "A2", 10, 200)

        create_line_menu(self, 260, lambda: controller.show_frame(PerfektLevel4), 'level',
                         "Level 4", self.scores[4],
                         "Find the Partizip II of A2 verbs in isolation")

        create_line_menu(self, 290, lambda: controller.show_frame(PerfektLevel5), 'level',
                         "Level 5", self.scores[5],
                         "Find the Partizip II of A2 verbs in sentences")

        create_line_menu(self, 320, lambda: controller.show_frame(PerfektLevel6), 'level',
                         "Level 6", self.scores[6],
                         "Find the Hilfsverb of A2 verbs in sentences")

        create_section(self, "B1", 10, 350)

        create_line_menu(self, 410, lambda: controller.show_frame(PerfektLevel7), 'level',
                         "Level 7", self.scores[7],
                         "Find the Partizip II of 75 B1 verbs")

        create_line_menu(self, 440, lambda: controller.show_frame(PerfektLevel8), 'level',
                         "Level 8", self.scores[8],
                         "Find the Partizip II of 75 B1 verbs")

        create_button_back(self, "Back to Menu", lambda: controller.show_frame(StartPage))

    def update_data(self):
        from utils.exercises import (perfekt)
        from utils.statistics import highest_level_exercise
        from utils.statistics import answered_questions_by_exercise_and_level
        from utils.statistics import total_questions_by_exercise_and_level

        for level in range(1, highest_level_exercise(perfekt)+1):
            score = (f"{answered_questions_by_exercise_and_level(perfekt, level)} / "
                     f"{total_questions_by_exercise_and_level(perfekt, level)}")
            self.scores[level].set(score)