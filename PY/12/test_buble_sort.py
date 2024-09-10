data = [28,20,9,8,23,-8]

pocet = len(data)


while pocet:
    pocet -= 1
    for index in range(len(data) - 1):
        a = data[index]
        b = data[index+1]
        
        if a > b:
            data[index] = b
            data[index+1] = a

print(data)