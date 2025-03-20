from data_processing.exercises import (artikel, pronomen, konnektoren, praepositionen_grammatik, adjektivdeklinationen,
                                       praesens, praepositionen_konjugation, imperativ, perfekt, praeteritum,
                                       konjunktiv,
                                       partizip_I,
                                       verben, adjektive, adverbien, deverbale_substantive, trennbare_verben)

QUESTION_TRANSLATION = {
    artikel: {
        1: "Finde den Nominativ bestimmten Artikel, der in den folgenden Satz passt:"
           "<br><br><center>{question} \u25CF {gender}</center>",
        2: "Finde den Akkusativ bestimmten Artikel, der in den folgenden Satz passt:"
           "<br><br>{question} \u25CF {gender}",
        3: "Finde den Dativ bestimmten Artikel, der in den folgenden Satz passt:"
           "<br><br>{question} \u25CF {gender}",
        4: "Finde den bestimmten Artikel, der in den folgenden Satz passt:"
           "<br><br>{question} \u25CF {gender}",
        5: "Finde den Nominativ unbestimmten Artikel, der in den folgenden Satz passt:"
           "<br><br>{question} \u25CF {gender}",
        6: "Finde den Akkusativ unbestimmten Artikel, der in den folgenden Satz passt:"
           "<br><br>{question} \u25CF {gender}",
        7: "Finde den Dativ unbestimmten Artikel, der in den folgenden Satz passt:"
           "<br><br>{question} \u25CF {gender}",
        8: "Finde den unbestimmten Artikel, der in den folgenden Satz passt:"
           "<br><br>{question} \u25CF {gender}",
        9: "Finde den bestimmten Artikel, der in den folgenden Satz passt:"
           "<br><br>{question}",
        10: "Übersetz das folgenden Artikels:"
            "<br><br><strong>{question}</strong>",
        11: "Finde den fehlenden Artikel im folgenden Satz:"
            "<br><br>{question}"
            "<br><br>{english}",
        12: "Übersetz das folgenden Artikels:"
            "<br><br><strong>{question}</strong>",
        13: "Finde den fehlenden Artikel im folgenden Satz:"
            "<br><br>{question}"
            "<br><br>{english}",
    },

    pronomen: {
        1: "Finde das Nominativpronomen, das in den folgenden Satz passt:"
           "<br><br>{question} \u25CF {person}",
        2: "Finde das Akkusativpronomen, das in den folgenden Satz passt:"
           "<br><br>{question} \u25CF {person}",
        3: "Finde das Dativpronomen, das in den folgenden Satz passt:"
           "<br><br>{question} \u25CF {person}",
        4: "Finde das Pronomen, das in den folgenden Satz passt:"
           "<br><br>{question} \u25CF {person}",
        5: "Finde das Reflexivpronomen, das in den folgenden Satz passt:"
           "<br><br>{question} \u25CF {person}",
        6: "Finde das Pronomen, das in den folgenden Satz passt:"
           "<br><br>{question} \u25CF {person}",
        7: "Übersetz das folgenden Pronomens:"
           "<br><br><strong>{question}</strong>",
        8: "Finde das fehlende Pronomen im folgenden Satz:"
           "<br><br>{question}"
           "<br><br>{english}",
        9: "Finde das fehlende Nominativ-Relativpronomen im folgenden Satz:"
           "<br><br>{question}",
        10: "Finde das fehlende Akkusativ-Relativpronomen im folgenden Satz:"
            "<br><br>{question}",
        11: "Finde das fehlende Dativ-Relativpronomen im folgenden Satz:"
            "<br><br>{question}",
        12: "Finde das fehlende Genitiv-Relativpronomen im folgenden Satz:"
            "<br><br>{question}",
        13: "Finde das fehlende Relativpronomen im folgenden Satz:"
            "<br><br>{question}",
        14: "Finde das fehlende Relativpronomen im folgenden Satz:"
            "<br><br>{question}",
    },

    konnektoren: {
        1: "Übersetz das folgenden Konnektors:"
           "<br><br><strong>{question}</strong>",
        2: "Finde den fehlenden Konnektor im folgenden Satz:"
           "<br><br>{question}"
           "<br><br>{english}",
        3: "Übersetz das folgenden Konnektors:"
           "<br><br><strong>{question}</strong>",
        4: "Finde den fehlenden Konnektor im folgenden Satz:"
           "<br><br>{question}"
           "<br><br>{english}",
        5: "Übersetz das folgenden Konnektors:"
           "<br><br><strong>{question}</strong>",
        6: "Finde den fehlenden Konnektor im folgenden Satz:"
           "<br><br>{question}"
           "<br><br>{english}",
        7: "Übersetz das folgenden Konnektors:"
           "<br><br><strong>{question}</strong>",
        8: "Finde den fehlenden Konnektor im folgenden Satz:"
           "<br><br>{question}"
           "<br><br>{english}",
    },

    praepositionen_grammatik: {
        1: "Finde die Übersetzung der folgenden Präposition:"
           "<br><br>{question}",
        2: "Finde die Präposition, die in den folgenden Satz passt:"
           "<br><br>{question}"
           "<br><br>{english}",
        3: "Finde die Präposition, die in den folgenden Satz passt:"
           "<br><br>{question}"
           "<br><br>{english}",
        4: "Finde die Präposition, die in den folgenden Satz passt:"
           "<br><br>{question}"
           "<br><br>{english}",
        5: "Finde die Präposition, die in den folgenden Satz passt:"
           "<br><br>{question}"
           "<br><br>{english}",
        6: "Finde die Präposition, die in den folgenden Satz passt:"
           "<br><br>{question}"
           "<br><br>{english}",
        7: "Finde die Präposition, die in den folgenden Satz passt:"
           "<br><br>{question}"
           "<br><br>{english}",
        8: "Finde die Präposition, die in den folgenden Satz passt:"
           "<br><br>{question}"
           "<br><br>{english}",
        9: "Finde die Übersetzung der folgenden Präposition:"
           "<br><br>{question}",
        10: "Finde die Präposition, die in den folgenden Satz passt:"
             "<br><br>{question}"
             "<br><br>{english}",
        11: "Finde die Übersetzung der folgenden Präposition:"
             "<br><br>{question}",
        12: "Finde die Präposition, die in den folgenden Satz passt:"
             "<br><br>{question}"
             "<br><br>{english}",
        13: "Finde die Präposition (durch oder von), die in den folgenden Satz passt:"
             "<br><br>{question}"
             "<br><br>{english}",
        14: "Finde die Präposition (aus oder vor), die in den folgenden Satz passt:"
             "<br><br>{question}"
             "<br><br>{english}",
        15: "Finde die Präposition (zu oder für) und den Artikel, die in den folgenden Satz passen:"
             "<br><br>{question}"
             "<br><br>{english}",
        16: "Finde die Übersetzung der folgenden Präposition:"
             "<br><br>{question}",
        17: "Finde die Präposition, die in den folgenden Satz passt:"
             "<br><br>{question}"
             "<br><br>{english}",
    },

    adjektivdeklinationen: {
        1: "Ergänz den Satz mit der richtigen Form des angegebenen Adjektivs:"
           "<br><br>{question} \u25CF {case} \u25CF {adjective}",
        2: "Ergänz den Satz mit der richtigen Form des angegebenen Adjektivs:"
           "<br><br>{question} \u25CF {adjective}",
        3: "Ergänz den Satz mit der richtigen Form des angegebenen Adjektivs:"
           "<br><br>{question} \u25CF {adjective}",
        4: "Ergänz den Satz mit der richtigen Form des angegebenen Adjektivs:"
           "<br><br>{question} \u25CF {adjective}",
        5: "Ergänz den Satz mit der richtigen Form des angegebenen Adjektivs:"
           "<br><br>{question} \u25CF {adjective}",
        6: "Ergänz den Satz mit der richtigen Form des angegebenen Adjektivs:"
           "<br><br>{question} \u25CF {adjective}",
        7: "Ergänz den Satz mit der richtigen Form des angegebenen Adjektivs:"
           "<br><br>{question} \u25CF {adjective}",
        8: "Ergänz den Satz mit der richtigen Form des angegebenen Adjektivs:"
           "<br><br>{question} \u25CF {adjective}",
        9: "Ergänz den Satz mit der richtigen Form des angegebenen Adjektivs:"
           "<br><br>{question} \u25CF {case} \u25CF {adjective}",
        10: "Ergänz den Satz mit der richtigen Form des angegebenen Adjektivs:"
            "<br><br>{question} \u25CF {adjective}",
        11: "Ergänz den Satz mit der richtigen Form des angegebenen Adjektivs:"
            "<br><br>{question} \u25CF {adjective}",
        12: "Ergänz den Satz mit der richtigen Form des angegebenen Adjektivs:"
            "<br><br>{question} \u25CF {adjective}",
        13: "Ergänz den Satz mit der richtigen Form des angegebenen Adjektivs:"
            "<br><br>{question} \u25CF {adjective}",
        14: "Ergänz den Satz mit der richtigen Form des angegebenen Adjektivs:"
            "<br><br>{question} \u25CF {adjective}",
        15: "Ergänz den Satz mit der richtigen Form des angegebenen Adjektivs:"
            "<br><br>{question} \u25CF {case} \u25CF {adjective}",
        16: "Ergänz den Satz mit der richtigen Form des angegebenen Adjektivs:"
            "<br><br>{question} \u25CF {adjective}",
    },

    praesens: {
        1: "Ergänz den Satz mit dem Präsens des folgenden Verb:<br><br>{alinea}{question} \u25CF {person} _____",
        2: "Ergänz den Satz mit dem Präsens des folgenden Verb:<br><br>{alinea}{question} \u25CF {person} _____",
        3: "Ergänz den Satz mit dem Präsens des folgenden Verb:<br><br>{alinea}{question} \u25CF {person} _____",
        4: "Ergänz den Satz mit dem Präsens des folgenden Verb:<br><br>{alinea}{question} \u25CF {person} _____",
        5: "Ergänz den Satz mit dem Präsens des folgenden Verb:<br><br>{alinea}{question} \u25CF {person} _____",
        6: "Ergänz den Satz mit dem Präsens des folgenden Verb:<br><br>{alinea}{question} \u25CF {person} _____",
        7: "Ergänz den Satz mit dem Präsens des folgenden Verb:<br><br>{alinea}{question} \u25CF {person} _____",
        8: "Ergänz den Satz mit dem Präsens des folgenden Verb:<br><br>{alinea}{question} \u25CF {person} _____",
        9: "Ergänz den Satz mit dem Präsens des folgenden Verb:<br><br>{alinea}{question} \u25CF {person} _____",
        10: "Ergänz den Satz mit dem Präsens des folgenden Verb:<br><br>{alinea}{question} \u25CF {person} _____",
        11: "Ergänz den Satz mit dem Präsens des folgenden Verb:<br><br>{alinea}{question} \u25CF {person} _____",
        12: "Ergänz den Satz mit dem Präsens des folgenden Verb:<br><br>{alinea}{question} \u25CF {person} _____",
        13: "Ergänz den Satz mit dem Präsens des folgenden Verb:<br><br>{alinea}{question} \u25CF {person} _____",
        14: "Ergänz den Satz mit dem Präsens des folgenden Verb:<br><br>{alinea}{question} \u25CF {person} _____",
        15: "Ergänz den Satz mit dem Präsens des folgenden Verb:<br><br>{alinea}{question} \u25CF {person} _____",
        16: "Ergänz den Satz mit dem Präsens des folgenden Verb:<br><br>{alinea}{question} \u25CF {person} _____",
        17: "Ergänz den Satz mit dem Präsens des folgenden Verb:<br><br>{alinea}{question} \u25CF {person} _____",
        18: "Ergänz den Satz mit dem Präsens des folgenden Verb:<br><br>{alinea}{question} \u25CF {person} _____",
        19: "Ergänz den Satz mit dem Präsens des folgenden Verb:<br><br>{alinea}{question} \u25CF {person} _____",
        20: "Ergänz den Satz mit dem Präsens des folgenden Verb:<br><br>{alinea}{question} \u25CF {person} _____",
        21: "Ergänz den Satz mit dem Präsens des folgenden Verb:<br><br>{alinea}{question} \u25CF {person} _____",
        22: "Ergänz den Satz mit dem Präsens des folgenden Verb:<br><br>{alinea}{question} \u25CF {person} _____",
        23: "Ergänz den Satz mit dem Präsens des folgenden Verb:<br><br>{alinea}{question} \u25CF {person} _____",
        24: "Ergänz den Satz mit dem Präsens des folgenden Verb:<br><br>{alinea}{question} \u25CF {person} _____",
    },

    praepositionen_konjugation: {
        1: "Finde die Präposition, die zu folgendem Verb passt:<br><br>{english} = {question} _____",
        2: "Ergänz den Satz mit der passenden Präposition:<br><br>{question}<br><br>{english}",
        3: "Finde die Präposition, die zu folgendem Verb passt:<br><br>{english} = {question} _____",
        4: "Ergänz den Satz mit der passenden Präposition:<br><br>{question}<br><br>{english}",
        5: "Finde die Präposition, die zu folgendem Verb passt:<br><br>{english} = {question} _____",
        6: "Ergänz den Satz mit der passenden Präposition:<br><br>{question}<br><br>{english}",
        7: "Ergänz den Satz mit dem passenden Da-Wort:<br><br>{question}<br><br>{english}",
        8: "Ergänz den Satz mit dem passenden Wo-Wort:<br><br>{question}<br><br>{english}",
        9: "Finde die Präposition, die zu folgendem Verb passt:<br><br>{english} = {question} _____",
        10: "Ergänz den Satz mit der passenden Präposition:<br><br>{question}<br><br>{english}",
        11: "Finde die Präposition, die zu folgendem Nomen passt:<br><br>{english} = {question} _____",
        12: "Ergänz den Satz mit der passenden Präposition:<br><br>{question}<br><br>{english}",
        13: "Finde die Präposition, die zu folgendem Adjektiv passt:<br><br>{english} = {question} _____",
        14: "Ergänz den Satz mit der passenden Präposition:<br><br>{question}<br><br>{english}",
    },

    perfekt: {
        1: "Finde das Partizip II des folgenden Verb:<br><br>{question}",
        2: "Finde das Partizip II des folgenden Verb:<br><br>{question}",
        3: "Finde das Partizip II des folgenden Verb:<br><br>{question}",
        4: "Finde das Partizip II des folgenden Verb:<br><br>{question}",
        5: "Finde das Partizip II des folgenden Verb:<br><br>{question}",
        6: "Finde das Partizip II des folgenden Verb:<br><br>{question}",
        7: "Finde das Partizip II des folgenden Verb:<br><br>{question}",
        8: "Finde das Partizip II des folgenden Verb:<br><br>{question}",
        9: "Finde das Partizip II des folgenden Verb:<br><br>{question}",
        10: "Finde das Partizip II des folgenden Verb:<br><br>{question}",
        11: "Finde das Partizip II des folgenden Verb:<br><br>{question}",
        12: "Finde das Partizip II des folgenden Verb:<br><br>{question}",
        13: "Finde das Partizip II des folgenden Verb:<br><br>{question}",
        14: "Finde das Partizip II des folgenden Verb:<br><br>{question}",
        15: "Finde das Partizip II des folgenden Verb:<br><br>{question}",
        16: "Finde das Partizip II des folgenden Verb:<br><br>{question}",
    },

    praeteritum: {
        1: "Finde das Präteritum des folgenden Verb:<br><br>{question} \u25CF {person} _____",
        2: "Ergänz den Satz mit dem Präteritum (3. Person Singular) des folgenden Verb:<br><br>{question} \u25CF er/sie/es _____",
        3: "Ergänz den Satz mit dem Präteritum (3. Person Singular) des folgenden Verb:<br><br>{question} \u25CF er/sie/es _____",
        4: "Ergänz den Satz mit dem Präteritum (3. Person Singular) des folgenden Verb:<br><br>{question} \u25CF er/sie/es _____",
        5: "Ergänz den Satz mit dem Präteritum (3. Person Singular) des folgenden Verb:<br><br>{question} \u25CF er/sie/es _____",
        6: "Ergänz den Satz mit dem Präteritum (3. Person Singular) des folgenden Verb:<br><br>{question} \u25CF er/sie/es _____",
        7: "Ergänz den Satz mit dem Präteritum (3. Person Singular) des folgenden Verb:<br><br>{question} \u25CF er/sie/es _____",
        8: "Ergänz den Satz mit dem Präteritum (3. Person Singular) des folgenden Verb:<br><br>{question} \u25CF er/sie/es _____",
        9: "Ergänz den Satz mit dem Präteritum (3. Person Singular) des folgenden Verb:<br><br>{question} \u25CF er/sie/es _____",
        10: "Ergänz den Satz mit dem Präteritum (3. Person Singular) des folgenden Verb:<br><br>{question} \u25CF er/sie/es _____",
        11: "Ergänz den Satz mit dem Präteritum (3. Person Singular) des folgenden Verb:<br><br>{question} \u25CF er/sie/es _____",
        12: "Ergänz den Satz mit dem Präteritum (3. Person Singular) des folgenden Verb:<br><br>{question} \u25CF er/sie/es _____",
        13: "Ergänz den Satz mit dem Präteritum (3. Person Singular) des folgenden Verb:<br><br>{question} \u25CF er/sie/es _____",
        14: "Ergänz den Satz mit dem Präteritum (3. Person Singular) des folgenden Verb:<br><br>{question} \u25CF er/sie/es _____",
        15: "Ergänz den Satz mit dem Präteritum (3. Person Singular) des folgenden Verb:<br><br>{question} \u25CF er/sie/es _____",
        16: "Ergänz den Satz mit dem Präteritum (3. Person Singular) des folgenden Verb:<br><br>{question} \u25CF er/sie/es _____",
        17: "Ergänz den Satz mit dem Präteritum (3. Person Singular) des folgenden Verb:<br><br>{question} \u25CF er/sie/es _____",
    },

    imperativ: {
        1: "Ergänz den Satz mit dem Imperativ des folgenden Verb:<br><br>{question} \u25CF {person} \u25CF _____",
        2: "Ergänz den Satz mit dem Imperativ des folgenden Verb:<br><br>{question} \u25CF {person} \u25CF _____",
        3: "Ergänz den Satz mit dem Imperativ des folgenden Verb:<br><br>{question} \u25CF {person} \u25CF _____",
        4: "Ergänz den Satz mit dem Imperativ des folgenden Verb:<br><br>{question} \u25CF {person} \u25CF _____",
        5: "Ergänz den Satz mit dem Imperativ des folgenden Verb:<br><br>{question} \u25CF {person} \u25CF _____",
        6: "Ergänz den Satz mit dem Imperativ des folgenden Verb:<br><br>{question} \u25CF {person} \u25CF _____",
    },

    konjunktiv: {
        1: "Ergänz den Satz mit dem Konjunktiv II des folgenden Verb:<br><br>{question} \u25CF {person} _____",
    },

    partizip_I: {
        1: "Finde das Partizip I des folgenden Verb:<br><br>{question} \u25CF Englisch: {english}",
        2: "Finde das Partizip I des folgenden Verb:<br><br>{question} \u25CF Englisch: {english}",
        3: "Finde das Partizip I des folgenden Verb:<br><br>{question} \u25CF Englisch: {english}",
    },

    adverbien: {
        1: "Übersetz das folgenden Adverb:"
           "<br><br><strong>{question}</strong>",
        2: "Ergänz den Satz mit dem fehlenden Adverb:"
           "<br><br>{question}<br><br>{english}",
        3: "Übersetz das folgenden Adverb:"
           "<br><br><strong>{question}</strong>",
        4: "Ergänz den Satz mit dem fehlenden Adverb:"
           "<br><br>{question}<br><br>{english}",
        5: "Übersetz das folgenden Adverb:"
           "<br><br><strong>{question}</strong>",
        6: "Ergänz den Satz mit dem fehlenden Adverb:"
           "<br><br>{question}<br><br>{english}",
        7: "Übersetz das folgenden Adverb:"
           "<br><br><strong>{question}</strong>",
        8: "Ergänz den Satz mit dem fehlenden Adverb:"
           "<br><br>{question}<br><br>{english}",
        9: "Übersetz das folgenden Adverb:"
           "<br><br><strong>{question}</strong>",
        10: "Ergänz den Satz mit dem fehlenden Adverb:"
            "<br><br>{question}<br><br>{english}",
        11: "Übersetz das folgenden Adverb:"
            "<br><br><strong>{question}</strong>",
        12: "Ergänz den Satz mit dem fehlenden Adverb:"
            "<br><br>{question}<br><br>{english}",
        13: "Übersetz das folgenden Adverb:"
            "<br><br><strong>{question}</strong>",
        14: "Ergänz den Satz mit dem fehlenden Adverb:"
            "<br><br>{question}<br><br>{english}",
    },

    verben: {
        1: "Übersetz das folgenden Verb:"
           "<br><br><strong>{question}</strong>",
        2: "Übersetz das folgenden Verb:"
           "<br><br><strong>{question}</strong>",
        3: "Übersetz das folgenden Verb:"
           "<br><br><strong>{question}</strong>",
        4: "Übersetz das folgenden Verb:"
           "<br><br><strong>{question}</strong>",
        5: "Übersetz das folgenden Verb:"
           "<br><br><strong>{question}</strong>",
        6: "Übersetz das folgenden Verb:"
           "<br><br><strong>{question}</strong>",
        7: "Übersetz das folgenden Verb:"
           "<br><br><strong>{question}</strong>",
        8: "Übersetz das folgenden Verb:"
           "<br><br><strong>{question}</strong>",
        9: "Übersetz das folgenden Verb:"
           "<br><br><strong>{question}</strong>",
        10: "Übersetz das folgenden Verb:"
            "<br><br><strong>{question}</strong>",
        11: "Übersetz das folgenden Verb:"
            "<br><br><strong>{question}</strong>",
        12: "Übersetz das folgenden Verb:"
            "<br><br><strong>{question}</strong>",
        13: "Übersetz das folgenden Verb:"
            "<br><br><strong>{question}</strong>",
        14: "Übersetz das folgenden Verb:"
            "<br><br><strong>{question}</strong>",
        15: "Übersetz das folgenden Verb:"
            "<br><br><strong>{question}</strong>",
        16: "Übersetz das folgenden Verb:"
            "<br><br><strong>{question}</strong>",
        17: "Übersetz das folgenden Verb:"
            "<br><br><strong>{question}</strong>",
        18: "Übersetz das folgenden Verb:"
            "<br><br><strong>{question}</strong>",
        19: "Übersetz das folgenden Verb:"
            "<br><br><strong>{question}</strong>",
        20: "Übersetz das folgenden Verb:"
            "<br><br><strong>{question}</strong>",
    },

    trennbare_verben: {
        1: "Übersetz das folgende (un)trennbare Verb basierend auf dem angegebenen Stammverb:"
           "<br><br><strong>{question}</strong> \u25CF {german}",
        2: "Übersetz das folgende (un)trennbare Verb basierend auf dem angegebenen Präfix:"
           "<br><br><strong>{question}</strong> \u25CF {prefix}",
        3: "Übersetz das folgende (un)trennbare Verb basierend auf dem angegebenen Stammverb:"
           "<br><br><strong>{question}</strong> \u25CF {german}",
        4: "Übersetz das folgende (un)trennbare Verb basierend auf dem angegebenen Stammverb:"
           "<br><br><strong>{question}</strong> \u25CF {german}",
        5: "Übersetz das folgende (un)trennbare Verb basierend auf dem angegebenen Präfix:"
           "<br><br><strong>{question}</strong> \u25CF {prefix}",
        6: "Übersetz das folgende (un)trennbare Verb basierend auf dem angegebenen Präfix:"
           "<br><br><strong>{question}</strong> \u25CF {prefix}",
        7: "Übersetz das folgende (un)trennbare Verb basierend auf dem angegebenen Stammverb:"
           "<br><br><strong>{question}</strong> \u25CF {german}",
        8: "Übersetz das folgende (un)trennbare Verb basierend auf dem angegebenen Stammverb:"
           "<br><br><strong>{question}</strong> \u25CF {german}",
        9: "Übersetz das folgende (un)trennbare Verb basierend auf dem angegebenen Präfix:"
           "<br><br><strong>{question}</strong> \u25CF {prefix}",
        10: "Übersetz das folgende (un)trennbare Verb basierend auf dem angegebenen Präfix:"
            "<br><br><strong>{question}</strong> \u25CF {prefix}",
    },

    deverbale_substantive: {
        1: "Finde das passende Nomen:<br><br>{english}: {german}<br><br>{question}: _____",
        2: "Finde das passende Nomen:<br><br>{english}: {german}<br><br>{question}: _____",
        3: "Finde das passende Nomen:<br><br>{english}: {german}<br><br>{question}: _____",
        4: "Finde das passende Nomen:<br><br>{english}: {german}<br><br>{question}: _____",
        5: "Finde das passende Nomen:<br><br>{english}: {german}<br><br>{question}: _____",
        6: "Finde das passende Nomen:<br><br>{english}: {german}<br><br>{question}: _____",
        7: "Finde das passende Nomen:<br><br>{english}: {german}<br><br>{question}: _____",
        8: "Finde das passende Nomen:<br><br>{english}: {german}<br><br>{question}: _____",
        9: "Finde das passende Nomen:<br><br>{english}: {german}<br><br>{question}: _____",
        10: "Finde das passende Nomen:<br><br>{english}: {german}<br><br>{question}: _____",
        11: "Finde das passende Nomen:<br><br>{english}: {german}<br><br>{question}: _____",
        12: "Finde das passende Nomen:<br><br>{english}: {german}<br><br>{question}: _____",
    },

}