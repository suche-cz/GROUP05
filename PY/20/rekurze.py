# rekurze.py
"""
rekurzivní funkce, kdy funkce volá sama sebe
- musí tam být podmínka, kdy už se volat nebude
"""

def test(num):
    print(num)
    if num < 100:
        test(num + 1)
    else:
        print('konec')

test(10)


