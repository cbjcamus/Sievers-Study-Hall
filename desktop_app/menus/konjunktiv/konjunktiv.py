import tkinter as tk

from desktop_app.interface.style import bg_color
from desktop_app.interface.widgets import (create_title, create_section, create_button_back, create_line_menu)
from menus.konjunktiv.level1 import KonjunktivLevel1



class Konjunktiv(tk.Frame):
    def __init__(self, parent, controller):
        from menus.startpage import StartPage

        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg=bg_color)

        self.scores = {i: tk.StringVar() for i in range(0, 20)}

        create_title(self, "Konjunktiv")

        create_section(self, "A2", 10, 50)

        create_line_menu(self, 110, lambda: controller.show_frame(KonjunktivLevel1), 'level',
                         "Level 1", self.scores[1], "Find the Konjunktiv of the most common German verbs")

        create_button_back(self, "Back to Menu", lambda: controller.show_frame(StartPage))

    def update_data(self):
        from utils.exercises import (konjunktiv)
        from utils.statistics import highest_level_exercise
        from utils.statistics import answered_questions_by_exercise_and_level
        from utils.statistics import total_questions_by_exercise_and_level

        for level in range(1, highest_level_exercise(konjunktiv)+1):
            score = (f"{answered_questions_by_exercise_and_level(konjunktiv, level)} / "
                     f"{total_questions_by_exercise_and_level(konjunktiv, level) * 6}")
            self.scores[level].set(score)