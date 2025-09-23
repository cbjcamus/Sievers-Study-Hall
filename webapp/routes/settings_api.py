from flask import jsonify, request
from flask_login import login_required, current_user
from . import routes_bp
from users.users.models import db
from users.users.models import UserSettings, DEFAULT_SETTINGS


@routes_bp.route("/api/settings", methods=["GET"])
@login_required
def get_settings():
    row = get_or_create_settings(current_user.id)
    return jsonify(row.settings)


@routes_bp.route("/api/settings", methods=["POST"])
@login_required
def update_settings():
    row = get_or_create_settings(current_user.id)
    payload = request.get_json(silent=True) or {}
    # only accept known keys; add more as you introduce them
    allowed = set(DEFAULT_SETTINGS.keys())
    for k, v in payload.items():
        if k in allowed:
            row.settings[k] = v
    db.session.commit()
    return jsonify(row.settings)


def get_or_create_settings(user_id):
    row = UserSettings.query.get(user_id)
    if not row:
        row = UserSettings(user_id=user_id, settings=dict(DEFAULT_SETTINGS))
        db.session.add(row); db.session.commit()
    else:
        # backfill any new defaults without overwriting existing values
        changed = False
        for k, v in DEFAULT_SETTINGS.items():
            if k not in row.settings:
                row.settings[k] = v; changed = True
        if changed: db.session.commit()
    return row


@routes_bp.app_context_processor
def inject_theme_flag():
    theme = "night"
    if current_user.is_authenticated:
        row = get_or_create_settings(current_user.id)  # <-- use the helper
        if row and row.settings:
            theme = row.settings.get("theme", "night")
    return {"is_day_mode": theme == "day"}