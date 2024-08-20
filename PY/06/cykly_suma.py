# cykly_suma.py

def suma(cisla: list[int]):
    vysledek = 0
    
    for cislo in cisla:
        vysledek = vysledek + cislo
    
    return vysledek


def main():
    data = [1, 238, 20, 87, 287, 10]
    result = suma(data)
    print(result)

    data = [10, 38, 0, 8, 87, 1]
    result = suma(data)
    print(result)


main()


