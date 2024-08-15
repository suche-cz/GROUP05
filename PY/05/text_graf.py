# text_graf.py

data = [18, 90, 17, 6, 88]



def create_graf(data: list, symbol):
    for value in data:
        print(symbol * value)


create_graf(data, '-')
create_graf(data, '*')

