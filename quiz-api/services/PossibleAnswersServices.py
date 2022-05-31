
from models.PossibleAnswers import PossibleAnswers

def PossibleAnswersFromJson(payload):
    answers = []
    try:
        possibleAnswers = payload['possibleAnswers']
    except:
        return "Missing possibleAnswers field"
    for element in possibleAnswers:
        try:
            text = element['text']
        except:
            return "Missing text field"
        try:
            isCorrect = element['isCorrect']
        except:
            return "Missing isCorrect field or not a bool"
        answers.append(PossibleAnswers(text, isCorrect))
    return answers

def PossibleAnswersFromSQL(payload):
    answers = []
    for element in payload:
        try:
            text = element[0]
        except:
            return "Missing text field"
        try:
            isCorrect = element[1] == "True"
        except:
            return "Missing isCorrect field"
        answers.append(PossibleAnswers(text, isCorrect))
    return answers
