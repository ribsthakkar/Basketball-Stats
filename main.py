import Tkinter as tk
import ttk
from PIL import ImageTk,Image
from team import *
import sqlite3
conn = sqlite3.connect('roster.db')
c = conn.cursor()
c.execute("SELECT * FROM roster")


class MainGUI(tk.Frame):
    tlCount = 0
    increment = 0
    def __init__(self, parent,*args,**kwargs):
        tk.Frame.__init__(self, parent,*args,**kwargs)
        #self.pack()
        homeImage = Image.open('homepage.jpg')
        self.imageHome = ImageTk.PhotoImage(homeImage)
        backgroundLabel=tk.Label(parent,image = self.imageHome)
        backgroundLabel.place(x=0,y=0,relwidth = 1,relheight = 1)
        wd = homeImage.width
        hd = homeImage.height
        parent.minsize(width=wd,height=hd)
        parent.resizable(False,False)
        #root.maxsize(width=500,height=450)

        titleLabel = tk.Label(parent, text = "BasketStats", font = ("AmericanTypewriter-Bold",80),bd = 0)
        titleLabel.place(x = 80, y= 10)

        teamButton = tk.Button(parent,text="Add to Basketball Roster",command=lambda:self.Team(parent),bd = 0)
        createButton = tk.Button(parent,text="Create New Basketball Game",command=lambda:self.Create(parent),bd = 0)
        loadButton = tk.Button(parent,text="Load Existing Basketball Game",command=lambda:self.Load(parent),bd = 0)
        viewButton = tk.Button(parent,text = "View Completed Basketball Games",command = lambda:self.View(parent),bd = 0)

        teamButton.place(x=240,y=120)
        createButton.place(x = 240, y = 180)
        loadButton.place(x = 230, y = 240)
        viewButton.place(x = 225, y = 300)
        parent.protocol("WM_DELETE_WINDOW", lambda:quit())
    def Team(self,parent):
        print("Team Created")
        parent.withdraw()
        if(self.tlCount==0):
            top = tk.Toplevel(parent)
            self.tlCount+=1
            top.title("Create a Team")
            top.minsize(width=300,height=100)
            top.resizable(False,False)
            top.protocol("WM_DELETE_WINDOW", lambda:self.topDestroy(top))
            tk.Label(top, text="First Name").grid(row=0)
            tk.Label(top, text="Last Name").grid(row=1)
            tk.Label(top, text="Jersey Number").grid(row=2)
            fN = tk.Entry(top)
            lN = tk.Entry(top)
            jN = tk.Entry(top)

            fN.grid(row=0, column=1)
            lN.grid(row=1, column=1)
            jN.grid(row=2, column = 1)


            quitButton = tk.Button(top,text="Quit",command=lambda:self.topDestroy(top))
            quitButton.grid(row = 4,column = 4)
            submitButton = tk.Button(top,text="Submit",command=lambda:addPlayer(fN.get(),lN.get(),jN.get()))
            submitButton.grid(row=4,column = 2)
            def addPlayer(fName,lName,jNum):
                if(len(fName)==0 or len(lName)==0 or len(jNum)==0):
                    print("There is number(s) in your name, letter(s) in your jersey number slot, or not all of the slots are filled!")
                else:
                    newPlayer = Team(lName,fName,jNum)
                    c.execute("INSERT INTO roster VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",(newPlayer.firstName,newPlayer.lastName,newPlayer.number,0,0,0,0,0,0,0,0,0,0,0,0,0))
                    conn.commit()
                    print(newPlayer.firstName + " " + newPlayer.lastName + " #"+ newPlayer.number)
                    self.topDestroy(top)
                    self.tlCount = 0
            top.mainloop()
        parent.deiconify()
        print("return to main")
    def Create(self,parent):
        print("Game Created")
        parent.withdraw()
        if(self.tlCount==0):
            parent.withdraw()
            top = tk.Toplevel(parent)
            self.tlCount+=1
            top.protocol("WM_DELETE_WINDOW", lambda:self.topDestroy(top))
            top.title("Create a game")
            top.minsize(width=1000,height=750)
            top.resizable(False,False)
            updater = Team(None,None,None)
            completeButton = tk.Button(top,text="End Game").grid(row=1,column=18)
            saveButton = tk.Button(top,text="Save").grid(row=2,column=18)
            quitButton = tk.Button(top,text="Quit",command=lambda:self.topDestroy(top))
            addReb = tk.Button(top,text="Add Rebound").grid(row=18,column=18)
            delReb = tk.Button(top,text="Delete Rebound").grid(row=19,column=18)
            addStl = tk.Button(top,text="Add Steal").grid(row=20,column=18)
            delStl = tk.Button(top,text="Delete Steal").grid(row=21,column=18)
            addBlk = tk.Button(top,text="Add Block").grid(row=22,column=18)
            delBlk = tk.Button(top,text="Delete Block").grid(row=23,column=18)
            addAst = tk.Button(top,text="Add Assist").grid(row=24,column=18)
            delAst = tk.Button(top,text="Delete Assist").grid(row=25,column=18)
            addFls = tk.Button(top,text="Add Foul").grid(row=26,column=18)
            delFls = tk.Button(top,text="Delete Foul").grid(row=27,column=18)
            addTo = tk.Button(top,text="Add Turnover").grid(row=28,column=18)
            delTo = tk.Button(top,text="Delete Turnover").grid(row=29,column=18)
            canvas = tk.Canvas(top, width = 848, height = 449)
            canvas.grid(row=0,column=0,rowspan=17,columnspan = 17)
            self.img = ImageTk.PhotoImage(Image.open('court.png'))
            iLabel = tk.Label(top,image = self.img)
            canvas.create_image(0,0,image=self.img,anchor="nw")
            playerList = []
            namesList=[]
            increment = tk.IntVar()
            index = 0
            def sel():
                #index = playerList.index(player)
                print(playerList[increment.get()].printInfo())
            for dbPlayer in dbPlayerList:
                pList = list(dbPlayer)
                x = Team(pList[1],pList[0],pList[2])
                print(x.printInfo())
                playerList.append(x)
            for player in playerList:
                b = tk.Radiobutton(top, text=player.printInfo(), value=playerList.index(player),variable=increment,command=lambda:sel(),indicatoron=0)
                b.grid(row=18+self.increment,column=0,columnspan=2,sticky="w")
                self.increment+=1
            def printcoords(event):
                print (event.x,event.y)
                #print(updater.printInfo())
            canvas.bind("<Button-1>",printcoords)
            quitButton.grid(row=3,column=18)
            top.mainloop()
        #parent.deiconify()
        self.increment =0
        print("return to main")
    def Load(self,parent):
        print ("Loading Game")
        parent.withdraw()
        if(self.tlCount==0):
            top = tk.Toplevel(parent)
            self.tlCount+=1
            top.title("Create a Team")
            top.protocol("WM_DELETE_WINDOW", lambda:self.topDestroy(top))
            quitButton = tk.Button(top,text="Quit",command=lambda:self.topDestroy(top))
            quitButton.place(x=10,y=10)
            top.mainloop()
        parent.deiconify()
        print("return to main")
    def View(self,parent):
        print("Viewing Game")
        parent.withdraw()
        if(self.tlCount==0):
            top = tk.Toplevel(parent)
            self.tlCount+=1
            top.title("Create a Team")
            top.protocol("WM_DELETE_WINDOW", lambda:self.topDestroy(top))
            quitButton = tk.Button(top,text="Quit",command=lambda:self.topDestroy(top))
            quitButton.place(x=10,y=10)
            top.mainloop()
        parent.deiconify()
        print("return to main")
    def topDestroy(self,top):
        top.destroy()
        self.tlCount=0
        parent = tk.Toplevel()
        parent.title("Home")
        my_gui = MainGUI(parent)
        parent.mainloop()



if __name__ == '__main__':
    root = tk.Tk()
    root.title("Home")
    c.execute("SELECT * FROM roster")
    dbPlayerList = list(c.fetchall())
    my_gui = MainGUI(root)
    root.mainloop()
    c.execute("SELECT * FROM roster")
    print(c.fetchall())
    conn.close()
