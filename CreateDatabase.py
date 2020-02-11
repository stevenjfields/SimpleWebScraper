import sqlite3
DB_NAME = 'MMA.db'

def CreateDB():
    conn = sqlite3.connect(DB_NAME)
    db = conn.cursor()

    # Fight table
  
    # Fighters table
    db.execute('''CREATE TABLE Fighters
                (FighterID INTEGER PRIMARY KEY AUTOINCREMENT,
                Name text, Height text, Weight text,
                Reach text, Stance text, DOB text,
                Nickname text)''')

    # Fight table
    db.execute('''CREATE TABLE Fights
                (FightID INTEGER PRIMARY KEY AUTOINCREMENT, 
                Red_Corner int NOT NULL, Blue_Corner int NOT NULL,
                R_Knockdowns tinyint, R_Sig_Str_Landed smallint, R_Sig_Str_Attempted smallint,
                R_Total_Str_Landed smallint, R_Total_Str_Attemped smallint,
                R_Takedowns_Landed tinyint, R_Takedowns_Attempted tinyint,
                R_Submissions_Attempted tinyint, R_Passes tinyint, R_Reversals tinyint,
                B_Knockdowns tinyint, B_Sig_Str_Landed smallint, B_Sig_Str_Attempted smallint,
                B_Total_Str_Landed smallint, B_Total_Str_Attemped smallint,
                B_Takedowns_Landed tinyint, B_Takedowns_Attempted tinyint,
                B_Submissions_Attempted tinyint, B_Passes tinyint, B_Reversals tinyint,
                Ref text, Date text, FightCard text, Winner int, Outcome text,
                Weightclass text, Location text,
                FOREIGN KEY (Red_Corner) REFERENCES Fighters(FighterID),
                FOREIGN KEY (Blue_Corner) REFERENCES Fighters(FighterID),
                FOREIGN KEY (Winner) REFERENCES Fighters(FighterID))''')
    
    # Round table
    db.execute('''CREATE TABLE Round
                (RoundID int NOT NULL, FightID int NOT NULL, Knockdowns tinyint, 
                Sig_Str_Landed smallint, Sig_Str_Attempted smallint,
                Total_Str_Landed smallint, Total_Str_Attemped smallint,
                Takedowns_Landed tinyint, Takedowns_Attempted tinyint,
                Submissions_Attempted tinyint, Passes tinyint, Reversals tinyint,
                PRIMARY KEY (RoundID),
                FOREIGN KEY (FightID) REFERENCES Fight(FightID))''')

if __name__ == '__main__':
    CreateDB()