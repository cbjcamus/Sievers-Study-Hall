import os
from datetime import timedelta

from flask import Flask
from flask_session import Session

from webapp.routes import routes

app = Flask(__name__,
            static_url_path='/webapp/static',
            static_folder='webapp/static',
            template_folder='webapp/templates')
app.secret_key = 'this_is_a_bad_secret_key_but_I_believe_it_works'

app.register_blueprint(routes)

# Set up server-side session storage
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = os.path.join(os.path.dirname(__file__), 'flask_session')
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=90)
Session(app)

app.config['SESSION_COOKIE_SECURE'] = True # Only if your app is on HTTPS (which it is on PythonAnywhere)
app.config['SESSION_COOKIE_HTTPONLY'] = True # Good practice for security
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax' # Recommended for most cases

app.config['SESSION_COOKIE_DOMAIN'] = '.sieversstudyhall.com' # <<< IMPORTANT: Replace with your actual domain
app.config['SESSION_COOKIE_PATH'] = '/'


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # Default to 8080 if PORT is not set
    app.run(host="0.0.0.0", port=port)

