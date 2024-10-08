def vypocet(a, b, callback=None):
    vysledek = a + b
    if callback:
        callback(vysledek)
    return vysledek

def funkce1(vysledek):
    print('Super výpočet! výsledek je:', vysledek)

def funkce2(vysledek):
    print('Dobrá práce! výsledek je:', vysledek)

def vytiskni_vysledek(vysledek):
    print(vysledek)

def uloz_vysledek(vysledek):
    with open('PY/20/vysledek.txt', mode='a', encoding='utf-8') as file:
        file.write(str(vysledek) + '\n')

"""
Pokračujeme v 19:50
"""

vypocet(10, 100, vytiskni_vysledek)
vypocet(20, 200, uloz_vysledek)
vypocet(20, 300, uloz_vysledek)
vypocet(20, 400, uloz_vysledek)
vypocet(20, 500, uloz_vysledek)
vypocet(10, 100)
