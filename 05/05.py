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
query1 = "SELECT * FROM STORE;"
cursor.execute(query1)
results1 = cursor.fetchall()


   

query2 = "desc STORE;"
cursor.execute(query2)
results2 = cursor.fetchall()
header=[]
for row in results2:
    header.append(row[0])

print(header)
file = open("05\\dataset.csv",'w+',newline='')

import csv

csv_writer = csv.writer(file)

csv_writer.writerow(header)
csv_writer.writerows(results1)
