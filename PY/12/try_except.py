# try_except.py
# pokračujeme v 19:43
try:
    print(1)
    print(1 / 0)
    print(2)
except ZeroDivisionError:
    print('dělení nulou')
except (KeyError, IndexError):
    print('key or index error')
except Exception as err:
    print('Nějaká chyba - toto je obecná chyba', type(err))
finally:
    print("tato část se vykoná vždy")
