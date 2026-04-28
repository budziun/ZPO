#27.04.2025
#Lab 10
#Wzorce czynnościowe
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
print("\nCZĘŚĆ B")

from enum import Enum
from typing import List

class Stan(Enum):
    NOWE = "nowe"
    W_REALIZACJI = "w realizacji"
    ZREALIZOWANE = "zrealowane"

class Order:
    def __init__(self,order_id: int, stan: Stan):
        self.order_id = order_id
        self.stan = stan
    def __str__(self):
        return f"Zamówienie o ID:{self.order_id} ma status {self.stan.value}"

class OrderIterator:
    def __init__(self,orders: List[Order], stan: Stan):
        self.orders = orders
        self._obecny_stan = stan
        self._index = 0

    def __iter__(self):
        return self
    def __next__(self):
        while self._index < len(self.orders):
            order = self.orders[self._index]
            self._index += 1
            if order.stan == self._obecny_stan:
                return order

        raise StopIteration()

class OrderManagmentSystem:
    def __init__(self):
        self.orders: List[Order] = []
    def add_order(self, order: Order):
        self.orders.append(order)
    def get_orders(self, stan: Stan) -> OrderIterator:
        return OrderIterator(self.orders, stan)

system = OrderManagmentSystem()
system.add_order(Order(1,Stan(Stan.NOWE)))
system.add_order(Order(2,Stan(Stan.ZREALIZOWANE)))
system.add_order(Order(3,Stan(Stan.NOWE)))
system.add_order(Order(4,Stan(Stan.W_REALIZACJI)))

system_iterator_new = system.get_orders(Stan(Stan.NOWE))

for order in system_iterator_new:
    print(order)

system_iterator_closed = system.get_orders(Stan(Stan.ZREALIZOWANE))
system_iterator_current = system.get_orders(Stan(Stan.W_REALIZACJI))

for order in system_iterator_current:
    print(order)

for order in system_iterator_closed:
    print(order)

# CZĘŚĆ C
# Stworzyć generator, który będzie zwracał kolejne elementy
# ciągu harmonicznego. Generator skończy zwracać wartości gdy wartość
# w mianowniku wyniesie wartość przekazaną jako parametr funkcji
# generatora.
print("\nCZĘŚĆ C")

from typing import Generator

def harmon_generator(value):
    n = 1
    while True:
        wynik = 1/n
        if wynik < value:
            break
        yield wynik
        n += 1

h = harmon_generator(0.07)

for n in h:
    print(n)

# Metoda Szablonowa
# ZAD 3
# CZĘŚĆ A
# Przygotować schematyczne rozwiązanie do przetwarzania dokumentów
# w różnych formatach (np. PDF, DOCX, TXT), wykorzystując metodę
# szablonową do definiowania wspólnego schematu ich przetwarzania.
print("\nZAD 3 - CZĘŚĆ A")

class Document(ABC):
    def __init__(self,name:str):
        self.name = name
    @abstractmethod
    def get_document(self):
        pass
    @abstractmethod
    def extract_document(self):
        pass
    @abstractmethod
    def validate_document(self):
        pass
    @abstractmethod
    def format_document(self):
        pass
    @abstractmethod
    def save_document(self):
        print(f"Zapisano dokument jako {self.name}")

    def document_procesing(self):
        self.get_document()
        self.extract_document()
        self.validate_document()
        self.format_document()
        self.save_document()
        print()

class PDF(Document):
    def __init__(self,name:str):
        super().__init__(name)
        self.name = name
    def get_document(self):
        print("Otworzno dokument PDF")
    def extract_document(self):
        print("Rozpoznano dane za pomocą OCR")
    def validate_document(self):
        print("Zwalidowano dane w dokumencie przy uzyciu Adobe")
    def format_document(self):
        print("Sformatowano dokument do rozmiaru A4")
    def save_document(self):
        print(f"Zapisano dokument {self.name}.pdf")

class DOCX(Document):
    def __init__(self,name:str):
        super().__init__(name)
        self.name = name
    def get_document(self):
        print("Otworzno dokument DOCX")
    def extract_document(self):
        print("Rozpoznano dane za pomocą NLP")
    def validate_document(self):
        print("Zwalidowano dane przy uzyciu Word.exe")
    def format_document(self):
        print("Sformatowano dokument do rozmiaru A5")
    def save_document(self):
        print(f"Zapisano dokument {self.name}.docx")

class TXT(Document):
    def __init__(self,name:str):
        super().__init__(name)
        self.name = name
    def get_document(self):
        print("Otworzno dokument TXT")
    def extract_document(self):
        print("Rozpoznano dane przy uzyciu COPILOT AI MICROSOFT")
    def validate_document(self):
        print("Zwaldiowano przy użciu Notatnik COPILOT EDITION")
    def format_document(self):
        print("Sformatowano dokument do COPILOT AI")
    def save_document(self):
        print(f"Zapisano dokument {self.name}.txt")

pdf = PDF(name="lab1")
word = DOCX("cw1")
txt = TXT("asbufabsuifas")

pdf.document_procesing()
word.document_procesing()
txt.document_procesing()

# CZĘŚĆ B
# Zaprojektować schematyczny system obsługi zamówień,
# w którym metoda szablonowa określa proces realizacji zamówienia,
# a szczegóły zależą od podklasy (np. dostawa standardowa, ekspresowa,
# odbiór osobisty).

class Order(ABC):
    def __init__(self,order_id: int):
        self.order_id = order_id
    @abstractmethod
    def get_order(self):
        pass
    @abstractmethod
    def package_order(self):
        pass
    @abstractmethod
    def ready_to_claim(self):
        pass
    @abstractmethod
    def collected(self):
        pass
    def ship(self):
        pass
    def quality_control(self):
        pass
    def in_transit(self):
        pass

    def deliver(self):
        if StandardDelivery:
            self.get_order()
            self.package_order()
            self.quality_control()
            self.ship()
            self.in_transit()
            self.ready_to_claim()
            self.collected()
        elif ExpressDelivery:
            self.get_order()
            self.package_order()
            self.ship()
            self.ready_to_claim()
            self.collected()
        elif PersonalDelivery:
            self.get_order()
            self.package_order()
            self.ready_to_claim()
            self.collected()
        print()

class StandardDelivery(Order):
    def __init__(self,order_id:int):
        super().__init__(order_id)
        self.order_id = order_id
    def get_order(self):
        print(f"Wpłyneło zamówienie o id:{self.order_id}")
    def package_order(self):
        print(f"Spakowano zamówienie ID:{self.order_id}")
    def quality_control(self):
        print(f"Zamówienie ID {self.order_id} przeszło przez kontrole jakości")
    def ship(self):
        print(f"Wysłano zamówienie ID:{self.order_id} kurierem")
    def in_transit(self):
        print(f"Zamówienie w trasie")
    def ready_to_claim(self):
        print(f"Zamówienie ID:{self.order_id} gotowe do odbioru")
    def collected(self):
        print(f"Odebrano zamówienie ID:{self.order_id}")

class ExpressDelivery(Order):
    def __init__(self,order_id:int):
        super().__init__(order_id)
        self.order_id = order_id
    def get_order(self):
        print(f"Wpłyneło zamówienie o id:{self.order_id}")
    def package_order(self):
        print(f"Spakowano zamówienie ID:{self.order_id}")
    def ship(self):
        print(f"Wysłano zamówienie ID:{self.order_id} kurierem")
    def ready_to_claim(self):
        print(f"Zamówienie ID:{self.order_id} gotowe do odbioru")
    def collected(self):
        print(f"Odebrano zamówienie ID:{self.order_id}")

class PersonalDelivery(Order):
    def __init__(self,order_id:int):
        super().__init__(order_id)
        self.order_id = order_id
    def get_order(self):
        print(f"Wpłyneło zamówienie o id:{self.order_id}")
    def package_order(self):
        print(f"Spakowano zamówienie ID:{self.order_id}")
    def ready_to_claim(self):
        print(f"Zamówienie ID:{self.order_id} gotowe do odbioru")
    def collected(self):
        print(f"Odebrano zamówienie ID:{self.order_id}")

order1 = StandardDelivery(101)
order1.deliver()

order2 = PersonalDelivery(22)
order2.deliver()

order3 = ExpressDelivery(33)
order3.deliver()

# CZĘŚĆ C
print("CZĘŚĆ C")
# Utworzyć schematyczną aplikację przeznaczoną do eksportowania
# danych w różnych formatach (np. CSV, JSON, XML), w której
# metoda szablonowa definiuje podstawowy proces generowania pliku.

class FileType(ABC):
    def __init__(self,name:str):
        self.name = name
    @abstractmethod
    def save(self):
        pass
    @abstractmethod
    def render(self):
        pass
    @abstractmethod
    def encode(self):
        pass
    @abstractmethod
    def saved_file(self):
        pass
    def save_as(self):
        self.encode()
        self.render()
        self.save()
        self.saved_file()
        print()

class CSV(FileType):
    def __init__(self,name:str):
        super().__init__(name)
        self.name = name

    def encode(self):
        print("Zakodowano plik w UTF-8")
    def render(self):
        print("Uruchomiono rendering na CPU")
    def save(self):
        print("Zapisywanie do pliku CSV")
    def saved_file(self):
        print(f"Zapisano jako {self.name}.csv")

class XML(FileType):
    def __init__(self,name:str):
        super().__init__(name)
        self.name = name

    def encode(self):
        print("Zakodowano plik w HEX")
    def render(self):
        print("Uruchomiono render na RAMie")
    def save(self):
        print("Zapisywanie do pliku XML")
    def saved_file(self):
        print(f"Zapisano jako {self.name}.xml")

class JSON(FileType):
    def __init__(self,name:str):
        super().__init__(name)
        self.name = name
    def encode(self):
        print("Zakodowano plik w binarnym ciągu")
    def render(self):
        print("GPU Render obiektów")
    def save(self):
        print("Zapisywanie do pliku JSON")
    def saved_file(self):
        print(f"Zapisano jako {self.name}.json")

csv = CSV("dane1")
json = JSON("api_dzik")
xml = XML("geodezja_dane2026")

csv.save_as()
json.save_as()
xml.save_as()
