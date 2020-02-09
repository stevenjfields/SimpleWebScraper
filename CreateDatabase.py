import sqlite3
DB_NAME = 'MMA.db'

def CreateDB():
    conn = sqlite3.connect(DB_NAME)
    db = conn.cursor()

    # Fight table
  
    # Fighters table
    db.execute('''CREATE TABLE Fighters
                (Name text, Height text, Weight text, Reach text
                Stance text, DOB text)''')
    
    # Round table
    db.execute('''CREATE TABLE Round
                (RoundID int NOT NULL, FightID int NOT NULL, Knockdowns tinyint, 
                Sig_Str_Landed smallint, Sig_Str_Attempted smallint,
                Total_Str_Landed smallint, Total_Str_Attemped smallint,
                Takedowns_Landed tinyint, Takedowns_Attempted tinyint,
                Submissions_Attempted tinyint, Passes tinyint, Reversals tinyint,
                PRIMARY KEY (RoundID),
                FOREIGN KEY (FightID) REFERENCES Fight(FightID))''')
    
    # Fight table
