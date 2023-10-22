from connection_1 import *
from create_db import *


def post_db():
    db = input("Enter New Database Name: ")
    if db_exists(c_db, db):
        print("DB name already exists")
        get_db()
        exit()
    else:
        status = create_db(c_db, db)
        if status:
            print("DB created")
        else:
            print("Unable to create")
        tb = input("Enter New Table Name: ")
        if tb_exists(c_db, db, tb):
            print("Table name already exists")
            get_db()
        else:
            print("table created")
            get_db()


def get_db():
    data = database_list(c_db)
    for i in data:
        print(". " + i)
    db = input("Enter DB Name: ")
    try:
        data = table_list(c_db, db)
        print("Tables: ")
        if not data:
            print("None")
        else:
            for i in data:
                print(". " + i)
        tb = input("Enter Table Name: ")
        data = table_detail(c_db, tb)
        for i in data:
            print(i)
    except mysql.connector.errors.ProgrammingError:
        print("Invalid Entry")


c_db = connect_db()
choice = input("1, Create database \n 2, Show Database")
if choice == "1":
    post_db()
elif choice == "2":
    get_db()


