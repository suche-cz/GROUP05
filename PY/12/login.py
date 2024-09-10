# login.py

data = {
    'danil': 'heslo1234',
    'suche': 'heslo1234',
    'jana': 'tadara62',
}

# navrhněte funkci pro přihlašování

def login(username, password):
    if username in data and data[username] == password:
        return True
    
    return False


while True:
    u = input('Zadej username: ')
    p = input('zadej heslo: ')

    try:
        if not u:
            raise ValueError('Zadej username')
        if not p:
            raise ValueError('Zadej heslo')
        if ' ' in u or not u.islower():
            raise ValueError('Neplatný username')
        
        result = login(u, p)
        if result:
            print('OK')
            break
        else:
            print('try again')
    except Exception as e:
        print(e)





