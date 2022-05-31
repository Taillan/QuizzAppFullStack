from models.Question import Question
from dao.QuestionDAO import saveQuestion, getQuestion, updateQuestion, deleteQuestion
from dao.PossibleAnswersDAO import deletePossibleAnswers, savePossibleAnswers, getPossibleAnswers
from services.PossibleAnswersServices import PossibleAnswersFromJson, PossibleAnswersFromSQL

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

def UpdateQuestionService(question_id, payload):
    question = QuestionFromJson(payload)
    updateQuestion(question, question_id)

def DeleteQuestionService(question_id):
    deleteQuestion(question_id)
    deletePossibleAnswers(question_id)
    
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