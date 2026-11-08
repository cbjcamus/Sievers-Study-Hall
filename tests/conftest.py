"""Shared test fixtures and utilities."""

import pytest
from flask import Flask, Blueprint
from flask_login import LoginManager

from users.rate_limiting.decorator import rate_limit_exercise_submission
from users.users.models import db, User


@pytest.fixture
def app():
    """Create Flask app for testing."""
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.secret_key = "test-secret"

    db.init_app(app)

    login_manager = LoginManager(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Create test blueprint with rate-limited endpoint
    bp = Blueprint('test', __name__)

    @bp.route('/test-endpoint', methods=['POST'])
    @rate_limit_exercise_submission
    def test_endpoint():
        return {"status": "ok"}

    app.register_blueprint(bp)

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


def make_test_user(email):
    """Create a test user."""
    user = User(email=email)
    user.set_password("password")
    db.session.add(user)
    db.session.commit()
    return user


@pytest.fixture
def redis_client():
    """Get a fake Redis client for testing."""
    import fakeredis
    return fakeredis.FakeRedis(decode_responses=False)




