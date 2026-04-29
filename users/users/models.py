from datetime import datetime, timezone

from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

from sqlalchemy.ext.mutable import MutableDict
from sqlalchemy.dialects.sqlite import JSON as SQLITE_JSON


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False, index=True)

    def __init__(self, email, **kwargs):
        super().__init__(**kwargs)
        self.email = email

    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def set_password(self, pw): self.password_hash = generate_password_hash(pw)
    def check_password(self, pw): return check_password_hash(self.password_hash, pw)


class UserSettings(db.Model):
    __tablename__ = "user_settings"
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    settings = db.Column(MutableDict.as_mutable(SQLITE_JSON), nullable=False, default=dict)


class UserExerciseState(db.Model):
    __tablename__ = "user_exercise_state"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False, index=True)
    unit = db.Column(db.String(64), nullable=False)
    exercise = db.Column(db.Integer, nullable=False)
    # Mirrors your session but keyed by stable content hashes (qids); structure example:
    # { "correct_ids": ["qid1","qid2"], "incorrect": {"qid7": "mein falsches wort"} }
    state = db.Column(db.JSON, nullable=False, default=dict)

    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc), nullable=False)
    completed_at = db.Column(db.DateTime, nullable=True)

    __table_args__ = (
        db.UniqueConstraint("user_id", "unit", "exercise", name="uq_user_unit_exercise"),
        db.Index("idx_unit_exercise", "unit", "exercise"),
    )


class Bookmark(db.Model):
    __tablename__ = "bookmarks"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False,)

    unit = db.Column(db.String(64), nullable=False)
    exercise = db.Column(db.Integer, nullable=False)
    level = db.Column(db.String(8), nullable=False)

    result = db.Column(db.String(10), nullable=False)
    user_answer = db.Column(db.Text, nullable=True)
    feedback_message = db.Column(db.Text, nullable=False)

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone.utc),)

    # relationship back to the user
    user = db.relationship("User",backref=db.backref("bookmarks", lazy="dynamic"))

    def __repr__(self):
        return f"<Bookmark id={self.id} user_id={self.user_id} unit={self.unit} exercise={self.exercise}>"


class UserUnitHomeProgress(db.Model):
    __tablename__ = "user_unit_home_progress"

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    unit = db.Column(db.String(100), primary_key=True)
    completed_exercises = db.Column(db.Integer, default=0)
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))