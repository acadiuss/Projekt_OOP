import tkinter as tk
from tkinter import messagebox
from dbConnection import create_connection
import Registration
import Login

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Panel Rejestracji i Logowania")
        self.root.geometry("300x250")

        # Etykieta powitalna
        self.label = tk.Label(root, text="Wybierz opcję:", font=("Arial", 14))
        self.label.pack(pady=10)

        # Przycisk Rejestracja
        self.register_button = tk.Button(root, text="Rejestracja", command=self.open_registration)
        self.register_button.pack(pady=5)

        # Przycisk Logowanie
        self.login_button = tk.Button(root, text="Logowanie", command=self.open_login)
        self.login_button.pack(pady=5)

    def open_registration(self):
        # Nowe okno do rejestracji
        self.registration_window = tk.Toplevel(self.root)
        self.registration_window.title("Rejestracja")
        self.registration_window.geometry("300x200")

        tk.Label(self.registration_window, text="Email:").pack(pady=5)
        self.email_entry = tk.Entry(self.registration_window)
        self.email_entry.pack(pady=5)

        tk.Label(self.registration_window, text="Hasło:").pack(pady=5)
        self.password_entry = tk.Entry(self.registration_window, show="*")
        self.password_entry.pack(pady=5)

        tk.Button(self.registration_window, text="Zarejestruj się", command=self.register_user).pack(pady=10)

    def open_login(self):
        # Nowe okno do logowania
        self.login_window = tk.Toplevel(self.root)
        self.login_window.title("Logowanie")
        self.login_window.geometry("300x200")

        tk.Label(self.login_window, text="Email:").pack(pady=5)
        self.login_email_entry = tk.Entry(self.login_window)
        self.login_email_entry.pack(pady=5)

        tk.Label(self.login_window, text="Hasło:").pack(pady=5)
        self.login_password_entry = tk.Entry(self.login_window, show="*")
        self.login_password_entry.pack(pady=5)

        tk.Button(self.login_window, text="Zaloguj się", command=self.login_user).pack(pady=10)

    def register_user(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        # Wywołanie klasy Registration
        registration = Registration()
        try:
            registration.register(email, password)
            messagebox.showinfo("Rejestracja", "Rejestracja zakończona pomyślnie!")
            self.registration_window.destroy()
        except Exception as e:
            messagebox.showerror("Błąd", f"Rejestracja nie powiodła się: {e}")

    def login_user(self):
        email = self.login_email_entry.get()
        password = self.login_password_entry.get()

        # Wywołanie klasy Login
        login = Login()
        if login.check(email, password):
            messagebox.showinfo("Logowanie", "Logowanie udane!")
            self.login_window.destroy()
        else:
            messagebox.showerror("Błąd", "Logowanie nieudane. Sprawdź swoje dane.")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
