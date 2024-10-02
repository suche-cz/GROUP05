# module1.py

# CZ, US

vek_map = {
    'US': 21,
    'JP': 20,
    'KU': 16, # Kuba
    'IA': 16, # Irán
}

def je_dospely(vek: int, zeme: str):
    if vek < 0:
        raise ValueError()
    
    if zeme in vek_map:
        vek_mez = vek_map[zeme]
    else:
        vek_mez = 18

    return vek >= vek_mez


def je_dospely_old(vek: int, zeme: str):
    if vek < 0:
        raise ValueError()
    
    if zeme == 'CZ':
        return vek >= 18
    
    if zeme == 'US':
        return vek >= 21

    if zeme == 'SK':
        return vek >= 20

