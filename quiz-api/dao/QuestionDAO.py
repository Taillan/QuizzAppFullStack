from db_connect import db_connection, cur

def saveQuestion(question):
    instruction = f'insert into Question (title,text,position,image) values ("{question.title}","{question.text}","{question.position}","{question.image}")'
    db_connection(instruction)
    return cur.lastrowid

# TODO Manque les possible answer #
def updateQuestion(question, question_id):
    instruction =   f'update Question set title="{question.title}", text="{question.text}", \
                image="{question.image}", position={question.position} where id={question_id}'
    return db_connection(instruction)
    
def getQuestion(position):    
    instruction = f'select * from Question where position={position}'
    return db_connection(instruction).fetchone()

def getAllQuestion():
    instruction = f'select * from Question'
    return db_connection(instruction).fetchall()

def deleteQuestion(id):
    instruction = f'delete from Question where id={id}'
    return db_connection(instruction)