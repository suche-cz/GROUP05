# nested_list.py

data = [
    ['Šaty', 2000, 1],
    ['Boty', 1000, 1],
    ['Ponožky', 50, 1],
    ['Klobouk', 500, 1],
]

for item in data:
    print(item[0], item[1])

print('--------------------')

for nazev, cena, x in data:
    print(nazev)
