from connection_1 import *


def db_exists(c_db, db):
    data = database_list(c_db)
    if not data:
        return False
    else:
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


def create_tb(c_db, tb, arg):
    cursor_db = c_db.cursor()
    # try:
    s = ""
    for key, value in arg.items():
        if value.lower() == "int":
            s += f"{key} INT, "
        else:
            s += f"{key} CHAR(100), "
    s = s[:-2]
    print(s)
    cursor_db.execute(
        "CREATE TABLE " + tb + " (id INT PRIMARY KEY, {});".format(s)
    )
    return True
    # except mysql.connector.errors.ProgrammingError:
    #     return False
