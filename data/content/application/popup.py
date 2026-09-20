from typing import cast

from flask import session

from data.content.unit.unit_content_by_language import UNIT_NAME

session = cast(dict, session)


def get_popup_title(language):
    popup_title = {
        'english': 'Progress erased',
        'french': 'Progrès effacé',
    }

    return popup_title[language]


def get_popup_text(unit, exercise, language):
    popup_text = {
        'english': (
            f"Progress erased for {UNIT_NAME[language][unit]} - Exercise {exercise} due to insufficient memory."
            f"<br><br>To save your progress over the long run and on multiple devices, and access additional features such as bookmarks, "
            f"<a href=\"/signup\" target=\"_blank\">create an account</a>."
            f"<br><br>For more information, consult the "
            f"<a href=\"https://sieversstudyhall.substack.com/p/faq\" target=\"_blank\">FAQ</a>."
        ),

        'french': (
            f"Progression effacée pour {UNIT_NAME[language][unit]} - Exercice {exercise} en raison d'une mémoire insuffisante."
            f"<br><br>Pour sauvegarder votre progression sur le long terme et sur plusieurs appareils,"
            f" et pour accéder à des fonctionnalité supplémentaires comme les marque-pages, "
            f"<a href=\" /signup\" target=\"_blank\">créez un compte</a>. "
            f"<br><br>Pour plus d'informations, consultez la "
            f"<a href=\"https://sieversstudyhall.substack.com/p/faq-8cc\" target=\"_blank\">Foire-à-Questions</a>."
        ),
    }
    return popup_text[language]

