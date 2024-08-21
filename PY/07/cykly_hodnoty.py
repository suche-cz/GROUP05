# cykly_hodnoty.py

ceny = ['Boty', 1000,'Šaty', 2000,'Klobouk', 500,'Ponožky', 50]
#        0      1     2      3     4         5    6         7 
# vyprintujte názvy

pocet = len(ceny)
max_cena = 0
max_nazev = ''

for index in range(0, pocet, 2):
    nazev = ceny[index]
    cena = ceny[index+1]
    print(nazev, cena)

    if cena > max_cena:
        max_cena = cena
        max_nazev = nazev

print('---')
print('MAX cena:', max_nazev, max_cena)
