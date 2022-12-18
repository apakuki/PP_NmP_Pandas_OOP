import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='udemy_python'
)

# cursor that communicates with the database server (DBMS)
my_cursor = mydb.cursor()

# my_cursor.execute("CREATE TABLE student(name VARCHAR(255), age TINYINT, address VARCHAR(255))")
my_cursor.execute('SHOW TABLES')

for table in my_cursor:
    print(table)
