# vydelat_penize.py

import random

cilova_castka = 1_000_000
aktualni_castka = 10_000


while aktualni_castka < cilova_castka:
    vydelane_penize = random.randint(10, 100) * 1000
    aktualni_castka += vydelane_penize
    print('Vydělal jsem', vydelane_penize)
    print('Moje aktuální částka je', aktualni_castka)
    print()



