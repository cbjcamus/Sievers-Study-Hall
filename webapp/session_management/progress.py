from webapp.session_management.total_questions import compute_total_questions, compute_highest_exercise
from webapp.session_management.session_ import progress, result


def compute_answered_questions(session, unit, exercise=None):
    if exercise is not None:
        return compute_answered_questions_exercise_session(session, unit, exercise)

    elif exercise is None:
        return compute_answered_questions_unit_session(session, unit)

    else:
        return 0


def compute_answered_questions_unit_session(session, unit):
    answered_questions = 0
    for exercise in range(1, compute_highest_exercise(unit) + 1):
        answered_questions_exercise = compute_answered_questions_exercise_session(session, unit, exercise)
        answered_questions = answered_questions + answered_questions_exercise
    return int(answered_questions)


def compute_answered_questions_exercise_session(session, unit, exercise):
    if result in session and unit in session[result] and str(exercise) in session[result][unit]:
        return compute_total_questions(unit, exercise=exercise)

    elif progress in session and unit in session[progress]:
        if str(exercise) in session[progress][unit]:
            return sum(session[progress][unit][str(exercise)].values())
        else:
            return 0

    else:
        return 0

