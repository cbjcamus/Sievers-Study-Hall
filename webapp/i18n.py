LANG_CODES = ("en", "fr")
DICT_KEYS = {"en": "english", "fr": "french"}

'''
def get_language(request=None, session=None):
    """
    Returns the current language key used in content dictionaries,
    e.g. 'english' or 'french'.
    Priority:
      1. session['lang'] if set
      2. request.accept_languages if available
      3. default to English
    """
    lang_code = "en"
    try:
        if session and session.get("lang") in LANG_CODES:
            lang_code = session["lang"]
        elif request and request.accept_languages:
            match = request.accept_languages.best_match(LANG_CODES)
            if match:
                lang_code = match
    except Exception:
        pass

    return DICT_KEYS.get(lang_code, "english")
'''

def get_language(request=None, session=None):
    lang_code = get_lang_code(request, session)
    return DICT_KEYS.get(lang_code, "english")


def get_lang_code(request=None, session=None):
    try:
        # 1. Explicit URL parameter
        if request:
            url_lang = request.args.get("lang")
            if url_lang in LANG_CODES:
                return url_lang

        # 2. Existing session
        if session and session.get("lang") in LANG_CODES:
            return session["lang"]

        # 3. Browser preference
        if request and request.accept_languages:
            match = request.accept_languages.best_match(LANG_CODES)
            if match:
                return match
    except Exception:
        pass

    return "en"


def dict_key_for(code: str) -> str:
    return DICT_KEYS.get(code, "english")