from connection_1 import *
from addition import *


mydb = connect_1("mydatabase")
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
for i in mycursor:
  print(i[0])
#
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")
for i in mycursor:
  print(i[0])

mycursor = mydb.cursor()
mycursor.execute("select * from class")
for i in mycursor:
  print(i)

# mycursor.execute('INSERT INTO class VALUES (150, "Geo", 50, "F")')
# mydb.commit()
# mycursor.execute("select * from class")
# for i in mycursor:
#   print(i)

mycursor.execute('SELECT * FROM class WHERE stud_age=22 AND stud_gender="M";')
for i in mycursor:
  print(i)

mycursor.execute('SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA=DATABASE()AND TABLE_NAME="class"')
for i in mycursor:
  print(i)
# mycursor = mydb.cursor()
# mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")