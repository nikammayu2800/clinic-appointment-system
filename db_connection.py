import mysql.connector

def connect_db():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root1234',
            database='clinic_db'
        )
        print("connection check :", connection)
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
