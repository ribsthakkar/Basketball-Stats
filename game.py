import sqlite3
import os


class Game:
    def __init__(self,name):
        self.plageScore = 0
        self.oppScore = 0
        self.name = name
        conn = sqlite3.connect('Games/'+name+'.db')
        c = conn.cursor()
        if (not os.path.isfile('Games/'+name+'.db')):
            c.execute("""CREATE TABLE shots (
             initials text,
             xCoord integer,
             yCoord integer,
             made boolean,
             half integer
             ) """)
        else:
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
    def upOpp(self):
        self.oppScore+=1
    def downOpp(self):
        self.oppScore-=1
