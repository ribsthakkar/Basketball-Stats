import sqlite3



class Game:
    def __init__(self,name):
         hScore = 0
         aScore = 0
         self.name = name
         conn = sqlite3.connect('/Games/'+name+'.db')
         c = conn.cursor()
         if (!os.path.isfile('/Games/'+name+'.db')):
             c.execute("""CREATE TABLE shots (
             initials text,
             xCoord integer,
             yCoord integer,
             half integer
             ) """)
