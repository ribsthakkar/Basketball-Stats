from PIL import Image, ImageDraw
import sqlite3
import os

gameName="testgame"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "Games/"+gameName+".db")
conn3=sqlite3.connect(db_path)
c3=conn3.cursor()
c3.execute("""SELECT * FROM stats""")
dbPlayerList = list(c3.fetchall())
print(dbPlayerList)
conn3.commit()
