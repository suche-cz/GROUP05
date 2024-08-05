# test_delka.py
"""
uživatel zadá své jméno
a program mu zjistí jakou délku má jeho jméno

- odstraníme bíle znaky (prazdné znaky)

"""

jmeno = input('Zadej své jméno: ')
jmeno = jmeno.replace(' ', '')

print(jmeno)
print(len(jmeno))

print(jmeno.count('a'))

data = ['A', 'B', 'C']

str_data = ','.join(data)

print(str_data)


