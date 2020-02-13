import sqlite3

class Fight:
    Red_Corner = 0
    Blue_Corner = 0
    Ref = ""
    Date = ""
    FightCard = ""
    Winner = 0
    Outcome = ""
    Weightclass = ""
    Location = ""
    Rounds = 0

    def __init__(self):
        pass

    def __init__(self, fight_info):
        self.Red_Corner = fight_info[0]
        self.Blue_Corner = fight_info[1]
        self.Ref = fight_info[2]
        self.Date = fight_info[3]
        self.FightCard = fight_info[4]
        self.Winner = fight_info[5]
        self.Outcome = fight_info[6]
        self.Weightclass = fight_info[7]
        self.Location = fight_info[8]
        self.Rounds = fight_info[9]

    def save(self, db_conn):
        sql = '''INSERT INTO Fights (Red_Corner, Blue_Corner, Ref,
                Date, FightCard, Winner, Outcome, Weightclass, Location, Rounds)
                VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''

        db_conn.execute(sql, (self.Red_Corner, self.Blue_Corner,
            self.Ref, self.Date, self.FightCard, self.Winner,
            self.Outcome, self.Weightclass, self.Location, self.Rounds))

if __name__ == '__main__':
    # For Debug Purposes Only
    conn = sqlite3.connect('MMA.db')
    db_conn = conn.cursor()

    test_stats = [1, 2, 'Dan Miragliotta', 'February 08, 2020', 
                    'UFC 247: Jones vs. Reyes', 1, 'U-Dec',
                    'Light Heavyweight', 'Houston, Texas, USA', 5]

    this_fight = Fight(test_stats)
    this_fight.save(db_conn)
    conn.commit()