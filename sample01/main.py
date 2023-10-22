from connection_1 import *

c_db = connect_db()
data = database_list(c_db)
for i in data:
    print(". " + i[0])
db = input("Enter DB Name: ")
# try:
data = database_detail(c_db, db)
print("Tables: ")
for i in data:
    print(". " + i[0])
tb = input("Enter Table Name: ")
data = table_detail(c_db, tb)
for i in data:
    print(i)
# except mysql.connector.errors.ProgrammingError:
#     print("Invalid Entry")
