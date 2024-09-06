fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

# print(fruits.count('apple'))

#print(fruits.count('tangerine'))

# print(fruits.index('banana'))

# print(fruits.index('banana', 4))

fruits.reverse()
# print(fruits)

fruits.append('grape')
# print(fruits)

fruits.sort(key=lambda x: x[1], reverse=True)
# reverse=True
# key=lambda x: len(x)
# print(fruits)

posledni = fruits.pop()
print(posledni)
print(fruits)