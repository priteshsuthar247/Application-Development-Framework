import mysql.connector
import pandas as pd

# Database Configuration
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "testdb"
}

# Load external data (CSV file) and rename the PRICE_$ column
df = pd.read_csv("07/dataset.csv").rename(columns={"PRICE_$": "PRICE"})

def update_store():
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    # SQL Query: Update only existing records
    sql = """
    UPDATE STORE 
    SET P_NAME = %s, PRICE_$ = %s, P_TYPE = %s 
    WHERE P_ID = %s
    """

    values = [(row.P_NAME, row.PRICE, row.P_TYPE, row.P_ID) for _, row in df.iterrows()]
    
    cursor.executemany(sql, values)

    connection.commit()
    print(f"{cursor.rowcount} records updated.")

    cursor.close()
    connection.close()

# Execute update
update_store()
