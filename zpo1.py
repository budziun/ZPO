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
        super().__init__(first_name,last_name,salary)
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
Transaction = namedtuple("Transaction", ["transaction_id", "amount", "currency"])

tranzakcja1 = Transaction(transaction_id=1, amount=100.00, currency="PLN")

class BankAccount:
    def __init__(self, balance: float):
        self.balance = balance

    def get_balance(self) -> float:
        return self.balance

    def apply_transaction(self, transaction: Transaction) -> None:
        self.balance -= transaction.amount


konto = BankAccount(balance=1000.00)

print(konto.balance)
konto.apply_transaction(tranzakcja1)
print(konto.balance)
konto.apply_transaction(tranzakcja1)
print(konto.balance)

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

#ZAD10
# Utworzyć klasę Robot z metodą operate(), zwracającą "Performing task", oraz AI z metodą think(),
# zwracającą "Processing data". Następnie utworzyć klasę Android, która dziedziczy po obu
# i dodaje własną metodę self_learn().

class Robot:
    def operate(self)-> str:
        return "Performing task"

class AI:
    def think(self)-> str:
        return "Processing data"

class Android(Robot, AI):
    def self_learn(self)-> str:
        return "Self learning"

print("ZAD10")
andoird = Android()
print(andoird.operate())
print(andoird.think())
print(andoird.self_learn())

#ZAD11
#Stworzyć klasę TemperatureConverter, która będzie zawierać metody statyczne
# celsius_to_fahrenheit() oraz fahrenheit_to_celsius().

class TemperatureConverter:
    value : float

    def __init__(self, value: float) -> None:
        self.value = value

    def value(self):
        return self.value

    @staticmethod
    def celcius_to_fahrenheit(value: float) -> float:
        return value * 9 / 5 + 32
    @staticmethod
    def fahrenheit_to_celcius(value: float) -> float:
        return round((value - 32 )/1.8,2)

print("\nZAD11")
celcius = TemperatureConverter(36)
print(celcius.value)
print(celcius.celcius_to_fahrenheit(celcius.value))
far = TemperatureConverter(100)
print(far.value)
print(far.fahrenheit_to_celcius(far.value))

#ZAD12
#Przygotować klasę IDGenerator z metodą klasową generate_id(),
# która automatycznie generuje unikalne identyfikatory dla obiektów.
# Każdy nowo utworzony obiekt powinien otrzymać kolejny numer ID.

class IDGenerator:
    amount = 0

    def __init__(self) -> None:
        self.id = IDGenerator.generate_id()

    @classmethod
    def generate_id(cls) -> int:
        cls.amount +=1
        return cls.amount

print("\nZAD12")
obiekt1 = IDGenerator()
obiekt2 = IDGenerator()
obiekt3 = IDGenerator()

print("Obiekt 3:",obiekt3.id)
print("Obiekt 1:",obiekt1.id)
print("Obiekt 2:",obiekt2.id)

#ZAD13
# Utworzyć klasę Store z atrybutem klasowym total_customers oraz metodą add_customer(),
# zwiększającą wartość tego atrybutu. Dodać metodę klasową get_total_customers(),
# która zwróci liczbę klientów.

class Store:
    total_customers = 0

    @classmethod
    def get_total_customers(cls) -> int:
        return cls.total_customers

    @classmethod
    def add_customers(cls) -> None:
        cls.total_customers += 1

print("\nZAD13")
print(Store.get_total_customers())
Store.add_customers()
print(Store.get_total_customers())

#ZAD14
#Stworzyć klasę MathOperations zawierającą zarówno metody statyczne (add(), multiply())
# jak i metody klasowe (identity_matrix(cls, size), tworzącą macierz jednostkową [size x size]).

import numpy as np

class MathOperations:
    @staticmethod
    def add(a : int,b : int) -> int:
        return a+b
    @staticmethod
    def multiply(a : int,b : int)-> int:
        return a*b
    @classmethod
    def identity_matrix(cls,size):
        return np.eye(size)

print("\nZAD14")
print(MathOperations.add(2,2))
print(MathOperations.multiply(2,200))
print(MathOperations.identity_matrix(3))

#ZAD 15
# Utworzyć klasę GameCharacter, która ma atrybut klasowy default_health=100 oraz metodę
# restore_health(), ustawiającą zdrowie obiektu na wartość domyślną. Dodać metodę klasową
# set_default_health(cls, new_value), pozwalającą na zmianę domyślnego zdrowia dla wszystkich postaci.

class GameCharacter:
    default_health = 100

    def restore_health(self) -> None:
        self.health = GameCharacter.default_health

    @classmethod
    def set_default_health(cls,new_value):
        cls.default_health = new_value

    def __init__(self, health: int) -> None:
        self.health = health

print("\nZAD15")
bohater1 = GameCharacter(67)
bohater2 = GameCharacter(33)
bohater3 = GameCharacter(21)
print(bohater1.health)
print(bohater2.health)
print(bohater3.health)

bohater1.restore_health()
print("\nnowe hp bohater1: ",bohater1.health)
GameCharacter.set_default_health(200)
bohater2.restore_health()
bohater3.restore_health()
print("\nbohater2 hp:",bohater2.health)
print("bohater3 hp:",bohater3.health)

# ZAD 16
# Stworzyć klasę abstrakcyjną Shape z metodą abstrakcyjną area().
# Następnie utworzyć klasy Circle i Rectangle, implementujące metodę area().

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> str:
        pass

class Cicle(Shape):
    def area(self) -> str:
        return "Kształt koło"

class Rectangle(Shape):
    def area(self) -> str:
        return "Kształt prostokąt"

kolo = Cicle()
prostokat = Rectangle()

print("\nZAD16")
print(kolo.area())
print(prostokat.area())


# ZAD 17
# Zaimplementować klasę abstrakcyjną PaymentProcessor z metodami authorize_payment() i capture_payment().
# Następnie utworzyć klasy CreditCardPayment i PayPalPayment, implementujące te metody na różne sposoby.

class PaymentProcessor(ABC):
    @abstractmethod
    def authorize_payment(self)-> str:
        return "Autoryzacja"
    def capture_payment(self) -> str:
        return "Zarejestrowano płatność"

class CreditCardPayment(PaymentProcessor):
    def authorize_payment(self) -> str:
        return "Sprawdzanie CVV karty"
    def capture_payment(self) -> str:
        return "Zarejestrowano płatność kartą"

class PayPalPayment(PaymentProcessor):
    def authorize_payment(self) -> str:
        return "Logowanie do PayPal"
    def capture_payment(self) -> str:
        return "Zapłacono z  PayPal"

karta1 = CreditCardPayment()
paypal1 = PayPalPayment()

print("\nZAD17")
print(karta1.authorize_payment())
print(karta1.capture_payment())
print(paypal1.authorize_payment())
print(paypal1.capture_payment())
#test = PaymentProcessor() # blad nie mozna utworzyc z klasy abstrackycjnej obiektu,
# moglem dac pass metody w klasie abstrakcyjnej

#ZAD18
# Utworzyć klasę abstrakcyjną Vehicle z metodą max_speed(),
# a następnie stworzyć klasy Car i Bicycle, definiującą ich maksymalną prędkość.


class Vehicle(ABC):
    @abstractmethod
    def max_speed(self) -> int:
        pass

class Car(Vehicle):
    def max_speed(self) -> int:
        return 220

class Bicycle(Vehicle):
    def max_speed(self) -> int:
        return 35

auto = Car()
bicycle = Bicycle()
print("\nZAD18")
print(auto.max_speed())
print(bicycle.max_speed())
#ZAD19
# Przygotować klasę abstrakcyjną DatabaseConnection z metodami connect() i execute_query().
# Utworzyć klasy MySQLConnection oraz PostgreSQLConnection, implementujące te metody na różne sposoby.

class DatabaseConnection(ABC):
    @abstractmethod
    def connect(self) -> None:
        pass
    @abstractmethod
    def execute_query(self) -> None:
        pass

class MySQLConnection(DatabaseConnection):
    def connect(self) -> str:
        return "połączono z bazą danych MySQL"
    def execute_query(self) -> str:
        return  "Wykonano zapytanie do bazy danych MySQL"

class PostgreSQLConnection(DatabaseConnection):
    def connect(self) -> str:
        return "Połączono z bazą danych PostgreSQL"
    def execute_query(self) -> str:
        return "Wykonano zapytanie do bazy PostgreSQL"

mysql = MySQLConnection()
sql = PostgreSQLConnection()
print("\nZAD19")
print(mysql.connect())
print(mysql.execute_query())
print(sql.connect())
print(sql.execute_query())

#ZAD20
# Utworzyć klasę abstrakcyjną Instrument z metodą play(),
# a następnie zaimplementować klasy Piano i Guitar, które będą miały różne wersje tej metody

class Instrument(ABC):
    @abstractmethod
    def play(self)-> str:
        pass

class Piano(Instrument):
    def play(self)-> str:
        return "Do re mi fa so la si do"

class Guitar(Instrument):
    def play(self)-> str:
        return "Gitara ma strun wiele, struna miłości gra jej na czele"

pianino = Piano()
gitara_siema = Guitar()

print("\nZAD20")
print(pianino.play())
print(gitara_siema.play())
