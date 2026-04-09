def ensure_session_dictionary(session, dictionary):
    if dictionary not in session or not isinstance(session[dictionary], dict):
        session[dictionary] = {}


def update_session_dictionary(session, dictionary, key, value):
    ensure_session_dictionary(session, dictionary)

    data = dict(session[dictionary])
    data[key] = value
    session[dictionary] = data


def read_session_dictionary(session, dictionary, key, default=None):
    ensure_session_dictionary(session, dictionary)

    return session[dictionary].get(key, default)


def delete_session_dictionary(session, dictionary, key):
    ensure_session_dictionary(session, dictionary)
    session[dictionary].pop(key, None)


def read_feedback(session):
    ensure_session_dictionary(session, "feedback")

    feedback = session.pop("feedback", None) or {}
    result = feedback.get("result")
    user_answer = feedback.get("user_answer")
    previous_question_id = feedback.get("previous_question_id")

    return result, user_answer, previous_question_id


def add_new_id_in_session(session, dictionary, key, question_id):
    ensure_session_dictionary(session, dictionary)

    key_list = read_session_dictionary(session, dictionary, key, default=[])
    key_list = key_list + [question_id]

    update_session_dictionary(session, dictionary, key, key_list)