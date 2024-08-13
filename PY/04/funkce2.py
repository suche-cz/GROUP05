# funkce2.py
# vytvořte funkci s názvem avg - average
# která vytvoří průměrnou hodnotu 3 vstupních čísel a, b, c
# 1,2,3 -> 2
# 5, 20, 10 -> 10.166666
# teorie: sečtu čísla a,b,c a pak je vydělím 3

def avg(a, b, c):
    soucet = a + b + c
    vysledek = soucet / 3
    return round(vysledek, 3)


vypocet1 = avg(10, 27, 28)
vypocet2 = avg(10, 399, 208)

print(vypocet1, vypocet2)