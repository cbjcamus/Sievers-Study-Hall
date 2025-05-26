from webapp.session_management.total_questions import compute_total_questions, compute_highest_level
from webapp.session_management.session_ import progress, result


def compute_answered_questions(session, exercise, level=None):
    if level is not None:
        return compute_answered_questions_level_session(session, exercise, level)

    elif level is None:
        return compute_answered_questions_exercise_session(session, exercise)

    else:
        return 0


def compute_answered_questions_exercise_session(session, exercise):
    answered_questions = 0
    for level in range(1, compute_highest_level(exercise) + 1):
        answered_questions_level = compute_answered_questions_level_session(session, exercise, level)
        answered_questions = answered_questions + answered_questions_level
    return int(answered_questions)


def compute_answered_questions_level_session(session, exercise, level):
    if result in session and exercise in session[result] and str(level) in session[result][exercise]:
        return compute_total_questions(exercise, level=level)

    elif progress in session and exercise in session[progress]:
        if str(level) in session[progress][exercise]:
            return sum(session[progress][exercise][str(level)].values())
        else:
            return 0

    else:
        return 0

