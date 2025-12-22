import os
from datetime import timedelta
from flask import Flask
from flask_mail import Mail
from flask_login import LoginManager
from flask_migrate import Migrate

from webapp.routes import routes_bp
from users.users.models import db, User
from users.progress.models import UserExerciseState  # noqa: F401

app = Flask(__name__,
            static_url_path='/webapp/static',
            static_folder='webapp/static',
            template_folder='webapp/templates')
app.secret_key = 'this_is_a_secret_key_for_local_environment'

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dev.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD")

mail = Mail()
mail.init_app(app)

db.init_app(app)

migrate = Migrate(app, db)

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

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # Default to 8080 if PORT is not set
    app.run(host="0.0.0.0", port=port)

