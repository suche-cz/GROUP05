# cykly_dvojice.py

studenti = ['Věra', 'Jan', 'Dmitry P.', 'Milan', 'Dmitry Y.', 'Timur']
#            0       1      2            3        4            5

pocet = len(studenti)

for index in range(0, pocet, 2):
    print(index, index + 1)
    print(studenti[index], studenti[index + 1])


