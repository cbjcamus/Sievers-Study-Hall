import tkinter as tk

from interface.constants import (font,
                                 font_size_title,
                                 font_size_subtitle,
                                 font_size_section,
                                 font_size_textbox,
                                 bg_color)


def create_title(window, text):
    title_label = tk.Label(window, text=text, font=(font, font_size_title), pady=0, bg=bg_color)
    title_label.place(relx=0.5, rely=0, anchor="n")
    return


def create_subtitle(window, text):
    subtitle_label = tk.Label(window, text=text, font=(font, font_size_subtitle), pady=0, bg=bg_color)
    subtitle_label.place(relx=0.5, y=font_size_subtitle + 10, anchor="n")
    return


def create_section(frame, text, x, y):
    section_label = tk.Label(frame, text=text, font=(font, font_size_section), bg=bg_color)
    section_label.place(x=x, y=y)
    return


def create_button(frame, text, x, y, command):
    button = tk.Button(frame, text=text, command=command, bg=bg_color)
    button.place(x=x, y=y, anchor="w")
    return


def create_text_box(window, text, y):
    text_box = tk.Label(window, text=text, font=(font, font_size_textbox), bg=bg_color)
    text_box.place(relx=0.5, y=y, anchor="center")
    return text_box


def create_text_box_scores(window, text, y, type):
    if type == 'level':
        x = 100
    elif type == 'exercise':
        x = 200
    else:
        x = 0
    text_box = tk.Label(window, textvariable=text, font=(font, font_size_textbox), bg=bg_color)
    text_box.place(x=x, y=y, anchor="w")


def create_button_back(frame, text, command):
    button = tk.Button(frame, text=text, command=command, bg=bg_color)
    button.place(relx=0.5, rely=0.98, anchor="s")
    return


def create_frame(window):
    frame = tk.Frame(window, bg=bg_color)
    frame.place(x=20, y=20)
    return frame


'''
def create_text_box_scores_levels(window, text, y):
    text_box = tk.Label(window, textvariable=text, font=(font, font_size_textbox), bg=bg_color)
    text_box.place(x=100, y=y, anchor="w")
    return text_box


def create_text_box_scores_exercises(window, text, y):
    text_box = tk.Label(window, textvariable=text, font=(font, font_size_textbox), bg=bg_color)
    text_box.place(x=200, y=y, anchor="w")
    return text_box
    
'''