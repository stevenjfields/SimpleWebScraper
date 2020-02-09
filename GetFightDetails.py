import requests
import sqlite3
from bs4 import BeautifulSoup as bs
Debug = False

def GetFightDetails(url):
    response = requests.get(url)
    content = bs(response.content, "html.parser")
    if Debug:
        # print(content.prettify)
        pass

    lists = []
    tables = content.find_all('table')
    for table in tables:
        bodies = table.find_all('tbody')
        for body in bodies:
            rows = body.find_all('tr')
            for row in rows:
                list1 = []
                list2 = []
                stats = row.find_all('td', attrs={'class':'b-fight-details__table-col'})
                for stat in stats:
                    values = stat.find_all('p')
                    list1.append(values[0].text.lstrip().rstrip())
                    list2.append(values[1].text.lstrip().rstrip())
                lists.append(list1)
                lists.append(list2)
    # Two types of lists:
    # List one: Name, Knockdowns, Sig. Str. (x of y), Sig. Str. %, Total Str. (x of y), Takedowns (x of y), TD %, Sub. Att., Pass, Reversals
    # List two: Name, Sig. Str. (x of y), Sig. Str. %, Head (x of y), Body (x of y), Leg (x of y), Distance (x of y), Clinch (x of y), Ground (x of y)

    fighter1 = []
    fighter2 = []
    switch = True
    for this_list in lists:
        if switch:
            fighter1.append(this_list)
            switch = False
        else:
            fighter2.append(this_list)
            switch = True

    if Debug:
        for this_list in lists:
            for item in this_list:
                print(item)
        print(fighter1)
        print(fighter2)

if __name__ == '__main__':
    Debug = True
    GetFightDetails('http://www.ufcstats.com/fight-details/82177c0f91d9618a')
    #GetFightDetails('http://www.ufcstats.com/fight-details/eed6c9aff2234b7a')