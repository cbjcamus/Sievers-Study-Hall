from typing import cast
from flask import session, request

from webapp.i18n import get_language

from webapp.content.unit.title_page import TITLE_PAGE

session = cast(dict, session)


def get_popup_title(unit, exercise):

    language = get_language(request, session)

    if language == 'english':
        popup_title = f"Progress erased"

    else:
        popup_title = f"Progrès effacé"

    return popup_title


def get_popup_text(unit, exercise):
    language = get_language(request, session)

    if language == 'english':
        popup_text = (f"Progress erased for {TITLE_PAGE[unit]} - Exercise {exercise} due to insufficient memory."
                      f"<br><br>To save your progress over the long run and on multiple devices, and access additional features such as bookmarks, "
                      f"<a href=\"/signup\" target=\"_blank\">create an account</a>."
                      f"<br><br>For more information, consult the "
                      f"<a href=\"https://sieversstudyhall.substack.com/p/faq\" target=\"_blank\">FAQ</a>.")

    else:
        popup_text = (f"Progression effacée pour {TITLE_PAGE[unit]} - Exercice {exercise} en raison d'une mémoire insuffisante."
                      f"<br><br>Pour enregistrer votre progression sur le long terme et sur plusieurs appareils, et pour accéder à des fonctionnalité supplémentaires comme les marque-pages, "
                      f"<a href=\" /signup\" target=\"_blank\">créez un compte</a>. "
                      f"<br><br>Pour plus d'informations, consultez la "
                      f"<a href=\"https://sieversstudyhall.substack.com/p/faq-8cc\" target=\"_blank\">Foire-à-Questions</a>.")

    return popup_text

