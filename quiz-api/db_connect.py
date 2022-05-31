from audioop import mul
import sqlite3

database = "database.db"

def db_connection(instruction, multiple=True):
    try:
        #création d'un objet connection
        db = sqlite3.connect(database)

        sql_result = db.execute(instruction)
        if multiple:
            result = sql_result.fetchall()
        else:
            result = sql_result.fetchone()
        db.commit()
        # set the sqlite connection in "manual transaction mode"
        # (by default, all execute calls are performed in their own transactions, not what we want)
        db.isolation_level = None
        db.close()
        return result
    except sqlite3.Error as er:
        print("error : ", er)