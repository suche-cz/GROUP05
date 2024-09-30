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

class ProductEmptyError(Exception):
    pass


class Produkt:
    """ Katalogový Produkt """
    def __init__(self, nazev: str, cena: int):
        self.nazev = nazev
        self.cena = cena
        self._sklad = {}
    
    def __str__(self):
        return f'<Produkt> {self.nazev}'

    def add(self, _id: int=None, polozka: 'PolozkaProduktu'=None):
        if not _id and not polozka:
            raise ValueError('Zadej jedno z _id nebo polozka')
        
        if _id:
            polozka = PolozkaProduktu(_id, self)

        self._sklad[polozka.id] = polozka

    def get(self) -> 'PolozkaProduktu':
        if not self._sklad:
            raise ProductEmptyError()

        first_id = tuple(self._sklad)[0] # dalo by se udělat jako next(iter(self.polozky), None)
        return self._sklad.pop(first_id)

    def info(self):
        for key, item in self._sklad.items():
            print(key, item)
            
        print(f'Celkem {self.nazev}:', len(self._sklad))
        print()



class PolozkaProduktu:
    """ Kus Produktu """
    def __init__(self, _id: int, produkt: Produkt):
        self.id = _id
        self.produkt = produkt
    
    def __str__(self):
        # f'{self.produkt.nazev}: {self.id}'
        return self.produkt.nazev + ': ' + str(self.id)
    
    def __repr__(self):
        return str(self)


class Nakup:
    def __init__(self):
        self.datum = dt.datetime.now()
        self._polozky: list[PolozkaProduktu] = []
    
    def add(self, produkt: Produkt):
        try:
            polozka = produkt.get()
            print(polozka, 'přidána do košíku')
            self._polozky.append(polozka)
        except ProductEmptyError:
            print('Tato položka není dostupná', produkt)

    def remove(self, produkt: Produkt):
        # Uděleje metodu clear na třídě Nakup, která vysype celý košík
        for item in self._polozky:
            if item.produkt == produkt:
                self._polozky.remove(item)
                break # chceme odstranit pouze jednou
    
    def clear(self):
        # self._polozky = []
        self._polozky.clear()
    
    def faktura(self):
        print('---------- Faktura ----------')
        # celkem = sum(x.produkt.cena for x in self._polozky)
        celkem = 0
        for item in self._polozky:
            celkem += item.produkt.cena
            print(item, '\t', item.produkt.cena, 'Kč')

        print('-----------------------------')
        print('Celkem:', '\t', celkem, 'Kč')
        print('-----------------------------')


p1 = Produkt('IPhone 16', 20_000) # katalogový produkt
p2 = Produkt('Televize LG', 10_000)

p1.add(_id=1)
p1.add(polozka=PolozkaProduktu(4, p1))
p1.add(_id=2)
p1.add(_id=3)
p1.add(_id=5)
p1.add(_id=6)
p1.add(_id=7)
p1.add(_id=8)
p2.add(_id=10)

# p1.info()
# p2.info()

muj_nakup = Nakup()
muj_nakup.add(p1)
muj_nakup.add(p1)
muj_nakup.add(p1)
muj_nakup.add(p1)
muj_nakup.add(p1)
muj_nakup.add(p2)
# muj_nakup.remove(p1)

muj_nakup.faktura()

p1.info()