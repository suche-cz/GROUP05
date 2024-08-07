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


user_folder = 'C:\\AKADEMIE\\GROUP05\\PY\\03\\users'

volba = input('Pro přihlášení zadejte 1, pro registraci zadejte 2: ')

if volba == '1':
    print('chcete se přihlásit')

    username = input('zadejte username: ')
    password = input('zadejte heslo: ')

    filename = username + '.txt'
    filename = os.path.join(user_folder, filename)

    user_exists = os.path.isfile(filename)
    success = False

    if user_exists:
        with open(filename) as file:
            content = file.read()

            if content == password:
                success = True
    
    if success:
        print('úspěšné příhlášení')
    else:
        print('příhlášení se nepodařilo')

elif volba == '2':
    print('chcete se registrovat')
    username = input('zadejte username: ')
    password = input('zadejte heslo: ')

    filename = username + '.txt'
    filename = os.path.join(user_folder, filename)

    user_exists = os.path.isfile(filename)

    if user_exists:
        print("zvolte prosím jiný username")
    else:
        with open(filename, mode='w') as file:
            file.write(password)
            print("registrace úspěšná")

else:
    print('neplatná volba')




