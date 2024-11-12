import mysql.connector
from mysql.connector import Error

# Funkcja do połączenia z bazą danych MySQL
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',       # Użyj localhost lub 127.0.0.1
            database='user_db',
            user='root',   # Wprowadź swoją nazwę użytkownika
            password='' # Wprowadź swoje hasło
        )
        if connection.is_connected():
            print("Połączono z bazą danych MySQL")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None
    
