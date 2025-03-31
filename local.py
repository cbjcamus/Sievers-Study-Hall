import os
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
app.config['SESSION_PERMANENT'] = False  # Optional: Sessions expire on browser close
Session(app)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # Default to 8080 if PORT is not set
    app.run(host="0.0.0.0", port=port)

'''
cd /home/cbjcamus/Deutschtrainer
git pull origin main
touch /var/www/cbjcamus_pythonanywhere_com_wsgi.py

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
'''


# TODO Priority before April 1st
# Separate Adverbien in 2


# TODO Exercises
# Wortschatz: adjektives
# Wortschatz: adjektives to substantives
# Wortschatz: adjektives to verben
# Wortschatz: adjektives: write the opposite
# Wortschatz: verben to adjective in bar and lich
# Wortschatz: adjektives Partizip II and I
# Wortschatz: number, ordinal, fractions, double/triple, percent, mathematical terms like plus minus average

# relative pronouns wer wen wem was -> done, needs proofreading


# TODO To add
# Words in trag (Antrag, Vertrag, Betrag, Beitrag)


# TODO Format
# 90 and above green, 80 to 90 Yellow, 70 to 80 Orange, below red
# name of the website

# Framework
# Learn, Discover and Play
# Review, Practice and Reinforce
# Consolidate, Summarize and Apply

# Sources
# 500 verbs german tv: https://www.reddit.com/r/German/comments/6gbcnv/500_verbs_sorted_by_frequency_from_tv/
# routledge: Tubbiefox https://docs.google.com/spreadsheets/d/1r9HwvVpo35MFxnJ_5W6RKlDfx5VzmQVcnpJTgrNUY9I/edit?gid=1814339112#gid=1814339112
# https://docs.google.com/spreadsheets/d/1H8hMTSSVMMss-1aSGgndFaHlYa7kuJ161CtwADwQc9M/edit?gid=0#gid=0