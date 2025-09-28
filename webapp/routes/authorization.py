from datetime import datetime

from flask import render_template, request, redirect, url_for, flash, session
from flask_login import login_user, current_user, logout_user, login_required
from pandas.io.formats.format import return_docstring

from data.data_processing.units import units
from data.data_processing.data_loading import load_data_exercise
from users.session_management.verification_session import is_exercise_in_unit

from users.users.models import db, User
from users.progress.models import UserExerciseState
from users.progress.service import make_qid
from users.questions.total_questions import compute_total_questions, compute_highest_exercise
from users.session_management.logging import log_new_signup

from webapp.routes.settings_api import get_or_create_settings

from . import routes_bp

from itsdangerous import URLSafeTimedSerializer, BadSignature, SignatureExpired
from flask import current_app

RESET_SALT = "password-reset"  # just a constant string

def _make_serializer():
    # uses your Flask SECRET_KEY
    return URLSafeTimedSerializer(current_app.config["SECRET_KEY"])

def generate_reset_token(user):
    s = _make_serializer()
    # encode user id (or email); id is fine
    return s.dumps({"uid": user.id}, salt=RESET_SALT)

def verify_reset_token(token, max_age_seconds=3600):
    s = _make_serializer()
    try:
        data = s.loads(token, salt=RESET_SALT, max_age=max_age_seconds)
    except SignatureExpired:
        return None  # token valid but expired
    except BadSignature:
        return None
    uid = data.get("uid")
    return User.query.get(uid)

import smtplib, ssl
from email.message import EmailMessage

def send_password_reset_email(to_email, reset_url):
    msg = EmailMessage()
    msg["Subject"] = "Reset your Sievers Study Hall password"
    msg["From"] = "no-reply@sieversstudyhall.com"
    msg["To"] = to_email
    msg.set_content(f"Click the link to reset your password:\n{reset_url}\nThis link expires in 1 hour.")

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.yourprovider.tld", 465, context=context) as smtp:
        smtp.login("SMTP_USERNAME", "SMTP_PASSWORD")
        smtp.send_message(msg)

# --- Forgot password: request form ---
@routes_bp.route("/forgot-password", methods=["GET", "POST"])
def forgot_password():
    if current_user.is_authenticated:
        return redirect(url_for("routes.settings"))

    if request.method == "POST":
        email = (request.form.get("email") or "").strip().lower()
        user = User.query.filter_by(email=email).first()
        if user:
            token = generate_reset_token(user)
            reset_url = url_for("routes.reset_password", token=token, _external=True)
            send_password_reset_email(email, reset_url)
            current_app.logger.info(f"[reset-link] {reset_url}")
            flash("If that email exists, a reset link has been sent.", "info")
            # You can also display the link in dev:
            if current_app.debug:
                flash(f"Dev reset link: {reset_url}", "info")
        else:
            # Do not reveal whether email exists
            flash("If that email exists, a reset link has been sent.", "info")
        return redirect(url_for("routes.signin"))

    return render_template("authorization/forgot_password.html")

# --- Reset password: uses token ---
@routes_bp.route("/reset-password/<token>", methods=["GET", "POST"])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for("routes.settings"))

    user = verify_reset_token(token)
    if not user:
        flash("This reset link is invalid or has expired.", "error")
        return redirect(url_for("routes.forgot_password"))

    if request.method == "POST":
        pw1 = request.form.get("password") or ""
        pw2 = request.form.get("password2") or ""
        if not pw1 or not pw2:
            flash("Please enter and confirm your new password.", "error")
            return redirect(url_for("routes.reset_password", token=token))
        if pw1 != pw2:
            flash("Passwords do not match.", "error")
            return redirect(url_for("routes.reset_password", token=token))
        if len(pw1) < 8:
            flash("Password must be at least 8 characters.", "error")
            return redirect(url_for("routes.reset_password", token=token))

        user.set_password(pw1)
        db.session.commit()
        flash("Your password has been updated. Please sign in.", "success")
        return redirect(url_for("routes.signin"))

    return render_template("authorization/reset_password.html", token=token)


@routes_bp.route("/signin", methods=["GET", "POST"])
def signin():
    # Already logged in? Go to settings.
    if current_user.is_authenticated:
        return redirect(url_for("routes.settings"))

    if request.method == "POST":
        email = (request.form.get("email") or "").strip().lower()
        password = request.form.get("password") or ""
        remember = bool(request.form.get("remember"))

        user = User.query.filter_by(email=email).first()
        if not user or not user.check_password(password):
            flash("Invalid email or password.", "error")
            return redirect(url_for("routes.signin"))

        login_user(user, remember=remember)
        next_url = request.args.get("next") or url_for("routes.home")

        try:
            get_or_create_settings(current_user.id)
        except Exception:
            pass

        return redirect(next_url)

    # GET
    return render_template("authorization/signin.html")


@routes_bp.route("/signup", methods=["GET", "POST"])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for("routes.settings"))

    if request.method == "POST":
        email = (request.form.get("email") or "").strip().lower()
        pw1 = request.form.get("password") or ""
        pw2 = request.form.get("password2") or ""

        if not email or not pw1 or not pw2:
            flash("Email and both passwords are required.", "error")
            return redirect(url_for("routes.signup"))
        if pw1 != pw2:
            flash("Passwords do not match.", "error")
            return redirect(url_for("routes.signup"))
        if User.query.filter_by(email=email).first():
            flash("Email already registered.", "error")
            return redirect(url_for("routes.signup"))

        # create user
        user = User(email=email)
        user.set_password(pw1)
        db.session.add(user)
        db.session.commit()

        login_user(user)

        log_new_signup(user)
        merge_anonymous_progress_in_database()
        clean_session_after_signing_up()

        try:
            get_or_create_settings(current_user.id)
        except Exception:
            pass

        return redirect(url_for("routes.home"))

    # GET
    return render_template("authorization/signup.html")


@routes_bp.route("/signout", methods=["POST"])
@login_required
def signout():
    logout_user()
    flash("Signed out.", "info")
    return redirect(url_for("routes.signin"))


def merge_anonymous_progress_in_database():
    if not current_user.is_authenticated:
        return

    for unit in units:
        unit_data = session.get(unit)
        if not isinstance(unit_data, dict):
            continue

        for exercise_str, ex_data in list(unit_data.items()):
            if not isinstance(ex_data, dict):
                continue
            try:
                ex = int(exercise_str)
            except (TypeError, ValueError):
                continue

            # ---- Load current exercise data (MUST exist) ----
            try:
                df = load_data_exercise(unit, ex)  # <-- pass INT, not str
            except Exception as e:
                print(f"[merge] skip {unit}/{ex}: load_data_exercise failed: {e}")
                continue
            if df is None or len(df) == 0:
                print(f"[merge] skip {unit}/{ex}: empty dataset")
                continue
            for col in ("Nr", "question", "answer"):
                if col not in df.columns:
                    print(f"[merge] skip {unit}/{ex}: missing column {col}")
                    df = None
                    break
            if df is None:
                continue

            total_questions = int(compute_total_questions(unit, ex))

            # ---- Build Nr -> qid mapping ----
            nr_to_qid = {}
            for _, row in df.iterrows():
                try:
                    nr = int(row["Nr"])
                except Exception:
                    continue
                qid = make_qid(
                    unit, ex,
                    str(row.get("question", "")),
                    str(row.get("answer", "")),
                    str(row.get("type", "")),
                )
                nr_to_qid[nr] = qid

            # inside your loop per (unit, ex):
            progress_nrs = [int(n) for n in (ex_data.get("progress") or []) if str(n).isdigit()]
            falses_nrs   = [int(n) for n in (ex_data.get("falses")   or []) if str(n).isdigit()]
            wrong_texts  = list(ex_data.get("incorrect_answer", [])) or []

            has_detail  = bool(progress_nrs or falses_nrs)
            has_summary = "result" in ex_data
            if not has_detail and not has_summary:
                continue

            row = UserExerciseState.query.filter_by(user_id=current_user.id, unit=unit, exercise=ex).first()
            if not row:
                row = UserExerciseState(user_id=current_user.id, unit=unit, exercise=ex, state={})
                db.session.add(row)

            if has_summary:
                score = float(ex_data["result"])
                total_questions = compute_total_questions(unit, ex)
                row.state = {"score": score, "total_questions": int(total_questions)}
            else:
                correct = sorted(set(progress_nrs) - set(falses_nrs))
                inc_map = {}
                for i, nr in enumerate(falses_nrs):
                    if nr in correct or nr in inc_map: continue
                    inc_map[nr] = wrong_texts[i] if i < len(wrong_texts) else ""
                # merge with any existing counts/nrs
                s_old = row.state or {}
                old_correct = set(int(n) for n in s_old.get("correct_nrs", []))
                old_incorrect = {int(k): v for k, v in (s_old.get("incorrect") or {}).items()}
                # promote if needed
                for n in correct: old_incorrect.pop(n, None)
                row.state = {
                    "correct_nrs": sorted(old_correct | set(correct)),
                    "incorrect": {str(k): v for k, v in {**old_incorrect, **inc_map}.items()},
                }

            row.updated_at = datetime.utcnow()
            db.session.commit()
            # then trim session keys
            for key in ("progress", "falses", "incorrect_answer"):
                ex_data.pop(key, None)


def clean_session_after_signing_up():
    for unit in units:
        if unit in session:
            del session[unit]

    if 'unfinished_exercise' in session:
        del session['unfinished_exercise']

    return