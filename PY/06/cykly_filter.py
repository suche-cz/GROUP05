# cykly_filter.py

data = [1, 238, 20, 87, 287, 10]

def filter_cisla_100(cisla):
    for cislo in cisla:
        if cislo < 100:
            print(cislo)

filter_cisla_100(data)
