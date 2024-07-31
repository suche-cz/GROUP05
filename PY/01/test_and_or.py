# test_and_or.py

cena_do = 100_000
barva = 'red'


nabizena_cena = input('Zadejte cenu: ')
nabizena_barva = input('Zadejte barvu: ')
nabizena_cena = int(nabizena_cena)

# AND - chceme aby platily obě části podmínky

if nabizena_cena <= cena_do and nabizena_barva == barva:
    print("Vaše auto chci")
else:
    print("Nechci vaše auto")

