from webapp.content.exercise.feedbacks import FEEDBACK
from webapp.content.exercise.questions import QUESTION
from webapp.session_management.normalization import get_list_of_correct_answers

def format_feedback(df, unit, exercise):
    template = FEEDBACK[unit][exercise]
    result = []
    for _, row in df.iterrows():
        formatted = template.format(
            previous_question=row.get("question", ""),
            correct_answers=get_list_of_correct_answers(row.get("answer", ""), unit),
            english=row.get("english", ""),
            german=row.get("german", ""),
            adjective=row.get("adjective", ""),
            gender=row.get("gender", ""),
            case=row.get("case", ""),
            article=row.get("article", ""),
            person=row.get("person", ""),
            prefix=row.get("prefix", ""),
            explanation=row.get("explanation", "")
        )
        result.append(formatted)
    return result


def format_question(df, unit, exercise):
    template = QUESTION[unit][exercise]
    result = []
    for _, row in df.iterrows():
        formatted = template.format(
            question=row.get("question", ""),
            correct_answers=row.get("answer", ""),
            english=row.get("english", ""),
            german=row.get("german", ""),
            adjective=row.get("adjective", ""),
            gender=row.get("gender", ""),
            case=row.get("case", ""),
            article=row.get("article", ""),
            person=row.get("person", ""),
            prefix=row.get("prefix", ""),
            explanation=row.get("explanation", "")
        )
        result.append(formatted)
    return result
