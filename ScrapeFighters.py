import requests
from bs4 import BeautifulSoup
import string
import Fighter
from Fighter import Fighter

# Input url
def ScrapeFighters(conn):
    db_conn = conn.cursor()
    ufc_fighters_page = 'http://ufcstats.com/statistics/fighters?char=!&page=all'
    for char in string.ascii_lowercase:
        url = ufc_fighters_page.replace('!', char)
        response = requests.get(url)
        content = BeautifulSoup(response.content, 'html.parser')
        table_rows = content.find_all('tr')
        for table_row in table_rows:
            link = table_row.find('a')
            if link is not None:
                details_response = requests.get(link['href'])
                details_content = BeautifulSoup(details_response.content, 'html.parser')
                fighter_stats = []
                name = details_content.find('span', attrs={'class':'b-content__title-highlight'})
                fighter_stats.append(name.text.lstrip().rstrip())
                stats = details_content.find('ul')
                info = stats.find_all('li', attrs={'class':'b-list__box-list-item_type_block'})
                for stat in info:
                    i = stat.find('i')
                    i.decompose()
                    fighter_stats.append(stat.text.lstrip().rstrip())        
                nickname = details_content.find('p', attrs={'class':'b-content__Nickname'})
                if nickname is not None:
                    fighter_stats.append(nickname.text.lstrip().rstrip())
                else:
                    fighter_stats.append('')
                print(fighter_stats)
                this_fighter = Fighter(fighter_stats)
                this_fighter.save(db_conn)
                conn.commit()    

if __name__ == '__main__':
    import sqlite3
    conn = sqlite3.connect('MMA.db')
    ScrapeFighters(conn)