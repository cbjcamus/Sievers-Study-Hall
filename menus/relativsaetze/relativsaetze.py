import tkinter as tk

from interface.style import bg_color
from interface.widgets import (create_title, create_section, create_button_back, create_line_menu)
from menus.relativsaetze.level1 import RelativsaetzeLevel1
from menus.relativsaetze.level2 import RelativsaetzeLevel2
from menus.relativsaetze.level3 import RelativsaetzeLevel3
from menus.relativsaetze.level4 import RelativsaetzeLevel4
from menus.relativsaetze.level5 import RelativsaetzeLevel5
from menus.relativsaetze.level6 import RelativsaetzeLevel6
from menus.relativsaetze.level7 import RelativsaetzeLevel7


class Relativsaetze(tk.Frame):
    def __init__(self, parent, controller):
        from menus.startpage import StartPage

        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg=bg_color)

        self.scores = {i: tk.StringVar() for i in range(0, 20)}

        create_title(self, "Relativsätze")

        create_section(self, "B1", 10, 50)

        create_line_menu(self, 110, lambda: controller.show_frame(RelativsaetzeLevel1), 'level',
                         "Level 1", self.scores[1],
                         "Nominative relativpronomen in sentences")

        create_line_menu(self, 140, lambda: controller.show_frame(RelativsaetzeLevel2), 'level',
                         "Level 2", self.scores[2],
                         "Accusative relativpronomen in sentences")

        create_line_menu(self, 170, lambda: controller.show_frame(RelativsaetzeLevel3), 'level',
                         "Level 3", self.scores[3],
                         "Dative relativpronomen in sentences")

        create_line_menu(self, 200, lambda: controller.show_frame(RelativsaetzeLevel4), 'level',
                         "Level 4", self.scores[4],
                         "Genitive relativpronomen in sentences")

        create_line_menu(self, 230, lambda: controller.show_frame(RelativsaetzeLevel5), 'level',
                         "Level 5", self.scores[5],
                         "Relativpronomen in all cases in sentences")

        create_line_menu(self, 260, lambda: controller.show_frame(RelativsaetzeLevel6), 'level',
                         "Level 6", self.scores[6],
                         "Relativpronomen with some prepositions in sentences")

        create_section(self, "B2", 10, 290)

        #create_line_menu(self, 350, lambda: controller.show_frame(RelativsaetzeLevel7), 'level',
        #                 "Level 7", self.scores[7],
        #                 "Relativpronomen for places in sentences")


        create_button_back(self, "Back to Menu", lambda: controller.show_frame(StartPage))

    def update_data(self):
        from utils.exercises import relativSaetze
        from utils.statistics import highest_level_exercise
        from utils.statistics import answered_questions_by_exercise_and_level
        from utils.statistics import total_questions_by_exercise_and_level

        for level in range(1, highest_level_exercise(relativSaetze)+1):
            score = (f"{answered_questions_by_exercise_and_level(relativSaetze, level)} / "
                     f"{total_questions_by_exercise_and_level(relativSaetze, level)}")
            self.scores[level].set(score)