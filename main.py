from dbConnection import create_connection
import Registration
from Login import *


def main():
    
        print("Sprawdzam polaczenie z baza danych . . . ")
        dbConnection= create_connection()
        
        print("Wybierz opcję:")
        print("1 - Rejestracja")
        print("2 - Logowanie")
        action = input("Podaj numer opcji: ")

        if action == '1':
            # Rejestracja nowego użytkownika
            registration = Registration()
            email = input("Podaj email do rejestracji: ")
            password = input("Podaj hasło do rejestracji: ")
            registration.register(email, password)
        elif action == '2':
            # Tworzenie instancji klasy Login i logowanie
            osoba = Login()
            osoba.log()
        else:
            print("Niepoprawny wybór. Wybierz 1 dla rejestracji lub 2 dla logowania.")


if __name__ == "__main__":
    main()