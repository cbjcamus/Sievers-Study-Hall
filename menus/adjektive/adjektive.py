import tkinter as tk

from interface.style import bg_color
from interface.widgets import (create_title, create_section, create_button_back, create_line_menu)
from menus.adjektive.level1 import AdjektiveLevel1

class Adjektive(tk.Frame):
    def __init__(self, parent, controller):
        from menus.startpage import StartPage

        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg=bg_color)

        self.scores = {i: tk.StringVar() for i in range(0, 20)}

        create_title(self, "Adjektive")

        create_section(self, "A1", 10, 50)

        create_line_menu(self, 110, lambda: controller.show_frame(AdjektiveLevel1), 'level',
                         "Level 1", self.scores[1], "A1 Adjectives English to German Translation")

        create_line_menu(self, 140, lambda: controller.show_frame(AdjektiveLevel1), 'level',
                         "Level 2", self.scores[2], "A1 Adjective -- Comparative")

        create_line_menu(self, 170, lambda: controller.show_frame(AdjektiveLevel1), 'level',
                         "Level 3", self.scores[3], "A1 Adjectives -- Superlative")

        create_section(self, "A2", 10, 200)

        create_line_menu(self, 260, lambda: controller.show_frame(AdjektiveLevel1), 'level',
                         "Level 4", self.scores[4], "A2 Adjectives English to German Translation")

        create_line_menu(self, 290, lambda: controller.show_frame(AdjektiveLevel1), 'level',
                         "Level 5", self.scores[5], "A2 Adjective -- Comparative")

        create_line_menu(self, 320, lambda: controller.show_frame(AdjektiveLevel1), 'level',
                         "Level 6", self.scores[6], "A2 Adjectives -- Superlative")

        create_button_back(self, "Back to Menu", lambda: controller.show_frame(StartPage))

    def update_data(self):
        from utils.exercises import adjektive
        from utils.statistics import highest_level_exercise
        from utils.statistics import answered_questions_by_exercise_and_level
        from utils.statistics import total_questions_by_exercise_and_level

        for level in range(1, highest_level_exercise(adjektive)+1):
            score = (f"{answered_questions_by_exercise_and_level(adjektive, level)} / "
                     f"{total_questions_by_exercise_and_level(adjektive, level)}")
            self.scores[level].set(score)