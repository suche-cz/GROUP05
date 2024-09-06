a = [1,2,3]
d = {'x': a, 'y': a}
b = a
print(id(a))
print(id(d['x']))
print(id(d['y']))

a.append('new value')

print(a)
print(b)
print(d['x'])
print(d['y'])

c = [1, 2, 3, 'new value']

print(c == a) # hodnotové porovnání
print(c is a) # "objektové" porovnání
