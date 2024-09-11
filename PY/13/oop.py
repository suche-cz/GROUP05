# oop.py
# OOP = Objektově orientované programování

"""

třída - obecná definice objetu
class

instance/objekt - konkrétní výskyt objektu
instance/object


Suche: já
Věra: já

"""


class Clovek:
    def __init__(self, name, age, height=None):
        # nastavení atributů
        self.jmeno = name
        self.vek = age
        self.vyska = height
    
    def pozdrav(self):
        # metoda = chování
        print(f"Ahoj já jsem {self.jmeno} a je mi {self.vek} let")

    def jsem_dospely(self):
        if self.vek > 17:
            return True
        else:
            return False

    # vytvořte metodu jsem_dospely, který vratí True/False podle toho zda je dospely


jana = Clovek('Jana', 20, 190) #vytvoření instance
jana.pozdrav()

petr = Clovek('Petr', 24)
petr.pozdrav()
print(petr.jsem_dospely())

