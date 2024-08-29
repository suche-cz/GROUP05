# cviceni_dict2.py

lide = {
    'Jan': 180,
    'Petr': 170,
    'Jana': 200,
}

dalsi_lide = {
    'Kuba': 160,
    'Petr': 190,
    # 'Leoš': 200,
}

lide.update(dalsi_lide)
print(lide)

print(lide['Petr']) # ok protože Petr je v dict
print(lide.get('Petr')) # ok protože používáme .get
# print(lide['Leoš']) # KeyError protože Leoš není v dict
print(lide.get('Leoš')) # vrátí None
print(lide.get('Leoš', 0)) # vrátí 0
