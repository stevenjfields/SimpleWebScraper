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
        self.FightID = fight_info[0]
        self.R_Knockdowns = fight_info[1]
        self.R_Sig_Str_Landed = fight_info[2]
        self.R_Sig_Str_Attempted = fight_info[3]
        self.R_Total_Str_Landed = fight_info[4]
        self.R_Total_Str_Attempted = fight_info[5]
        self.R_Takedowns_Landed = fight_info[6]
        self.R_Takedowns_Attempted = fight_info[7]
        self.R_Submissions_Attempted = fight_info[8]
        self.R_Passes = fight_info[9]
        self.R_Reversals = fight_info[10]
        self.R_Head_Strikes_Landed[11]
        self.R_Head_Strikes_Attempted[12]
        self.R_Body_Strikes_Landed[13]
        self.R_Body_Strikes_Attempted[14]
        self.R_Leg_Strikes_Landed[15]
        self.R_Leg_Strikes_Attempted[16]
        self.R_Distance_Strikes_Landed[17]
        self.R_Distance_Strikes_Attempted[18]
        self.R_Clinch_Strikes_Landed[19]
        self.R_Clinch_Strikes_Attempted[20]
        self.R_Ground_Strikes_Landed[21]
        self.R_Ground_Strikes_Attempted[22]
        self.B_Knockdowns = fight_info[23]
        self.B_Sig_Str_Landed = fight_info[24]
        self.B_Sig_Str_Attempted = fight_info[25]
        self.B_Total_Str_Landed = fight_info[26]
        self.B_Total_Str_Attempted = fight_info[27]
        self.B_Takedowns_Landed = fight_info[28]
        self.B_Takedowns_Attempted = fight_info[29]
        self.B_Submissions_Attempted = fight_info[30]
        self.B_Passes = fight_info[31]
        self.B_Reversals = fight_info[32]
        self.B_Head_Strikes_Landed[33]
        self.B_Head_Strikes_Attempted[34]
        self.B_Body_Strikes_Landed[35]
        self.B_Body_Strikes_Attempted[36]
        self.B_Leg_Strikes_Landed[37]
        self.B_Leg_Strikes_Attempted[38]
        self.B_Distance_Strikes_Landed[39]
        self.B_Distance_Strikes_Attempted[40]
        self.B_Clinch_Strikes_Landed[41]
        self.B_Clinch_Strikes_Attempted[42]
        self.B_Ground_Strikes_Landed[43]
        self.B_Ground_Strikes_Attempted[44]
        self.RoundNumber = fight_info[45]

    #Need to adjust for added variables above
    def save(self, db_conn):
        sql = '''INSERT INTO Round (FightID, R_Knockdowns,
                R_Sig_Str_Landed, R_Sig_Str_Attempted, R_Total_Str_Landed,
                R_Total_Str_Attempted, R_Takedowns_Landed, R_Takedowns_Attempted,
                R_Submissions_Attempted, R_Passes, R_Reversals,
                B_Knockdowns, B_Sig_Str_Landed, B_Sig_Str_Attempted,
                B_Total_Str_Landed, B_Total_Str_Attempted, B_Takedowns_Landed,
                B_Takedowns_Attempted, B_Submissions_Attempted, B_Passes, B_Reversals,
                RoundNumber)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
        
        db_conn.execute(sql, 
        (self.FightID, self.R_Knockdowns, 
        self.R_Sig_Str_Landed, self.R_Sig_Str_Attempted, 
        self.R_Total_Str_Landed, self.R_Total_Str_Attempted,
        self.R_Takedowns_Landed, self.R_Takedowns_Attempted,
        self.R_Submissions_Attempted, self.R_Passes,
        self.R_Reversals, self.B_Knockdowns,
        self.B_Sig_Str_Landed, self.B_Sig_Str_Attempted,
        self.B_Total_Str_Landed, self.B_Total_Str_Attempted,
        self.B_Takedowns_Landed, self.B_Takedowns_Attempted,
        self.B_Submissions_Attempted, self.B_Passes,
        self.B_Reversals, self.RoundNumber))

if __name__ == '__main__':
    # For Debug Purposes Only
    conn = sqlite33.connect('MMA.db')
    db_conn = conn.cursor()

    test_stats = [1, ]