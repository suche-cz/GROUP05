# staty_dict.py

# dict = dictionary = slovník
# hashtable, hashmapa, mapa nebo mapovací tabulka

"""
dict = datová struktura s klíčem a hodnotou
klíč musí unikátní
klíčem může být: str, int, bool, float, None, tuple
hodnotou může být cokoliv
hodnoty získáváme pomocí klíče data[key]
nezáleží na pořadí, tady jsou důležíté ty klíče
od PY 3.8 - je pořadí klíčů dané tak jak tam byly přidané
"""

staty = {
    'CZ': 10_000_000,
    'SK': 6_000_000,
    'DE': 50_000_000,
}

# získání hodnoty
print(staty['CZ'])

# přepsání klíče a hodnoty
staty['SK'] = 7_000_000

# přídání klíče a hodnoty
staty['BR'] = 80_000_000

# smazání hodnoty
del staty['DE']

print(len(staty))

for key in staty:
    print(key, staty[key])
