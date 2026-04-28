#27.04.2025
#Lab 10
#Wzorce czynnościowe
# Strategia
# Zad 1
# CZĘŚĆ A
# Strategia
print("ZAD 1 - CZĘŚĆ A")
# Zaimplementować system obliczania podatku od wartości
# towarów dla różnych krajów, stosując wzorzec strategii.

from abc import ABC, abstractmethod

class TaxStrategy(ABC):
    @abstractmethod
    def calulate_tax(self, price: float):
        pass

class PolandTaxStrategy(TaxStrategy):
    def calulate_tax(self, price: float) -> float:
        return price * 0.23
class UsaTaxStrategy(TaxStrategy):
    def calulate_tax(self, price: float) -> float:
        return price * 0.12
class GermanTaxStrategy(TaxStrategy):
    def calulate_tax(self, price: float) -> float:
        return price * 0.19

class TaxCalculator:
    def __init__(self,strategy: TaxStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: TaxStrategy):
        self.strategy = strategy

    def calculate_tax(self,price:float)->float:
        tax = self.strategy.calulate_tax(price)
        total = price + tax
        return total

calculator_pl = TaxCalculator(PolandTaxStrategy())
calculator_us = TaxCalculator(UsaTaxStrategy())
calculator_de = TaxCalculator(GermanTaxStrategy())

cena = 100
print(f"Produkt wart {cena} w Polsce z podatkiem kosztuje:",calculator_pl.calculate_tax(cena))
print(f"Produkt wart {cena} w USA z podatkiem kosztuje:",calculator_us.calculate_tax(cena))
print(f"Produkt wart {cena} w Niemczech z podatkiem kosztuje:",calculator_de.calculate_tax(cena))

# CZĘŚĆ B
# Stworzyć trywialną grę, w której różne typy postaci
# używają odmiennych strategii ataku, np. agresywny, defensywny,
# chybił-trafił.

print("\nCZĘŚĆ B")
from random import choice

class PlayerStrategy(ABC):
    def __init__(self):
        self.power = None
        self.name = None
        self.a = None

    @abstractmethod
    def hit(self):
        pass

class AtackerStrategy(PlayerStrategy):
    def __init__(self):
        super().__init__()
        self.power = 100
        self.name = "Ronaldo"
    def hit(self) -> str:
        return f"Ja, {self.name} uderzam w trybie agresywnym z mocą {self.power}"

class DefenderStrategy(PlayerStrategy):
    def __init__(self):
        super().__init__()
        self.power = 10
        self.name = "Ramos"
    def hit(self):
        return f"Ja, {self.name} uderzam w trybie defensynym z mocą {self.power}"

class LuckyStrategy(PlayerStrategy):
    def __init__(self):
        super().__init__()
        self.power = 1000
        self.name = "Dawid Jańczyk"
    def hit(self):
        return f"Ja, {self.name} uderzam na chybił trafił z mocą {self.power}"

class StrategyChooser:
    def __init__(self,strategy: PlayerStrategy = None):
        self.strategy = strategy
        self.strategies = [AtackerStrategy(),DefenderStrategy(),LuckyStrategy()]

    def use_strategy(self):
        if self.strategy:
            print(self.strategy.hit())
            return

        print(choice(self.strategies).hit())


chooser = StrategyChooser()
chooser.use_strategy()

# CZĘŚĆ C
print("\nCZĘŚĆ C")
# Przygotować implementację przeznaczoną do sortowania
# wektora wartości liczbowych, który automatycznie dobiera
# metodę sortowania jako strategię.

class SortStrategy(ABC):
    @abstractmethod
    def sort(self,data):
        pass

class BubbleSortStrategy(SortStrategy):
    def sort(self,data):
        print(f"Posortowano Bubble Sortem wektor {data}")
        return sorted(data)

class InserSortStrategy(SortStrategy):
    def sort(self,data):
        print(f"Posortowano Insert Sortem wektor {data}")
        return sorted(data)

class BogoSortStrategy(SortStrategy):
    def sort(self,data):
        print(f"Posortowano Bogo Sortem wektor {data}")
        return sorted(data)

class SortStrategyChooser:
    def __init__(self, strategy: SortStrategy= None):
        self.strategy = strategy
        self.strategies = [BubbleSortStrategy(),InserSortStrategy(),BogoSortStrategy()]
    def sort(self,data):
        if not self.strategy:
            selected_strategy = choice(self.strategies)
        else:
            selected_strategy = self.strategy

        return selected_strategy.sort(data)

wektor = [2,1,3,7,6,9]
sort = SortStrategyChooser()
print(sort.sort(wektor))

# ZAD 2
# CZĘŚĆ A
print("\nZAD 2 - CZĘŚĆ A")
# Iterator (+ generator)
# Zaimplementować iterator do poruszania się
# po elementach wektora w odwrotnej kolejności

from typing import Generator

class VectorIterator:
    def __init__(self,vector):
        self.vector = vector
        self.index = len(vector)-1

    def __iter__(self):
        return self
    def __next__(self):
        if self.index < 0:
            raise StopIteration
        value = self.vector[self.index]
        self.index -= 1
        return value

wektor2 = [2, 1, 3, 7, 6, 9]
iterator = VectorIterator(wektor2)
for _ in range(len(wektor2)):
    print(iterator.__next__())

# CZĘŚĆ B
# Stworzyć system zarządzania zamówieniami,
# który pozwala iterować po zamówieniach według
# statusu (np. nowe, w realizacji, zrealizowane).

