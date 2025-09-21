from flask import Blueprint
routes_bp = Blueprint("routes", __name__)

# Import submodules so their route decorators run
from . import authorization, exercises, menu, background  # noqa: E402,F401

__all__ = ["routes_bp"]