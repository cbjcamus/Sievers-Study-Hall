from flask import session
from flask_login import current_user

from users.users.models import UserSettings

DEFAULT_SETTINGS = {
    "feedback_enabled": True,
    "theme": "night",
    "special_characters_enabled": True,
    "instruction_page_enabled": True,
}


def is_feedback_enabled():
    if current_user.is_authenticated:
        row = UserSettings.query.get(current_user.id)
        if row and row.settings:
            return row.settings.get("feedback_enabled", DEFAULT_SETTINGS["feedback_enabled"])
        return DEFAULT_SETTINGS["feedback_enabled"]

    anon_settings = session.get("settings", {})
    return anon_settings.get("feedback_enabled", DEFAULT_SETTINGS["feedback_enabled"])


def get_theme():
    if current_user.is_authenticated:
        row = UserSettings.query.get(current_user.id)
        if row and row.settings:
            return row.settings.get("theme", DEFAULT_SETTINGS["theme"])
        return DEFAULT_SETTINGS["theme"]

    anon_settings = session.get("settings", {})
    return anon_settings.get("theme", DEFAULT_SETTINGS["theme"])


def are_special_characters_enabled():
    if current_user.is_authenticated:
        row = UserSettings.query.get(current_user.id)
        if row and row.settings:
            return row.settings.get(
                "special_characters_enabled",
                DEFAULT_SETTINGS["special_characters_enabled"]
            )
        return DEFAULT_SETTINGS["special_characters_enabled"]

    anon_settings = session.get("settings", {})
    return anon_settings.get(
        "special_characters_enabled",
        DEFAULT_SETTINGS["special_characters_enabled"]
    )


def is_instruction_page_enabled():
    if current_user.is_authenticated:
        row = UserSettings.query.get(current_user.id)
        if row and row.settings:
            return row.settings.get(
                "instruction_page_enabled",
                DEFAULT_SETTINGS["instruction_page_enabled"]
            )
        return DEFAULT_SETTINGS["instruction_page_enabled"]

    anon_settings = session.get("settings", {})
    return anon_settings.get(
        "instruction_page_enabled",
        DEFAULT_SETTINGS["instruction_page_enabled"]
    )


def get_filename_empty_bookmark():
    if get_theme() == 'day':
        return "icons/bookmark/empty_day.png"
    else:
        return "icons/bookmark/empty.png"


def get_filename_full_bookmark():
    if get_theme() == 'day':
        return "icons/bookmark/full_day.png"
    else:
        return "icons/bookmark/full.png"


def get_filename_flag():
    if get_theme() == 'day':
        return "icons/flag/flag_black.png"
    else:
        return "icons/flag/flag_white.png"
