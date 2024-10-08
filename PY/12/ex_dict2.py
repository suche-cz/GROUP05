# ex_dict2.py

"""
Exercise 5: Create a dictionary by extracting the keys from a given dictionary
Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.
"""

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york",    
}

keys = ["name", "salary"]

result = {}

for key in keys:
    print(key)
    result[key] = sample_dict[key]

print(result)


