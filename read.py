import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='vendas',
)

cursor = connection.cursor()

sql = 'SELECT * from vendas.produtos'

cursor.execute(sql)
results = cursor.fetchall()

cursor.close()
connection.close()

for result in results:
    print(result)