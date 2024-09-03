# ex_dict9.py - cvičení na dict z pynative

"""
Exercise 9: Get the key of a minimum value from the following dictionary
"""

sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

min_key = ''
min_value = 100_000

for key, value in sample_dict.items():
    if value < min_value:
        min_value = value
        min_key = key

print(min_key, min_value)

