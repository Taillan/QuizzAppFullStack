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