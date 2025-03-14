import os
from flask import Flask
from webapp.routes import routes

app = Flask(__name__,
            static_url_path='/webapp/static',
            static_folder='webapp/static',
            template_folder='webapp/templates')
app.secret_key = 'this_is_a_bad_secret_key_but_I_believe_it_works'

app.register_blueprint(routes)



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # Default to 8080 if PORT is not set
    app.run(host="0.0.0.0", port=port)

'''
cd /home/cbjcamus/Deutschtrainer
git pull origin main
touch /var/www/cbjcamus_pythonanywhere_com_wsgi.py

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
'''


# TODO Priority
# Pronomen: relativsaetze wo wohin woher
# add verfügen über
# all sentences in english with a specific format
# take care of feedback


# TODO Exercises
# Praeposition konjugation update list verbs
# Wortschatz: adjektives (include sentences to simplify with Partizip II and I)
# Wortschatz: adjektives to substantives
# Wortschatz: number, ordinal, fractions, double/triple, percent
# Articles: genitive articles
# Possessive pronomen
# Possessive article
# präpositionen grammatik: bei vs mit vs neben, auf vs an, aus vs von
# relative pronouns wer wen wem was
# als, als ob, als wenn in subjunktiv II

# TODO Format
# https://en.wikipedia.org/wiki/Eduard_Sievers for logo
# How to have ss in the answer (adjektivedeklinationen)
# 90 and above green, 70 to 90 orange, below 70 red
# 3 cases for question, answer and proverb

# Framework
# Learn, Discover and Play
# Review, Practice and Reinforce
# Consolidate, Summarize and Apply

# Sources
# 500 verbs german tv: https://www.reddit.com/r/German/comments/6gbcnv/500_verbs_sorted_by_frequency_from_tv/
# routledge: Tubbiefox https://docs.google.com/spreadsheets/d/1r9HwvVpo35MFxnJ_5W6RKlDfx5VzmQVcnpJTgrNUY9I/edit?gid=1814339112#gid=1814339112
# https://docs.google.com/spreadsheets/d/1H8hMTSSVMMss-1aSGgndFaHlYa7kuJ161CtwADwQc9M/edit?gid=0#gid=0