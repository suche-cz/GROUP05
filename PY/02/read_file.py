# read_file.py
# C:\AKADEMIE\GROUP05\PY\02>
"""
mode r = read (default)
mode w = write
mode a = append
"""

cesta = 'PY/02/test_file.txt'


with open(cesta, mode='w') as file:
    # poznámka: pokud soubor neexistuje bude vytvořen
    file.write("\nHELLO FROM PYTHON")

with open(cesta) as file:
    print(file.read())