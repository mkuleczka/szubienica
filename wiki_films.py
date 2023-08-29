import requests
from bs4 import BeautifulSoup
import re


def get_list_polish_fairy_tails(name="https://pl.wikipedia.org/wiki/Kategoria:Polskie_filmy_dla_dzieci_i_młodzieży"):
    url_address = requests.get(name)
    soup = BeautifulSoup(url_address.content, 'html.parser')

    film_list = []
    for i in soup.find_all('a', href=True, title=True):
        if i['href'][0:6] == '/wiki/' and not re.search(r":", i['href']):
            title = i['title']
            if title.find('(') != -1:
                b = title.index('(')
                title = title[:b - 1]
            film_list.append(title)

    return film_list


url_1 = "https://pl.wikipedia.org/w/index.php?title=Kategoria:Amerykańskie_filmy_dla_dzieci_i_młodzieży" \
        "&pageuntil=Scooby-Doo%21%3A+Pora+księżycowego+potwora#mw-pages"
url_2 = "https://pl.wikipedia.org/w/index.php?title=Kategoria:Amerykańskie_filmy_dla_dzieci_i_młodzieży" \
        "&pagefrom=Scooby-Doo%21%3A+Pora+księżycowego+potwora#mw-pages"


def get_list_american_fairy_tails(name=(url_1, url_2)):
    film_list = []
    for url_ in range(len(name)):
        url_address = requests.get(name[url_])
        soup = BeautifulSoup(url_address.content, 'html.parser')

        list_ = []
        for i in soup.find_all('a', href=True, title=True):
            if i['href'][0:6] == '/wiki/':
                title = i['title']
                if title.find('(') != -1:
                    b = title.index('(')
                    title = title[:b - 1]
                list_.append(title)

        unnecessary_1 = list_.index('Kategoria:Amerykańskie telewizyjne seriale dla dzieci i młodzieży')
        unnecessary_2 = list_.index('Specjalna:Kategorie')
        film_list += list_[unnecessary_1 + 1:unnecessary_2]

    return film_list