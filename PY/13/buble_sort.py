# buble_sort.py

numbers = [50, 28, 25 , 17, 8, 6]
#           0  1  2   3   4   5

def buble_sort(data):
    pocet = len(data)

    for a in range(pocet-1):
        for index in range(pocet - 1):
            x = index
            y = index + 1

            a = data[x]
            b = data[y]
            
            if a > b:
                data[x] = b
                data[y] = a


buble_sort(numbers)
print(numbers)
