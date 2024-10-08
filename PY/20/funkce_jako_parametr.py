# funkce_jako_parametr.py

def test1(a, b):
    print(a, b)


test1('Ahoj', 'Pepo')
test1('Ok', 'Hotovo')


znamky = {
    1: 'Výborně',
    2: 'Chvalitebně',
    3: 'Dobře',
    4: 'Dostatečně',
    5: 'Nedostatečně',
    6: 'Katastrofa',
}

def vyprat():
    print('Peru prádlo')

def uvarit():
    print('Vařím')

def get_text_znamky(znamka: int, callback):
    callback()
    return znamky[znamka]


print(get_text_znamky(1, vyprat))
print(get_text_znamky(3, uvarit))
