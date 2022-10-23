import sqlite3
import random

class League():
    def __init__(self):
        self.connect()
    
    def connect(self):
        self.con = sqlite3.connect("library.db")
        self.cursor = self.con.cursor()

    def disconnect(self):
        self.con.close()

    def create_teams_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Teams (Name Text, Overall INT, Budget[M] INT, Points INT, Wins INT, Loses INT, Draws INT)")
        self.con.commit()

    def create_seasons_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Seasons (Year INT, Champion TEXT, Second TEXT, Third TEXT)")
        self.con.commit()

    def add_seasons_data(self,year,champ,sec,third):
        self.cursor.execute("INSERT INTO Seasons VALUES(?,?,?,?)",(year,champ,sec,third))
        self.con.commit()

    def add_teams_data(self,name,overall,budget,points,wins,loses,draws):
        self.cursor.execute("INSERT INTO Teams VALUES(?,?,?,?,?,?,?)",(name,overall,budget,points,wins,loses,draws))
        self.con.commit()

    def increase_win(self,name):
        statement = "SELECT Wins FROM Teams where Name = ?"
        statement2 = "UPDATE Teams Set Wins = ? where Name = ?"

        self.cursor.execute(statement,(name,))
        number = self.cursor.fetchall()
        new_number = number[0][0]
        new_number += 1

        self.cursor.execute(statement2,(new_number,name,))
        self.con.commit()
    
    def increase_lose(self,name):
        statement = "SELECT Loses FROM Teams where Name = ?"
        statement2 = "UPDATE Teams Set Loses = ? where Name = ?"

        self.cursor.execute(statement,(name,))
        number = self.cursor.fetchall()
        new_number = number[0][0]
        new_number += 1

        self.cursor.execute(statement2,(new_number,name,))
        self.con.commit()

    def increase_draw(self,name):
        statement = "SELECT Draws FROM Teams where Name = ?"
        statement2 = "UPDATE Teams Set Draws = ? where Name = ?"

        self.cursor.execute(statement,(name,))
        number = self.cursor.fetchall()
        new_number = number[0][0]
        new_number += 1

        self.cursor.execute(statement2,(new_number,name,))
        self.con.commit()

    def calculate_overall(self):
        pass

    def calculate_points(self):
        statement = "SELECT Name,Wins,Draws FROM Teams"
        statement2 = "UPDATE Teams SET Points = ? where Name = ?"
        self.cursor.execute(statement)
        team_list = self.cursor.fetchall()
        for i in team_list:
            points = i[1] * 3 + i[2] * 1
            self.cursor.execute(statement2,(points,i[0]))
            self.con.commit()

    def update_budget(self,name,new_budget):
        statement = "UPDATE Teams SET Budget = ? where Name = ?"
        
        self.cursor.execute(statement,(new_budget,name,))
        self.con.commit()
    
    def update_overall(self,name,ovr):
        statement = "UPDATE Teams SET Overall = ? where Name = ?"

        self.cursor.execute(statement,(ovr,name,))
        self.con.commit()

    def reset_database(self):
        statement = "SELECT * FROM Teams"
        statement2 = "UPDATE Teams SET Wins = 0 where Name = ?"
        statement3 = "UPDATE Teams SET Loses = 0 where Name = ?"
        statement4 = "UPDATE Teams SET Draws = 0 where Name = ?"
        statement5 = "UPDATE Teams SET Budget = 100 where Name = ?"

        self.cursor.execute(statement)
        team_list = self.cursor.fetchall()

        for i in team_list:
            self.cursor.execute(statement2,(i[0],))
            self.cursor.execute(statement3,(i[0],))
            self.cursor.execute(statement4,(i[0],))
            self.cursor.execute(statement5,(i[0],))
        self.calculate_points()

        self.con.commit()
    
    def return_or(self,team1,team2):
        statement = "SELECT Name,Overall FROM Teams where Name = ?"
        self.cursor.execute(statement,(team1,))
        team1_stats = self.cursor.fetchall()

        self.cursor.execute(statement,(team2,))
        team2_stats = self.cursor.fetchall()
        
        team1_ovr = team1_stats[0][1] - 70
        team2_ovr = team2_stats[0][1] - 70
        
        return [team1_ovr,team2_ovr]

#League().reset_database()

League().disconnect()