import requests
from bs4 import BeautifulSoup

# Go through each fight card, retieving some data and passing it on.
def ScrapeFightCards(conn):
    ufc_fight_card_list = 'http://ufcstats.com/statistics/events/completed?page=all'
    response = requests.get(ufc_fight_card_list)
    content = BeautifulSoup(response.content, 'html.parser')
    table_body = content.find('tbody')
    table_rows = table_body.find_all('tr')
    table_rows = table_rows[1:]
    for table_row in table_rows:
        upcoming = table_row.find('img')
        if upcoming is None:
            fight_card_url = table_row.find('a')
            fight_card = fight_card_url.text.lstrip().rstrip()
            date = table_row.find('span', attrs={'class':'b-statistics__date'}).text.lstrip().rstrip()
            location = table_row.find('td', attrs={'class':
                'b-statistics__table-col b-statistics__table-col_style_big-top-padding'}
                ).text.lstrip().rstrip()
            ScrapeFights(conn, fight_card_url['href'], date, fight_card, location)

# Go through each fight on a fight card, retrieving winner and passing it on.
def ScrapeFights(conn, url, date, fight_card, location):
    response = requests.get(url)
    content = BeautifulSoup(response.content, 'html.parser')
    table_body = content.find('tbody')
    table_rows = table_body.find_all('tr')
    for table_row in table_rows:
        fighters = table_row.find('td', attrs={'style':'width:100px',
        'class':'b-fight-details__table-col l-page_align_left'})
        winner = fighters.find('p').text.lstrip().rstrip()
        ScrapeFight(conn, table_row.get('data-link'), date, fight_card, location, winner)

# Create a record of each fight, passing data on for the rounds.
def ScrapeFight(conn, url, date, fight_card, location, winner):
    pass

# Create round by round entries for the fight that calls this method.
def ScrapeRounds(url):
    pass

if __name__ == '__main__':
    import sqlite3
    conn = sqlite3.connect('MMA.db')
    ScrapeFightCards(conn)