import tkinter as tk

from interface.style import bg_color
from interface.widgets import (create_title, create_section, create_button_back, create_line_menu)
from menus.artikel.level1 import ArtikelLevel1
from menus.artikel.level2 import ArtikelLevel2
from menus.artikel.level3 import ArtikelLevel3
from menus.artikel.level4 import ArtikelLevel4
from menus.artikel.level5 import ArtikelLevel5
from menus.artikel.level6 import ArtikelLevel6
from menus.artikel.level7 import ArtikelLevel7
from menus.artikel.level8 import ArtikelLevel8
from menus.artikel.level9 import ArtikelLevel9
from menus.artikel.level10 import ArtikelLevel10
from menus.artikel.level11 import ArtikelLevel11
from menus.artikel.level12 import ArtikelLevel12
from menus.artikel.level13 import ArtikelLevel13

class Artikel(tk.Frame):
    def __init__(self, parent, controller):
        from menus.startpage import StartPage

        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg=bg_color)

        self.scores = {i: tk.StringVar() for i in range(0, 20)}

        create_title(self, "Artikel")

        create_section(self, "A1", 10, 50)

        create_line_menu(self, 110, lambda: controller.show_frame(ArtikelLevel1), 'level',
                         "Level 1", self.scores[1],
                         "Nominative Definite articles")

        create_line_menu(self, 140, lambda: controller.show_frame(ArtikelLevel2), 'level',
                         "Level 2", self.scores[2],
                         "Accusative Definite articles")

        create_line_menu(self, 170, lambda: controller.show_frame(ArtikelLevel3), 'level',
                         "Level 3", self.scores[3],
                         "Dative Definite articles")

        create_line_menu(self, 200, lambda: controller.show_frame(ArtikelLevel4), 'level',
                         "Level 4", self.scores[4],
                         "Nominative, Accusative, and Dative Definite articles")

        create_line_menu(self, 230, lambda: controller.show_frame(ArtikelLevel5), 'level',
                         "Level 5", self.scores[5],
                         "Nominative Indefinite articles")

        create_line_menu(self, 260, lambda: controller.show_frame(ArtikelLevel6), 'level',
                         "Level 6", self.scores[6],
                         "Accusative Indefinite articles")

        create_line_menu(self, 290, lambda: controller.show_frame(ArtikelLevel7), 'level',
                         "Level 7", self.scores[7],
                         "Dative Indefinite articles")

        create_line_menu(self, 320, lambda: controller.show_frame(ArtikelLevel8), 'level',
                         "Level 8", self.scores[8],
                         "Nominative, Accusative, and Dative Indefinite articles")

        create_section(self, "A2", 10, 350)

        create_line_menu(self, 410, lambda: controller.show_frame(ArtikelLevel9), 'level',
                         "Level 9", self.scores[9],
                         "Accusative and Dative definite article with prepositions")

        create_line_menu(self, 440, lambda: controller.show_frame(ArtikelLevel10), 'level',
                         "Level 10", self.scores[10],
                         "Simple Articles isolated")

        create_line_menu(self, 470, lambda: controller.show_frame(ArtikelLevel11), 'level',
                         "Level 11", self.scores[11],
                         "Simple Articles in sentences")

        create_section(self, "B2", 10, 500)

        create_line_menu(self, 560, lambda: controller.show_frame(ArtikelLevel12), 'level',
                         "Level 12", self.scores[12],
                         "Common Articles isolated")

        create_line_menu(self, 590, lambda: controller.show_frame(ArtikelLevel13), 'level',
                         "Level 13", self.scores[13],
                         "Common Articles in sentences")

        create_button_back(self, "Back to Menu", lambda: controller.show_frame(StartPage))

    def update_data(self):
        from utils.exercises import artikel
        from utils.statistics import highest_level_exercise
        from utils.statistics import answered_questions_by_exercise_and_level
        from utils.statistics import total_questions_by_exercise_and_level

        for level in range(1, highest_level_exercise(artikel)+1):
            score = (f"{answered_questions_by_exercise_and_level(artikel, level)} / "
                     f"{total_questions_by_exercise_and_level(artikel, level)}")
            self.scores[level].set(score)