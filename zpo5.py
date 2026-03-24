# 24.03.2026
# LAB5
# Wzorce strukturalne
# Adapter
#ZAD1
# CZĘŚĆ A
# Zaimplementować wzorzec Adapter, który pozwoli na użycie klasy
# z (z metodą print_old()) w nowym systemie wymagającym metody
# print_new().


class Old:
    def __init__(self,name: str,age: int,old: str):
        self.name = name
        self.age = age
        self.old = old
    def print_old(self) -> str:
        return "zwaracam stare"

class New:
    def __init__(self,name: str,age: int,new: str):
        self.name = name
        self.age = age
        self.new = new
    def print_new(self) -> str:
        return "zwaracam nowe"

class OldNewAdapter:
    def __init__(self,new: New):
        self.new = new
    def print_new(self) -> str:
        return "zwaracam nowe"
    def print_old(self) -> str:
        return "zwaracam stare"

old = Old("Stary OBIekt",67,"Old")
new = New("Nowy obiekt",23,"New")

print("ZAD1")
print("CZĘŚĆ A")
print(old.print_old())
print(old.old)
print(old.age)

staro_nowe = OldNewAdapter(new)
print(staro_nowe.print_new())
print(staro_nowe.print_old())

#CZĘŚĆ B
#Przygotować klasę Adapter, która konwertuje wartości temperatury
# w stopniach Fahrenheita na stopnie Celsjusza, używając
# przygotowanej klasy FahrenheitSensor.

print("\nCZĘŚĆ B")

class FahrenheitSensor:
    def __init__(self, temperature: float):
       self.temperature = temperature
class CelciusSensor:
    def __init__(self, temperature: float):
        self.temperature = temperature

class Adapter:
    to_convert_temeprature = float

    def __init__(self, fahr: FahrenheitSensor) -> None:
        self.fahr = fahr
        self.to_convert_temeprature = fahr.temperature

    def convert_temeprature_to_celcius(self) -> float:
        return round((self.fahr.temperature - 32) / 1.8, 2)

fahr = FahrenheitSensor(100)
adapter = Adapter(fahr)
print(adapter.convert_temeprature_to_celcius())
fahr2 = FahrenheitSensor(0)
adapter2 = Adapter(fahr2)
print(adapter2.convert_temeprature_to_celcius())

# CZĘŚĆ C
# Utworzyć adapter umożliwiający korzystanie z dwóch różnych
# systemów płatności, gdzie przykładowo jeden obsługuje PayPal,
# drugi Stripe, ale klient korzysta z ujednoliconego interfejsu.

class PayPal:
    def pay_paypal(self, kwota: float):
        return f"Zapłacono przy użyciu Paypal {kwota} PLN"
class Stripe:
    def pay_stripe(self, kwota: float):
        return f"Zapłacono używając Stripe {kwota} PLN"
class Blik:
    def pay_blik(self, kwota: float):
        return f"Zapłacono blikiem {kwota} PLN"

class Payment:
    def pay(self, kwota: float, rodzaj: str):
        if(rodzaj == "PayPal"):
            return PayPal().pay_paypal(kwota)
        elif(rodzaj == "Stripe"):
            return Stripe().pay_stripe(kwota)
        elif(rodzaj == "Blik"):
            return Blik().pay_blik(kwota)
        else:
            return f"Przepraszamy, nie obsługujemy płatności za pomocą {rodzaj}, opłać inną metodą płatności kwotę {kwota} PLN"

print("\nCZĘŚĆ C")
tranzakcja = Payment()
print(tranzakcja.pay(2137,"Blik"))
print(tranzakcja.pay(6767,"PayPal"))
print(tranzakcja.pay(10,"Stripe"))
print(tranzakcja.pay(1000000,"PaySafeCard"))