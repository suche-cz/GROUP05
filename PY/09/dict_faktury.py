# dict_faktury.py
import os, csv

path = 'PY/06/faktury_md_2024.csv'
# p = r'C:\AKADEMIE\GROUP05\PY\09\dict_faktury.py'

data = {}

with open(path, encoding='utf-8') as file:
    file.readline()
    reader = csv.reader(file)

    for line in reader:
        nazev = line[3]
        castka = float(line[5])

        if nazev not in data:
            data[nazev] = castka
        else:
            puvodni_hodnota = data[nazev]
            data[nazev] = puvodni_hodnota + castka

data_list = list(data.items())
data_list.sort(key=lambda x: x[1])

for item in data_list:
    print(item)
