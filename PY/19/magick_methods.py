class Human:
    # protokolarní rozhraní
    # máme magickou metodu __
    # existuje operace build in pythonu

    def __add__(self, other):
        return 10
    
    def __str__(self):
        return "HELLO"

jana = Human()
petr = Human()

vysledek = jana + petr

print(vysledek)
print(str(jana))