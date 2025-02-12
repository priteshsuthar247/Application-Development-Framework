# Aim
# Write a Python program that retrieves data from a SQL database and saves it as a CSV file.

import mysql.connector
from mysql.connector import Error

connection = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='root',
            database='testdb'
        )
cursor = connection.cursor()
query = "SELECT * FROM STORE"
cursor.execute(query)
results = cursor.fetchall()
for row in results:
    print(row)
cursor.close()

file = open("")