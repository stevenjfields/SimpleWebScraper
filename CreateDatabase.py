import sqlite3
DB_NAME = 'MMA.db'

def CreateDB():
    conn = sqlite3.connect(DB_NAME)
    db = conn.cursor()
  
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
                Ref text, Date text, FightCard text, Winner int, Outcome text,
                Weightclass text, Location text, Rounds tinyint,
                FOREIGN KEY (Red_Corner) REFERENCES Fighters(FighterID),
                FOREIGN KEY (Blue_Corner) REFERENCES Fighters(FighterID),
                FOREIGN KEY (Winner) REFERENCES Fighters(FighterID))''')
    
    # Round table
    db.execute('''CREATE TABLE Round
                (RoundID INTEGER PRIMARY KEY AUTOINCREMENT,
                FightID int NOT NULL,
                R_Knockdowns tinyint, R_Sig_Str_Landed smallint, R_Sig_Str_Attempted smallint,
                R_Total_Str_Landed smallint, R_Total_Str_Attempted smallint,
                R_Takedowns_Landed tinyint, R_Takedowns_Attempted tinyint,
                R_Submissions_Attempted tinyint, R_Passes tinyint, R_Reversals tinyint,
                R_Head_Strikes_Landed smallint, R_Head_Strikes_Attempted smallint,
                R_Body_Strikes_Landed smallint, R_Body_Strikes_Attempted smallint,
                R_Leg_Strikes_Landed smallint, R_Leg_Strikes_Attempted smallint,
                R_Distance_Strikes_Landed smallint, R_Distance_Strikes_Attempted smallint,
                R_Clinch_Strikes_Landed smallint, R_Clinch_Strikes_Attempted smallint,
                R_Ground_Strikes_Landed smallint, R_Ground_Strikes_Attempted smallint,
                B_Knockdowns tinyint, B_Sig_Str_Landed smallint, B_Sig_Str_Attempted smallint,
                B_Total_Str_Landed smallint, B_Total_Str_Attempted smallint,
                B_Takedowns_Landed tinyint, B_Takedowns_Attempted tinyint,
                B_Submissions_Attempted tinyint, B_Passes tinyint, B_Reversals tinyint,
                B_Head_Strikes_Landed smallint, B_Head_Strikes_Attempted smallint,
                B_Body_Strikes_Landed smallint, B_Body_Strikes_Attempted smallint,
                B_Leg_Strikes_Landed smallint, B_Leg_Strikes_Attempted smallint,
                B_Distance_Strikes_Landed smallint, B_Distance_Strikes_Attempted smallint,
                B_Clinch_Strikes_Landed smallint, B_Clinch_Strikes_Attempted smallint,
                B_Ground_Strikes_Landed smallint, B_Ground_Strikes_Attempted smallint,
                RoundNumber tinyint,
                FOREIGN KEY (FightID) REFERENCES Fight(FightID))''')

if __name__ == '__main__':
    CreateDB()

    # SELECT Fights.FightCard, f1.Name Red_Corner, SUM(rounds.R_Sig_Str_Landed), f2.Name Blue_Corner, SUM(rounds.B_Sig_Str_Landed)
    # FROM Fights
    # LEFT JOIN Fighters f1 on (Fights.Red_Corner=f1.FighterID)
    # LEFT JOIN Fighters f2 on (Fights.Blue_Corner=f2.FighterID)
    # LEFT JOIN Round rounds ON (Fights.FightID=Round.FightID)

    # Select SUM(R_Sig_Str_Landed)
    # From Round
    # where Round.FightID = 1