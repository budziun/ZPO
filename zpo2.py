## 3.03.2026
## Zadania - Wzorce krecyjne - wyklad 2
# https://github.com/betacord/ZPO/blob/main/2_creational_patterns.ipynb

# ZAD1 - Budowniczy
# punkt A

print("ZAD1")
print("\nCZĘŚĆ A")
# Przygotować klasę Pizza, która będzie mogła zawierać różne składniki (ser, salami, pieczarki, cebula itd.).
# Zastosować wzorzec budowniczego, aby umożliwić stopniowe dodawanie składników do pizzy.

from abc import ABC, abstractmethod

class BuilderPizza():
    ingredients = []

    @abstractmethod
    def dodaj_ser(self) -> None:
        pass
    @abstractmethod
    def dodaj_pieczarki(self) -> None:
        pass
    @abstractmethod
    def dodaj_cebula(self) -> None:
        pass
    @abstractmethod
    def dodaj_salami(self) -> None:
        pass
    @abstractmethod
    def dodaj_rukola(self) -> None:
        pass

class Pizza(BuilderPizza):
    ingredients = []

    def __init__(self,ingredients):
        self.ingredients = ingredients
    def dodaj_ser(self) -> None:
        self.ingredients.append("Ser")
    def dodaj_pieczarki(self) -> None:
        self.ingredients.append("Pieczarki")
    def dodaj_cebula(self) -> None:
        self.ingredients.append("Cebula")
    def dodaj_salami(self) -> None:
        self.ingredients.append("Salami")
    def dodaj_rukola(self) -> None:
        self.ingredients.append("Rukola")


pizza1 = Pizza([])
print(pizza1.ingredients)
pizza1.dodaj_ser()
print(pizza1.ingredients)
pizza1.dodaj_pieczarki()
print(pizza1.ingredients)
pizza1.dodaj_salami()
print(pizza1.ingredients)
pizza1.dodaj_rukola()
print(pizza1.ingredients)
pizza1.dodaj_cebula()
print(pizza1.ingredients)

# Punkt B

# Rozszerzyć istniejącą implementację budowniczego tak, aby umożliwić budowanie
# różnych wariantów obiektów (np. dla pizzy vege, mięsnej, serowej, itd.).


class BuilderPizza2():
    ingredients = []

    @abstractmethod
    def dodaj_ser(self) -> None:
        pass
    @abstractmethod
    def dodaj_pieczarki(self) -> None:
        pass
    @abstractmethod
    def dodaj_cebula(self) -> None:
        pass
    @abstractmethod
    def dodaj_salami(self) -> None:
        pass
    @abstractmethod
    def dodaj_rukola(self) -> None:
        pass
    @abstractmethod
    def pizza_vege(self) -> None:
        pass
    @abstractmethod
    def pizza_miesna(self) -> None:
        pass
    @abstractmethod
    def pizza_serowa(self) -> None:
        pass

class Pizza2(BuilderPizza2):
    ingredients = []

    def __init__(self,ingredients):
        self.ingredients = ingredients
    def dodaj_ser(self) -> None:
        self.ingredients.append("Ser")
    def dodaj_pieczarki(self) -> None:
        self.ingredients.append("Pieczarki")
    def dodaj_cebula(self) -> None:
        self.ingredients.append("Cebula")
    def dodaj_salami(self) -> None:
        self.ingredients.append("Salami")
    def dodaj_rukola(self) -> None:
        self.ingredients.append("Rukola")
    def pizza_vege(self) -> None:
        self.dodaj_ser()
        self.dodaj_rukola()
        self.dodaj_pieczarki()
        self.dodaj_cebula()

    def pizza_miesna(self) -> None:
        self.dodaj_ser()
        self.dodaj_pieczarki()
    def pizza_serowa(self) -> None:
        self.dodaj_ser()

print("\nCZĘŚĆ B")
pizza_2 = Pizza2([])
pizza_2.pizza_vege()
print("Pizza vege",pizza_2.ingredients)
pizza_3 = Pizza2([])
pizza_3.pizza_miesna()
print("Pizza miesna",pizza_3.ingredients)
pizza_4 = Pizza2([])
pizza_4.pizza_serowa()
print("Pizza serowa",pizza_4.ingredients)

print("\nCZĘŚĆ C")
# Przygotować klasę Computer, która posiada wiele parametrów przekazywanych w inicjalizatorze.
# Przerobić nastęopnie kod tak, aby zamiast dużego konstruktora użyć wzorca budowniczego

class ComputerBuilder(ABC):
    parts = []

    @abstractmethod
    def dodaj_cpu(self) -> None:
        pass
    @abstractmethod
    def dodaj_gpu(self) -> None:
        pass
    @abstractmethod
    def dodaj_ram(self) -> None:
        pass
    @abstractmethod
    def dodaj_disk(self) -> None:
        pass


class Computer(ComputerBuilder):
    parts = []

    def dodaj_cpu(self, cpu) -> str:
        return self.parts.append(cpu)

    def dodaj_gpu(self, gpu) -> str:
        return self.parts.append(gpu)

    def dodaj_ram(self, ram) -> str:
        return self.parts.append(ram)

    def dodaj_disk(self, disk) -> str:
        return self.parts.append(disk)

    def __init__(self, parts):
        self.parts = parts


komputer1 = Computer([])
print(komputer1.parts)
komputer1.dodaj_cpu("Ryzen 7 7800x3d")
print(komputer1.parts)
komputer1.dodaj_gpu("RTX 5060ti 16GB")
print(komputer1.parts)
komputer1.dodaj_cpu("16 GB DDR5")
print(komputer1.parts)
komputer1.dodaj_disk("Dysk jeden tera, potem mniej")
print(komputer1.parts)

#ZAD2 - Metoda wytwórcza
print("\nZAD2")
print("CZĘŚĆ A")

# Utworzyć interfejs Document i klasy: WordDocument, PDFDocument, a następnie przygotować metodę
# wytwórczą, która decyduje, jaki dokument utworzyć na podstawie zadanego rozszerzenia pliku.

class Document(ABC):
    @abstractmethod
    def get_type(self)-> str:
        pass

class DocumentFactory(ABC):
    @abstractmethod
    def create_document(self) -> Document:
        pass

class WordDocument(Document):
    def get_type(self) -> str:
        return "Utworzono plik Word"
class PDFDocument(Document):
    def get_type(self) -> str:
        return "Utworzono plik PDF"

class WordFactory(WordDocument):
    def create_document(self) -> Document:
        return WordDocument()

class PDFFactory(DocumentFactory):
    def create_document(self) -> Document:
        return PDFDocument()

class FileFactory:
    _factories: dict

    def __init__(self) -> None:
        self._factories = {
            ".docx": WordFactory,
            ".pdf": PDFFactory,
        }

    def create_document(self, type_: str) -> Document:
        return self._factories[type_]().create_document()

factory = FileFactory()
word = factory.create_document(".docx")
pdf = factory.create_document(".pdf")

print(word.get_type())
print(pdf.get_type())

