import mysql.connector
import csv
import uuid

def connect_db():
    """Connects to the MySQL database server."""
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="tus"  
        )
    except mysql.connector.Error as err:
        return None

def create_database(connection):
    """Creates the database ALX_prodev if it does not exist."""
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
    cursor.close()

def connect_to_prodev():
    """Connects to the ALX_prodev database."""
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="tus", 
            database="ALX_prodev"
        )
    except mysql.connector.Error as err:
        return None

def create_table(connection):
    """Creates the user_data table."""
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_data (
            user_id VARCHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL NOT NULL,
            INDEX (user_id)
        )
    """)
    print("Table user_data created successfully")
    cursor.close()

def insert_data(connection, data_file):
    """Inserts data from a CSV file into the database."""
    cursor = connection.cursor()
    with open(data_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute("""
                INSERT IGNORE INTO user_data (user_id, name, email, age)
                VALUES (%s, %s, %s, %s)
            """, (row['user_id'], row['name'], row['email'], row['age']))
    connection.commit()
    cursor.close()