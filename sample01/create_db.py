from connection_1 import *


def db_exists(c_db, db):
    data = database_list(c_db)
    if db in data:
        return True
    return False


def tb_exists(c_db, db, tb):
    data = table_list(c_db, db)
    if tb in data:
        return True
    return False


def create_db(c_db, db):
    cursor_db = c_db.cursor()
    try:
        cursor_db.execute("CREATE DATABASE " + db)
        return True
    except mysql.connector.errors.ProgrammingError:
        return False

