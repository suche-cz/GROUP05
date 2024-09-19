# clovek.py

"""
vytvořte třídu Clovek
atributy:
- id: int
- jmeno
- vek
- popis

vytvořte 2 instance z třídy Clovek

def metoda(self) = instanční metoda = pracuje s danou instancí

@classmethod
def metada(cls) = třídní metoda (class method) = metoda, která pracuje s třídou

"""
import datetime as dt

with open('PY/14/template.html', encoding='utf-8') as file:
    TEMPLATE = file.read()

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

    @classmethod
    def spolecni_pratele(cls, clovek1: 'Clovek', clovek2: 'Clovek'):
        return clovek1.pratele & clovek2.pratele
    
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
    
    def pridej_vice_pratel(self, list_pratel: list):
        for clovek in list_pratel:
            self.pridej_pritele(clovek)

    def vytvor_html(self):
        html = TEMPLATE

        d = self.datum_narozeni
        datum_narozeni = f'{d.day}. {d.month}. {d.year}'

        replace_values = (
            ('{id}', str(self.id)),
            ('{jmeno}', self.jmeno),
            ('{vek}', str(self.vek)),
            ('{datum_narozeni}', datum_narozeni),
            ('{popis}', self.popis),
            ('{pratele}', self.get_html_pratel()),
        )

        for key, value in replace_values:
            html = html.replace(key, value)
        
        html_path = f'PY/14/html/{self.id}.html'
        with open(html_path, mode='w', encoding='utf-8') as file:
            file.write(html)
    
    def get_html_pratel(self):
        html = ''
        for item in self.pratele:
            html += f'<li>{item.jmeno}</li>'

        return html


jana = Clovek(1, 'Jana', dt.date(2000, 4, 12), 'Hello I am Jana')
petr = Clovek(2, 'Petr', dt.date(1997, 10, 20), 'Hello I am Petr')
suche = Clovek(3, 'Suche', dt.date(1900, 12, 20), "I'll be Back!")

jana.pridej_vice_pratel([petr, suche, jana])
petr.pridej_pritele(suche)
print(jana.pratele)
print(Clovek.spolecni_pratele(jana, petr))

jana.vytvor_html()
petr.vytvor_html()