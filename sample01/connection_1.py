import mysql.connector


def connect_db():
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="kl39r059708031994",
    )
    return mydb


def get_database(c_db, db):
    db_cursor = c_db.cursor()
    db_cursor.execute("USE " + db)
    db_cursor.execute("SHOW TABLES;")
    return db_cursor


def get_table(c_db, tb):
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
