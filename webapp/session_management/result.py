from webapp.session_management.score import compute_score


def register_result(session, unit, exercise):
    score_exercise = compute_score(session, unit, exercise)

    if 'result' not in session:
        session['result'] = {}

    if unit not in session['result']:
        session['result'][unit] = {}

    if str(exercise) not in session['result'][unit]:
        session['result'][unit][str(exercise)] = {}

    session['result'][unit][str(exercise)] = round(score_exercise, 2)

    if unit in session['progress'] and str(exercise) in session['progress'][unit]:
        del session['progress'][unit][str(exercise)]

    if unit in session['score'] and str(exercise) in session['score'][unit]:
        del session['score'][unit][str(exercise)]

    session.modified = True
    return

