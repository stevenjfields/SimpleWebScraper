import sqlite3

class Fight:
    Red_Corner = 0
    Blue_Corner = 0
    R_Knockdowns = 0
    R_Sig_Str_Landed = 0
    R_Sig_Str_Attempted = 0
    R_Total_Str_Landed = 0
    R_Total_Str_Attempted = 0
    R_Takedowns_Landed = 0
    R_Takedowns_Attempted = 0
    R_Submissions_Attempted = 0
    R_Passes = 0
    R_Reversals = 0
    B_Knockdowns = 0
    B_Sig_Str_Landed = 0
    B_Sig_Str_Attempted = 0
    B_Total_Str_Landed = 0
    B_Total_Str_Attempted = 0
    B_Takedowns_Landed = 0
    B_Takedowns_Attempted = 0
    B_Submissions_Attempted = 0
    B_Passes = 0
    B_Reversals = 0
    Ref = ""
    Date = ""
    FightCard = ""
    Winner = 0
    Outcome = ""
    Weightclass = ""
    Location = ""

    class __init__(self):
        pass

    class __init__(self, fight_info):
        self.Red_Corner = fight_info[0]
        self.Blue_Corner = fight_info[1]
        self.R_Knockdowns = fight_info[2]
        self.R_Sig_Str_Landed = fight_info[3]
        self.R_Sig_Str_Attempted = fight_info[4]
        self.R_Total_Str_Landed = fight_info[5]
        self.R_Total_Str_Attempted = fight_info[6]
        self.R_Takedowns_Landed = fight_info[7]
        self.R_Takedowns_Attempted = fight_info[8]
        self.R_Submissions_Attempted = fight_info[9]
        self.R_Passes = fight_info[10]
        self.R_Reversals = fight_info[11]
        self.B_Knockdowns = fight_info[12]
        self.B_Sig_Str_Landed = fight_info[13]
        self.B_Sig_Str_Attempted = fight_info[14]
        self.B_Total_Str_Landed = fight_info[15]
        self.B_Total_Str_Attempted = fight_info[16]
        self.B_Takedowns_Landed = fight_info[17]
        self.B_Takedowns_Attempted = fight_info[18]
        self.B_Submissions_Attempted = fight_info[19]
        self.B_Passes = fight_info[20]
        self.B_Reversals = fight_info[21]
        self.Ref = fight_info[22]
        self.Date = fight_info[23]
        self.FightCard = fight_info[24]
        self.Winner = fight_info[25]
        self.Outcome = fight_info[26]
        self.Weightclass = fight_info[27]
        self.Location = fight_info[28]

    def save(self, db_conn):
        sql = '''INSERT INTO Fights (Red_Corner, Blue_Corner, R_Knockdowns,
                R_Sig_Str_Landed, R_Sig_Str_Attempted, R_Total_Str_Landed,
                R_Total_Str_Attempted, R_Takedowns_Landed, R_Takedowns_Attempted,
                R_Submissions_Attempted, R_Passes, R_Reversals,
                B_Knockdowns, B_Sig_Str_Landed, B_Sig_Str_Attempted,
                B_Total_Str_Landed, B_Total_Str_Attempted, B_Takedowns_Landed,
                B_Takedowns_Attempted, B_Submissions_Attempted, B_Passes, B_Reversals,
                Ref, Date, FightCard, Winner, Outcome, Weightclass, Location)
                VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''

                db_conn.execute(sql, (self.Red_Corner, self.Blue_Corner,
                    self.R_Knockdowns, self.R_Sig_Str_Landed, self.R_Sig_Str_Attempted,
                    self.R_Total_Str_Landed, self.R_Total_Str_Attempted,
                    self.R_Takedowns_Landed, self.R_Takedowns_Attempted,
                    self.R_Submissions_Attempted, self.R_Passes, self.R_Reversals,
                    self.B_Knockdowns, self.B_Sig_Str_Landed, self.B_Sig_Str_Attempted,
                    self.B_Total_Str_Landed, self.B_Total_Str_Attempted,
                    self.B_Takedowns_Landed, self.B_Takedowns_Attempted,
                    self.B_Submissions_Attempted, self.B_Passes, self.B_Reversals,
                    self.Ref, self.Date, self.FightCard, self.Winner,
                    self.Outcome, self.Weightclass, self.Location))
