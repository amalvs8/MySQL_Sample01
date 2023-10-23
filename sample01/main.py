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
        get_tb(db)
    else:
        arg = {}
        col = []
        d_type = []
        n = int(input("Enter No. of Columns: "))
        for i in range(n):
            print("Enter Column Name: ")
            col.append(input())
            print("Enter Datatype: str/int ")
            d_type.append(input())
        for i in range(n):
            arg[col[i]] = d_type[i]
        status = create_tb(c_db, tb, arg)
        if status:
            print("Table Created")
            get_tb(db)
        else:
            print("Unable to Create")


def get_db():
    data = database_list(c_db)
    print("___Database___")
    for i in data:
        print(". " + i)
    print("1. Create Database")
    print("2. Show Database")
    choice = input()
    if choice == "1":
        post_db()
    elif choice == "2":
        db = input("Enter DB Name: ")
        if db_exists(c_db, db):
            get_tb(db)
        else:
            print("DB Doesn't Exists")
            get_db()
    else:
        print("Invalid Entry")
        get_db()


def get_tb(db):
    data = table_list(c_db, db)
    print("___Tables___")
    if not data:
        print(None)
    else:
        for i in data:
            print(". " + i)
    print("1. Create Table")
    print("2. Show Table")
    choice = input()
    if choice == "1":
        post_tb(db)
    elif choice == "2":
        tb_detail(db)
    else:
        print("Invalid Entry")
        get_tb(db)


def tb_detail(db):
    tb = input("Enter Table Name: ")
    if tb_exists(c_db, db, tb):
        data = table_detail(c_db, tb)
        if not data:
            print(None)
            exit()
        else:
            for i in data:
                print(i)
    else:
        print("Table doesn't Exists")
        get_tb(db)


c_db = connect_db()
get_db()
print("hhhhh")