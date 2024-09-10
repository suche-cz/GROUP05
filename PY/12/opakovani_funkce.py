data = [
    'Jana',
    'Petr',
    'Leoš',
    'Leonard',
    'Patrik',
]


def vyhledej(prvni_pismeno, delka):
    for jmeno in data:
        if jmeno[0] == prvni_pismeno and len(jmeno) == delka:
            return jmeno
    
    return None


print(vyhledej('P', 6)) # -> Patrik
print(vyhledej('L', 4)) # -> Leoš

