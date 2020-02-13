import requests
from bs4 import BeautifulSoup
import string

# Input url
def ScrapeFighters():
    ufc_fighters_page = 'http://ufcstats.com/statistics/fighters?char=!&page=all'
    for char in string.ascii_lowercase:
        print(ufc_fighters_page.replace('!', char))

if __name__ == '__main__':
    ScrapeFighters()