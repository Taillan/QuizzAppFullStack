from db_connect import db_connection

def saveQuestion(question):
    instruction = f'insert into Question(title,text,position,image) values ("{question.title}","{question.text}","{question.position}","{question.image}")'
    return db_connection(instruction)

# TODO Manque les possible answer #
def updateQuestion(question, question_id):
    instruction =   f'update Question set title="{question.title}", text="{question.text}", \
                image="{question.image}", position={question.position} where id={question_id}'
    return db_connection(instruction)
    
def getQuestion(id):    
    instruction = f'select title,text,position,image from Question where id={id}'
    return db_connection(instruction, False)

def deleteQuestion(id):
    instruction = f'delete from Question where id={id}'
    return db_connection(instruction)