# 13.04.2026
# LAB7
# Wzorce strukturalne
# Fasada
# ZAD 3
# CZĘŚĆ A

# Przygotować klasę fasady, która upraszcza operacje
# na plikach (zapis, odczyt, usuwanie), ukrywając
# niskopoziomowe operacje (otwarcie, zamknięcie).

from typing import Any

class Save():
    def __init__(self,filename:str) -> None:
        self.filename = filename
    def save_file(self):
        filename = self.filename
        print(f" Zapisano plik {filename}")

class Read():
    def __init__(self,filename:str) -> None:
        self.filename = filename
    def open_file(self):
        filename = self.filename
        print(f"Otworzono plik {filename}")
    def close_file(self):
        filename = self.filename
        print(f"Zamknięto plik {filename}")

class Delete():
    def __init__(self,filename:str) -> None:
        self.filename = filename
    def delete_file(self):
        filename = self.filename
        print(f"Usunięto plik {filename}")

class file():
    def __init__(self, filename: str):
        self.filename = filename
        self.save_system = Save(filename)
        self.read_system = Read(filename)
        self.delete_system = Delete(filename)

    def usun_plik(self):
        print("\nOperacja usun plik")
        self.read_system.open_file()
        self.delete_system.delete_file()
        self.read_system.close_file()

    def zapisz_plik(self):
        print("\nOperacja zapisz plik")
        self.read_system.open_file()
        self.save_system.save_file()
        self.read_system.close_file()

    def odczytaj_plik(self):
        print("\nOperacja odczytaj plik")
        self.read_system.open_file()
        self.read_system.close_file()

plik = file("plik1")
plik.odczytaj_plik()
plik.zapisz_plik()
plik.usun_plik()

print("\nCZĘŚĆ B")
# część B
#Zaimplementować fasadę dla biblioteki graficznej,
# która zapewnia prostszy interfejs do skalowania,
# zmiany kolorów i kompresji obrazów.

class Graphic_bib():
    def __init__(self,file:str) -> None:
        self.file = file
    def pick_curren_color(self):
        print("Wybrano aktualny kolor")
    def change_color(self):
        print("Zmieniono kolor")
    def zapisz_kolor(self):
        print("Zapisano kolor")
    def wczytaj_obraz(self):
        print("Wczytano obraz")
    def kompresja_png_na_jpg(self):
        print("Skompresowano plik png na jpg")
    def zapisz_obraz(self):
        print("Zapisano obraz")
    def wybierz_figure(self):
        print("Wybrano punkt")
    def zmniejsz_figure(self):
        print("Zmniejsz figure")
    def wyswietl_figure(self):
        print("Wyswietlono figure")

class GUI_bib():
    def __init__(self, filename: str):
        self.filename = filename
        self.operation = Graphic_bib(filename)

    def zmiana_koloru(self):
        print("\nZmiana koloru:")
        self.operation.pick_curren_color()
        self.operation.change_color()
        self.operation.zapisz_kolor()
    def skaluj(self):
        print("\nOperacja skalowanie:")
        self.operation.wybierz_figure()
        self.operation.zmniejsz_figure()
        self.operation.wyswietl_figure()
    def kopmpresja(self):
        print("\nOperacja kopmpresja png na jpg:")
        self.operation.wczytaj_obraz()
        self.operation.kompresja_png_na_jpg()
        self.operation.zapisz_obraz()

gui = GUI_bib("zmiana_koloru")
gui.zmiana_koloru()
gui.skaluj()
gui.kopmpresja()

print("\nCZEŚĆ C")
#CZEŚĆ C
# Utworzyć fasadę do obsługi systemu kolejek (np. RabbitMQ, Kafka),
# która ułatwia wysyłanie i odbieranie wiadomości poprzez wspólny interfejs.

class RabitMQ():
    def __init__(self, message:str) -> None:
        self.message = message
    def send(self):
        print("Wyslano wiadomosc do serwera")
    def server_exchange(self):
        print("Serwer otrzymal wiadomosc, zamiana na token")
    def server_route(self):
        print("Przekazanie wiadomosci za pomoca routingu")
    def queue_decode(self):
        print("Dekodowanie wiadomosci")
    def add_queue(self):
        print("Dodano wiadomosc do kolejki")
    def subscribe_queue(self):
        print("Pobieranie wiadomisci z kolejki")
    def show_message(self):
        print("Odczytanie wiadomosci")

class Kafka():
    def __init__(self, message:str) -> None:
        self.message = message
    def send(self):
        print("Wyslano wiadomosc do serwera")
    def server_get_message(self):
        print("Odczytanie wiadomosci przez serwer")
    def add_queue(self):
        print("Dodano wiadomosc do kolejki na serwerze")
    def subscribe_queue(self):
        print("Pobieranie wiadomisci z kolejki na serwerze")
    def read(self):
        print("Odczytanie wiadomości pobranej z kolejki")

class fasada_programów():
    def __init__(self, message:str) -> None:
        self.message = message
        self.rabit = RabitMQ(message)
        self.kafka = Kafka(message)
    def send_rabit(self):
        print("\nOperacja wysylanie w RabitMQ:")
        self.rabit.send()
        self.rabit.server_exchange()
        self.rabit.server_route()
        self.rabit.add_queue()
    def get_rabit(self):
        print("\nPobranie wiadomosci z kolejki i odczyt za pomocą RabitMQ:")
        self.rabit.subscribe_queue()
        self.rabit.queue_decode()
        self.rabit.show_message()
    def send_kafka(self):
        print("\nOperacja wysylanie w Kafka:")
        self.kafka.send()
        self.kafka.server_get_message()
        self.kafka.add_queue()
    def get_kafka(self):
        print("\nOperacja odbierania wiadomości w Kafka:")
        self.kafka.subscribe_queue()
        self.kafka.read()

kolejki = fasada_programów("wiadomosc 1")
kolejki.send_rabit()
kolejki.get_rabit()
kolejki.send_kafka()
kolejki.get_kafka()

# Wzorce strukturalne
# Kompozyt
#ZAD 4 punkt A
print("\nZAD 4 - PUNKT A")

# Zaimplementować hierarchię obiektów systemu plików w postaci klas File i Directory,
# gdzie katalogi mogą zawierać zarówno pliki, jak i
# inne katalogi, umożliwiając rekursywne operacje.

from abc import ABC, abstractmethod


class Component(ABC):
    def __init__(self, name: str) -> None:
        self.name = name
        self._parent = None

    def add(self, component: "Component") -> None:
        pass

    def remove(self, component: "Component") -> None:
        pass

    def is_composite(self) -> bool:
        return False

    @abstractmethod
    def show_directory(self, indent: int = 0) -> None:
        pass

    @abstractmethod
    def delete(self) -> None:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass


class File(Component):
    def __init__(self, filename: str) -> None:
        super().__init__(filename)
        self.filename = filename

    def show_directory(self, indent: int = 0) -> None:
        print("  " * indent + str(self))

    def delete(self) -> None:
        if self._parent:
            self._parent.remove(self)
        print(f"Usunięto plik: {self.filename}")

    def __str__(self) -> str:
        return f"Plik: {self.filename}"


class Directory(Component):
    def __init__(self, directory: str) -> None:
        super().__init__(directory)
        self.directory = directory
        self.children = []

    def is_composite(self) -> bool:
        return True

    def add(self, component: Component) -> None:
        component._parent = self
        self.children.append(component)

    def remove(self, component: Component) -> None:
        component._parent = None
        self.children.remove(component)

    def show_directory(self, indent: int = 0) -> None:
        print("  " * indent + str(self))
        for item in self.children:
            item.show_directory(indent + 1)

    def delete(self) -> None:
        for item in self.children[:]:
            item.delete()
        self.children.clear()
        if self._parent:
            self._parent.remove(self)
        print(f"Usunięto katalog: {self.directory}")

    def __str__(self) -> str:
        return f"Katalog: {self.directory}"


katalog = Directory("root")
zdjecia = Directory("zdjecia")
muzyka = Directory("muzyka")
katalog.add(zdjecia)
katalog.add(muzyka)
obrazek1 = File("obrazek1.txt")
katalog.add(obrazek1)
obrazek2 = File("dasads")
zdjecia.add(obrazek2)
print("\n")
katalog.show_directory()
zdjecia.delete()
print("\n")
katalog.show_directory()

# CZĘŚĆ B
print("\nCZĘŚĆ B\n")

# Przygotować system, w którym pojedynczy użytkownik
# oraz grupy użytkowników mogą mieć przypisane uprawnienia,
# a grupy mogą zawierać inne grupy.

class Component2(ABC):
    def __init__(self,name: str) -> None:
        self.name = name
        self._parent = None
        self.permissions: set = set()
    def add(self,component: "Component2") -> None:
        pass
    def remove(self,component: "Component2") -> None:
        pass
    def add_permissions(self,perm:str) -> None:
        self.permissions.add(perm)
    def has_permissions(self,perm: str) -> bool:
        return perm in self.permissions
    @abstractmethod
    def show(self,indent: int = 0) -> None:
        pass
    @abstractmethod
    def __str__(self) -> str:
        pass

class User(Component2):
    def __init__(self, name: str) -> None:
        super().__init__(name)
    def show(self,indent: int = 0) -> None:
        perms = ", ".join(self.permissions) if self.permissions else "brak"
        print(" " * indent + str(self) + " " + perms)
    def __str__(self):
        return f"User: {self.name}"

class Group(Component2):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.children: list[Component2] = []
    def add(self,component: Component2) -> None:
        component._parent = self
        self.children.append(component)
    def remove(self,component: Component2) -> None:
        component._parent = None
        self.children.remove(component)
    def add_permissions(self,perm:str) -> None:
        self.permissions.add(perm)
        for child in self.children:
            child.add_permissions(perm)
    def show(self,indent: int = 0) -> None:
        perms = ", ".join(self.permissions) if self.permissions else "brak"
        print(" " * indent + str(self) + " " + perms)
        for child in self.children:
            child.show(indent + 1)
    def __str__(self) -> str:
        return f"Group: {self.name}"

admin = Group("admin")
developer = Group("developer")

jakub = User("jakub")
adam = User("adam")
szymon = User("szymon")

admin.add(developer)
admin.add(jakub)
developer.add(adam)
developer.add(szymon)

admin.add_permissions("delete")
jakub.add_permissions("read")
developer.add_permissions("write")
szymon.add_permissions("read")

admin.show()

print("\nCZĘŚĆ C")
# CZESC C

# Stworzyć system umożliwiający kompozycję raportów finansowych,
# gdzie sekcje raportu mogą zawierać zarówno pojedyncze
# wartości, jak i inne sekcje.

class Component3(ABC):
    def __init__(self,name: str) -> None:
        self.name = name
        self._parent = None

    def add(self,componet: "Component3"):
        pass
    def remove(self,component: "Component3"):
        pass
    @abstractmethod
    def total(self):
        pass
    @abstractmethod
    def show(self,indent: int = 0):
        pass
    @abstractmethod
    def __str__(self) -> str:
        pass

class Value(Component3):
    def __init__(self, name: str, value: float) -> None:
        super().__init__(name)
        self.value = value
    def total(self):
        return self.value
    def show(self,indent: int = 0):
        print("  " * indent + f"{self.name}: {self.value:.2f} PLN")
    def __str__(self):
        return f"{self.name}: {self.value:.2f} PLN"

class Section(Component3):
    def __init__(self, name: str):
        super().__init__(name)
        self.children: list[Component3] = []
    def add(self,component: "Component3"):
        component._parent = self
        self.children.append(component)
    def remove(self,component: "Component3"):
        component._parent = None
        self.children.remove(component)
    def total(self) -> float:
        return sum(child.total() for child in self.children)
    def show(self,indent: int = 0):
        print("  " * indent + f"[{self.name}]  SUMA: {self.total():.2f} PLN")
        for child in self.children:
            child.show(indent + 1)
    def __str__(self):
        return f"Section: {self.name}"

raport = Section("Raport 2025")

przychody = Section("Przychody")
przychody.add(Value("FV Xtraders",120000.00))
przychody.add(Value("Strona fundacja",2137.67))

koszty = Section("Koszty")
koszty.add(Value("Nowy PC",8999.99))
koszty.add(Value("Najem lokalu",30000.00))

raport.add(przychody)
raport.add(koszty)

raport.show()
