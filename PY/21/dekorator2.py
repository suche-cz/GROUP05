# dekorator2.py
"""
dekorator je funkce, která přijimá jinou funkci a vrátí její zmodifikovanou verzi
"""

def print_result(func):
    def inner(a, b):
        print('PRINT ::..')
        result = func(a, b)
        print('Udělal jsem výpočet a výsledek je:', result)
        return result

    return inner


def vypocet(a, b):
    return 10 + 20

vypocet = print_result(vypocet) # explicitní nahrazení puvodní funkce


@print_result # takto se dělá pak dekorátor
def dalsi(a, b):
    return 10 * 20


print(vypocet())

print(dalsi())
