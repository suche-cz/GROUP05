# oop_zapouzdreni.py
"""
+ je zde i polymorfismus
private - sourkomý
public - veřejný
"""


class Clovek:
    def __init__(self, jmeno, vek):
        self.jmeno = jmeno # public
        self._vek = vek # toto je privátní proměnná (variable)
        self._privatni_metoda() # privátní proměnné a metody mohu používat uvnitř třídy
    
    def __str__(self):
        return self.jmeno

    def __len__(self):
        # tato funkce se zavolá při zavolání len()
        return len(self.jmeno)
    
    def __add__(self, clovek):
        return [self, clovek]

    def __eq__(self, other):
        if self.jmeno == other.jmeno and self._vek == other._vek:
            return True
        else:
            return False

    def metoda(self, default='xyz'):
        print(default)
    
    def get_vek(self):
        # zde může být nějaká další logika ...
        return self._vek
    
    def _privatni_metoda(self):
        pass





jana = Clovek('Jana', 30)
print(jana.jmeno) # použití veřejné proměnné mimo třídu
print(jana._vek) # použití privátní proměnné mimo třídu - toto bych neměl dělat
# jana._vek = 0  # toto je potom použití na vlastní riziko

print(len(jana))

petr = Clovek('Jana', 30)

dvojice = petr + jana
print(dvojice)


print(petr == jana)
print(petr is jana)