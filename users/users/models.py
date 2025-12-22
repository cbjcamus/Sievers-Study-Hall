from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, current_user
from werkzeug.security import generate_password_hash, check_password_hash
db = SQLAlchemy()


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def set_password(self, pw): self.password_hash = generate_password_hash(pw)
    def check_password(self, pw): return check_password_hash(self.password_hash, pw)


from sqlalchemy.ext.mutable import MutableDict
from sqlalchemy.dialects.sqlite import JSON as SQLITE_JSON  # or PostgreSQL JSONB


class UserSettings(db.Model):
    __tablename__ = "user_settings"
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    settings = db.Column(MutableDict.as_mutable(SQLITE_JSON), nullable=False, default=dict)

DEFAULT_SETTINGS = {"feedback_enabled": False, "theme": "night"}  # extend anytime


def is_feedback_enabled():
    if not current_user.is_authenticated:
        # anonymous users: fall back to False or your default
        return DEFAULT_SETTINGS["feedback_enabled"]

    row = UserSettings.query.get(current_user.id)
    if row and row.settings:
        return row.settings.get("feedback_enabled", DEFAULT_SETTINGS["feedback_enabled"])
    return DEFAULT_SETTINGS["feedback_enabled"]


def get_theme():
    if not current_user.is_authenticated:
        # anonymous users: fall back to False or your default
        return DEFAULT_SETTINGS["theme"]

    row = UserSettings.query.get(current_user.id)
    if row and row.settings:
        return row.settings.get("theme", "night")
    return DEFAULT_SETTINGS["theme"]


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