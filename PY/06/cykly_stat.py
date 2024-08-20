# cykly_stat.py

data = [1, 238, -20, 87, 287, -10]


def najdi_nejmensi(cisla: list[int]):
    nejmensi = cisla[0]

    for cislo in cisla:
        if cislo < nejmensi:
            nejmensi = cislo

    return nejmensi


def najdi_nejvetsi(cisla: list[int]):
    nejvetsi = cisla[0]

    for cislo in cisla:
        if cislo > nejvetsi:
            nejvetsi = cislo
            

    return nejvetsi


print(najdi_nejmensi(data))
print(najdi_nejmensi([1, 2, 6, 8, -1, -9, 19, 27]))
print(najdi_nejvetsi(data))
print(najdi_nejvetsi([1, 2, 6, 8, -1, -9, 19, 27]))
