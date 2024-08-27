# stavba_veze.py

cilova_vyska = 250 # 250 m
aktualni_vyska = 0
pocet_metru_za_den = 2.5

pocet = 0

while aktualni_vyska < cilova_vyska:
    pocet += 1
    aktualni_vyska += pocet_metru_za_den
    print(aktualni_vyska, pocet)

print('budova byla dokočena v', pocet, 'dnech')
