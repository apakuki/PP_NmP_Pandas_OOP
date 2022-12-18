import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='your password',
    database='udemy_python'
)

# cursor that communicates with the database server (DBMS)
my_cursor = mydb.cursor()

# my_cursor.execute('CREATE DATABASE udemy_python')