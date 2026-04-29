from flask import session, request
from flask_login import current_user, login_required

from typing import cast

from data.content.unit.stars import STARS
from data.content.unit.unit_page import UNIT_PAGE
from data.content.unit.title_page import TITLE_PAGE
from data.content.unit.unit_content_by_language import HOME_DESCRIPTION, INTRODUCTION
from data.content.application.text import YOUR_ANSWER, META_DESCRIPTION
from data.content.application.buttons import HOMEPAGE, UNIT_PARTICULARLY_LIKE_BY_USERS

from data.data_processing.units import units
from data.data_processing.exercises import get_exercises_by_unit_and_level, levels, get_level_from_exercise
from data.data_processing.total_questions import total_question_exercises, highest_exercise_per_unit

from users.users.models import Bookmark
from users.users.settings import get_filename_empty_bookmark, get_filename_full_bookmark, get_filename_flag
from users.progress.score import write_score, get_lowest_scored_exercises
from users.progress.progress import compute_answered_questions, update_progress_in_home_page, is_exercise_started, \
    get_fraction_exercises_finished_by_level, get_random_unit_and_lowest_unfinished_exercise, get_unfinished_exercises, \
    get_progress_home_page
from users.questions.content_format import format_correction, format_description

from . import routes_bp

from webapp.i18n import get_language
from webapp.style.icons import STAR_GOLD

session = cast(dict, session)


@routes_bp.route('/', endpoint='home')
def home():

    language = get_language(request, session)

    home_description = HOME_DESCRIPTION[language]
    meta_description = META_DESCRIPTION[language]

    '''
    if not isinstance(session.get('progress'), dict):
        session['progress'] = {}

    completed_exercises = session['progress']
    if current_user.is_authenticated:
        for unit in units:
            if unit not in completed_exercises:
                update_progress_in_home_page(session, unit)

    session.modified = True
    '''

    completed_exercises = {unit: get_progress_home_page(session, unit) for unit in units}

    return render_template('home.html',
                           title_page=TITLE_PAGE,
                           unit_page=UNIT_PAGE,
                           unit_stars=STARS,
                           STAR_GOLD=STAR_GOLD,
                           home_description=home_description,
                           completed_exercises=completed_exercises,
                           highest_exercise=highest_exercise_per_unit,
                           UNIT_PARTICULARLY_LIKE_BY_USERS=UNIT_PARTICULARLY_LIKE_BY_USERS[language],
                           meta_description=meta_description,
                           user_is_connected=current_user.is_authenticated,
                           )


for unit in units:
    route_path = UNIT_PAGE[unit]
    template = 'unit.html'

    def make_route(unit=unit):
        endpoint_name = f'dynamic_route_{unit}'
        @routes_bp.route(route_path, endpoint=endpoint_name)
        def dynamic_route():
            language = get_language(request, session)
            title_page = TITLE_PAGE[unit]
            introduction = INTRODUCTION[language].get(unit, {})
            meta_description = META_DESCRIPTION[language]

            exercises_A1 = get_exercises_by_unit_and_level(unit, 'A1')
            exercises_A2 = get_exercises_by_unit_and_level(unit, 'A2')
            exercises_B1 = get_exercises_by_unit_and_level(unit, 'B1')
            exercises_B2 = get_exercises_by_unit_and_level(unit, 'B2')
            exercises_C1 = get_exercises_by_unit_and_level(unit, 'C1')
            exercises_C2 = get_exercises_by_unit_and_level(unit, 'C2')

            update_progress_in_home_page(session, unit)

            return render_template(template,
                                   title_page=title_page,
                                   answered_questions=compute_answered_questions,
                                   total_questions=total_question_exercises,
                                   score=write_score,
                                   introduction=introduction,
                                   format_description=format_description,
                                   homepage=HOMEPAGE[language],
                                   meta_description=meta_description,
                                   is_exercise_started=is_exercise_started,
                                   exercises_A1=exercises_A1,
                                   exercises_A2=exercises_A2,
                                   exercises_B1=exercises_B1,
                                   exercises_B2=exercises_B2,
                                   exercises_C1=exercises_C1,
                                   exercises_C2=exercises_C2,
                                   )
        return dynamic_route

    make_route()


@routes_bp.route('/settings', endpoint='settings')
def settings():

    language = get_language(request, session)

    page = {
        'english': 'menu/settings_en.html',
        'french': 'menu/settings_fr.html',
    }

    email = current_user.email if current_user.is_authenticated else None

    return render_template(page[language],
                           email=email,
                           is_authenticated=current_user.is_authenticated,
                           )


@routes_bp.route('/about', endpoint='about')
def about():

    language = get_language(request, session)

    page = {
        'english': 'menu/about_en.html',
        'french': 'menu/about_fr.html',
    }

    return render_template(page[language])


@routes_bp.route("/bookmarks")
@login_required
def bookmarks():

    language = get_language(request, session)

    bookmark = (
        Bookmark.query
        .filter_by(user_id=current_user.id)
        .order_by(Bookmark.created_at.desc())
        .all()
    )

    page = {
        'english': 'menu/bookmarks_en.html',
        'french': 'menu/bookmarks_fr.html',
    }

    return render_template(page[language],
                           bookmarks=bookmark,
                           is_feedback_box=True,
                           your_answer=YOUR_ANSWER[language],
                           title_page=TITLE_PAGE,
                           force_full_bookmark=True,
                           format_correction=format_correction,
                           icon_empty=get_filename_empty_bookmark(),
                           icon_full=get_filename_full_bookmark(),
                           icon_flag=get_filename_flag(),
                           language=language,
                           )


@routes_bp.route("/progress")
def progress():

    language = get_language(request, session)

    page = {
        'english': 'menu/progress_en.html',
        'french': 'menu/progress_fr.html',
    }

    fraction_level_finished = {level: get_fraction_exercises_finished_by_level(session, level) for level in levels}
    random_unit_exercise = {level: get_random_unit_and_lowest_unfinished_exercise(session, level) for level in levels}

    unfinished_exercises = get_unfinished_exercises(session)

    lowest_score_exercises = get_lowest_scored_exercises()

    return render_template(
        page[language],
        title_page=TITLE_PAGE,
        levels=levels,
        fractions=fraction_level_finished,
        random_unit_exercise=random_unit_exercise,
        unfinished_exercises=unfinished_exercises,
        answered_questions=compute_answered_questions,
        total_questions=total_question_exercises,
        score=write_score,
        is_exercise_started=is_exercise_started,
        lowest_score_exercises=lowest_score_exercises,
        get_level_from_exercise=get_level_from_exercise,
        )


@routes_bp.route("/robots.txt")
def robots_txt():
    content = (
        "User-agent: *\n"
        "Disallow:\n"
        "Sitemap: https://www.sieversstudyhall.com/sitemap.xml\n"
    )
    return Response(content, mimetype="text/plain")


from flask import Response, url_for, render_template, current_app
from werkzeug.routing import BuildError
import datetime

@routes_bp.route("/sitemap.xml")
def sitemap():
    pages = []
    today = datetime.date.today().isoformat()

    def add(endpoint: str):
        try:
            pages.append({
                "loc": url_for(endpoint, _external=True),
                "lastmod": today
            })
        except BuildError:
            current_app.logger.warning(
                f"Could not build sitemap URL for endpoint: {endpoint}"
            )

    add("routes.home")

    for unit in units:
        add(f"routes.dynamic_route_{unit}")

    sitemap_xml = render_template("sitemap_template.xml", pages=pages)
    return Response(sitemap_xml, mimetype="application/xml")