from flask import Blueprint, request, session, redirect, url_for
routes_bp = Blueprint("routes", __name__)

from webapp.i18n import get_lang_code, dict_key_for  # noqa: E402

@routes_bp.app_context_processor
def inject_language():
    code = get_lang_code(request, session)
    return {
        "lang_code": code,               # "en" or "fr"
        "language": dict_key_for(code),  # "english" or "french" (your dict key)
    }

@routes_bp.route("/lang/<code>")
def set_lang(code):
    if code in ("en", "fr"):
        session["lang"] = code
    return redirect(request.referrer or url_for("routes.home"))


# Import submodules so their route decorators run
from . import authorization, exercises, menu, background  # noqa: E402,F401

__all__ = ["routes_bp"]