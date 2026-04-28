# 14.04.2026
# LAB8
# Wzorce strukturalne
# Most
# ZAD 5
# CZESC A

print("ZAD 5 - CZĘŚĆ A")

# Stwórz abstrakcyjną klasę Document, która będzie
# reprezentowała plik PDF oraz dwie niezależne
# implementacje renderowania
# (LightThemeRenderer, DarkThemeRenderer),
# łącząc je mostem.

from abc import ABC, abstractmethod

class Renderer(ABC):
    @abstractmethod
    def render_title(self,title:str):
        pass
    @abstractmethod
    def render_content(self,content:str):
        pass

class LightThemeRenderer(Renderer):
    def render_title(self,title:str):
        return f"(Motyw jasny) - Tytul: {title}"
    def render_content(self,content:str):
        return f"(Motyw jasny) - Tresc: {content}"

class DarkThemeRenderer(Renderer):
    def render_title(self,title:str):
        return f"[Motyw ciemny] Tytul: {title}"
    def render_content(self,content:str):
        return f"[Motyw ciemny] Tresc: {content}"


class AbstractDocument(ABC):

    def __init__(self, title: str,content: str,renderer: Renderer) -> None:
        self.title = title
        self.content = content
        self.renderer = renderer
    @abstractmethod
    def render(self):
        pass

class PDFDocument(AbstractDocument):
    def render(self):
        print("PDF DOC")
        print(self.renderer.render_title(self.title))
        print(self.renderer.render_content(self.content))
        print()


light = LightThemeRenderer()
dark = DarkThemeRenderer()

doc1 = PDFDocument("Raport nr 1","tessc bla bla bla",light)
doc2 = PDFDocument("Raport nr 1","tessc bla bla bla",dark)

doc1.render()
doc2.render()

print("CZĘŚĆ B")
# CZĘŚĆ B

# Zaimplementować system, w którym abstrakcja RemoteControl
# może sterować różnymi typami urządzeń
# (np. telewizor, radio, dron), niezależnie od
# ich implementacji.

class Device(ABC):
    @abstractmethod
    def turn_on_device(self):
        pass
    @abstractmethod
    def turn_off_device(self):
        pass
    @abstractmethod
    def make_command(self,value):
        pass


class Radio(Device):
    def turn_on_device(self):
        print("Włączono radio")
    def turn_off_device(self):
        print("Wyłączono radio")
    def make_command(self,value):
        print(f"Zmieniono głośność radia o {value}")

class Dron(Device):
    def turn_on_device(self):
        print("Włączono drona")
    def turn_off_device(self):
        print("Wyłączono drona")
    def make_command(self,value):
        print(f"Zmieniono pozycje drona o {value} jednostek")

class Telewizor(Device):
    def turn_on_device(self):
        print("Włączono telewizor")
    def turn_off_device(self):
        print("Wyłączono telewizor")
    def make_command(self,value):
        print(f"Zmieniono kanał na {value}")

class RemoteControl:
    def __init__(self, device: Device):
        self.device = device
    def turn_on(self):
        self.device.turn_on_device()
    def turn_off(self):
        self.device.turn_off_device()
    def make_command(self,value):
        self.device.make_command(value)

radio = Radio()
tv = Telewizor()
dron = Dron()

pilot = RemoteControl(radio)
pilot.turn_on()
pilot.make_command("20")
pilot.turn_off()
print()
pilot2 = RemoteControl(tv)
pilot2.turn_on()
pilot2.make_command("Polsat")
pilot2.turn_off()
print()
pilot3 = RemoteControl(dron)
pilot3.turn_on()
pilot3.make_command("1000")
pilot3.turn_off()
print("\nCZĘŚĆ C")
#CZĘŚĆ C
# Stwórz hierarchię na bazie abstrakcji Shape (np. Circle, Rectangle),
# a następnie oddzielić implementacje renderowania
# dla różnych technologii graficznych (SVG, BMP).

class FileType(ABC):
    @abstractmethod
    def render_shape(self,shape):
        pass
class SVGRender(FileType):
    def render_shape(self,shape):
        return(f"Wygenerowano figure: {shape} zgodnie z matematycznymi formułami w SVG")

class BMPRender(FileType):
    def render_shape(self,shape):
        return(f"Wygenerowano figure: {shape} zgodnie z podanymi pikselami w BMP")

class Shape(ABC):
    def __init__(self, filetype: FileType):
        self.filetype = filetype

    @abstractmethod
    def render(self):
        pass

class Triangle(Shape):
    def render(self):
        print(self.filetype.render_shape("trójkąt"))

class Rectangle(Shape):
    def render(self):
        print(self.filetype.render_shape("prostokąt"))

svg = SVGRender()
bmp = BMPRender()

trojkatsvg = Triangle(svg)
prostokatbmp = Rectangle(bmp)

trojkatsvg.render()
prostokatbmp.render()

trojkatbmp = Triangle(bmp)
prostokatsvg = Rectangle(svg)

trojkatbmp.render()
prostokatsvg.render()

# ZAD 6 - Pełnomocnik
# CZĘŚĆ A
print("\nZAD 6 - CZĘŚĆ A")
# Zaimplementować pełnomocnika, który umożliwia zdalne wykonywanie operacji na
# serwerze poprzez API, ale lokalnie sprawdza uprawnienia
# użytkownika przed wysłaniem żądania.

class AbstractAPI(ABC):
    @abstractmethod
    def request_data(self, endpoint: str) -> None:
        pass
    @abstractmethod
    def send_data(self, endpoint: str) -> None:
        pass

class API(AbstractAPI):
    def request_data(self, endpoint: str) -> None:
        print(f"Wysłano zapytanie {endpoint} do serwera")
    def send_data(self, endpoint: str) -> None:
        print(f"Wysłano dane z {endpoint} do serwera")

class Proxy(AbstractAPI):

    def __init__(self, api:API, user_role: str) -> None:
        self._api = api
        self._user_role = user_role
        self._is_authenticated = False

    def check_access(self) -> bool:
        if self._user_role == "admin":
            self._is_authenticated = True
            return True
        return False

    def request_data(self, endpoint: str) -> None:
        if self.check_access():
            self._api.request_data(endpoint)
        else:
            print("Brak dostepu, nie jesteś adminem!")

    def send_data(self, endpoint: str) -> None:
        if self.check_access():
            self._api.send_data(endpoint)
        else:
            print("Brak dostępu, nie wyślesz bo nie jesteś adminem")

api = API()

proxy_admin = Proxy(api,"admin")
proxy_admin.request_data("/request_data")
proxy_admin.send_data("/send_data")

guest = Proxy(api,"guest")
guest.request_data("/request_data")
guest.send_data("/send_data")

# CZĘŚĆ B
print("\nCZĘŚĆ B")
# Stworzyć pełnomocnika dla klasy HeavyObject,
# który tworzy rzeczywistą instancję dopiero w momencie
# pierwszego wywołania metody.

class Object(ABC):
    @abstractmethod
    def process(self):
        pass

class HeavyObject(Object):
    def __init__(self):
        print("Rozpoczęcie akcji HeavyObject")

    def process(self):
        print("Przetwarzanie danych do HeavyObject")

class ProxyObject(Object):
    def __init__(self):
        self._real_object = None
        print("Proxy: Obiekt rzeczywsity nie istnieje jeszcze")

    def process(self):
        if self._real_object is None:
            print("Proxy: Tworzenie obiektu rzeczywistego")
            self._real_object = HeavyObject()

        self._real_object.process()

proxy = ProxyObject()
proxy.process()
proxy.process()

#CZĘŚĆ C
print("\nCZĘŚĆ C")
# Przygotować pełnomocnika, który umożliwia dostęp do plików
# tylko użytkownikom o odpowiednich uprawnieniach,
# blokując w ten sposób nieautoryzowane operacje.

class FileSystem(ABC):
    @abstractmethod
    def read_file(self,filename: str):
        pass
    def save_file(self,filename: str):
        pass
    def modify_file(self,filename: str):
        pass

class WindowsFileSystem(FileSystem):
    def read_file(self,filename: str):
        print(f"Odycztano plik: {filename}")
    def save_file(self,filename: str):
        print(f"Zapisano plik: {filename}")
    def modify_file(self,filename: str):
        print(f"Zmodyfikowano plik: {filename}")

class FileProxy(FileSystem):
    def __init__(self, filesystem: FileSystem,user_role: str):
        self.filesystem = filesystem
        self.user_role = user_role

    def read_file(self,filename: str):
        if self.user_role in ["admin", "guest","moderator"]:
            self.filesystem.read_file(filename)
        else:
            print(f"Nie masz uprawnien do odczytu pliku {filename}")

    def save_file(self,filename: str):
        if self.user_role in ["admin","moderator"]:
            self.filesystem.save_file(filename)
        else:
            print(f"Nie masz uprawnien do zapisu pliku {filename}")

    def modify_file(self,filename: str):
        if self.user_role == "admin":
            self.filesystem.modify_file(filename)
        else:
            print(f"Nie masz uprawnien do modyfikacji pliku {filename}")

windows = WindowsFileSystem()
guest_proxy = FileProxy(windows,"guest")
mod_proxy = FileProxy(windows,"moderator")
admin_proxy = FileProxy(windows,"admin")

guest_proxy.read_file("test.txt")
guest_proxy.save_file("test.txt")
guest_proxy.modify_file("test.txt")

mod_proxy.read_file("test.txt")
mod_proxy.save_file("test.txt")
mod_proxy.modify_file("test.txt")

admin_proxy.read_file("test.txt")
admin_proxy.save_file("test.txt")
admin_proxy.modify_file("test.txt")