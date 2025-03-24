alinea = "&emsp;"


def format_english(text):
    return text


def format_german(text):
    return text


def italicise(text):
    return f"<i>{text}</i>"


def change_color(text, color="#AEEEEE"):
    return f'<span style="color: {color};">{text}</span>'


def change_font(text, font="Courier New"):
    return f'<span style="font-family: {font};">{text}</span>'