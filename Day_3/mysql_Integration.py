import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root123',
    database = 'school'
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM students")

# for row in cursor.fetchall():
#     print(row)

print(cursor.fetchall())

cursor.close()
conn.close()