"""
Unit tests for the exercise-state cache (users/progress/exercise_state_cache.py)
and its usage in users/progress/progress.py and users/progress/score.py.

Covers:
- get_user_exercise_states() issuing a single query per request.
- The per-request cache being scoped per user.
- is_exercise_started / is_exercise_completed_db / get_lowest_scored_exercises
  returning the expected results.
"""

import pytest
from flask import Flask, g
from flask_login import LoginManager, login_user

from users.users.models import db, User, UserExerciseState
from users.progress.exercise_state_cache import get_user_exercise_states
from users.progress.progress import is_exercise_started, is_exercise_completed_db
from users.progress.score import get_lowest_scored_exercises

UNIT = "genus"


@pytest.fixture
def app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.secret_key = "test-secret"

    db.init_app(app)

    login_manager = LoginManager(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


def make_user(email):
    user = User(email=email)
    user.set_password("password")
    db.session.add(user)
    db.session.commit()
    return user


def make_state(user, unit, exercise, state):
    row = UserExerciseState(user_id=user.id, unit=unit, exercise=exercise, state=state)
    db.session.add(row)
    db.session.commit()
    return row


def count_queries(app):
    """Counts SQL statements executed against user_exercise_state while in scope."""
    counter = {"n": 0}

    def before_cursor_execute(conn, cursor, statement, parameters, context, executemany):
        if "user_exercise_state" in statement and statement.strip().upper().startswith("SELECT"):
            counter["n"] += 1

    from sqlalchemy import event

    with app.app_context():
        engine = db.engine
        event.listen(engine, "before_cursor_execute", before_cursor_execute)
        try:
            yield counter
        finally:
            event.remove(engine, "before_cursor_execute", before_cursor_execute)


@pytest.fixture
def query_counter(app):
    gen = count_queries(app)
    counter = next(gen)
    yield counter
    next(gen, None)


def test_get_user_exercise_states_issues_single_query_for_many_lookups(app, query_counter):
    user = make_user("one@example.com")
    for exercise in range(1, 6):
        make_state(user, UNIT, exercise, {"score": 0.5})

    with app.test_request_context():
        for exercise in range(1, 6):
            states = get_user_exercise_states(user.id)
            assert (UNIT, exercise) in states

    # Regardless of how many exercises were looked up, only one query should
    # have been issued (cached on flask.g for the request).
    assert query_counter["n"] == 1


def test_cache_is_scoped_per_user_within_same_request(app, query_counter):
    user_a = make_user("a@example.com")
    user_b = make_user("b@example.com")
    make_state(user_a, UNIT, 1, {"score": 0.9})
    make_state(user_b, UNIT, 1, {"score": 0.1})

    with app.test_request_context():
        states_a = get_user_exercise_states(user_a.id)
        states_b = get_user_exercise_states(user_b.id)

        assert states_a[(UNIT, 1)].state["score"] == 0.9
        assert states_b[(UNIT, 1)].state["score"] == 0.1

    # Switching users mid-request must trigger a fresh query each time.
    assert query_counter["n"] == 2


def test_is_exercise_started_matches_row_state(app):
    user = make_user("started@example.com")
    make_state(user, UNIT, 1, {"correct_nrs": ["1"]})
    make_state(user, UNIT, 2, {})

    with app.test_request_context():
        login_user(user)

        assert is_exercise_started(session={}, unit=UNIT, exercise=1) is True
        assert is_exercise_started(session={}, unit=UNIT, exercise=2) is False
        # Exercise 3 has no row at all.
        assert is_exercise_started(session={}, unit=UNIT, exercise=3) is False


def test_is_exercise_completed_db_matches_row_state(app):
    user = make_user("completed@example.com")
    make_state(user, UNIT, 1, {"score": 1.0})
    make_state(user, UNIT, 2, {"correct_nrs": ["1"]})

    with app.test_request_context():
        assert is_exercise_completed_db(user.id, UNIT, 1) is True
        assert is_exercise_completed_db(user.id, UNIT, 2) is False
        # No row exists for exercise 3.
        assert is_exercise_completed_db(user.id, UNIT, 3) is False


def test_get_lowest_scored_exercises_sorted_and_limited(app):
    user = make_user("scores@example.com")
    make_state(user, UNIT, 1, {"score": 0.9})
    make_state(user, UNIT, 2, {"score": 0.2})
    make_state(user, UNIT, 3, {"score": 0.5})
    make_state(user, UNIT, 4, {})  # no score -> excluded

    with app.test_request_context():
        login_user(user)

        result = get_lowest_scored_exercises(limit=2)

    assert result == [(UNIT, 2, 0.2), (UNIT, 3, 0.5)]


def test_get_lowest_scored_exercises_empty_for_anonymous_user(app):
    with app.test_request_context():
        assert get_lowest_scored_exercises() == []
