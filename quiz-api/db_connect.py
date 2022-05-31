from audioop import mul
import sqlite3

database = "database.db"

try:
    #création d'un objet connection
    con = sqlite3.connect(database, check_same_thread=False)
    cur = con.cursor()
    # set the sqlite connection in "manual transaction mode"
    # (by default, all execute calls are performed in their own transactions, not what we want)
    con.isolation_level = None
except sqlite3.Error as er:
    print("error : ", er)

def db_connection(instruction):
    try:
        #création d'un objet connection
        sql_result = cur.execute(instruction)            
        con.commit()        
        return sql_result
    except sqlite3.Error as er:
        print("error : ", er)