# test_sets.py

# set = množina
# teorie množin
"""
1 - neřeší se pozice, indexy, pořadí ..
2 - unikatní "výčet prvků"
"""



zakladni_cisla = {0, 1, 2, 3, 4, 5, 10, 100, 100}
cela_cisla = {-3, -2, -1, 0, 1, 2, 3, 4, 5}


prunik = zakladni_cisla & cela_cisla
sjednoceni = zakladni_cisla | cela_cisla
rozdil_1 = zakladni_cisla - cela_cisla
rozdil_2 = cela_cisla - zakladni_cisla

print(prunik)
print(sjednoceni)
print(rozdil_1)
print(rozdil_2)

