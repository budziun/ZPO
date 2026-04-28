# 27.04.2026
# LAB9
# Wzorce strukturalne
# PYŁEK
# ZAD 7
# CZESC A
from tkinter.font import names

print("ZAD 7 - CZĘŚĆ A")
# Utworzyć system, który pozwala na współdzielenie
# ikon używanych w różnych częściach interfejsu użytkownika,
# zmniejszając zużycie pamięci.

from abc import ABC, abstractmethod
from random import choice

class Icon:
    def __init__(self,name:str,logo: str):
        self.name = name
        self.logo = logo
        print(f"Utworzono ikonę o nazwie: {name} i z obrazkiem {logo}")

class FacebookIcon(Icon):
    pass
class YoutubeIcon(Icon):
    pass

class IconFactory:
    @staticmethod
    def get_icon(name:str,logo:str) -> Icon:
        if logo == "facebook":
            return FacebookIcon(name,logo)
        elif logo == "youtube":
            return YoutubeIcon(name,logo)
        else:
            raise ValueError("Nie ma takiego logo")

class Phone:
    def __init__(self):
        self.icon = []
    def phone_apps(self):
        for _ in range(2):
            name = self._get_name()
            logo = self._get_logo()

            icon = IconFactory.get_icon(name,logo)

            self.icon.append(icon)

    def _get_name(self):
        return choice(["facebook","youtube"])
    def _get_logo(self):
        return choice(["facebook","youtube"])

phone = Phone()
phone.phone_apps()

#CZĘŚĆ B
print("\nCZĘŚĆ B")
#Zaimplementować pyłek, gdzie każdy produkt dzieli wspólną
# reprezentację etykiety (np. nazwa, kod kreskowy),
# a unikalne pozostają jedynie informacje o lokalizacji
# i stanie magazynowym.

class Products:
    def __init__(self,name:str,ean:int):
        self.name = name
        self.ean = ean

class ProductsFactory:
    _labels = {}

    @classmethod
    def get_label(cls,name:str,ean:int) -> Products:
        key = (name,ean)
        if key not in cls._labels:
            cls._labels[key] = Products(name,ean)
        return cls._labels[key]

class Inventory:
    def __init__(self, location: str,stock:int,product : Products):
        self.location = location
        self.stock = stock
        self.product = product

    def __str__(self):
        return f"Produkt: {self.product.name} [{self.product.ean}] znajduje się w {self.location} w ilości sztuk {self.stock}"

magazyn = []

produkty = [
    ("Mleko",9842819404,"Olsztyn",15),
    ("Cola",89088492,"Grudziądz",100),
    ("Ser piórko",8592108504,"Gruta",1)
]

for nazwa, ean, lokacja, stan in produkty:
    etykieta = ProductsFactory.get_label(nazwa, ean)

    item = Inventory(lokacja, stan, etykieta)
    magazyn.append(item)

for i in magazyn:
    print(i)

print("\nCZĘŚĆ C")
# CZĘŚĆ C
# Zaimplementuj wzorzec Pyłek, aby zoptymalizować
# przechowywanie kolorów w edytorze grafiki

class Colors(ABC):
    red: int
    green: int
    blue: int

    def __init__(self,red:int,green:int,blue:int):
        self.red = red
        self.green = green
        self.blue = blue
    def display(self):
        return f"Kolor ma barwy: {self.red} {self.green} {self.blue}"

class ColorsFactory:
    _colors = {}
    @classmethod
    def get_colors(cls,red:int,green:int,blue:int) -> Colors:
        key = (red,green,blue)

        if key not in cls._colors:
            cls._colors[key] = Colors(red,green,blue)

        return cls._colors[key]

class Pixel:
    def __init__(self,x:int,y:int,color:Colors,):
        self.x = x
        self.y = y
        self.color = color
    def draw(self):
        print(f"Pixel {self.color.display()} {self.x} {self.y}")

rysunek = []
red = ColorsFactory.get_colors(255, 0, 0)
rysunek.append(Pixel(10, 10, red))
rysunek.append(Pixel(20, 20, red))
rysunek.append(Pixel(30, 30, red))

green = ColorsFactory.get_colors(0, 255, 0)
rysunek.append(Pixel(40, 40, green))
rysunek.append(Pixel(50, 50, green))

blue = ColorsFactory.get_colors(0,0,255)
rysunek.append(Pixel(60, 60, blue))

for i in rysunek:
    i.draw()