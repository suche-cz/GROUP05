class Tvor:
    pass

class Obratlovici(Tvor):
    pass

class LetejiciTvor(Obratlovici):
    def letej(self):
        print('létám')

class ChodiciTvor(Obratlovici):
    def jdi(self):
        print('jdu')

class PlavajiciTvor(Obratlovici):
    def plav(self):
        print('plavu')

class Opice(ChodiciTvor, PlavajiciTvor):
    def __init__(self, jmeno):
        super().__init__()
        self.jmeno = jmeno

class Ryba(PlavajiciTvor):
    pass

class Kacha(PlavajiciTvor, LetejiciTvor, ChodiciTvor):
    pass


o = Opice('Agata')
o.plav()
o.jdi()
# o.letej()

print(vars(o)) # vrátí proměnné které jsou definované na o
print(Opice.mro()) # model resolution order
print(str.mro())


