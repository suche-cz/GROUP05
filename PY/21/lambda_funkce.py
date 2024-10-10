# lambda_funkce.py

fce = lambda x: x * 2

print(fce(10))

def test(x, func):
    return func(x)


test(10, lambda x: x * 100)

cisla = [10, 92, 298, 11, 291, 221]

result = filter(lambda x: x % 10 == 2, cisla)
result2 = [x for x in cisla if x % 10 == 2]

print(list(result))
print(result2)

result3 = map(lambda x: x * 10, cisla)
result4 = [x * 10 for x in cisla]

print(list(result3))
print(result4)


