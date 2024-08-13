# funkce v programování je kousek kódu, který je pojmenovaný
# def 
"""

1. definovaný název
2. může mít paramerty
3. musí být napsána obecně
4. hromadnosti - lze použít na různé parametry
5. dokončení v rozumném čase
6. determinovatelnost
"""

def secti_cisla(a, b, c=0):
    """
    Tato funkce sečte 3 čísla
    """
    print(a)
    print(b)
    print(c)
    return a + b + c


vysledek = secti_cisla(1, 2)


a = 10
# garbage collector

print(a)

print(secti_cisla(10,20,30))
