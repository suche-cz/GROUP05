# cykly_dalsi.py

# range(10) - 0 až 9
# range(4, 10) - 4 až 9
# range(4, 10, 2) - 4, 6, 8

print(list(range(10)))
print(list(range(4, 10)))
print(list(range(4, 10, 2)))

data = ['Petr', 'Jan', 'Lena', 'Kamil', 'Kuba']
#        0       1      2       3        4

for index in range(len(data)):
    print(index, data[index])






