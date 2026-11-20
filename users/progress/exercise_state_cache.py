from flask import g

from users.users.models import UserExerciseState


def get_user_exercise_states(user_id):
    """
    Returns all UserExerciseState rows for a user as a {(unit, exercise): row} map.

    The result is fetched with a single query and cached on flask.g for the
    duration of the request, so callers that need per-exercise lookups (e.g.
    when iterating over every exercise of a level) avoid issuing one query per
    exercise.

    Args:
        user_id (int): The authenticated user's id.

    Returns:
        dict[tuple[str, int], UserExerciseState]: Lookup of exercise state rows.
    """
    cache = getattr(g, "_exercise_state_cache", None)

    if cache is None or cache.get("user_id") != user_id:
        rows = UserExerciseState.query.filter_by(user_id=user_id).all()
        cache = {
            "user_id": user_id,
            "states": {(row.unit, row.exercise): row for row in rows},
        }
        g._exercise_state_cache = cache

    return cache["states"]


def get_user_exercise_state(user_id, unit, exercise):
    """
    Returns a single UserExerciseState row, using the per-request cache first.

    Falls back to a direct query on a cache miss so rows created earlier in the
    same request (after the cache was filled) are still found.
    """
    row = get_user_exercise_states(user_id).get((unit, exercise))

    if row is None:
        row = UserExerciseState.query.filter_by(
            user_id=user_id, unit=unit, exercise=exercise
        ).first()

    return row
