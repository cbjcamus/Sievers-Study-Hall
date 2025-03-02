import tkinter as tk

from desktop_app.interface.style import bg_color
from desktop_app.interface.widgets import (create_title, create_section, create_button_back,
                                           create_line_menu)
from menus.imperativ.level1 import ImperativLevel1
from menus.imperativ.level2 import ImperativLevel2
from menus.imperativ.level3 import ImperativLevel3
from menus.imperativ.level4 import ImperativLevel4
from menus.imperativ.level5 import ImperativLevel5


class Imperativ(tk.Frame):
    def __init__(self, parent, controller):
        from menus.startpage import StartPage

        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg=bg_color)

        self.scores = {i: tk.StringVar() for i in range(0, 20)}

        create_title(self, "Imperativ")

        create_section(self, "A1", 10, 50)

        #create_button(self, "Level 1", 10, 100, lambda: controller.show_frame(ImperativLevel1))
        #create_text_box_scores(self, self.scores[1], 100, 'level')
        #create_text_info(self, "Find the Imperativ of the following verbs", 100)

        create_line_menu(self, 110, lambda: controller.show_frame(ImperativLevel1), 'level',
                         "Level 1", self.scores[1], "Find the Imperativ of A1 verbs")

        create_line_menu(self, 140, lambda: controller.show_frame(ImperativLevel2), 'level',
                         "Level 2", self.scores[2], "Find the Imperativ of A1 verbs")

        create_line_menu(self, 170, lambda: controller.show_frame(ImperativLevel3), 'level',
                         "Level 3", self.scores[3], "Find the Imperativ of A1 verbs")

        create_line_menu(self, 200, lambda: controller.show_frame(ImperativLevel4), 'level',
                         "Level 4", self.scores[4], "Find the Imperativ of A1 verbs")

        create_line_menu(self, 230, lambda: controller.show_frame(ImperativLevel5), 'level',
                         "Level 5", self.scores[5], "Find the Imperativ of A1 verbs")

        create_button_back(self, "Back to Menu", lambda: controller.show_frame(StartPage))

    def update_data(self):
        from utils.exercises import (imperativ)
        from utils.statistics import highest_level_exercise
        from utils.statistics import answered_questions_by_exercise_and_level
        from utils.statistics import total_questions_by_exercise_and_level

        for level in range(1, highest_level_exercise(imperativ)+1):
            score = (f"{answered_questions_by_exercise_and_level(imperativ, level)} / "
                     f"{total_questions_by_exercise_and_level(imperativ, level) * 3}")
            self.scores[level].set(score)