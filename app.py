import os
from datetime import timedelta

from flask import Flask

from webapp.routes import routes

app = Flask(__name__,
            static_url_path='/webapp/static',
            static_folder='webapp/static',
            template_folder='webapp/templates')
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'secret_key_for_development_environment')

app.register_blueprint(routes)

app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=30)
