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
from pydantic import BaseModel, Field


@dataclass
class Product:
    name: str
    price: float
    category: str = field(default="General")

    def __post_init__(self):
        if self.price <= 0:
            raise ValueError(f"Cena musi być większa od zera a jest {self.price}")

try:
    produkt1 = Product(name="produkt1", price=-1000.00)
except ValueError as e:
    print(e)

produkt2 = Product(name="produkt2", price=1000.00)
print(produkt2.price)
print(produkt2.category)

#ZAD5
# Utworzyć klasę Car z atrybutami brand, model i year. Następnie dodać metodę is_classic(),
# która zwróci True, jeśli samochód ma ponad 25 lat.

class Car:
    brand: str
    model: str
    year: int

    def __init__(self, brand : str, model : str, year : int):
        self.brand = brand
        self.model = model
        self.year = year
    def isClassic(self)-> bool:
        if 2026-self.year > 25:
            return True
        else:
            return False


autko_stare = Car("Fiat", "126p", 1990)
print(f"1990 auto: ",autko_stare.isClassic())
autko_nowe = Car("Tesla","Y", 2020)
print(f"2020 auto: ",autko_nowe.isClassic())

#ZAD6
#Stworzyć klasy ElectricVehicle oraz GasolineVehicle, które mają metodę fuel_type(),
# zwracającą odpowiednio "electric" i "gasoline". Następnie utworzyć klasę HybridCar,
# która dziedziczy po obu i nadpisuje metodę fuel_type(), aby zwracała "hybrid".

class ElectricVehicle:
    def fuel_type(self)-> str:
        return "electric"

class GasolineVehicle:
    def fuel_type(self)-> str:
        return "gasoline"

class HybridCar(ElectricVehicle, GasolineVehicle):
    def fuel_type(self)-> str:
        return "hybrid"

elektryk = ElectricVehicle()
gazolina = GasolineVehicle()
hybryda = HybridCar()
print("Elektryk jeździ na: ",elektryk.fuel_type())
print("Gaziutek jeździ na: ",gazolina.fuel_type())
print("Hybryda jeździ na: ",hybryda.fuel_type())

#ZAD7
#Utworzyć klasę Person z metodą introduce(), zwracającą "I am a person".
# Następnie stworzyć klasy Worker i Student, które dziedziczą po Person i zmieniają tę metodę na "I am a worker"
# oraz "I am a student". Następnie utworzyć klasę WorkingStudent, która dziedziczy zarówno po Worker, jak i Student,
# i sprawdź, jak Python rozwiąże konflikt metod.

class Person:
    name: str
    lastname: str

    def __init__(self, name: str, lastname: str) -> None:
        self.name = name
        self.lastname = lastname
    def introduce(self) -> str:
        return "I am a person"

class Worker(Person):
    def introduce(self) -> str:
        return "I am a worker"

class Student(Person):
    def introduce(self) -> str:
        return "I am a student"

class WorkingStudent(Worker, Student):
    pass

pracujacy_student = WorkingStudent("Jakub", "Budzich")
print(pracujacy_student.introduce())
# Zwróciło że jest Worker

class WorkingStudent2(Student, Worker):
    pass

pracujacy_student2 = WorkingStudent2("Jakub", "Budzich")
print(pracujacy_student2.introduce())
# Zwróciło Student
# Czyli w python pierwsze dziediczenie jest ważniejsze i liczy się po jakiej klasie wpierw dziediczymy.

#ZAD8
# Utworzyć klasy Animal i Pet. Klasa Animal powinna mieć metodę make_sound(),
# zwracającą "Some sound", a Pet powinna mieć metodę is_domestic(), zwracającą True.
# Następnie utworzyć klasę Dog, dziedziczącą po obu, i dostosować metody tak, aby pasowały do psa.

class Animal:
    def make_sound(self) -> str:
        return "Some sound"

class Pet:
    def is_domestic(self) -> bool:
        return True

class Dog(Animal, Pet):
    def make_sound(self) -> str:
        return "Hau Hau Hau"

burek = Dog()
print(burek.make_sound())
print(burek.is_domestic())

#ZAD9
# Zaimplementować klasy FlyingVehicle i WaterVehicle, które mają metody move(),
# zwracające odpowiednio "I fly" oraz "I sail". Następnie stworzyć klasę AmphibiousVehicle,
# która łączy obie i pozwala na wybór trybu działania.

class FlyingVehicle:
    def move(self)-> str:
        return "I fly"

class WaterVehicle:
    def move(self)-> str:
        return "I sail"

class AmphibiousVehicle(FlyingVehicle, WaterVehicle):
    mode: str

    def __init__(self, mode: str) -> None:
        self.mode = mode

    def move(self) -> str:
        if self.mode == "Water":
            return WaterVehicle.move(self)
        elif self.mode == "Air":
            return FlyingVehicle.move(self)


samolot = AmphibiousVehicle("Air")
lodka = AmphibiousVehicle("Water")
print(samolot.move())
print(lodka.move())
