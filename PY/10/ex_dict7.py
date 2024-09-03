# ex_dict7.py - cvičení na dict z pynative
"""
Exercise 7: Check if a value exists in a dictionary
We know how to check if the key exists in a dictionary.
Sometimes it is required to check if the given value is present.

Write a Python program to check if value 200 exists in the following dictionary.
"""

sample_dict = {'a': 100, 'b': 200, 'c': 300, 'd': 200}

for key in sample_dict:
    if sample_dict[key] == 200:
        print(True)
        break


print(200 in sample_dict.values())
