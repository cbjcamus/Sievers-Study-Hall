from flask import render_template, session, Response, request
from flask_login import current_user

from typing import cast

from . import routes_bp

from data.data_processing.units import units
from data.data_processing.total_questions import total_question_exercises, highest_exercise

from users.users.models import Bookmark, get_filename_empty_bookmark, get_filename_full_bookmark
from users.progress.score import write_score
from users.progress.progress import compute_answered_questions, compute_completed_exercises, update_progress_in_session

from users.questions.pick_a_question import get_question_from_incorrect_answer

from webapp.i18n import get_language
from webapp.content.unit.stars import STARS
from webapp.content.unit.unit_page import UNIT_PAGE
from webapp.content.unit.title_page import TITLE_PAGE
from webapp.content.unit.introduction import INTRODUCTION
from webapp.content.unit.template_path import TEMPLATE_PATH
from webapp.content.unit.home_description import HOME_DESCRIPTION
from webapp.content.unit.french.home_description_fr import HOME_DESCRIPTION_FR
from webapp.content.unit.english.home_description_en import HOME_DESCRIPTION_EN
from webapp.content.exercise.content_exercises import DESCRIPTION

from webapp.content.application.text import YOUR_ANSWER, META_DESCRIPTION
from webapp.content.application.buttons import HOMEPAGE, UNIT_PARTICULARLY_LIKE_BY_USERS

from webapp.style.icons import STAR_GOLD

session = cast(dict, session)


@routes_bp.route('/', endpoint='home')
def home():

    language = get_language(request, session)

    home_description = HOME_DESCRIPTION[language]
    meta_description = META_DESCRIPTION[language]

    if not isinstance(session.get('progress'), dict):
        session['progress'] = {}

    progress = session['progress']
    for unit in units:
        if unit not in progress:
            update_progress_in_session(session, unit)

    session.modified = True

    return render_template('home.html',
                           title_page=TITLE_PAGE,
                           unit_page=UNIT_PAGE,
                           unit_stars=STARS,
                           STAR_GOLD=STAR_GOLD,
                           home_description=home_description,
                           completed_exercises=progress,
                           highest_exercise=highest_exercise,
                           UNIT_PARTICULARLY_LIKE_BY_USERS=UNIT_PARTICULARLY_LIKE_BY_USERS[language],
                           meta_description=meta_description,
                           )


@routes_bp.route('/settings', endpoint='settings')
def settings():

    language = get_language(request, session)

    if language == "english":
        return render_template('menu/settings_en.html',
                               email=current_user.email,
                               )

    elif language == "french":
        return render_template('menu/settings_fr.html',
                               email=current_user.email,
                               )


@routes_bp.route('/about', endpoint='about')
def about():

    language = get_language(request, session)

    if language == "english":
        return render_template('menu/about_en.html',
                               )

    elif language == "french":
        return render_template('menu/about_fr.html',
                               )


@routes_bp.route("/bookmarks")
def bookmarks():

    language = get_language(request, session)

    bookmarks = (
        Bookmark.query
        .filter_by(user_id=current_user.id)
        .order_by(Bookmark.created_at.desc())
        .all()
    )

    if language == "english":
        return render_template("menu/bookmarks_en.html",
                               bookmarks=bookmarks,
                               is_feedback_box=True,
                               your_answer=YOUR_ANSWER[language],
                               title_page=TITLE_PAGE,
                               force_full_bookmark=True,
                               get_question_from_incorrect_answer=get_question_from_incorrect_answer,
                               icon_empty=get_filename_empty_bookmark(),
                               icon_full=get_filename_full_bookmark(),
                               )

    elif language == "french":
        return render_template("menu/bookmarks_fr.html",
                           bookmarks=bookmarks,
                           is_feedback_box=True,
                           your_answer=YOUR_ANSWER[language],
                           title_page=TITLE_PAGE,
                           force_full_bookmark=True,
                           get_question_from_incorrect_answer=get_question_from_incorrect_answer,
                            icon_empty=get_filename_empty_bookmark(),
                            icon_full=get_filename_full_bookmark(),
                           )


for unit in units:
    route_path = UNIT_PAGE[unit]
    template = TEMPLATE_PATH[unit]

    def make_route(unit=unit, template=template):
        endpoint_name = f'dynamic_route_{unit}'
        @routes_bp.route(route_path, endpoint=endpoint_name)
        def dynamic_route():
            language = get_language(request, session)
            introduction = INTRODUCTION[language].get(unit, {})
            meta_description = META_DESCRIPTION[language].get(unit, {})

            update_progress_in_session(session, unit)

            return render_template(template,
                                   answered_questions=compute_answered_questions,
                                   total_questions=total_question_exercises,
                                   score=write_score,
                                   introduction=introduction,
                                   description_templates=DESCRIPTION[language],
                                   homepage=HOMEPAGE[language],
                                   meta_description=meta_description,
                                   )
        return dynamic_route

    make_route()


@routes_bp.route('/robots.txt')
def robots_txt():
    return Response(
        "User-agent: *\nDisallow:\nSitemap: https://www.sieversstudyhall.com/sitemap.xml",
        mimetype='text/plain'
    )


from flask import Response, url_for, render_template
from werkzeug.routing import BuildError
import datetime

@routes_bp.route("/sitemap.xml")
def sitemap():
    pages = []
    today = datetime.date.today().isoformat()

    def add(endpoint: str):
        try:
            pages.append({"loc": url_for(endpoint, _external=True), "lastmod": today})
        except BuildError:
            pass

    # IMPORTANT: if these routes are on a blueprint, you likely need the blueprint prefix.
    # Example: "routes_bp.home" or "menu.home" depending on how you named/registered it.
    add("routes.home")
    add("routes.settings")
    add("routes.contact")

    for unit in units:
        add(f"routes.dynamic_route_{unit}")

    sitemap_xml = render_template("sitemap_template.xml", pages=pages)
    return Response(sitemap_xml, mimetype="application/xml")