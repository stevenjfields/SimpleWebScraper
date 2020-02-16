import requests
from bs4 import BeautifulSoup

def ScrapeFightCards(conn):
    ufc_fight_card_list = 'http://ufcstats.com/statistics/events/completed?page=all'
    response = requests.get(ufc_fight_card_list)
    content = BeautifulSoup(response.content, 'html.parser')
    table_rows = content.find_all('tr')
    for table_row in table_rows:

def ScrapeFightStats(conn):