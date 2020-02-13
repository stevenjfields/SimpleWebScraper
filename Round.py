import sqlite3

class Round:
    FightID = 0
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
    R_Head_Strikes_Landed = 0
    R_Head_Strikes_Attempted = 0
    R_Body_Strikes_Landed = 0
    R_Body_Strikes_Attempted = 0
    R_Leg_Strikes_Landed = 0
    R_Leg_Strikes_Attempted = 0
    R_Distance_Strikes_Landed = 0
    R_Distance_Strikes_Attempted = 0
    R_Clinch_Strikes_Landed = 0
    R_Clinch_Strikes_Attempted = 0
    R_Ground_Strikes_Landed = 0
    R_Ground_Strikes_Attempted = 0
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
    B_Head_Strikes_Landed = 0
    B_Head_Strikes_Attempted = 0
    B_Body_Strikes_Landed = 0
    B_Body_Strikes_Attempted = 0
    B_Leg_Strikes_Landed = 0
    B_Leg_Strikes_Attempted = 0
    B_Distance_Strikes_Landed = 0
    B_Distance_Strikes_Attempted = 0
    B_Clinch_Strikes_Landed = 0
    B_Clinch_Strikes_Attempted = 0
    B_Ground_Strikes_Landed = 0
    B_Ground_Strikes_Attempted = 0
    RoundNumber = 0

    def __init__(self):
        pass

    def __init__(self, stat_list):
        self.FightID = stat_list[0]
        self.R_Knockdowns = stat_list[1]
        self.R_Sig_Str_Landed = stat_list[2]
        self.R_Sig_Str_Attempted = stat_list[3]
        self.R_Total_Str_Landed = stat_list[4]
        self.R_Total_Str_Attempted = stat_list[5]
        self.R_Takedowns_Landed = stat_list[6]
        self.R_Takedowns_Attempted = stat_list[7]
        self.R_Submissions_Attempted = stat_list[8]
        self.R_Passes = stat_list[9]
        self.R_Reversals = stat_list[10]
        self.R_Head_Strikes_Landed = stat_list[11]
        self.R_Head_Strikes_Attempted = stat_list[12]
        self.R_Body_Strikes_Landed = stat_list[13]
        self.R_Body_Strikes_Attempted = stat_list[14]
        self.R_Leg_Strikes_Landed = stat_list[15]
        self.R_Leg_Strikes_Attempted = stat_list[16]
        self.R_Distance_Strikes_Landed = stat_list[17]
        self.R_Distance_Strikes_Attempted = stat_list[18]
        self.R_Clinch_Strikes_Landed = stat_list[19]
        self.R_Clinch_Strikes_Attempted = stat_list[20]
        self.R_Ground_Strikes_Landed = stat_list[21]
        self.R_Ground_Strikes_Attempted = stat_list[22]
        self.B_Knockdowns = stat_list[23]
        self.B_Sig_Str_Landed = stat_list[24]
        self.B_Sig_Str_Attempted = stat_list[25]
        self.B_Total_Str_Landed = stat_list[26]
        self.B_Total_Str_Attempted = stat_list[27]
        self.B_Takedowns_Landed = stat_list[28]
        self.B_Takedowns_Attempted = stat_list[29]
        self.B_Submissions_Attempted = stat_list[30]
        self.B_Passes = stat_list[31]
        self.B_Reversals = stat_list[32]
        self.B_Head_Strikes_Landed = stat_list[33]
        self.B_Head_Strikes_Attempted = stat_list[34]
        self.B_Body_Strikes_Landed = stat_list[35]
        self.B_Body_Strikes_Attempted = stat_list[36]
        self.B_Leg_Strikes_Landed = stat_list[37]
        self.B_Leg_Strikes_Attempted = stat_list[38]
        self.B_Distance_Strikes_Landed = stat_list[39]
        self.B_Distance_Strikes_Attempted = stat_list[40]
        self.B_Clinch_Strikes_Landed = stat_list[41]
        self.B_Clinch_Strikes_Attempted = stat_list[42]
        self.B_Ground_Strikes_Landed = stat_list[43]
        self.B_Ground_Strikes_Attempted = stat_list[44]
        self.RoundNumber = stat_list[45]

    #Need to adjust for added variables above
    def save(self, db_conn):
        sql = '''INSERT INTO Round (FightID, R_Knockdowns,
        R_Sig_Str_Landed, R_Sig_Str_Attempted,
        R_Total_Str_Landed, R_Total_Str_Attempted,
        R_Takedowns_Landed, R_Takedowns_Attempted,
        R_Submissions_Attempted, R_Passes, R_Reversals,
        R_Head_Strikes_Landed, R_Head_Strikes_Attempted,
        R_Body_Strikes_Landed, R_Body_Strikes_Attempted,
        R_Leg_Strikes_Landed, R_Leg_Strikes_Attempted,
        R_Distance_Strikes_Landed, R_Distance_Strikes_Attempted,
        R_Clinch_Strikes_Landed, R_Clinch_Strikes_Attempted,
        R_Ground_Strikes_Landed, R_Ground_Strikes_Attempted,
        B_Knockdowns, B_Sig_Str_Landed, B_Sig_Str_Attempted,
        B_Total_Str_Landed, B_Total_Str_Attempted, B_Takedowns_Landed,
        B_Takedowns_Attempted, B_Submissions_Attempted, B_Passes,
        B_Reversals, B_Head_Strikes_Landed, B_Head_Strikes_Attempted,
        B_Body_Strikes_Landed, B_Body_Strikes_Attempted,
        B_Leg_Strikes_Landed, B_Leg_Strikes_Attempted,
        B_Distance_Strikes_Landed, B_Distance_Strikes_Attempted,
        B_Clinch_Strikes_Landed, B_Clinch_Strikes_Attempted,
        B_Ground_Strikes_Landed, B_Ground_Strikes_Attempted, RoundNumber)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
        
        db_conn.execute(sql, 
        (self.FightID, self.R_Knockdowns,
        self.R_Sig_Str_Landed, self.R_Sig_Str_Attempted,
        self.R_Total_Str_Landed, self.R_Total_Str_Attempted,
        self.R_Takedowns_Landed, self.R_Takedowns_Attempted,
        self.R_Submissions_Attempted, self.R_Passes,
        self.R_Reversals, self.R_Head_Strikes_Landed,
        self.R_Head_Strikes_Attempted, self.R_Body_Strikes_Landed,
        self.R_Body_Strikes_Attempted, self.R_Leg_Strikes_Landed,
        self.R_Leg_Strikes_Attempted, self.R_Distance_Strikes_Landed,
        self.R_Distance_Strikes_Attempted, self.R_Clinch_Strikes_Landed,
        self.R_Clinch_Strikes_Attempted, self.R_Ground_Strikes_Landed,
        self.R_Ground_Strikes_Attempted, self.B_Knockdowns,
        self.B_Sig_Str_Landed, self.B_Sig_Str_Attempted,
        self.B_Total_Str_Landed, self.B_Total_Str_Attempted,
        self.B_Takedowns_Landed, self.B_Takedowns_Attempted,
        self.B_Submissions_Attempted, self.B_Passes, self.B_Reversals,
        self.B_Head_Strikes_Landed, self.B_Head_Strikes_Attempted,
        self.B_Body_Strikes_Landed, self.B_Body_Strikes_Attempted,
        self.B_Leg_Strikes_Landed, self.B_Leg_Strikes_Attempted,
        self.B_Distance_Strikes_Landed, self.B_Distance_Strikes_Attempted,
        self.B_Clinch_Strikes_Landed, self.B_Clinch_Strikes_Attempted,
        self.B_Ground_Strikes_Landed, self.B_Ground_Strikes_Attempted,
        self.RoundNumber))

if __name__ == '__main__':
    # For Debug Purposes Only
    conn = sqlite3.connect('MMA.db')
    db_conn = conn.cursor()

    round1 = [1, 0, 17, 27, 17, 27, 0, 2, 0, 0, 0, 1, 5, 6, 8, #15
                    10, 14, 17, 26, 0, 1, 0, 0, 0, 23, 59, 23, 59, 0, #13
                    0, 0, 0, 0, 7, 33, 11, 14, 5, 12, 20, 56, 3, 3, #14
                    0, 0, 1]                                       #3
    round2 = [1, 0, 22, 37, 22, 37, 0, 0, 0, 0, 0, 8, 19, 5, 7,
                    9, 11, 22, 37, 0, 0, 0, 0, 0, 33, 68, 33, 68, 0,
                    0, 0, 0, 0, 11, 46, 12, 12, 10, 10, 33, 68, 0, 0,
                    0, 0, 2]
    round3 = [1, 0, 19, 34, 20, 35, 0, 2, 0, 0, 0, 7, 18, 5, 7,
                    7, 9, 19, 34, 0, 0, 0, 0, 0, 26, 45, 27, 46, 0,
                    0, 0, 0, 0, 7, 25, 13, 14, 6, 6, 23, 42, 3, 3,
                    0, 0, 3]
    round4 = [1, 0, 20, 34, 20, 35, 1, 3, 0, 0, 0, 8, 19, 6, 8,
                    6, 7, 17, 30, 3, 4, 0, 0, 0, 13, 41, 14, 42, 0,
                    0, 0, 0, 0, 7, 32, 4, 7, 2, 2, 12, 40, 1, 1,
                    0, 0, 4]
    round5 = [1, 0, 26, 34, 28, 36, 1, 2, 0, 0, 0, 7, 13, 8, 9,
                    11, 12, 26, 34, 0, 0, 0, 0, 0, 21, 46, 22, 48, 0,
                    0, 0, 0, 0, 9, 33, 8, 8, 4, 5, 21, 46, 0, 0,
                    0, 0, 5]

    this_round = Round(round1)
    this_round.save(db_conn)
    this_round = Round(round2)
    this_round.save(db_conn)
    this_round = Round(round3)
    this_round.save(db_conn)
    this_round = Round(round4)
    this_round.save(db_conn)
    this_round = Round(round5)
    this_round.save(db_conn)
    conn.commit()