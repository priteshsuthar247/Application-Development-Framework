# Aim
# Build a web application that queries a SQL database and displays the results on a web page.
from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Database Configuration
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "testdb"
}

def get_data():
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM STORE")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data

@app.route("/")
def index():
    data = get_data()
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
