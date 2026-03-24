#17.03.2026
# LAB4

#ZAD 4 - Prototyp
# CZĘŚĆ A
# Stworzyć klasę CharacterPrototype, która umożliwia klonowanie postaci w grze,
# a następnie utworzyć konkretne postaci: Mage, Warrior.

from copy import copy, deepcopy

from dateutil.utils import today
from numpy.ma.core import getdata


class Character:
    name: str
    age: int
    lvl: int
    type1: str
    def __init__(self, name, age, lvl, type1, **kwargs: dict):
        self.name = name
        self.age = age
        self.lvl = lvl
        self.type1 = type1
        for key in kwargs:
            setattr(self, key, kwargs[key])

    def __str__(self) -> str:
        summary = []

        for key, val in vars(self).items():
            summary.append(f"{key}: {val}\n")

        return "".join(summary)

print("ZAD1\nCZĘŚĆ A")
charakter1= Character(
    name="Jan",age=40,lvl=1,type1="npc" )
print(charakter1)

class CharacterPrototype:
    def __init__(self) -> None:
        self.objects = dict()
    def add_prototype(self, id_: int, obj) -> None:
        self.objects[id_] = obj
    def del_prototype(self, id_: int) -> None:
        del self.objects[id_]
    def clone(self, id_: int, **kwargs: dict):
        if id_ in self.objects:
            instance = deepcopy(self.objects[id_])

            for key in kwargs:
                setattr(instance, key, kwargs[key])

            return instance
        else:
            raise ModuleNotFoundError("ID not found!")

prototype = CharacterPrototype()
prototype.add_prototype(1, charakter1)
mag = prototype.clone(1, lvl=1, type1="Mage", age= 67)
print(mag)
prototype.add_prototype(2, mag)
warrior = prototype.clone(2, lvl=111, type1="Warrior")
print(warrior)

#CZĘŚĆ B
print("CZĘŚĆ B")
# Zaimplementować wzorzec Prototyp, a następnie przetestować różnice
# między płytkim a głębokim kopiowaniem wewnątrz.

class Prototyp:
    def __init__(self) -> None:
        self.objects = dict()

    def add_prototype(self, id_: int, obj) -> None:
        self.objects[id_] = obj

    def del_prototype(self, id_: int) -> None:
        del self.objects[id_]

    def clone(self, id_: int, **kwargs: dict):
        if id_ in self.objects:
            instance = copy(self.objects[id_])

            for key in kwargs:
                setattr(instance, key, kwargs[key])

            return instance
        else:
            raise ModuleNotFoundError("ID not found!")

    def deep_clone(self, id_: int, **kwargs: dict):
        if id_ in self.objects:
            instance = deepcopy(self.objects[id_])

            for key in kwargs:
                setattr(instance, key, kwargs[key])

            return instance
        else:
            raise ModuleNotFoundError("ID not found!")

class Character2:
    name: str
    age: int
    lvl: int
    type1: str
    eq = []
    def __init__(self, name, age, lvl, type1, eq, **kwargs: dict):
        self.name = name
        self.age = age
        self.lvl = lvl
        self.type1 = type1
        self.eq = eq
        for key in kwargs:
            setattr(self, key, kwargs[key])
    def __str__(self) -> str:
        summary = []

        for key, val in vars(self).items():
            summary.append(f"{key}: {val}\n")

        return "".join(summary)

compare= Character2(
    name="TEST",age=22,lvl=111,type1="Rycerz",eq=["miecz","tarcza"])
print(compare)
prototype_compare = Prototyp()
prototype_compare.add_prototype(3, compare)
compare_basic = prototype_compare.clone(3, name="Plytkie")
print(compare_basic)
prototype_compare.add_prototype(4, compare_basic)
compare_deep = prototype_compare.deep_clone(4,name="Glebokie")
print(compare_deep)

# CZĘŚĆ C
# tworzyć klasę Configuration zawierającą ustawienia pewnej aplikacji i zastosować wzorzec Prototyp tak,
# aby można było tworzyć kopie konfiguracji i je modyfikować niezależnie od oryginału.

class Configuration:
    def __init__(self,volume,language,font,login,password,lastUsed,**kwargs: dict):
        self.volume = volume
        self.language = language
        self.font = font
        self.login = login
        self.password = password
        self.lastUsed = lastUsed
        for key in kwargs:
            setattr(self, key, kwargs[key])

    def __str__(self) -> str:
        summary = []

        for key, val in vars(self).items():
            summary.append(f"{key}: {val}\n")

        return "".join(summary)

print("CZĘŚĆ C")
pycharm = Configuration(volume=30,language="pl",font=("Arial",20),login="admin",password="admin",lastUsed=getdata(today()))
print(pycharm)

class Prototyp_app:
    def __init__(self) -> None:
        self.objects = dict()
    def add_prototype(self, id_: int, obj) -> None:
        self.objects[id_] = obj
    def clone(self, id_: int, **kwargs: dict):
        instance = copy(self.objects[id_])

        for key in kwargs:
            setattr(instance, key, kwargs[key])

        return instance

prototyp_app = Prototyp_app()
prototyp_app.add_prototype(1, pycharm)
webstorm = prototyp_app.clone(1, volume=67,font=("Arial",32),login="webadmin",password="frontas123")
print(webstorm)
prototyp_app.add_prototype(2, webstorm)
postgresql = prototyp_app.clone(2,volume=0,language='en',login="postgres",password="baza123",lastUsed=getdata(today()))
print(postgresql)

# ZAD 5 - Singleton
# CZĘŚĆ A
# Zaimplementować Singleton DatabaseConnection, który zapewni,
# że dana aplikacja będzie używać tylko jednej instancji połączenia z bazą danych.

print("ZAD 5\nCZĘŚĆ A")

from typing_extensions import Self

class DatabaseConnection:
    _instance: Self = None

    def __new__(cls, * args: list,**kwargs: dict) -> Self:
        if cls._instance is None:
            instance = super().__new__(cls, *args, **kwargs)
            cls._instance = instance

        return cls._instance

con1 = DatabaseConnection()
con2 = DatabaseConnection()
print(con1 is con2)
print(con2 is con1)
# CZĘŚĆ B
# Zmodyfikować istniejącą implementację Singletona tak,
# aby umożliwić jednorazowe ustawienie parametrów konfiguracji,
# ale później uniemożliwić ich zmianę.

print("\nCZĘŚĆ B")

class Singleton:
    _instance: Self = None
    _instance_max_change: int = 0

    def __new__(cls, *args: list, **kwargs: dict) -> Self:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    def __init__(self, value: str = "first value"):
        if self._instance_max_change == 0:
            self._instance = self
            self._instance_max_change = 1
            print(value)
        else:
            print("nie mozna zmienic ustawien singlethona, jest juz obiekt utworzony")

ust1 = Singleton("pierwsza konfiguracja ok")
ust2 = Singleton("druga konfiguracja ok?")
print(ust1 is ust2)
print(ust1)
print(ust2)
