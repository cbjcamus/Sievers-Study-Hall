import tkinter as tk
import pandas as pd

from interface.style import bg_color, bullet
from interface.widgets import (create_title, create_button_back, create_subtitle, create_text_box,
                               create_entry, create_submit_button, create_result_text, create_feedback_text,
                               create_proverb_text, create_refresh_button, create_question_text)
from utils.normalization import is_equal
from utils.exercises import imperativ
from utils.paths import DATA_PATH, SCORE_PATH
from utils.proverbs import get_text_proverb

DATA_PATH = DATA_PATH[imperativ]
SCORE_PATH = f"{SCORE_PATH[imperativ]}/level2.csv"

class ImperativLevel2(tk.Frame):
    def __init__(self, parent, controller):
        from menus.imperativ.imperativ import Imperativ

        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg=bg_color)
        self.level = 2
        self.exercise = imperativ

        create_title(self, "Imperativ")
        create_subtitle(self, f"Level {self.level}")

        self.question = create_question_text(self)

        self.entry = create_entry(self)

        self.submit_button = create_submit_button(self, command=self.check_answer)

        self.result = create_result_text(self)

        self.feedback = create_feedback_text(self)

        self.proverb = create_proverb_text(self)

        create_button_back(self, "Back to Konjunktiv",
                           lambda: controller.show_frame(Imperativ))

        self.refresh_button = None
        self.load_data()
        self.get_new_question()

        self.entry.bind("<Return>", lambda event: self.check_answer())

    def load_data(self):
        try:
            self.scores = pd.read_csv(SCORE_PATH)
            self.prepare_dataframe()
            self.data = self.data[self.data["level"] == self.level]
            self.data = self.data.merge(self.scores, on="Nr", how="left").fillna(0)  # Merge only on "Nr"
            self.data = self.data[self.data["score"] == 0]
        except FileNotFoundError:
            self.prepare_dataframe()
            self.data = self.data[self.data["level"] == self.level]
            scores_df = pd.DataFrame({'Nr': self.data["Nr"].unique(), 'score': [0] * len(self.data["Nr"].unique())})
            scores_df.to_csv(SCORE_PATH, index=False)
            self.scores = pd.read_csv(SCORE_PATH)
            self.data = self.data.merge(self.scores, on="Nr", how="left").fillna(0)  # Merge only on "Nr"
            self.data = self.data[self.data["score"] == 0]
        except pd.errors.EmptyDataError:
            self.prepare_dataframe()
            self.data = self.data[self.data["level"] == self.level]
            scores_df = pd.DataFrame({'Nr': self.data["Nr"].unique(), 'score': [0] * len(self.data["Nr"].unique())})
            scores_df.to_csv(SCORE_PATH, index=False)
            self.scores = pd.read_csv(SCORE_PATH)
            self.data = self.data.merge(self.scores, on="Nr", how="left").fillna(0)  # Merge only on "Nr"
            self.data = self.data[self.data["score"] == 0]

    def prepare_dataframe(self):
        self.data = pd.read_csv(DATA_PATH)

        persons = ['du', 'ihr', 'Sie']
        new_rows = []

        for index, row in self.data.iterrows():
            for person in persons:
                new_row = row.drop(persons).to_dict()
                new_row['person'] = person
                new_row['imperativ'] = row[person]
                new_rows.append(new_row)

        self.data = pd.DataFrame(new_rows)
        self.data['Nr'] = range(1, len(self.data) + 1)

    def get_new_question(self):
        if not self.data.empty:
            self.current_question = self.data.sample(1).iloc[0]
            question = (f"Find the Imperativ of the following verb:"
                        f"\n\n{self.current_question['german']} {bullet} {self.current_question['person']}")
            self.question.config(text=question)
            self.proverb.config(text=get_text_proverb())
        else:
            self.question.config(text="All questions completed!")
            self.submit_button.place_forget()
            self.show_refresh_button()

    def check_answer(self):
        user_answer = self.entry.get().strip()
        correct_answer = self.current_question['imperativ'].strip()

        if is_equal(user_answer, correct_answer, self.exercise):
            self.result.config(text="Correct", fg="green")
            text = (f"{self.current_question['german']}, {self.current_question['person']} → "
                    f"{self.current_question['imperativ']}")
            self.feedback.config(text=text)
            self.update_score()
        else:
            self.result.config(text="Incorrect", fg="red")
            text = (f"{self.current_question['german']}, {self.current_question['person']} → "
                    f"{self.current_question['imperativ']}"
                    f"\n\nYour answer: {user_answer}")
            self.feedback.config(text=text)

        self.entry.delete(0, tk.END)
        self.get_new_question()

    def update_score(self):
        self.scores.loc[self.scores["Nr"] == self.current_question["Nr"], "score"] = 1
        self.scores.to_csv(SCORE_PATH, index=False)
        self.load_data()  # Reload data to remove answered questions

    def show_refresh_button(self):
        self.refresh_button = create_refresh_button(self, command=self.reset_scores)

    def reset_scores(self):
        self.scores = pd.read_csv(SCORE_PATH)
        self.data = pd.read_csv(DATA_PATH)
        self.scores = self.scores.merge(self.data, on="Nr", how="left")
        self.scores.loc[self.scores["level"] == self.level, "score"] = 0
        self.scores[['Nr', 'score']].to_csv(SCORE_PATH, index=False)
        self.refresh_button.place_forget()
        self.submit_button = create_submit_button(self, command=self.check_answer)
        self.load_data()
        self.get_new_question()

    def post_update(self):
        self.entry.focus()

    def update_data(self):
        pass