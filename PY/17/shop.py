# shop.py

"""

Produkt (Obecný prodkt) - IPhone 16, Mac Mini
- cena
- nazev
- polozky

IPhone 16
- polozky = {}


Položka Produktu:
- id
- produkt

Položka IPhone 16
- seriové číslo 0922329
- IPhone 16 (Produkt)

Nakup
- položky nakůpu
- datum a čas nákupu

Nákup:
datum a čas: 10. 8. 2022
položka = [
    IPhone 16 0922329,
    IPhone 16 0922328,
    IPhone 16 0922310,
]

- 1x IPhone 16
- 2x sluchátka Buts Pro

"""

import datetime as dt

class Cena:
    def __init__(self, produkt, datum, hodnota):
        self.produkt = produkt   
        self.datum = datum
        self.hodnota = hodnota


class Produkt:
    """ Katalogový Produkt """
    def __init__(self, nazev: str, cena: int):
        self.nazev = nazev
        self.cena = cena
        self.polozky = {} # TODO: nastavít jako privátní
    
    def __str__(self):
        return f'<Produkt> {self.nazev}'

    def add(self, _id: int):
        self.polozky[_id] = PolozkaProduktu(_id, self)

    def get(self):
        first_id = tuple(self.polozky)[0] # dalo by se udělat jako next(iter(self.polozky), None)
        return self.polozky.pop(first_id)


class PolozkaProduktu:
    """ Kus Produktu """
    def __init__(self, _id: int, produkt: Produkt):
        self.id = _id
        self.produkt = produkt
    
    def __str__(self):
        # f'{self.produkt.nazev}: {self.id}'
        return self.produkt.nazev + ': ' + str(self.id)


class Nakup:
    def __init__(self):
        self.datum = dt.datetime.now()
        self.polozky = []


p1 = Produkt('IPhone 16', 20_000) # katalogový produkt
p2 = Produkt('Televize LG', 10_000)

p1.add(1)
p1.add(2)
p1.add(3)

dalsi_iphone = p1.get()
dalsi_iphone = p1.get()
dalsi_iphone = p1.get()
dalsi_iphone = p1.get() # TOTO vyhodí chybu - TODO: opravit

print(dalsi_iphone)
print('-----------------')

for key, value in p1.polozky.items():
    print(value)
    # IPhone 16: 1298379873