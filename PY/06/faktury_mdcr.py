# faktury_mdcr.py

import os, csv

print(os.getcwd()) # get current working directory

with open('PY/06/faktury_md_2024.csv', encoding='utf-8') as file:
    file.readline()
    reader = csv.reader(file)

    max_castka = 0
    max_spolecnost = ''

    for line in reader:
        castka = float(line[5])
        if max_castka < castka:
            max_castka = castka
            max_spolecnost = line[3] + ' - ' + line[4]
    
    print(max_castka)
    print(max_spolecnost)
