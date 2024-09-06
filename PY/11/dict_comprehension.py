# dict_comprehension.py

jmena = ['Jana', 'Lukáš', 'Oto']

jmena = {x: len(x) for x in jmena if x[0] in 'JL'}

print(jmena)
