# test_vek.py

vek = input('Zadej svůj věk: ')
vek = int(vek)

if vek < 18:
    print("Jsi mladistvý")
elif vek == 18:
    print("Jsi čerstvě dospělý")
else:
    print("Jsi dospělý")


print('Zadal jsi:', vek)
print(type(vek))
