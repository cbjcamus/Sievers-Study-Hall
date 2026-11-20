from flask import Blueprint, redirect, request, session, url_for

routes_bp = Blueprint("routes", __name__)

from webapp.i18n import dict_key_for, get_lang_code


@routes_bp.app_context_processor
def inject_language():
    code = get_lang_code(request, session)
    return {
        "lang_code": code,
        "language": dict_key_for(code),
    }


from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse


@routes_bp.route("/lang/<code>")
def set_lang(code):
    if code not in ("en", "fr"):
        return redirect(url_for("routes.home"))

    # Keep the user's language preference in the session
    session["lang"] = code

    # Return to the page the user came from
    target = request.referrer or url_for("routes.home", _external=True)

    # Add/replace ?lang=xx while preserving other query parameters
    parsed = urlparse(target)
    query = dict(parse_qsl(parsed.query))
    query["lang"] = code

    target = urlunparse(parsed._replace(query=urlencode(query)))

    return redirect(target)


# Import submodules so their route decorators run
from . import authorization, background, exercises, menu  # noqa: F401

__all__ = ["routes_bp"]
