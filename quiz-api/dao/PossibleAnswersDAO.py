from db_connect import db_connection

def savePossibleAnswers(answers, question_id):
    instruction = (
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
    return db_connection(instruction)

def getPossibleAnswers(id):
    instruction = f'select text,isCorrect from PossibleAnswers where question_id={id}'
    return db_connection(instruction)

def deletePossibleAnswers(id):
    instruction = f'delete from PossibleAnswers where question_id={id}'
    return db_connection(instruction)