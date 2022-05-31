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

def getQuestion(int:id):
    db = get_db_connection()
    insertion_result = db.execute(
        f'select * from Question where id={id}'
    )
    db.close()

def deleteQuestion(int:id):
    db = get_db_connection()
    delete_result = db.execute(
        f'delet from Question where id={id}'
    )
    db.close()