# test_alg.py
import timeit


data = ['1', '2', '3', '4', '5'] * 1000

def test1():
    for item in data:
        pocet = len(data)
        vysledek = f'{item} / {pocet}'
        # print(vysledek)

def test2():
    pocet = len(data)

    for item in data:    
        vysledek = f'{item} / {pocet}'
        # print(vysledek)

print(timeit.timeit(test1, number=10000))
print(timeit.timeit(test2, number=10000))
