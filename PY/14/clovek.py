# clovek.py

"""
vytvořte třídu Clovek
atributy:
- id: int
- jmeno
- vek
- popis

vytvořte 2 instance z třídy Clovek
"""
import datetime as dt

class Clovek:
    def __init__(self, _id, jmeno, datum_narozeni, popis):
        self.id = _id
        self.jmeno = jmeno
        self.datum_narozeni = datum_narozeni
        self.popis = popis
        self.pratele = set()
    
    def __str__(self):
        # string reprezentace
        return f'{self.jmeno}[{self.id}]'
    
    def __repr__(self):
        # string reprezentace pro vytvoření kopie
        # také nám to ukáže objekt v datové struktuře
        return str(self)
    
    @property
    def vek(self):
        rozdil = dt.date.today() - self.datum_narozeni
        return int(rozdil.days / 365.25)
    
    def to_dict(self):
        return {
            'id': self.id,
            'jmeno': self.jmeno,
            'vek': self.vek,
            'popis': self.popis,
        }
    
    def pridej_pritele(self, clovek: 'Clovek'):
        if self is not clovek:
            self.pratele.add(clovek)
    
    def odeber_pritele(self, clovek: 'Clovek'):
        if clovek in self.pratele:
            self.pratele.remove(clovek)


jana = Clovek(1, 'Jana', dt.date(2000, 4, 12), 'Hello I am Jana')
petr = Clovek(2, 'Petr', dt.date(1997, 10, 20), 'Hello I am Petr')
suche = Clovek(3, 'Suche', dt.date(1900, 12, 20), "I'll be Back!")

print(jana.to_dict())
print(petr.to_dict())

suche.pridej_pritele(jana)
suche.pridej_pritele(petr)
# suche.pridej_pritele(jana, petr) #toto není připrave

jana.pridej_pritele(petr)
# jana.pridej_pritele(jana)
petr.pridej_pritele(jana)

jana.odeber_pritele(petr)
jana.pridej_pritele(suche)

print('Jana:', jana.pratele)
print('Petr:', petr.pratele)
print('Suche:', suche.pratele)
