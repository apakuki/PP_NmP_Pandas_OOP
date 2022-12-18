import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='udemy_python'
)

# cursor that communicates with the database server (DBMS)
my_cursor = mydb.cursor()

# my_cursor.execute('UPDATE student SET age=50 WHERE name="Kevin"')
# mydb.commit()

my_cursor.execute('SELECT * FROM student')
result = my_cursor.fetchall()

for row in result:
    print(row)







