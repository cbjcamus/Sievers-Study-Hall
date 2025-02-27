import tkinter as tk

from interface.style import bg_color
from interface.widgets import (create_title, create_section, create_button_back, create_line_menu)
from menus.adjektivdeklinationen.level1 import AdjektivdeklinationenLevel1
from menus.adjektivdeklinationen.level2 import AdjektivdeklinationenLevel2
from menus.adjektivdeklinationen.level3 import AdjektivdeklinationenLevel3
from menus.adjektivdeklinationen.level4 import AdjektivdeklinationenLevel4
from menus.adjektivdeklinationen.level5 import AdjektivdeklinationenLevel5
from menus.adjektivdeklinationen.level6 import AdjektivdeklinationenLevel6
from menus.adjektivdeklinationen.level7 import AdjektivdeklinationenLevel7
from menus.adjektivdeklinationen.level8 import AdjektivdeklinationenLevel8
from menus.adjektivdeklinationen.level9 import AdjektivdeklinationenLevel9
from menus.adjektivdeklinationen.level10 import AdjektivdeklinationenLevel10
from menus.adjektivdeklinationen.level11 import AdjektivdeklinationenLevel11
from menus.adjektivdeklinationen.level12 import AdjektivdeklinationenLevel12
from menus.adjektivdeklinationen.level13 import AdjektivdeklinationenLevel13
from menus.adjektivdeklinationen.level14 import AdjektivdeklinationenLevel14
from menus.adjektivdeklinationen.level15 import AdjektivdeklinationenLevel15
from menus.adjektivdeklinationen.level16 import AdjektivdeklinationenLevel16


class Adjektivdeklinationen(tk.Frame):
    def __init__(self, parent, controller):
        from menus.startpage import StartPage

        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg=bg_color)
        self.scores = {i: tk.StringVar() for i in range(0, 20)}

        create_title(self, "Adjektivdeklinationen")

        create_section(self, "A2", 10, 50)

        create_line_menu(self, 110, lambda: controller.show_frame(AdjektivdeklinationenLevel1), 'level',
                         "Level 1", self.scores[1],
                         "Nominative, Accusative, and Dative adjectives in isolation")

        create_line_menu(self, 140, lambda: controller.show_frame(AdjektivdeklinationenLevel2), 'level',
                         "Level 2", self.scores[2],
                         "Nominative adjectives in sentences")

        create_line_menu(self, 170, lambda: controller.show_frame(AdjektivdeklinationenLevel3), 'level',
                         "Level 3", self.scores[3],
                         "Accusative adjectives in sentences")

        create_line_menu(self, 200, lambda: controller.show_frame(AdjektivdeklinationenLevel4), 'level',
                         "Level 4", self.scores[4],
                         "Dative adjectives in sentences")

        create_line_menu(self, 230, lambda: controller.show_frame(AdjektivdeklinationenLevel5), 'level',
                         "Level 5", self.scores[5],
                         "Adjectives with Definite articles in sentences")

        create_line_menu(self, 260, lambda: controller.show_frame(AdjektivdeklinationenLevel6), 'level',
                         "Level 6", self.scores[6],
                         "Adjectives with Indefinite articles in sentences")

        create_line_menu(self, 290, lambda: controller.show_frame(AdjektivdeklinationenLevel7), 'level',
                         "Level 7", self.scores[7],
                         "Adjectives with no article in sentences")

        create_line_menu(self, 320, lambda: controller.show_frame(AdjektivdeklinationenLevel8), 'level',
                         "Level 8", self.scores[8],
                         "Nominative, Accusative, and Dative adjectives in sentences")

        create_section(self, "B1", 10, 350)

        create_line_menu(self, 410, lambda: controller.show_frame(AdjektivdeklinationenLevel9), 'level',
                         "Level 9", self.scores[9],
                         "Genitive, Possessive, Demonstrative, and Negative adjectives in isolation")

        create_line_menu(self, 440, lambda: controller.show_frame(AdjektivdeklinationenLevel10), 'level',
                         "Level 10", self.scores[10],
                         "Genitive adjectives in sentences")

        create_line_menu(self, 470, lambda: controller.show_frame(AdjektivdeklinationenLevel11), 'level',
                         "Level 11", self.scores[11],
                         "Possessive adjectives in sentences")

        create_line_menu(self, 500, lambda: controller.show_frame(AdjektivdeklinationenLevel12), 'level',
                         "Level 12", self.scores[12],
                         "Demonstrative adjectives in sentences")

        create_line_menu(self, 530, lambda: controller.show_frame(AdjektivdeklinationenLevel13), 'level',
                         "Level 13", self.scores[13],
                         "Negative adjectives in sentences")

        create_line_menu(self, 560, lambda: controller.show_frame(AdjektivdeklinationenLevel14), 'level',
                         "Level 14", self.scores[14],
                         "Genitive, Possessive, Demonstrative, and Negative adjectives in sentences")

        create_section(self, "B2", 10, 590)

        create_line_menu(self, 650, lambda: controller.show_frame(AdjektivdeklinationenLevel15), 'level',
                         "Level 15", self.scores[15],
                         "Other articles in isolation")

        create_line_menu(self, 680, lambda: controller.show_frame(AdjektivdeklinationenLevel16), 'level',
                         "Level 16", self.scores[16],
                         "Other articles in sentences")

        create_button_back(self, "Back to Menu", lambda: controller.show_frame(StartPage))

    def update_data(self):
        from utils.exercises import (adjektivDeklinationen)
        from utils.statistics import highest_level_exercise
        from utils.statistics import answered_questions_by_exercise_and_level
        from utils.statistics import total_questions_by_exercise_and_level

        for level in range(1, highest_level_exercise(adjektivDeklinationen)+1):
            score = (f"{answered_questions_by_exercise_and_level(adjektivDeklinationen, level)} / "
                     f"{total_questions_by_exercise_and_level(adjektivDeklinationen, level)}")
            self.scores[level].set(score)