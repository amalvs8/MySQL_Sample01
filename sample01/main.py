from connection_1 import *


c_db = connect_db()
db = input("Enter DB Name: ")
# try:
data = get_database(c_db, db)
print("Tables: ")
for i in data:
    print(". " + i[0])
tb = input("Enter Table Name: ")
data = get_table(c_db, tb)
for i in data:
    print(i)
# except mysql.connector.errors.ProgrammingError:
#     print("Invalid Entry")
