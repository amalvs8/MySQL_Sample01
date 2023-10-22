import mysql.connector


def connect_db():
    c_db = mysql.connector.connect(
      host="localhost",
      user="root",
      password="kl39r059708031994",
    )
    return c_db


def database_list(c_db):
    cursor_db = c_db.cursor()
    cursor_db.execute("SHOW DATABASES;")
    data = []
    for i in cursor_db:
        data.append(i)
    return data

def database_detail(c_db, db):
    cursor_db = c_db.cursor()
    cursor_db.execute("USE " + db + ";")
    cursor_db.execute("SHOW TABLES;")
    data = []
    for i in cursor_db:
        data.append(i)
    return data
    return data

def table_detail(c_db, tb):
    column = []
    data = []
    cursor_db = c_db.cursor()
    cursor_db.execute(
        'SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS '
        'WHERE TABLE_SCHEMA=DATABASE() AND TABLE_NAME="{}";'.format(tb)
    )
    for i in cursor_db:
        column.append(i[0])
    cursor_db.execute("SELECT * FROM " + tb + ";")
    for i in cursor_db:
        di = {}
        for j in range(len(i)):
            di[column[j]] = i[j]
        data.append(di)
    return data
