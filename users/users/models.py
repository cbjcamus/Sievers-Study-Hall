from datetime import datetime

from flask import session
from flask_login import UserMixin, current_user
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
db = SQLAlchemy()

from sqlalchemy.ext.mutable import MutableDict
from sqlalchemy.dialects.sqlite import JSON as SQLITE_JSON  # or PostgreSQL JSONB


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def set_password(self, pw): self.password_hash = generate_password_hash(pw)
    def check_password(self, pw): return check_password_hash(self.password_hash, pw)


class UserSettings(db.Model):
    __tablename__ = "user_settings"
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    settings = db.Column(MutableDict.as_mutable(SQLITE_JSON), nullable=False, default=dict)


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


class UserExerciseState(db.Model):
    __tablename__ = "user_exercise_state"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False, index=True)
    unit = db.Column(db.String(64), nullable=False)          # e.g., "verben", "adverbien"
    exercise = db.Column(db.Integer, nullable=False)         # display number (1..N), can be shifted later
    # Mirrors your session but keyed by stable content hashes (qids); structure example:
    # { "correct_ids": ["qid1","qid2"], "incorrect": {"qid7": "mein falsches wort"} }
    state = db.Column(db.JSON, nullable=False, default=dict)

    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    completed_at = db.Column(db.DateTime, nullable=True)

    __table_args__ = (
        db.UniqueConstraint("user_id", "unit", "exercise", name="uq_user_unit_exercise"),
        db.Index("idx_unit_exercise", "unit", "exercise"),
    )


class Bookmark(db.Model):
    __tablename__ = "bookmarks"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        nullable=False,
    )

    # "konnektoren" etc.
    unit = db.Column(db.String(64), nullable=False)

    # internal exercise number (int)
    exercise = db.Column(db.Integer, nullable=False)

    # CEFR level, e.g. "A1", "B2"
    level = db.Column(db.String(8), nullable=False)

    # "correct" / "incorrect" (you’ll enforce values in the app logic)
    result = db.Column(db.String(10), nullable=False)

    # what the user typed (can be empty / None)
    user_answer = db.Column(db.Text, nullable=True)

    # full rendered feedback snapshot
    feedback_message = db.Column(db.Text, nullable=False)

    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow,
    )

    # relationship back to the user
    user = db.relationship(
        "User",
        backref=db.backref("bookmarks", lazy="dynamic")
    )

    def __repr__(self):
        return f"<Bookmark id={self.id} user_id={self.user_id} unit={self.unit} exercise={self.exercise}>"
