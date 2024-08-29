# dict_counter.py

text = 'ůlaskdalkjsdoaijwdowijadklsjakljdoiawjioajdaskdjaůoisda'
data = {}

for letter in text:
    if letter not in data:
        data[letter] = text.count(letter)

print(data)
