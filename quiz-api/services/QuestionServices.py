from models.Question import Question
from dao.QuestionDAO import saveQuestion

def NewQuestionService(payload):
    question = QuestionFromJson(payload)
    saveQuestion(question)

def GetQuestionService(int:id):
    return 
    
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

