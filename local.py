import os
from datetime import timedelta

from flask import Flask

from webapp.routes import routes

app = Flask(__name__,
            static_url_path='/webapp/static',
            static_folder='webapp/static',
            template_folder='webapp/templates')
app.secret_key = 'this_is_a_secret_key_for_local_environment'

app.register_blueprint(routes)

app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=30)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # Default to 8080 if PORT is not set
    app.run(host="0.0.0.0", port=port)

