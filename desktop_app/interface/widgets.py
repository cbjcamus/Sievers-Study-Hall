import tkinter as tk

from utils.proverbs import get_text_proverb
from desktop_app.interface.style import (font,
                                         font_proverb,
                                         font_size_title,
                                         font_size_subtitle,
                                         font_size_section,
                                         font_size_textbox,
                                         font_size_proverb,
                                         bg_color,
                                         )


def create_title(window, text):
    title_label = tk.Label(window, text=text, font=(font, font_size_title), pady=0, bg=bg_color)
    title_label.place(relx=0.5, rely=0, anchor="n")
    return


def create_subtitle(window, text):
    subtitle_label = tk.Label(window, text=text, font=(font, font_size_subtitle), pady=0, bg=bg_color)
    subtitle_label.place(relx=0.5, y=font_size_subtitle + 20, anchor="n")
    return


def create_section(window, text, x, y):
    section_label = tk.Label(window, text=text, font=(font, font_size_section), bg=bg_color)
    section_label.place(x=x, y=y)
    return section_label


def create_button(window, text, x, y, command):
    button = tk.Button(window, text=text, command=command, bg=bg_color)
    button.place(x=x, y=y, anchor="w")
    return button


def create_text_box(window, text, y):
    text_box = tk.Label(window, text=text, font=(font, font_size_textbox), bg=bg_color)
    text_box.place(relx=0.5, y=y, anchor="center")
    return text_box


def create_text_box_scores(window, text, y, type):
    if type == 'level':
        x = 130
    elif type == 'exercise':
        x = 200
    else:
        x = 0
    text_box = tk.Label(window, textvariable=text, font=(font, font_size_textbox), bg=bg_color)
    text_box.place(x=x, y=y, anchor="w")
    return text_box


def create_text_info(window, text, y, type='level'):
    if type == 'level':
        x = 200
    elif type == 'exercise':
        x = 300
    else:
        x = 0
    text_box = tk.Label(window, text=text, font=(font, font_size_textbox), bg=bg_color)
    text_box.place(x=x, y=y, anchor="w")
    return text_box


def create_button_back(window, text, command):
    button = tk.Button(window, text=text, command=command, bg=bg_color)
    button.place(relx=0.5, rely=0.98, anchor="s")
    return


def create_frame(window):
    frame = tk.Frame(window, bg=bg_color)
    frame.place(x=20, y=20)
    return frame


def create_line_menu(window, y, command, page, text_button, text_score, text_info):
    button = create_button(window, text_button, 10, y, command)
    score_box = create_text_box_scores(window, text_score, y, page)
    info_box = create_text_info(window, text_info, y, type=page)
    return button, score_box, info_box


def create_question_text(window):
    question = create_text_box(window, "", 150)
    return question


def create_entry(window, question_lines=1):
    entry = tk.Entry(window)
    y = 200 + (question_lines - 1) * font_size_textbox
    entry.place(relx=0.5, y=y, anchor="n")
    return entry


def create_submit_button(window, command, question_lines=1):
    submit_button = tk.Button(window, text="Submit", command=command)
    y = 250 + (question_lines - 1) * font_size_textbox
    submit_button.place(relx=0.5 , y=y, anchor="n")
    return submit_button


def create_result_text(window, question_lines=1):
    result = tk.Label(window, text="", font=(font, font_size_textbox), bg=bg_color)
    y = 300 + (question_lines - 1) * font_size_textbox
    result.place(relx=0.5, y=y, anchor="n")
    return result


def create_feedback_text(window, question_lines=1):
    feedback = tk.Label(window, text="", font=(font, font_size_textbox), bg=bg_color)
    y = 300 + (question_lines - 1) * font_size_textbox + font_size_textbox * 2
    feedback.place(relx=0.5, y=y, anchor="n")
    return feedback


def create_proverb_text(window):
    text = get_text_proverb()
    proverb = tk.Label(window, text=text, font=(font_proverb, font_size_proverb), bg=bg_color)
    proverb.place(relx=0.5, rely=0.9, anchor="s")
    return proverb


def create_refresh_button(window, command, question_lines=1):
    refresh_button = tk.Button(window, text="Refresh", command=command)
    y = 250 + (question_lines - 1) * font_size_textbox
    refresh_button.place(relx=0.5, y=y, anchor="n")
    return refresh_button