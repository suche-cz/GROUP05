# load_page.py

import requests

def download_page(url, filename):
    response = requests.get(url)

    if response.status_code == 200:

        with open(f'PY/04/{filename}.html', mode='w', encoding='utf-8') as file:
            file.write(response.text)
    else:
        print('stránka vrátila stav', response.status_code)

download_page('https://www.google.com', 'new_google')