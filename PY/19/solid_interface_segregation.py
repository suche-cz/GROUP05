# interface_segregation.py

class Animal:
    # takto ne - potomci budou mít metody, které u nich být nemají
    def fly(self):
        pass

    def walk(self):
        pass

    def swim(self):
        pass

    def run(self):
        pass

class Lion(Animal):
    pass

class Falcon(Animal):
    pass


# --------------------------------------------------
# metody rozdělíme do vlastních tříd
class AnimalInteface:
    def change_position(self):
        pass


class FlyingAnimal(AnimalInteface):
    def fly(self):
        pass

class WalkingAnimal(AnimalInteface):
    def walk(self):
        pass

class SwimmingAnimal(AnimalInteface):
    def swim(self):
        pass

class RunningAnimal(AnimalInteface):
    def run(self):
        pass


# dědíme opravdu jen to co mají umět

class Lion(WalkingAnimal, SwimmingAnimal, RunningAnimal):
    def change_position(self):
        pass
        

class Falcon(FlyingAnimal, WalkingAnimal):
    pass



# Dependency Inversion Principle

def change_position(animal):
    animal.change_position()
