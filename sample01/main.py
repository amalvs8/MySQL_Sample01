from create_db import *


def post_db():
    db = input("Enter New Database Name: ")
    if db_exists(c_db, db):
        print("DB name already exists")
    else:
        status = create_db(c_db, db)
        if status:
            print("DB Created")
            get_db()
        else:
            print("Unable to Create")


def post_tb(db):
    tb = input("Enter New Table Name: ")
    if tb_exists(c_db, db, tb):
        print("Table name already exists")
        get_db()
    else:
        arg = {}
        col = []
        d_type = []
        n = int(input("Enter No. of Columns: "))
        for i in range(n):
            print("Enter Column Names: ")
            col.append(input())
            print("Enter Datatype: str/int ")
            d_type.append(input())
        for i in range(n):
            arg[col[i]] = d_type[i]
        status = create_tb(c_db, tb, arg)
        if status:
            print("Table Created")
        else:
            print("Unable to Create")


def get_db():
    data = database_list(c_db)
    for i in data:
        print(". " + i)
    db = input("Enter DB Name: ")
    try:
        print("1. Create Table")
        print("2. Show Table")
        choice = input()
        if choice == "1":
            post_tb(db)
        elif choice == "2":
            data = table_list(c_db, db)
            print("Tables: ")
            if not data:
                print(None)
                exit()
            else:
                for i in data:
                    print(". " + i)
            tb = input("Enter Table Name: ")
            data = table_detail(c_db, tb)
            if not data:
                print(None)
                exit()
            else:
                for i in data:
                    print(i)
        else:
            print("Invalid Entry")

    except mysql.connector.errors.ProgrammingError:
        print("Invalid Entry")


c_db = connect_db()
print("1. Create Database")
print("2. Show Database")
ch = input()
if ch == "1":
    post_db()
elif ch == "2":
    get_db()
else:
    print("Invalid Entry")