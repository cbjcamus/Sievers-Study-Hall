import json

from data.data_processing.units import units

from flask_login import current_user
from users.progress.models import UserExerciseState


def print_complete_session(session):
    """
    Prints the entire session dictionary, displaying progress and data for each unit and exercise.

    For each key in the session:
    - If the key corresponds to a known unit (as listed in the global 'units'),
      it prints each exercise and its associated values.
    - Otherwise, it prints the key and its value directly.

    Args:
        session (dict): The session dictionary to inspect.

    Returns:
        None
    """
    print("=== SESSION DATA ===")
    for key in session:
        if key in units:
            unit = key
            for exercise, value in session[unit].items():
                print(unit, exercise, value)
        else:
            print(key, session[key])
    return


def print_user_info_from_db():
    if current_user.is_authenticated:
        print("\n=== USER INFO ===")
        print(f"User ID: {current_user.id}")
        print(f"Email: {current_user.email}")
        print(f"Created at: {current_user.created_at}")

        print("\n=== DATABASE PROGRESS ===")
        rows = UserExerciseState.query.filter_by(user_id=current_user.id).all()
        if not rows:
            print("No progress stored in database yet.")
        for row in rows:
            state = row.state or {}
            score = 0.0
            total = state.get("total_questions")

            if "score" in state:  # prefer cached score
                score = float(state["score"])
            elif "result" in state:  # just in case you stored under "result"
                score = float(state["result"])
            elif "correct_ids" in state and total:
                score = len(state["correct_ids"]) / total if total > 0 else 0.0

            print(f"Unit: {row.unit}, Exercise: {row.exercise}, "
                  f"Score: {score:.2f}, "
                  f"Completed at: {row.completed_at}, "
                  f"Last update: {row.updated_at}")

            # Pretty-print the raw JSON state
            if state:
                print("  JSON state:")
                print(json.dumps(state, indent=4, ensure_ascii=False))
            else:
                print("  JSON state: {}")

    else:
        print("\n[User not signed in]")


def print_session_size(session):
    print("\n=== SESSION SIZE ===")
    print(f"Session size: {session_size(session)} bytes")


def session_size(session):
    """
    Calculates the size of the session data in bytes.

    Converts the session dictionary to a JSON string and encodes it in UTF-8,
    then returns the length of the resulting byte string.

    Args:
        session (dict): The session dictionary to measure.

    Returns:
        int: The size of the session in bytes.
    """
    session_data = dict(session)
    session_json = json.dumps(session_data)
    size_in_bytes = len(session_json.encode('utf-8'))
    return size_in_bytes