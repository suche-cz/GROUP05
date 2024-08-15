from urllib.request import urlretrieve
import requests


# 0 1
# 01010101

def download_image2(url, filename=None):
    names = url.split('/')
    filename = filename or names[-1]

    response = requests.get(url)
    with open(filename, mode='wb') as file:
        file.write(response.content)


def download_image(url, filename=None):
    """
    stahuje obrázek z url
    """
    urlretrieve(url, filename='muj-obrazek.png')
    print('tvuj obrázek byl uložen')


url = 'https://www.python.org/static/img/python-logo@2x.png'

download_image2(url)
