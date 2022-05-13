import sqlite3

database = "database.db"

def get_db_connection():
    #création d'un objet connection
    db_connection = sqlite3.connect(database)
    # set the sqlite connection in "manual transaction mode"
    # (by default, all execute calls are performed in their own transactions, not what we want)
    db_connection.isolation_level = None
    return db_connection
