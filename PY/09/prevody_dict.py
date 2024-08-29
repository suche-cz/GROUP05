# prevody_dict.py

lide = {
    'Jan': 180,
    'Petr': 170,
    'Jana': 200,
    '1': 1000000,
    True: False,
}

print(lide)
print(list(lide)) # převod na list
print(lide.values()) # získáme hodnoty
print(list(lide.values()))
print(lide.keys()) # získáme klíče
print(lide.items()) # získáme klíč i hodnotu

print()

for key, value in lide.items():
    print(key, value)

