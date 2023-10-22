import mysql.connector


def connect_1(arg):
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="kl39r059708031994",
      database=arg
    )
    return mydb
