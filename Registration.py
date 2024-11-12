from dbConnection import *

class Registration:
    def check(self, email, password):
        # Sprawdzanie, czy użytkownik istnieje w bazie
        connection = create_connection()
        cursor = connection.cursor()
        
        cursor.execute('SELECT * FROM users WHERE email = %s AND password = %s', (email, password))
        user = cursor.fetchone()
        
        cursor.close()
        connection.close()
        
        return user is not None  # Zwraca True, jeśli użytkownik istnieje

    def register(self, email, password):
        # Rejestracja nowego użytkownika
        connection = create_connection()
        cursor = connection.cursor()
        
        try:
            cursor.execute('INSERT INTO users (email, password) VALUES (%s, %s)', (email, password))
            connection.commit()
            print("Rejestracja zakończona pomyślnie!")
        except Error as e:
            print(f"Błąd przy rejestracji: {e}")
        finally:
            cursor.close()
            connection.close()
