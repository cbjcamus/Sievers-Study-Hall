from webapp.session_management.score import compute_score
from webapp.session_management.logging import log_exercise_completed
from webapp.session_management.verification_session import is_key_in_exercise, init_session_key


def register_progress(session, unit, exercise, nr):
    """
    Registers progress for a specific question number in a given unit and exercise.

    If the (unit, exercise) pair is not already listed in 'unfinished_exercise',
    it is added to that list.

    Ensures the 'progress' key exists in the session for the exercise, then appends
    the question number to the tracked progress list.

    Args:
        session (dict): The session dictionary tracking user progress.
        unit (str): The unit identifier.
        exercise (str or int): The exercise identifier.
        nr (int or str): The question number to register as answered.

    Returns:
        None
    """
    if (unit, exercise) not in session['unfinished_exercise']:
        session['unfinished_exercise'].append((unit, exercise))

    init_session_key(session, unit, exercise, 'progress')
    session[unit][str(exercise)]['progress'].append(nr)
    return


def register_false(session, unit, exercise, nr):
    """
    Records a question as incorrectly answered for a specific unit and exercise.

    Ensures the 'falses' key exists in the session for the given exercise, then appends
    the question number to the list of incorrect answers.

    Args:
        session (dict): The session dictionary tracking user progress.
        unit (str): The unit identifier.
        exercise (str or int): The exercise identifier.
        nr (int or str): The question number to mark as incorrect.

    Returns:
        None
    """
    if (unit, exercise) not in session['unfinished_exercise']:
        session['unfinished_exercise'].append((unit, exercise))

    init_session_key(session, unit, exercise, 'falses')
    session[unit][str(exercise)]['falses'].append(nr)
    return


def register_user_incorrect_answer(session, unit, exercise, incorrect_answer):
    """
    Stores the user's incorrect answer for a given unit and exercise.

    Ensures the 'incorrect_answer' key exists in the session for the specified exercise,
    then appends the user's incorrect response to the list.

    Args:
        session (dict): The session dictionary tracking user input.
        unit (str): The unit identifier.
        exercise (str or int): The exercise identifier.
        incorrect_answer (str): The user's incorrect answer to store.

    Returns:
        None
    """
    if (unit, exercise) not in session['unfinished_exercise']:
        session['unfinished_exercise'].append((unit, exercise))

    init_session_key(session, unit, exercise, 'incorrect_answer')
    session[unit][str(exercise)]['incorrect_answer'].append(incorrect_answer)
    return


def register_result(session, unit, exercise, feedback):
    """
    Finalizes and records the result of a completed exercise.

    If feedback is provided, prints a completion message.
    Ensures required session keys ('progress' and 'falses') exist before computing the score.
    Stores the computed score (rounded to two decimal places) under the 'result' key.

    Cleans up temporary progress data by removing:
    - 'progress' (answered questions),
    - 'falses' (incorrect question IDs),
    - 'incorrect_answer' (user's incorrect responses).

    Also removes the (unit, exercise) pair from the 'unfinished_exercise' list if present,
    and marks the session as modified to ensure the update is saved.

    Args:
        session (dict): The session dictionary tracking user data.
        unit (str): The unit identifier.
        exercise (str or int): The exercise identifier.
        feedback (any): Feedback data used to confirm completion.

    Returns:
        None
    """
    init_session_key(session, unit, exercise, 'progress')
    init_session_key(session, unit, exercise, 'falses')

    score_exercise = compute_score(session, unit, exercise)
    session[unit][str(exercise)]['result'] = round(score_exercise, 2)

    if feedback is not None:
        log_exercise_completed(unit, exercise, round(score_exercise, 2))

    if is_key_in_exercise(session, unit, exercise, 'progress'):
        del session[unit][str(exercise)]['progress']

    if is_key_in_exercise(session, unit, exercise, 'falses'):
        del session[unit][str(exercise)]['falses']

    if is_key_in_exercise(session, unit, exercise, 'incorrect_answer'):
        del session[unit][str(exercise)]['incorrect_answer']

    if (unit, exercise) in session['unfinished_exercise']:
        session['unfinished_exercise'].remove((unit, exercise))

    session.modified = True
    return
