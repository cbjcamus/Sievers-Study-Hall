from desktop_app.interface.style import height_between_lines, height_between_sections

def find_next_y(last_y, line=True, section=False):
    y_next = last_y + height_between_lines * line + height_between_sections * section
    return y_next

def find_former_y(widget, type):
    if type == 'line':
        button, score_box, info_box = widget
        former_y = button.winfo_y() + button.winfo_reqheight() / 2
    elif type == 'section':
        former_y = widget.winfo_y() + widget.winfo_reqheight() / 2
    else:
        former_y = widget.winfo_y() + widget.winfo_reqheight() / 2
    return former_y
