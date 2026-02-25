#ZAD1
class Employee:
    first_name: str
    last_name: str
    salary: float
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
    def get_full_name(self)->str:
        return f"{self.first_name} {self.last_name}"


prac1 = Employee("Jakub","Budzich",300.00)
print(prac1.get_full_name())
class Manager(Employee):
    department: str
    def __init__(self, first_name, last_name, department, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.department = department

    def get_department_info(self)->str:
        return f"{self.department}"

prac2 = Manager("Bakub","Judzich","WMII",30000.00)
print(prac2.get_department_info())

#ZAD2
# Utworzyć klasę Transaction jako namedtuple zawierającą transaction_id, amount oraz currency.
# Następnie zdefiniować klasę BankAccount, która będzie miała atrybut balance oraz metodę
# apply_transaction(), przyjmującą obiekt Transaction i modyfikującą saldo.

from collections import namedtuple
Transcation = namedtuple("Transcation", ["transcation_id", "amount", "currency"])

tranzakcja1 = Transcation(transcation_id=1, amount=100.00, currency="PLN")
print(tranzakcja1.transcation_id)

class BankAccount(Transcation):
    balance: float

    def __new__(Bank, transaction_id, amount, currency, balance):
        self = super(BankAccount, Bank).__new__(Bank, transaction_id, amount, currency)
        self.balance = balance
        return self

    def apply_transaction(self, transaction: Transcation)->None:
        self.balance -= transaction.amount
        return self.balance



b1 = BankAccount(transaction_id=2, amount=10.0, currency="PLN", balance=200.0)

print(b1.balance)
b1.apply_transaction(tranzakcja1)
print(b1.balance)

#ZAD3
#Napisać klasę Book używając dataclass, która zawiera title, author, year, price.
# Dodaj metodę apply_discount(), która obniży cenę książki o podany procent.

from dataclasses import dataclass, field

@dataclass
class Book:
    title: str
    author: str
    year: int
    price: float

    def apply_discount(self,discount: float)-> None:
        discount = discount / 100
        self.price -= self.price * discount
        return self.price

ksiazka1 = Book("Tytul1", "Autor1", 2026, 200.0)
print("Cena ksiazki: ",ksiazka1.price)
ksiazka1.apply_discount(23.00)
print(ksiazka1.price)

#ZAD4
#Stworzyć klasę Product jako dataclass zawierającą name, price, category, a następnie rozszerz
# ją o walidację ceny (powinna być większa od zera) oraz domyślną wartość category="General".

@dataclass
class Product:
    name: str
    price: float
    category: str = field(default="General")

    def __post_init__(self):
        if self.price <= 0:
            raise ValueError(f"Cena musi być większa od zera {self.price}")

produkt = Product(name="produkt1", price=100.00)
print(produkt.category)
produkt2 = Product(name="produkt2", price=-100.00)
print(produkt2.price)

#ZAD5


