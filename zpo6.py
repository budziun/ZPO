# 31.03.2026
# LAB6
# Wzorce strukturalne
# Dekorator
# ZAD 2
# CZĘŚĆ A
# Utworzyć dekoratory, które dodają dodatkowe uprawnienia użytkownikowi,
# np. "Admin", "Moderator", "Guest", rozszerzając bazową klasę User.
import sqlite3
from abc import ABC, abstractmethod
from typing import Any

class AbstractUser(ABC):
    @abstractmethod
    def login_user(self):
        pass

class User(AbstractUser):
    def __init__(self, login, password):
        self.login = login
        self.password = password
    def login_user(self):
        login = self.login
        return f"Zalogowano użytkownika: {login}"

class Decorator:
    def __init__(self, obj: Any) -> None:
        self.object = obj

    @abstractmethod
    def login_with_role(self):
        pass

class UserDecorator(Decorator):
    def __init__(self, obj: Any) -> None:
        super().__init__(obj)
        self.object = obj

    def add_role_Admin(self):
        self.role = "Admin"

    def add_role_Mod(self):
        self.role = "Moderator"

    def add_role_Guest(self):
        self.role = "Guest"

    def login_with_role(self):
        parent_value = self.object.login_user()
        role = self.role
        return f"Zalogowano użytkownika: {parent_value}, rola {role}"

print("CZĘŚĆ A")
uzytkownik1 = User(login="admin",password="admin")
print(uzytkownik1.login_user())
admin = UserDecorator(uzytkownik1)
admin.add_role_Admin()
print(admin.login_with_role())
uzytkownik2 = User(login="janex",password="zaq1@WSX")
uzytkownik2 = UserDecorator(uzytkownik2)
uzytkownik2.add_role_Mod()
print(uzytkownik2.login_with_role())
gosc = User(login="cozagosc",password="")
gosc = UserDecorator(gosc)
gosc.add_role_Guest()
print(gosc.login_with_role())

print("CZĘŚĆ B")
# Utworzyć dekorator, który automatycznie sprawdza poprawność argumentów
# przekazywanych do funkcji obsługujących formularze użytkownika.

class Form(ABC):
    def __init__(self, form):
        pass
    @abstractmethod
    def send_form(self):
        pass

class UserForm(Form):
    def __init__(self, name: str, phone_number: int, email: str, are_you_agree: bool):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.are_you_agree = are_you_agree

    def send_form(self):
        name = self.name
        phone_number = self.phone_number
        email = self.email
        are_you_agree = self.are_you_agree
        return f"Wysłano formularz\nImie: {name}, Nr telefonu: {phone_number}, Email: {email}, Czy zgadzam się na przechowanie moich danych w bazie: {are_you_agree}"

form1 = UserForm("Jakub", 666666666, "email@email.com", True)
print(form1.send_form())


class Decorator(ABC):
    def __init__(self, form_obj: Form):
        self._form = form_obj

    @abstractmethod
    def send_form(self) -> str:
        return self._form.send_form()

class FormValidateDecorator(Decorator):
    def send_form(self) -> str:
        if "@" not in self._form.email or self._form.email == "":
            return "\nNieprawidłowy adres email"

        if not self._form.are_you_agree:
            return "\nMusisz wyrazić zgodę na przetwarzanie danych"

        if len(self._form.name) == 0:
            return "\nPole login nie może być puste"

        phone_str = str(self._form.phone_number)
        if len(phone_str) == 0 or len(phone_str) > 9:
            return "\nNumer telefonu nie moze byc pusty lub wiekszy niz 9 cyfr"

        original_response = self._form.send_form()

        return f"\nFormularz Poprawny\n{original_response}"

form_no_name = UserForm("",512300300,"email@mail",True)
validate_form = FormValidateDecorator(form_no_name)
print(validate_form.send_form())
form_wrong_number = UserForm("adsad",51230030021331231,"email@mail",True)
validate_form2 = FormValidateDecorator(form_wrong_number)
print(validate_form2.send_form())
form_bad_mail = UserForm("dsdad",512300300,"",True)
validate_form3 = FormValidateDecorator(form_bad_mail)
print(validate_form3.send_form())
form_no_aggre = UserForm("WWW",512300300,"email@mail",False)
validate_form4 = FormValidateDecorator(form_no_aggre)
print(validate_form4.send_form())
validate_form5 = FormValidateDecorator(form1)
print(validate_form5.send_form())

#CZĘŚĆ C
print("\nCZĘŚĆ C")
# Przygotować dekorator, który dodaje logowanie czasu wykonania każdej transakcji
# na bazie danych, bez modyfikacji oryginalnych metod.

from time import time

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def disconnect(self):
        pass
    @abstractmethod
    def query(self):
        pass

class SQLDatabase(Database):
    def connect(self) -> str:
        return "Połączono z SQL"
    def disconnect(self) -> str:
        return "Rozłączono z SQL"
    def query(self) -> str:
        return "Wykonano zapytanie SQL"


sql = SQLDatabase()
print(sql.connect())
print(sql.query())
print(sql.disconnect())


def timeit(fn: callable) -> callable:
    def wrapper(*args: list) -> str:
        start = time()
        result = fn(*args)
        stop = time()

        print(stop - start)

        return result

    return wrapper

class SQLtime:
    @timeit
    def connect(self) -> str:
        return "Połączono z SQL"
    @timeit
    def disconnect(self) -> str:
        return "Rozłączono z SQL"
    @timeit
    def query(self) -> str:
        return "Wykonano zapytanie SQL"

print("\nSQLtime: ")
print(SQLtime().connect())
print(SQLtime().query())
print(SQLtime().disconnect())