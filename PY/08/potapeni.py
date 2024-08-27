# potapeni.py

aktualni_kyslik = 100
spotreba_kysliku = 1.5
min_kyslik = 50
# while cyklus, kde budete v každém kroku odečítat 1.5
# dokud je hodnota vyšší jak 50 tak se může potapěd dále,
# jinak to ukončíme a vyprintujeme, že se má vrátit

while aktualni_kyslik > min_kyslik:
    aktualni_kyslik -= spotreba_kysliku
    print('aktualni kyslík je', aktualni_kyslik)
else:
    print('Vrať se ...')


