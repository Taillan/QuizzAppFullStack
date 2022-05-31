from requests import request
from db_connect import get_db_connection

def saveQuestion(question):
    db = get_db_connection()
    insertion_result = db.execute(
        f'insert into Question values'
        f'("{question.title}",'
        f'"{question.text}",'
        f'"{question.position}",'
        f'"{question.image}")'
    )
    db.close()

# TODO Manque les possible answer #
def updateQuestion(question):
    db = get_db_connection()
    
    update_result = db.execute(
        f'update Question set '
        f'title="{question.title}",'
        f'text="{question.text}",'
        f'image="{question.image}" where position={question.position}'
    )
    db.close()
    
def getQuestion(int:id):
    db = get_db_connection()
    insertion_result = db.execute(
        f'select * from Question where id={id}'
    )
    db.close()

def deleteQuestion(int:id):
    db = get_db_connection()
    delete_result = db.execute(
        f'delet from Question where position={id}'
    )
    db.close()