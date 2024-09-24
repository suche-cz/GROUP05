# oop_overview.py

class Pes:
    MAX_POCET = 10 # class variable
    VSICHNI_PSI = set() # class variable

    def __init__(self, jmeno: str, pohlavi: bool, rasa: str, vek: int):
        self.jmeno = jmeno
        self.pohlavi = pohlavi
        self.rasa = rasa
        self.vek = vek

        if len(self.VSICHNI_PSI) < self.MAX_POCET:
            self.VSICHNI_PSI.add(self)
        else:
            raise ValueError('Max počet psů')

    def stekej(self):
        print(self.jmeno)
        print('waf waf')
    
    @classmethod
    def info(cls):
        print("classmethod", cls)
    
    @staticmethod
    def funkce(a, b):
        """ sedí na třídě, ale nemá reference na třídu ani instanci """
        print("Toto něco dělá, ale nemá to informaci o cls ani self")
    

    @property
    def lidsky_vek(self):
        # dynamicky vypočítaná hodnota
        return self.vek * 7


def funkce(a, b):
    """ sedí na třídě, ale nemá reference na třídu ani instanci """
    print("Toto něco dělá, ale nemá to informaci o cls ani self")

Pes.funkce(1, 2)
pes_funkce(1, 2)

muj_pes2 = Pes('Pepa', 1, 'Německý ovčák', 5)
muj_pes = Pes('Alík', 1, 'Německý ovčák', 5)
muj_pes.stekej()

print(muj_pes.vek)

print(Pes.VSICHNI_PSI)

