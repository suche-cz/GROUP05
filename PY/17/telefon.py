
class Sim:
    def __init__(self, cislo, operator, typ):
        self.cislo = cislo
        self.operator = operator
        self.typ = typ


class Telefon:
    def __init__(self, sim=None):
        self.sim = sim

    def get_cislo(self):
        return self.sim.cislo

t = Telefon()
s = Sim('7777', 'O2', 'Mini', t)

"""

obchod

produkty - IPhone 16

položky produktů - Iphone 16. vyr. č 29892873982

"""
