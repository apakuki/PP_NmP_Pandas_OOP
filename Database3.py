import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='udemy_python'
)

# cursor that communicates with the database server (DBMS)
my_cursor = mydb.cursor()

# sql_statement = 'INSERT INTO student(name, age, address) VALUES(%s, %s, %s)'
# values = ('Kevin', 34, '50447, 180 Jenna Lane')

# my_cursor.execute(sql_statement, values)
# mydb.commit()
my_cursor.execute('SELECT * FROM student')
result = my_cursor.fetchall()

for row in result:
    print(row)





