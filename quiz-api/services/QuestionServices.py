from models.Question import Question
from dao.QuestionDAO import *
from services.PossibleAnswersServices import *
from errors import NotFound
from db_connect import cur

def NewQuestionService(payload):
    question = QuestionFromJson(payload)
    question_id = saveQuestion(question)
    NewPossibleAnswersService(payload, question_id)
    return id

def GetQuestionService(position):
    sql_result = getQuestion(position)

    if sql_result == None:
        raise NotFound

    question = QuestionFromSQL(sql_result)
    answers = GetPossibleAnswersService(question.id)
    question.possibleAnswers = answers
    return question

def GetAllQuestionService():
    questions = AllQuestionFromSQL(getAllQuestion())
    for question in questions:
        answers = GetPossibleAnswersService(question.id)
        question.possibleAnswers = answers
    return questions

def UpdateQuestionService(question_id, payload):
    question = QuestionFromJson(payload)

    original = GetQuestionService(question_id)

    if question.position != original.position:
        print("olalala je dois changer les pos")

    updateQuestion(question, question_id)

    UpdatePossibleAnswerService(question_id, payload)

    return question_id

def DeleteQuestionService(question_id):
    deleteQuestion(question_id)

    if cur.rowcount == 0:
        raise NotFound
        
    DeletePossibleAnswerService(question_id)
    
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
        image = ""
    return Question(title, text, position, image)

def QuestionFromSQL(payload):
    try:
        id = payload[0]
    except:
        return "Missing id"
    try:
        title = payload[1]
    except:
        return "Missing title"
    try:
        text = payload[2]
    except:
        return "Missing text"
    try:
        position = payload[3]
    except:
        return "Missing title"
    try:
        image = payload[4]
    except:
        image = "falseb64imagecontent"
    return Question(title, text, position, image, id)

def AllQuestionFromSQL(payload):
    questions = []
    for question in payload:
        questions.append(QuestionFromSQL(question))
    return questions