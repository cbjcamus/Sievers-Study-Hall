from flask import render_template, session, Response
from flask_login import current_user

from typing import cast

from . import routes_bp

from data.data_processing.units import units

from users.progress.score import write_score
from users.progress.progress import compute_answered_questions
from users.questions.total_questions import compute_total_questions

from webapp.content.unit.stars import STARS
from webapp.content.unit.unit_page import UNIT_PAGE
from webapp.content.unit.title_page import TITLE_PAGE
from webapp.content.unit.introduction import INTRODUCTION
from webapp.content.unit.template_path import TEMPLATE_PATH
from webapp.content.exercise.descriptions import DESCRIPTION

from webapp.style.icons import STAR_GOLD

session = cast(dict, session)


@routes_bp.route('/', endpoint='home')
def home():
    return render_template('home.html',
                           answered_questions=compute_answered_questions,
                           total_questions=compute_total_questions,
                           score=write_score,
                           explanation=INTRODUCTION,
                           title_page=TITLE_PAGE,
                           button_unit=TITLE_PAGE,
                           unit_page=UNIT_PAGE,
                           unit_stars=STARS,
                           STAR_GOLD=STAR_GOLD,
                           )


@routes_bp.route('/settings', endpoint='settings')
def settings():
    return render_template('menu/settings.html',
                           email=current_user.email,
                           )


@routes_bp.route('/settings_old', endpoint='settings_old')
def settings_old():
    return render_template('menu/settings_old.html',
                           )


@routes_bp.route('/contact', endpoint='contact')
def contact():
    return render_template('menu/contact.html',
                           )


for unit in units:
    route_path = UNIT_PAGE[unit]
    template = TEMPLATE_PATH[unit]

    def make_route(unit=unit, template=template):
        endpoint_name = f'dynamic_route_{unit}'
        @routes_bp.route(route_path, endpoint=endpoint_name)
        def dynamic_route():
            introduction = INTRODUCTION.get(unit, {})
            return render_template(template,
                                   answered_questions=compute_answered_questions,
                                   total_questions=compute_total_questions,
                                   score=write_score,
                                   introduction=introduction,
                                   description_templates=DESCRIPTION,
                                   )
        return dynamic_route

    make_route()


@routes_bp.route('/robots.txt')
def robots_txt():
    return Response(
        "User-agent: *\nDisallow:\nSitemap: https://www.sieversstudyhall.com/sitemap.xml",
        mimetype='text/plain'
    )


@routes_bp.route('/sitemap.xml')
def sitemap():
    from flask import Response, url_for
    import datetime

    pages = []
    today = datetime.date.today().isoformat()

    # Static routes
    pages.append({'loc': url_for('home', _external=True), 'lastmod': today})
    pages.append({'loc': url_for('settings', _external=True), 'lastmod': today})
    pages.append({'loc': url_for('contact', _external=True), 'lastmod': today})

    # Dynamic unit routes
    for unit in units:
        endpoint = f'dynamic_route_{unit}'
        try:
            loc = url_for(endpoint, _external=True)
            pages.append({'loc': loc, 'lastmod': today})
        except:
            pass  # In case the endpoint wasn't properly registered

    sitemap_xml = render_template('sitemap_template.xml', pages=pages)
    return Response(sitemap_xml, mimetype='application/xml')