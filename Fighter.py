import sqlite3

class Fighter:
    Name = ""
    Height = ""
    Weight = ""
    Reach = ""
    Stance = ""
    DOB = ""
    db = None

    def __init__(self):
        pass

    def __init__(self, info_list):
        self.Name = info_list[0]
        self.Height = info_list[1]
        self.Weight = info_list[2][:3]
        self.Reach = info_list[3]
        self.Stance = info_list[4]
        self.DOB = info_list[5]
        self.db = db_conn

    def save(self, db_conn):
        sql = ('''INSERT INTO Fighters (Name, Height, Weight, Reach, Stance, DOB) 
        Values(?, ?, ?, ?, ?, ?);''')

        db_conn.execute(sql, (self.Name, self.Height, self.Weight, self.Reach, self.Stance, self.DOB))
        self.print_fighter()

    def print_fighter(self):
        print(f'{self.Name}, {self.Height}, {self.Weight}, {self.Reach}, {self.Stance}, {self.DOB}')

if __name__ == '__main__':
    # For Debug Purposes Only
    import requests
    from bs4 import BeautifulSoup

    conn = sqlite3.connect('MMA.db')
    db_conn = conn.cursor()

    response = requests.get('http://ufcstats.com/fighter-details/07f72a2a7591b409')
    content = BeautifulSoup(response.content, 'html.parser')

    fighter_stats = []

    name = content.find('span', attrs={'class':'b-content__title-highlight'})
    fighter_stats.append(name.text.lstrip().rstrip())
    print(fighter_stats)

    stats = content.find('ul')
    info = stats.find_all('li', attrs={'class':'b-list__box-list-item_type_block'})
    for stat in info:
        i = stat.find('i')
        i.decompose()
        fighter_stats.append(stat.text.lstrip().rstrip())

    this_fighter = Fighter(fighter_stats)
    this_fighter.save(db_conn)
    conn.commit()