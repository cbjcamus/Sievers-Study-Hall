from flask import jsonify, request, session
from flask_login import login_required, current_user

from . import routes_bp
from users.users.models import db, are_special_characters_enabled
from users.users.models import UserSettings, DEFAULT_SETTINGS, get_theme


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
    theme = get_theme()
    return {"is_day_mode": theme == "day"}


@routes_bp.route('/api/settings', methods=['GET', 'POST'])
def api_settings():
    if request.method == 'GET':
        if current_user.is_authenticated:
            row = UserSettings.query.get(current_user.id)
            settings = row.settings if row and row.settings else {}
        else:
            settings = session.get("settings", {})

        return jsonify({
            key: settings.get(key, default_value)
            for key, default_value in DEFAULT_SETTINGS.items()
        })

    data = request.get_json(silent=True) or {}

    if current_user.is_authenticated:
        row = UserSettings.query.get(current_user.id)
        if not row:
            row = UserSettings(user_id=current_user.id, settings={})
            db.session.add(row)

        settings = row.settings or {}
    else:
        settings = session.get("settings", {})

    for key, value in data.items():
        if key not in DEFAULT_SETTINGS:
            continue

        if key == "theme":
            if value in {"day", "night"}:
                settings[key] = value
        else:
            settings[key] = value

    if current_user.is_authenticated:
        row.settings = settings
        db.session.commit()
    else:
        session["settings"] = settings
        session.modified = True

    return jsonify({
        "success": True,
        **{
            key: settings.get(key, default_value)
            for key, default_value in DEFAULT_SETTINGS.items()
        }
    })


@routes_bp.app_context_processor
def inject_settings_flags():
    return {
        "is_day_mode": get_theme() == "day",
        "special_characters_enabled": are_special_characters_enabled(),
    }