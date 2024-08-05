# prace_s_cisly.py

"""
uzivatel bude zadávat čísla oddělená mezerou
např: 10 20 15 17 -19 100 27
naším úkolem je najít min max sum avg
"""

cisla = input("Zadej čísla: ") # získáváme hodnoty od uživatele jako str
data = cisla.split(' ') #rozdělíme hodnoty pomocí ' ' do list
data = list(map(int, data)) # na každý prvek data aplikujeme funkci int a celé to převedeme na list

suma = sum(data)
pocet = len(data)
prumer = suma / pocet

print('min', min(data))
print('max', max(data))
print('sum', suma)
print('prumer', prumer)
