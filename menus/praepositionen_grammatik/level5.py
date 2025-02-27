import tkinter as tk
import pandas as pd

from interface.style import bg_color
from interface.widgets import (create_title, create_button_back, create_subtitle,
                               create_entry, create_submit_button, create_result_text, create_feedback_text,
                               create_proverb_text, create_refresh_button, create_question_text)
from utils.normalization import is_equal
from utils.exercises import praepositionen_grammatik
from utils.paths import DATA_PATH, SCORE_PATH
from utils.proverbs import get_text_proverb

DATA_PATH = DATA_PATH[praepositionen_grammatik]
SCORE_PATH = f"{SCORE_PATH[praepositionen_grammatik]}/level5.csv"


class PraepositionenGrammatikLevel5(tk.Frame):
    def __init__(self, parent, controller):
        from menus.praepositionen_grammatik.praepositionen_grammatik import PraepositionenGrammatik

        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg=bg_color)
        self.level = 5
        self.exercise = praepositionen_grammatik

        create_title(self, "Präpositionen — Grammatik")
        create_subtitle(self, f"Level {self.level}")

        self.question = create_question_text(self)

        self.entry = create_entry(self, question_lines=3)

        self.submit_button = create_submit_button(self, command=self.check_answer, question_lines=3)

        self.result = create_result_text(self, question_lines=3)

        self.feedback = create_feedback_text(self, question_lines=3)

        self.proverb = create_proverb_text(self)

        create_button_back(self, "Back to Präpositionen",
                           lambda: controller.show_frame(PraepositionenGrammatik))

        self.refresh_button = None
        self.load_data()
        self.get_new_question()

        self.entry.bind("<Return>", lambda event: self.check_answer())

    def load_data(self):
        try:
            self.scores = pd.read_csv(SCORE_PATH)
            self.data = pd.read_csv(DATA_PATH)
            self.data = self.data[self.data["level"] == self.level]
            self.data = self.data.merge(self.scores, on="Nr", how="left").fillna(0)  # Merge only on "Nr"
            self.data = self.data[self.data["score"] == 0]
        except FileNotFoundError:
            self.data = pd.read_csv(DATA_PATH)
            self.data = self.data[self.data["level"] == self.level]
            scores_df = pd.DataFrame({'Nr': self.data["Nr"].unique(), 'score': [0] * len(self.data["Nr"].unique())})
            scores_df.to_csv(SCORE_PATH, index=False)
            self.scores = pd.read_csv(SCORE_PATH)
            self.data = self.data.merge(self.scores, on="Nr", how="left").fillna(0)  # Merge only on "Nr"
            self.data = self.data[self.data["score"] == 0]
        except pd.errors.EmptyDataError:
            self.data = pd.read_csv(DATA_PATH)
            self.data = self.data[self.data["level"] == self.level]
            scores_df = pd.DataFrame({'Nr': self.data["Nr"].unique(), 'score': [0] * len(self.data["Nr"].unique())})
            scores_df.to_csv(SCORE_PATH, index=False)
            self.scores = pd.read_csv(SCORE_PATH)
            self.data = self.data.merge(self.scores, on="Nr", how="left").fillna(0)  # Merge only on "Nr"
            self.data = self.data[self.data["score"] == 0]

    def get_new_question(self):
        if not self.data.empty:
            self.current_question = self.data.sample(1).iloc[0]
            question = (f"Find the präposition that fits in the following sentence:"
                        f"\n\n{self.current_question['german']}"
                        f"\n\n{self.current_question['english']}")
            self.question.config(text=question)
            self.proverb.config(text=get_text_proverb())
        else:
            self.question.config(text="All questions completed!")
            self.submit_button.place_forget()
            self.show_refresh_button()

    def check_answer(self):
        user_answer = self.entry.get().strip()
        correct_answer = self.current_question["preposition"].strip()

        if is_equal(user_answer, correct_answer, self.exercise):
            self.result.config(text="Correct", fg="green")
            text = (f"{self.current_question['sentence']}"
                    f"\n\n{self.current_question['english']}")
            self.feedback.config(text=text)
            self.update_score()
        else:
            self.result.config(text="Incorrect", fg="red")
            text = (f"{self.current_question['sentence']}"
                    f"\n\n{self.current_question['english']}"
                    f"\n\nYour answer: {user_answer}")
            self.feedback.config(text=text)

        self.entry.delete(0, tk.END)
        self.get_new_question()

    def update_score(self):
        self.scores.loc[self.scores["Nr"] == self.current_question["Nr"], "score"] = 1
        self.scores.to_csv(SCORE_PATH, index=False)
        self.load_data()

    def show_refresh_button(self):
        self.refresh_button = create_refresh_button(self, command=self.reset_scores, question_lines=3)

    def reset_scores(self):
        self.scores = pd.read_csv(SCORE_PATH)
        self.data = pd.read_csv(DATA_PATH)
        self.scores = self.scores.merge(self.data, on="Nr", how="left")
        self.scores.loc[self.scores["level"] == self.level, "score"] = 0
        self.scores[['Nr', 'score']].to_csv(SCORE_PATH, index=False)
        self.refresh_button.place_forget()
        self.submit_button = create_submit_button(self, command=self.check_answer, question_lines=3)
        self.load_data()
        self.get_new_question()

    def post_update(self):
        self.entry.focus()

    def update_data(self):
        pass