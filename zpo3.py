## 10.03.2026
## Zadania - Wzorce krecyjne - wyklad 2
# https://github.com/betacord/ZPO/blob/main/2_creational_patterns.ipynb

#zad 2
# CZĘŚĆ B

#Utworzyć klasę AnimalFactory, która na podstawie podanego parametru
# (np. "dog", "cat") zwraca obiekt odpowiedniej klasy (Dog, Cat).

from abc import ABC, abstractmethod
from unittest import case


class Animal(ABC):
    @abstractmethod
    def get(self):
        pass

class AnimalFactory(ABC):
    @abstractmethod
    def stworz(self) -> Animal:
        pass

class Dog(Animal):
    def get(self)-> str:
        return "Dog"
    def stworz(self):
        return "dog"
class Cat(Animal):
    def get(self)-> str:
        return "Cat"
    def stworz(self):
        return "Cat"
    def stworz(self):
        return "cat"

class DogFactory(AnimalFactory):
    def stworz(self)-> Animal:
        return Dog()

class CatFactory(AnimalFactory):
    def stworz(self)-> Animal:
        return Cat()


class Factory:
    _factories: dict

    def __init__(self) -> None:
        self._factories = {
            "dog": Dog,
            "cat": Cat,
        }

    def stworz(self, type_: str) -> Animal:
        return self._factories[type_]().stworz()

print("CZĘŚĆ B - zad2")
fabryka = Factory()
pies = fabryka.stworz("dog")
print(pies)
kot = fabryka.stworz("cat")
print(kot)
# mysz = fabryka.stworz("mysz") # erorr bo nie ma w slowniku

# CZĘŚĆ C
# Rozbuduj przygotowane implementacje Metody Wytwórczej, tak aby
# mogły obsługiwać dynamiczne rejestrowanie nowych klas zamiast
# statycznych instrukcji warunkowych.

class Mysz(Animal):
    def get(self)-> str:
        return "mysz"

class MyszFactory(AnimalFactory):
    def stworz(self)-> Animal:
        return Mysz()


class DynamicAnimal:
    _factories: dict

    def __init__(self) -> None:
        self._factories = {
            "dog": Dog,
            "cat": Cat,
        }

    def zarejestruj(self, type: str, fabryka: AnimalFactory) -> None:
        self._factories[type] = fabryka

    def stworz(self, type_: str) -> Animal:
        return self._factories[type_]().stworz()

fabryka2 = DynamicAnimal()
pies = fabryka2.stworz("dog")
print(pies)
kot = fabryka2.stworz("cat")
print(kot)
fabryka2.zarejestruj("mysz", MyszFactory)
mysz1 = fabryka2.stworz("mysz")
print(mysz1)


# ZAD 3 - Fabryka abstrakcyjna
# CZĘŚĆ A
# Utworzyć Fabrykę Abstrakcyjną do produkcji samochodów różnych marek (TeslaFactory, BMWFactory).
# Każda z fabryk powinna produkować dwa typy samochodów według nadwozia: Sedan i SUV.

from dataclasses import dataclass

@dataclass
class Sedan:
    brand: str
    model: str
    color: str
    body_type: str = "sedan"

@dataclass
class SUV:
    brand: str
    model: str
    color: str
    body_type: str = "suv"

class Factory(ABC):
    @abstractmethod
    def produce_suv(self, color: str) -> SUV:
        pass
    @abstractmethod
    def produce_sedan(self, color: str) -> Sedan:
        pass

class TeslaFactory(Factory):
    def produce_suv(self, color: str) -> SUV:
        suv = SUV(color=color, model="Cybertrcuk",brand = "Tesla")
        return suv
    def produce_sedan(self, color: str) -> Sedan:
        sedan = Sedan(color=color, model="Model S", brand="Tesla")
        return sedan


class BMWFactory(Factory):
    def produce_suv(self, color: str) -> SUV:
        return SUV(color=color, model="X5", brand="BMW")

    def produce_sedan(self, color: str) -> Sedan:
        return Sedan(color=color, model="M3", brand="BMW")

class AbstractFactory:
    @staticmethod
    def get_factory(brand: str) -> Factory:
        if brand == "BMW":
            return BMWFactory()
        elif brand == "Tesla":
            return TeslaFactory()
        else:
            raise ValueError("Nie ma fabryki takiej marki")

print("\nZAD3")
print("CZĘŚĆ A")
fabryka_bmw = AbstractFactory.get_factory(brand="BMW")
bmw_1 = fabryka_bmw.produce_suv(color="red")
print(bmw_1)
bmw_2 = fabryka_bmw.produce_sedan(color="blue")
print(bmw_2)
fabryka_tesla = AbstractFactory.get_factory(brand="Tesla")
tesla_1 = fabryka_tesla.produce_sedan(color="Black")
tesla_2 = fabryka_tesla.produce_suv(color="White")
print(tesla_1)
print(tesla_2)

# CZĘŚĆ B
#Do istniejącej implementacji Fabryki Abstrakcyjnej dodać nowy typ pojazdu:
# HatchbackCar, i zaktualizować kod tak, aby obsługiwał nową kategorię.

@dataclass
class HatchbackCar:
    brand: str
    model: str
    color: str
    body_type: str = "hatchback"

class Factory2(ABC):
    @abstractmethod
    def produce_suv(self, color: str) -> SUV:
        pass

    @abstractmethod
    def produce_sedan(self, color: str) -> Sedan:
        pass

    @abstractmethod
    def produce_hatchback(self,color: str) -> HatchbackCar:
        pass

class Tesla2Factory(Factory2):
    def produce_suv(self, color: str) -> SUV:
        suv = SUV(color=color, model="Cybertrcuk", brand="Tesla")
        return suv
    def produce_sedan(self, color: str) -> Sedan:
        sedan = Sedan(color=color, model="Model S", brand="Tesla")
        return sedan
    def produce_hatchback(self,color: str) -> HatchbackCar:
        hatchback = HatchbackCar(color=color, brand="Tesla", model="Tesla XYZ")
        return hatchback

class BMW2Factory(Factory2):
    def produce_suv(self, color: str) -> SUV:
        suv = SUV(color=color, model="X3", brand="BMW")
        return suv
    def produce_sedan(self, color: str) -> Sedan:
        sedan = Sedan(color=color, model="M3", brand="BMW")
        return sedan
    def produce_hatchback(self,color: str) -> HatchbackCar:
        hatchback = HatchbackCar(color=color, brand="BMW", model="Seria 1")
        return hatchback

class AbstractFactory2:
    @staticmethod
    def get_factory(brand: str) -> Factory2:
        if brand == "BMW":
            return BMW2Factory()
        elif brand == "Tesla":
            return Tesla2Factory()
        else:
            raise ValueError("Nie ma fabryki takiej marki")

print("\nCZĘŚĆ B")
nowa_bmw = AbstractFactory2.get_factory(brand="BMW")
bmw_hatchback = nowa_bmw.produce_hatchback(color="pink")
print(bmw_hatchback)

# CZĘŚĆ C
# Zaimplementować Fabrykę Abstrakcyjną do procesu produkcji smartfonów. Każda z fabryk
# powinna produkować dwa typy smartfonów: Apfel i Szajsung i dla każdego z nich modele z
# ostatnich 3 lat. Dodać do utworzonej implementacji trzeci typ smartfonu: MajFon.

@dataclass
class model2026:
    brand: str
    model: str = "17"
    storage: int = 128
@dataclass
class model2025:
    brand: str
    model: str = "16"
    storage: int = 64
@dataclass
class model2024:
    brand: str
    model: str = "15"
    storage: int = 32

class PhoneFactory(ABC):
    @abstractmethod
    def produce_2026(self, storage: int)-> model2026:
        pass
    @abstractmethod
    def produce_2025(self, storage: int)-> model2025:
        pass
    @abstractmethod
    def produce_2024(self, storage: int)-> model2024:
        pass

class ApfelFactory(PhoneFactory):
    def produce_2026(self, storage: int) -> model2026:
        apfel = model2026(brand="Apfel",storage=storage)
        return apfel
    def produce_2025(self, storage: int) -> model2025:
        apfel = model2025(brand="Apfel",storage=storage)
        return apfel
    def produce_2024(self, storage: int) -> model2024:
        apfel = model2024(brand="Apfel",storage=storage)
        return apfel

class SzajsungFactory(PhoneFactory):
    def produce_2026(self, storage: int) -> model2026:
        szajs = model2026(brand="Szajsung",storage=storage)
        return szajs
    def produce_2025(self, storage: int) -> model2025:
        szajs = model2025(brand="Szajsung",storage=storage)
        return szajs
    def produce_2024(self, storage: int) -> model2024:
        szajs = model2024(brand="Szajsung",storage=storage)
        return szajs
class MajFonFactory(PhoneFactory):
    def produce_2026(self, storage: int) -> model2026:
        maj = model2026(brand="MajFon",storage=storage)
        return maj
    def produce_2025(self, storage: int) -> model2025:
        maj = model2025(brand="MajFon",storage=storage)
        return maj
    def produce_2024(self, storage: int) -> model2024:
        maj = model2024(brand="MajFon",storage=storage)
        return maj

class AbstractFactoryPhone:
    @abstractmethod
    def get_factory(brand: str) -> PhoneFactory:
        if brand == "MajFon":
            return MajFonFactory()
        elif brand == "Apfel":
            return ApfelFactory()
        elif brand == "Szajsung":
            return SzajsungFactory()
        else:
            raise ValueError("Nie ma fabryki takiej marki")

print("CZĘŚĆ C")
fabryka_apfel = AbstractFactoryPhone.get_factory(brand="Apfel")
apfel2026 = fabryka_apfel.produce_2026(storage=128)
print(apfel2026)
apfel2025 = fabryka_apfel.produce_2025(storage=256)
print(apfel2025)
apfel2024 = fabryka_apfel.produce_2024(storage=32)
print(apfel2024)
fabryka_majfon = AbstractFactoryPhone.get_factory(brand="MajFon")
majfon2025 = fabryka_majfon.produce_2025(storage=128)
print(majfon2025)