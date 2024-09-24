# oop_super.py

class Ctverec:
    def __init__(self, strana_a):
        self.strana = strana_a
    
    def obsah(self):
        return self.strana ** 2


class Krychle(Ctverec):
    def obsah(self):
        obsah = super().obsah() # výpočet obsahu z parent class
        return obsah * 6
    

c = Ctverec(10)
print(c.obsah())



