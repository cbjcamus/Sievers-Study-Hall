from flask import current_app
from flask_mail import Message

def send_flag_email(unit, exercise, feedback_message, user_answer, result, reason, email=None):

    msg = Message(
        subject=f"Question flagged: {unit} / Exercise {exercise}",
        sender=current_app.config["MAIL_USERNAME"],
        recipients=[current_app.config["MAIL_USERNAME"]]
    )

    msg.body = f"""
A question has been flagged for review.

Unit: {unit}
Exercise: {exercise}
User email: {email or 'Anonymous'}

Feedback message: {feedback_message}
User answer: {user_answer}
Result: {result}
Reason: {reason}
"""

    from local import mail
    mail.send(msg)