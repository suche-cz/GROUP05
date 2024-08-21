# while_cyklus.py

data = ['A', 'B', 'C']

cislo = 0

while cislo < len(data):
    print(data[cislo])
    cislo += 1
    
cislo = 0

while True:
    if cislo >= len(data):
        break

    print(data[cislo])
    cislo += 1
    



