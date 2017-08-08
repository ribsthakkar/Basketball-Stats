import sqlite3
import os


class Game:
    #Creating an instance of the game class passing its name
    def __init__(self,name):
        self.plageScore = 0
        self.oppScore = 0
        self.name = name
        #checking if file exists in order to prevent duplication errors
        if (os.path.isfile('Games/'+name+'.db')):
            conn = sqlite3.connect('Games/'+name+'.db')
            c = conn.cursor()
        else:
            #if file doesn't exist then all of the neccessary tables are created inside the database
            conn = sqlite3.connect('Games/'+name+'.db')
            c = conn.cursor()
            c.execute("""CREATE TABLE shots (
             initials text,
             xCoord integer,
             yCoord integer,
             made boolean,
             half integer
             ) """)
            c.execute("""CREATE TABLE stats (
                     first text,
                     last text,
                     num text,
                     att2 integer,
                     att3 integer,
                     attf integer,
                     md2 integer,
                     md3 integer,
                     mdf integer,
                     reb integer,
                     stl integer,
                     blk integer,
                     ast integer,
                     tov integer,
                     fls integer,
                     pms integer
                     )  """)
            c.execute("""CREATE TABLE final (
                ourScore integer,
                opponetScore integer
                ) """)
    #The following methods increment or decrement the instance of the opponsent's score
    def upOpp(self):
        self.oppScore+=1
    def downOpp(self):
        if(not(self.oppScore==0)):
            self.oppScore-=1
