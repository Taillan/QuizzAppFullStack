from db_connect import get_db_connection

def saveQuestion(question):
    db = get_db_connection()
    insertion_result = db.execute( 
        f"insert into Question values"
        f"('{question.title}')"
        f"('{question.text}')"
        f"('{question.position}')"
        f"('{question.image}')"
    )
    db.close()
    