import tkinter as tk

from interface.style import bg_color
from interface.widgets import (create_title, create_section, create_button_back, create_line_menu)
from menus.verben.level1 import VerbenLevel1
from menus.verben.level2 import VerbenLevel2
from menus.verben.level3 import VerbenLevel3
from menus.verben.level4 import VerbenLevel4
from menus.verben.level5 import VerbenLevel5
from menus.verben.level6 import VerbenLevel6
from menus.verben.level7 import VerbenLevel7
from menus.verben.level8 import VerbenLevel8


class Verben(tk.Frame):
    def __init__(self, parent, controller):
        from menus.startpage import StartPage

        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg=bg_color)

        self.scores = {i: tk.StringVar() for i in range(0, 20)}

        create_title(self, "Verben")

        create_section(self, "A1", 10, 50)

        create_line_menu(self, 110, lambda: controller.show_frame(VerbenLevel1), 'level',
                         "Level 1", self.scores[1],
                         "General A1 verbs")

        create_section(self, "A2", 10, 140)

        create_line_menu(self, 200, lambda: controller.show_frame(VerbenLevel2), 'level',
                         "Level 2", self.scores[2],
                         "General A2 verbs")

        create_section(self, "B1", 10, 230)

        create_line_menu(self, 290, lambda: controller.show_frame(VerbenLevel3), 'level',
                         "Level 3", self.scores[3],
                         "General B1 verbs")

        create_line_menu(self, 320, lambda: controller.show_frame(VerbenLevel4), 'level',
                         "Level 4", self.scores[4],
                         "Everyday live verbs")

        create_line_menu(self, 320, lambda: controller.show_frame(VerbenLevel4), 'level',
                         "Level 10", self.scores[10],
                         "Food, Beverages, and Cooking verbs")

        create_line_menu(self, 350, lambda: controller.show_frame(VerbenLevel8), 'level',
                         "Level 11", self.scores[11],
                         "Free time, Hobbies, Traveling and Relaxing verbs")

        create_line_menu(self, 380, lambda: controller.show_frame(VerbenLevel8), 'level',
                         "Level 12", self.scores[12],
                         "Learning, Studying and Researching verbs")

        create_line_menu(self, 410, lambda: controller.show_frame(VerbenLevel8), 'level',
                         "Level 13", self.scores[13],
                         "Senses, emotions verbs")

        create_section(self, "B2", 10, 440)

        create_line_menu(self, 500, lambda: controller.show_frame(VerbenLevel5), 'level',
                         "Level 5", self.scores[5],
                         "General B2 verbs")

        create_line_menu(self, 530, lambda: controller.show_frame(VerbenLevel8), 'level',
                         "Level 8", self.scores[8],
                         "Verbs derived from comparative adjectives")

        create_line_menu(self, 560, lambda: controller.show_frame(VerbenLevel8), 'level',
                         "Level 9", self.scores[9],
                         "Transitive verbs")

        create_line_menu(self, 590, lambda: controller.show_frame(VerbenLevel8), 'level',
                         "Level 14", self.scores[14],
                         "Speaking and Thinking verbs")

        create_line_menu(self, 620, lambda: controller.show_frame(VerbenLevel8), 'level',
                         "Level 15", self.scores[15],
                         "Work, Economy and Production verbs")

        create_line_menu(self, 650, lambda: controller.show_frame(VerbenLevel8), 'level',
                         "Level 16", self.scores[16],
                         "Society, Government and Media verbs")

        create_line_menu(self, 680, lambda: controller.show_frame(VerbenLevel8), 'level',
                         "Level 17", self.scores[17],
                         "Money verbs")

        create_button_back(self, "Back to Menu", lambda: controller.show_frame(StartPage))

    def update_data(self):
        from utils.exercises import (verben)
        from utils.statistics import highest_level_exercise
        from utils.statistics import answered_questions_by_exercise_and_level
        from utils.statistics import total_questions_by_exercise_and_level

        for level in range(1, highest_level_exercise(verben)+1):
            score = (f"{answered_questions_by_exercise_and_level(verben, level)} / "
                     f"{total_questions_by_exercise_and_level(verben, level)}")
            self.scores[level].set(score)