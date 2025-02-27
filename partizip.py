import pandas as pd
import random
import tkinter as tk

# Load CSV files
data = pd.read_csv('partizip.csv')
scores = pd.read_csv('scores.csv')

# Merge data and scores on the German verb to ensure we have both Partizip II and scores
data = pd.merge(data, scores, on='german')


# Filter out verbs with a score of 3 (already known)
def get_trainable_verbs():
    return data[data['score'] < 3].to_dict(orient='records')


trainable_verbs = get_trainable_verbs()


# Function to save updated scores to the CSV
def save_scores():
    data[['german', 'score']].to_csv('scores.csv', index=False)


# Function to check user input
def check_answer():
    global current_verb
    answer = entry.get().strip()

    if answer == current_verb['partizip_II']:
        result_label.config(text="Correct!", fg="green")
        correct_answer_label.config(text="")
        your_answer_label.config(text="")
        # Increase score by 1, up to a maximum of 3
        data.loc[data['german'] == current_verb['german'], 'score'] += 1
        data.loc[data['german'] == current_verb['german'], 'score'] = data['score'].clip(upper=3)
    else:
        result_label.config(text="Incorrect!", fg="red")
        correct_answer_label.config(text=f"Correct answer: {current_verb['partizip_II']}")
        your_answer_label.config(text=f"Your answer: {answer}")
        # Reset score to 0 if wrong
        data.loc[data['german'] == current_verb['german'], 'score'] = 0

    # Save the updated scores
    save_scores()

    # Update the list of trainable verbs
    update_trainable_verbs()
    next_verb()


# Function to update the list of trainable verbs (those with scores < 3)
def update_trainable_verbs():
    global trainable_verbs
    trainable_verbs = get_trainable_verbs()


# Function to show the next verb
def next_verb():
    global current_verb
    if len(trainable_verbs) > 0:
        current_verb = random.choice(trainable_verbs)
        verb_label.config(text=f"What is the Partizip II of '{current_verb['german']}'?")
        entry.delete(0, tk.END)
        entry.focus_set()  # Refocus the text box after each question
    else:
        verb_label.config(text="Congratulations! You have completed all the verbs.")
        entry.config(state=tk.DISABLED)  # Disable entry if no more verbs to train


# UI elements
window = tk.Tk()
window.title("German Partizip II Trainer")

verb_label = tk.Label(window, text="")
verb_label.pack(pady=10)

entry = tk.Entry(window)
entry.pack(pady=10)

submit_button = tk.Button(window, text="Submit", command=check_answer)
submit_button.pack(pady=10)

result_label = tk.Label(window, text="", font=('Arial', 14))
result_label.pack(pady=10)

correct_answer_label = tk.Label(window, text="", font=('Arial', 12))
correct_answer_label.pack(pady=5)

your_answer_label = tk.Label(window, text="", font=('Arial', 12))
your_answer_label.pack(pady=5)

window.bind('<Return>', lambda event: check_answer())

entry.focus_set()

update_trainable_verbs()
next_verb()

window.mainloop()
