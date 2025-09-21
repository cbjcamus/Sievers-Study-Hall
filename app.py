import os
from datetime import timedelta
from flask import Flask
from flask_login import LoginManager

from webapp.routes import routes_bp
from users.users.models import db, User
from users.progress.models import UserExerciseState  # noqa: F401

app = Flask(__name__,
            static_url_path='/webapp/static',
            static_folder='webapp/static',
            template_folder='webapp/templates')
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'secret_key_for_development_environment')

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///prod.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# Minimal Flask-Login setup (needed for login_user/logout_user)
login_manager = LoginManager(app)
login_manager.login_view = "routes.signin"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

app.register_blueprint(routes_bp)

app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=30)

with app.app_context():
    db.create_all()
