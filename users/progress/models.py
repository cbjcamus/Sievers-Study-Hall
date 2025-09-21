from datetime import datetime
from users.users.models import db


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