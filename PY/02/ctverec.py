# ctverec.py

"""
uživatel zadá stranu čtverce
ukolem je: vypočítat:

1) obvod - 4 * a
2) obsah - a * a = a ** 2
"""

strana_a = input('zadej stranu a: ')

je_cislo = strana_a.isdecimal()

if je_cislo:
    strana_a = int(strana_a)

    if strana_a > 0:
        print("obvod:", strana_a * 4)
        print("obvod:", strana_a ** 2)
    else:
        print("Neplatná hodnota, zadejte kladné číslo")
else:
    print("Neplatná hodnota, zadejte číslo")


