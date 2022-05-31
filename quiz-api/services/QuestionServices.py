from models.Question import Question, PossibleAnswers
from dao.QuestionDAO import savePossibleAnswers, saveQuestion, getQuestion, getPossibleAnswers, updateQuestion

def NewQuestionService(payload):
    question = QuestionFromJson(payload)
    possibleAnswers = PossibleAnswersFromJson(payload)
    saveQuestion(question)
    savePossibleAnswers(possibleAnswers, payload['position'])

def GetQuestionService(id):
    question = QuestionFromSQL(getQuestion(id))
    answers = PossibleAnswersFromSQL(getPossibleAnswers(id))
    question.possibleAnswers = answers
    return question

def QuestionFromSQL(payload):
    try:
        title = payload[0]
    except:
        return "Missing title"
    try:
        text = payload[1]
    except:
        return "Missing text"
    try:
        position = payload[2]
    except:
        return "Missing title"
    try:
        image = payload[3]
    except:
        image = "falseb64imagecontent"
    return Question(title, text, position, image)

def UpdateQuestionService(payload):
    question = QuestionFromJson(payload)
    updateQuestion(question)

def DeleteQuestionService(question_id):
    deleteQuestion(question_id)
    
def QuestionFromJson(payload):    
    try:
        title = payload['title']
    except:
        return "Missing title field"
    try:
        text = payload['text']
    except:
        return "Missing text field"
    try:
        position = payload['position']
    except:
        return "Missing position field"
    try:
        image = payload['image']
    except:
        image = "falseb64imagecontent"
    return Question(title, text, position, image)

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
            isCorrect = element['isCorrect'] == "True"
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
