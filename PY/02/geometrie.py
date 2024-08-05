# geometrie.py

# výpočet obvodu trojúhelníku

"""
uživatel zadá 3 hodnoty vedle sebe např:
20 30 15
"""

hodnoty = input("Zadejte hodnoty trojůhelníka: ")

data = hodnoty.split(' ')

a, b, c = data

print(a + b + c)
print(int(a) + int(b) + int(c))


print(list(map(int, data)))
