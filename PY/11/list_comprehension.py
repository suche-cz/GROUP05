cisla = [1, 2, 3, 4, 5]
cisla2 = []

for cislo in cisla:
    if cislo > 3:
        cisla2.append(cislo ** 2)

print(cisla2)

#-------------------------------------

cisla3 = [x**2 for x in cisla if x > 3]

print(cisla3)