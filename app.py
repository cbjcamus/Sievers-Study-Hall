import os
from flask import Flask
from webapp.routes import routes

app = Flask(__name__,
            static_url_path='/webapp/static',
            static_folder='webapp/static',
            template_folder='webapp/templates')
app.secret_key = 'this_is_a_bad_secret_key_but_I_believe_it_works'

# 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

app.register_blueprint(routes)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # Default to 8080 if PORT is not set
    app.run(host="0.0.0.0", port=port)


# TODO Priority
# Pronomen: relativsaetze wo wohin woher
# score when finishing a level (current should be progress)
# reset button next to progress


# TODO Exercises
# Wortschatz: adjektives
# Wortschatz: nominalisation verbs
# Wortschatz: nominalisation adjektives
# Wortschatz: trennbare und untrennbare verben
# Wortschatz: formal verben
# Wortschatz: colloquial verben
# Wortschatz: verben that simplify
# Wortschatz: number, ordinal, fractions, double/triple, percent
# Articles: genitive articles
# Possessive pronomen
# Possessive article
# einzige -> adjective instead of adverb


# TODO Format
# https://en.wikipedia.org/wiki/Eduard_Sievers for logo
# Another color for Correct and Incorrect
# How to have ss in the answer (adjektivedeklinationen)

# Framework
# Learn & Discover
# Practice & Reinforce / Consolidate
# Apply & Summarize