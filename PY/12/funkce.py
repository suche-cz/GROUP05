# funkce.py

def vypocti(a, b, c):
    assert a > 0, 'A musí větší než 0'
    if b == 0:
        raise ValueError('hodnota b nesmí být 0')
    return a / b * c

try:
    vypocti(10, 0, 30)
    vypocti('10', 20, 30)
except TypeError:
    print('Zadal jsi nesprávné hodnoty')
except AssertionError as err:
    print(err)
    print('hodnota a musí být větší než 0')
except:
    print('Neznámá chyba')
