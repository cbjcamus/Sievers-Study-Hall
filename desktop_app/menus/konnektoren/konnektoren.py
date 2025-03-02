import tkinter as tk

from desktop_app.interface.style import bg_color
from desktop_app.interface.widgets import (create_title, create_section, create_button_back, create_line_menu)
from menus.konnektoren.level1 import KonnektorenLevel1
from menus.konnektoren.level2 import KonnektorenLevel2
from menus.konnektoren.level3 import KonnektorenLevel3
from menus.konnektoren.level4 import KonnektorenLevel4
from menus.konnektoren.level5 import KonnektorenLevel5
from menus.konnektoren.level6 import KonnektorenLevel6
from menus.konnektoren.level7 import KonnektorenLevel7
from menus.konnektoren.level8 import KonnektorenLevel8


class Konnektoren(tk.Frame):
    def __init__(self, parent, controller):
        from menus.startpage import StartPage

        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg=bg_color)

        self.scores = {i: tk.StringVar() for i in range(0, 20)}

        create_title(self, "Konnektoren")

        create_section(self, "A1", 10, 50)

        create_line_menu(self, 110, lambda: controller.show_frame(KonnektorenLevel1), 'level',
                         "Level 1", self.scores[1], "A1 Connectors isolated")

        create_line_menu(self, 140, lambda: controller.show_frame(KonnektorenLevel2), 'level',
                         "Level 2", self.scores[2], "A1 Connectors in sentences")

        create_section(self, "A2", 10, 170)

        create_line_menu(self, 230, lambda: controller.show_frame(KonnektorenLevel3), 'level',
                         "Level 3", self.scores[3], "A2 Connectors isolated")

        create_line_menu(self, 260, lambda: controller.show_frame(KonnektorenLevel4), 'level',
                         "Level 4", self.scores[4], "A2 Connectors in sentences")

        create_section(self, "B1", 10, 290)

        create_line_menu(self, 350, lambda: controller.show_frame(KonnektorenLevel5), 'level',
                         "Level 5", self.scores[5], "B1 Connectors isolated")

        create_line_menu(self, 380, lambda: controller.show_frame(KonnektorenLevel6), 'level',
                         "Level 6", self.scores[6], "B1 Connectors in sentences")

        create_section(self, "B2", 10, 410)

        create_line_menu(self, 470, lambda: controller.show_frame(KonnektorenLevel7), 'level',
                         "Level 7", self.scores[7], "B2 Connectors isolated")

        create_line_menu(self, 500, lambda: controller.show_frame(KonnektorenLevel8), 'level',
                         "Level 8", self.scores[8], "B2 Connectors in sentences")

        create_button_back(self, "Back to Menu", lambda: controller.show_frame(StartPage))

    def update_data(self):
        from utils.exercises import konnektoren
        from utils.statistics import highest_level_exercise
        from utils.statistics import answered_questions_by_exercise_and_level
        from utils.statistics import total_questions_by_exercise_and_level

        for level in range(1, highest_level_exercise(konnektoren)+1):
            score = (f"{answered_questions_by_exercise_and_level(konnektoren, level)} / "
                     f"{total_questions_by_exercise_and_level(konnektoren, level)}")
            self.scores[level].set(score)