import Tkinter as tk
import ttk
from PIL import ImageTk,Image
from team import *
import sqlite3
conn = sqlite3.connect('roster.db')
c = conn.cursor()


class MainGUI(tk.Frame):
    tlCount = 0
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
    def Team(self,parent):
        print("Team Created")
        parent.withdraw()
        if(self.tlCount==0):
            top = tk.Toplevel(parent)
            self.tlCount+=1
            top.title("Create a Team")
            top.minsize(width=300,height=100)
            top.resizable(False,False)

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
        parent.deiconify()
        print("return to main")
    def Create(self,parent):
        print("Game Created")
        parent.withdraw()
        if(self.tlCount==0):
            top = tk.Toplevel(parent)
            self.tlCount+=1
            top.title("Create a Team")
            quitButton = tk.Button(top,text="Quit",command=lambda:self.topDestroy(top))
            quitButton.place(x=10,y=10)
        parent.deiconify()
        print("return to main")
    def Load(self,parent):
        print ("Loading Game")
        parent.withdraw()
        if(self.tlCount==0):
            top = tk.Toplevel(parent)
            self.tlCount+=1
            top.title("Create a Team")
            quitButton = tk.Button(top,text="Quit",command=lambda:self.topDestroy(top))
            quitButton.place(x=10,y=10)
        parent.deiconify()
        print("return to main")
    def View(self,parent):
        print("Viewing Game")
        parent.withdraw()
        if(self.tlCount==0):
            top = tk.Toplevel(parent)
            self.tlCount+=1
            top.title("Create a Team")
            quitButton = tk.Button(top,text="Quit",command=lambda:self.topDestroy(top))
            quitButton.place(x=10,y=10)
        parent.deiconify()
        print("return to main")


    def topDestroy(self,top):
        top.destroy()
        self.tlCount=0



if __name__ == '__main__':
    root = tk.Tk()
    root.title("Home")
    my_gui = MainGUI(root)
    root.mainloop()
    c.execute("SELECT * FROM roster")
    print(c.fetchall())
    conn.close()
