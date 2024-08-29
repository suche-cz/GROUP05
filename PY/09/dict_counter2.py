# dict_counter2.py
# toto je jen cvičná verze, dict_counter.py je lepší
"""
logika:

1. procházím písmena v textu
2. pokud je písmeno v data
3. tak zvětším hodnotu
4. jinak založím klíč s písmenem a hodnotou 1
"""

text = 'asdkasdjaoisdaowejaijdaklscancjabfsfhaius'

data = {}

for letter in text:
    if letter in data:
        data[letter] += 1
    else:
        data[letter] = 1

print(data)

        

    


