# Aim
# Write a Python program that reads data from an API and inserts it into a SQL database.
import mysql.connector
import requests

# API URL to fetch cryptocurrency prices
API_URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana,cardano,dogecoin&vs_currencies=usd"

# Database Configuration
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "testdb"
}

def fetch_crypto():
    """Fetch cryptocurrency prices from CoinGecko API"""
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data")
        return {}

def insert_crypto(data):
    """Insert or update cryptocurrency prices in MySQL"""
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    sql = """
    INSERT INTO crypto_prices (coin_name, price_usd)
    VALUES (%s, %s)
    ON DUPLICATE KEY UPDATE price_usd = VALUES(price_usd)
    """

    values = [(coin, data[coin]["usd"]) for coin in data]

    cursor.executemany(sql, values)
    connection.commit()
    
    print(f"{cursor.rowcount} records inserted/updated.")
    
    cursor.close()
    connection.close()

# Fetch and insert data
crypto_data = fetch_crypto()
if crypto_data:
    insert_crypto(crypto_data)