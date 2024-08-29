staty = [
    'CZ', 10_000_000,
    'SK', 6_000_000,
    'DE', 50_000_000,
]

staty[1] = 9_000_000

staty2 = [
    ['CZ', 10_000_000,],
    ['SK', 6_000_000,],
    ['DE', 50_000_00,],
]

for index in range(0,6,2): # 6 předělat na len(staty)
    nazev = staty[index]
    pocet = staty[index+1]
    print(nazev, pocet)

print('------------------------------------')

for item in staty2:
    nazev = item[0]
    pocet = item[1]
    print(nazev, pocet)

print('------------------------------------')

for nazev, pocet in staty2:
    print(nazev, pocet)
