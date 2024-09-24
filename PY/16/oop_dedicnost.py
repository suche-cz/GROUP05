# oop_dedicnost.py

"""
1. potomek je speciální případ rodiče
2. potomek je schopen na 100% nahradit rodiče
"""

class Clovek:
    def __init__(self, jmeno, vek, vyska):
        self._jmeno = jmeno
        self._vek = vek
        self._vyska = vyska
    
    def predstav_se(self):
        print(f"Ahoj já jsem {self._jmeno} a mi {self._vek}")


class StydlivyClovek(Clovek):
    def predstav_se(self):
        """ override method """
        print(f"Ahoj ...")

dmitry = Clovek('Dmitry', 26, 190)
dmitry.predstav_se()

suche = StydlivyClovek('Suche', 34, 170)
suche.predstav_se()
