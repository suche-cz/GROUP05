# ex_dict1.py - cvičení na dict z pynative

"""
Exercise 1: Convert two lists into a dictionary
Below are the two lists. Write a Python program to convert them into a
dictionary in a way that item from list1 is the key and item from list2 is the value
"""


keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]


result = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

vysledek = {}

for index in range(len(keys)):
    print(index)
    key = keys[index]
    value = values[index]
    vysledek[key] = value

print(vysledek)


