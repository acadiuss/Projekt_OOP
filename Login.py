from Registration import *

class Login(Registration):
    def log(self):
        self.email = input("Podaj email: ")
        self.password = input("Podaj hasło: ")

        # Wywołanie metody check z klasy Registration
        if self.check(self.email, self.password):
            print("Logowanie udane!")
        else:
            print("Logowanie nieudane!")

