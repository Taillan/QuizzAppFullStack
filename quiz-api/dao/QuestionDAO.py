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
    
def savePossibleAnswers(answers, question_id):
    db = get_db_connection()
    insertion_result = db.execute(
        f'insert into PossibleAnswers(question_id,text,isCorrect) values'
        f'("{question_id}",'
        f'"{answers[0].text}",'
        f'"{answers[0].isCorrect}"),'

        f'("{question_id}",'
        f'"{answers[1].text}",'
        f'"{answers[1].isCorrect}"),'

        f'("{question_id}",'
        f'"{answers[2].text}",'
        f'"{answers[2].isCorrect}"),'

        f'("{question_id}",'
        f'"{answers[3].text}",'
        f'"{answers[3].isCorrect}")'
    )
    db.close()
    return "created"

def getQuestion(id):
    db = get_db_connection()
    get_result = db.execute(
        f'select * from Question where position={id}'
    )
    result = get_result.fetchone()
    db.close()
    return result

def getPossibleAnswers(id):
    db = get_db_connection()
    get_result = db.execute(
        f'select text,isCorrect from PossibleAnswers where question_id={id}'
    )
    result = get_result.fetchall()
    db.close()
    return result

def deleteQuestion(int:id):
    db = get_db_connection()
    delete_result = db.execute(
        f'delet from Question where position={id}'
    )
    db.close()