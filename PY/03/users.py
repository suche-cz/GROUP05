# users.py

"""

Dáme uživateli na výběr
1 - pro login
2 - pro sign up

pokud zadá 1
- požádáme jej o username a heslo
- zkontrolujeme zda existuje soubor pro uživatele,
pokud ano tak jej otevřeme a načteme obsah souboru ve kterém je heslo
a porovnáme s tím heslem co zadá uživatel

pokud zadá 2
- požádáme jej o username a heslo
- zkontrolujeme zda existuje soubor pro uživatele
pokud existuje tak mu oznámíme že toto uživatelské jméno nelze použít
jinak mu vytvoříme soubor s uživatelským jménem a zapíšeme do něj heslo
"""

import os

def get_user_data():
    username = input('zadejte username: ')
    password = input('zadejte heslo: ')
    return [username, password]

def get_user_filename(username):
    filename = username + '.txt'
    filename = os.path.join(user_folder, filename)
    return filename

def do_user_exists(filename):
    return os.path.isfile(filename)

def login(filename, password):
    with open(filename) as file:
        content = file.read()

        if content == password:
            return True
    
    return False

def register(filename, password):
    with open(filename, mode='w') as file:
        file.write(password)
        print("registrace úspěšná")


user_folder = 'C:\\AKADEMIE\\GROUP05\\PY\\03\\users'

volba = input('Pro přihlášení zadejte 1, pro registraci zadejte 2: ')

if volba == '1':
    print('chcete se přihlásit')

    username, password = get_user_data()
    filename = get_user_filename(username)
    user_exists = do_user_exists(filename)
    success = False

    if user_exists:
        success = login(filename, password)
    
    if success:
        print('úspěšné příhlášení')
    else:
        print('příhlášení se nepodařilo')

elif volba == '2':
    print('chcete se registrovat')

    username, password = get_user_data()
    filename = get_user_filename(username)
    user_exists = do_user_exists(filename)

    if user_exists:
        print("zvolte prosím jiný username")
    else:
        register(filename, password)

else:
    print('neplatná volba')




