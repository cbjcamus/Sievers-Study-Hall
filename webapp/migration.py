from users.users.models import db, UserExerciseState


def migrate_incorrect_state():
    rows = UserExerciseState.query.all()

    migrated = 0

    for row in rows:
        old_state = row.state or {}
        incorrect = old_state.get("incorrect") or {}

        new_incorrect = {}
        changed = False

        for nr, value in incorrect.items():

            if isinstance(value, str):
                new_incorrect[str(nr)] = {
                    "answer": value,
                    "translation": "",
                    "commentary": ""
                }
                changed = True
            else:
                new_incorrect[str(nr)] = value

        if changed:
            # IMPORTANT: create a new dict rather than mutate row.state
            new_state = dict(old_state)
            new_state["incorrect"] = new_incorrect

            row.state = new_state
            migrated += 1

    db.session.commit()

    print(f"Migrated {migrated} rows.")