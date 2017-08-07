import Tkinter as tk
import ttk
from PIL import ImageTk,Image,ImageDraw,ImageColor,ImageFont
from team import *
import sqlite3
import math
from game import *
import os
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
        loadButton = tk.Button(parent,text="View Season Stats",command=lambda:self.Season(parent),bd = 0)
        viewButton = tk.Button(parent,text = "View Completed Basketball Games",command = lambda:self.Game(parent),bd = 0)

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
            tim = Team(None,None,None)
            if(tim.rosterCount<=15):
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
                    c.close()
            top.mainloop()
        parent.deiconify()
        print("return to main")
    def Create(self,parent):
        print("Game Created")
        gameName = ""
        parent.withdraw()
        playerList = []
        ttlCount=0
        for dbPlayer in dbPlayerList:
            pList = list(dbPlayer)
            x = Team(pList[1],pList[0],pList[2])
            print(x.printInfo())
            playerList.append(x)
        #g1 = Game("PlaguevEurope.db")
        courtIm = Image.open('court.png')
        draw = ImageDraw.Draw(courtIm)
        def createGameWindow(gameObject,conn2,c2,gameName):
            print("Enter second here")
            parent.withdraw()
            top = tk.Toplevel(parent)
            self.tlCount+=1
            top.protocol("WM_DELETE_WINDOW", lambda:self.topDestroy(top))
            top.title("Record Game Stats")
            top.minsize(width=1000,height=750)
            top.resizable(False,False)
            def addRebound():
                playerList[var.get()].upReb()
                print(playerList[var.get()].reb)
                tk.Label(top, text=playerList[var.get()].reb).grid(row=18+var.get()+1,column=8,sticky="e")
            def delRebound():
                playerList[var.get()].downReb()
                tk.Label(top, text=playerList[var.get()].reb).grid(row=18+var.get()+1,column=8,sticky="e")
            def addSteal():
                playerList[var.get()].upStl()
                tk.Label(top, text=playerList[var.get()].stl).grid(row=18+var.get()+1,column=9,sticky="e")
            def delSteal():
                playerList[var.get()].downStl()
                tk.Label(top, text=playerList[var.get()].stl).grid(row=18+var.get()+1,column=9,sticky="e")
            def addBlock():
                playerList[var.get()].upBlk()
                tk.Label(top, text=playerList[var.get()].blk).grid(row=18+var.get()+1,column=10,sticky="e")
            def delBlock():
                playerList[var.get()].downBlk()
                tk.Label(top, text=playerList[var.get()].blk).grid(row=18+var.get()+1,column=10,sticky="e")
            def addAssist():
                playerList[var.get()].upAst()
                tk.Label(top, text=playerList[var.get()].ast).grid(row=18+var.get()+1,column=11,sticky="e")
            def delAssist():
                playerList[var.get()].downAst()
                tk.Label(top, text=playerList[var.get()].ast).grid(row=18+var.get()+1,column=11,sticky="e")
            def addFoul():
                playerList[var.get()].upFls()
                tk.Label(top, text=playerList[var.get()].fls).grid(row=18+var.get()+1,column=12,sticky="e")
            def delFoul():
                playerList[var.get()].downFls()
                tk.Label(top, text=playerList[var.get()].fls).grid(row=18+var.get()+1,column=12,sticky="e")
            def addTurnover():
                playerList[var.get()].upTo()
                tk.Label(top, text=playerList[var.get()].to).grid(row=18+var.get()+1,column=13,sticky="e")
            def delTurnover():
                playerList[var.get()].downTo()
                tk.Label(top, text=playerList[var.get()].to).grid(row=18+var.get()+1,column=13,sticky="e")
            def addFreeThrow():
                playerList[var.get()].upFT()
                tk.Label(top, text=playerList[var.get()].ftMd).grid(row=18+var.get()+1,column=6,sticky="e")
                tk.Label(top, text=playerList[var.get()].ftAtt).grid(row=18+var.get()+1,column=7,sticky="e")
            def delFreeThrow():
                playerList[var.get()].downFT()
                tk.Label(top, text=playerList[var.get()].ftMd).grid(row=18+var.get()+1,column=6,sticky="e")
                tk.Label(top, text=playerList[var.get()].ftAtt).grid(row=18+var.get()+1,column=7,sticky="e")
            def addFreeThrowM():
                playerList[var.get()].upFTM()
                tk.Label(top, text=playerList[var.get()].ftMd).grid(row=18+var.get()+1,column=6,sticky="e")
                tk.Label(top, text=playerList[var.get()].ftAtt).grid(row=18+var.get()+1,column=7,sticky="e")
            def delFreeThrowM():
                playerList[var.get()].downFTM()
                tk.Label(top, text=playerList[var.get()].ftMd).grid(row=18+var.get()+1,column=6,sticky="e")
                tk.Label(top, text=playerList[var.get()].ftAtt).grid(row=18+var.get()+1,column=7,sticky="e")
            def subInOut(diff):
                playerList[var.get()].calcPM(diff)
                tk.Label(top, text=playerList[var.get()].pm).grid(row=18+var.get()+1,column=14,sticky="e")
            def addOScore():
                gameObject.upOpp()
                tk.Label(top, text= gameObject.oppScore).grid(row=10,column=19,sticky="w")
            def delOScore():
                gameObject.downOpp()
                tk.Label(top, text=gameObject.oppScore).grid(row=10,column=19,sticky="w")
            def updateStats():
                print (len(playerList))
                for player in playerList:
                    c2.execute("INSERT INTO stats VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",(player.firstName,player.lastName,player.number,player.twoAtt,player.threeAtt,player.ftAtt,player.twoMd,player.threeMd,player.ftMd,player.reb,player.stl,player.blk,player.ast,player.to,player.fls,player.pm))
                    conn2.commit()
                c2.execute("INSERT INTO final VALUES(?,?)",(gameObject.plageScore,gameObject.oppScore))
                conn2.commit()
                for i in range(0,len(dbPlayerList)):
                    print(playerList[i].pm)
                    c.execute("UPDATE roster SET  att2=?, att3=?, attf=?, md2=?, md3=?, mdf=?, reb=?, stl=?, blk=?, ast=?, tov=?, fls=?, pms=? WHERE last=?",(dbPlayerList[i][3]+playerList[i].twoAtt,dbPlayerList[i][4]+playerList[i].threeAtt,dbPlayerList[i][5]+playerList[i].ftAtt,dbPlayerList[i][6]+playerList[i].twoMd,dbPlayerList[i][7]+playerList[i].threeMd,dbPlayerList[i][8]+playerList[i].ftMd,dbPlayerList[i][9]+playerList[i].reb,dbPlayerList[i][10]+playerList[i].stl,dbPlayerList[i][11]+playerList[i].blk,dbPlayerList[i][12]+playerList[i].ast,dbPlayerList[i][13]+playerList[i].to,dbPlayerList[i][14]+playerList[i].fls,dbPlayerList[i][15]+playerList[i].pm,dbPlayerList[i][1]))
                    conn.commit()
                self.topDestroy(top)
            completeButton = tk.Button(top,text="End Game",command=updateStats).grid(row=1,column=18)
            #saveButton = tk.Button(top,text="Save").grid(row=2,column=18)
            addOppScore = tk.Button(top,text="Add Point to Opponent",command=addOScore).grid(row=6,column=18)
            delOppScore = tk.Button(top,text="Delete Point to Opponent",command=delOScore).grid(row=7,column=18)
            quitButton = tk.Button(top,text="Quit",command=lambda:self.topDestroy(top))
            addReb = tk.Button(top,text="Add Rebound",command=addRebound).grid(row=18-3,column=18)
            delReb = tk.Button(top,text="Delete Rebound",command=delRebound).grid(row=19-3,column=18)
            addStl = tk.Button(top,text="Add Steal",command=addSteal).grid(row=20-3,column=18)
            delStl = tk.Button(top,text="Delete Steal",command=delSteal).grid(row=21-3,column=18)
            addBlk = tk.Button(top,text="Add Block",command=addBlock).grid(row=22-3,column=18)
            delBlk = tk.Button(top,text="Delete Block",command=delBlock).grid(row=23-3,column=18)
            addAst = tk.Button(top,text="Add Assist",command=addAssist).grid(row=24-3,column=18)
            delAst = tk.Button(top,text="Delete Assist",command=delAssist).grid(row=25-3,column=18)
            addFls = tk.Button(top,text="Add Foul",command=addFoul).grid(row=26-11,column=19)
            delFls = tk.Button(top,text="Delete Foul",command=delFoul).grid(row=27-11,column=19)
            addTo = tk.Button(top,text="Add Turnover",command=addTurnover).grid(row=28-11,column=19)
            delTo = tk.Button(top,text="Delete Turnover",command=delTurnover).grid(row=29-11,column=19)
            addFt = tk.Button(top,text="Add Free Throw",command=addFreeThrow).grid(row=30-11,column=19)
            delFt = tk.Button(top,text="Delete Free Throw",command=delFreeThrow).grid(row=31-11,column=19)
            addFtM = tk.Button(top,text="Add Free Throw Miss",command=addFreeThrowM).grid(row=32-11,column=19)
            delFtM = tk.Button(top,text="Delete Free Throw Miss",command=delFreeThrowM).grid(row=33-11,column=19)
            pmButton = tk.Button(top,text="Sub In/Out",command=lambda:subInOut(gameObject.plageScore-gameObject.oppScore)).grid(row=34-11,column=19)
            nameLabel = tk.Label(top,text="Name/Number",font = ("AmericanTypewriter-Bold")).grid(row=18,column=0,columnspan=2)
            twoMdLabel = tk.Label(top,text="2pt Made",font = ("AmericanTypewriter-Bold")).grid(row=18,column=2)
            twoAttLabel = tk.Label(top,text="2pt Attempt",font = ("AmericanTypewriter-Bold")).grid(row=18,column=3)
            threeMdLabel = tk.Label(top,text="3pt Made",font = ("AmericanTypewriter-Bold")).grid(row=18,column=4)
            threeAttLabel = tk.Label(top,text="3pt Attempt",font = ("AmericanTypewriter-Bold")).grid(row=18,column=5)
            ftMdLabel = tk.Label(top,text="FT Made",font = ("AmericanTypewriter-Bold")).grid(row=18,column=6)
            ftAttLabel = tk.Label(top,text="FT Attempt",font = ("AmericanTypewriter-Bold")).grid(row=18,column=7)
            rebLabel = tk.Label(top,text="Rebounds",font = ("AmericanTypewriter-Bold")).grid(row=18,column=8)
            stlLabel = tk.Label(top,text="Steals",font = ("AmericanTypewriter-Bold")).grid(row=18,column=9)
            blkLabel = tk.Label(top,text="Blocks",font = ("AmericanTypewriter-Bold")).grid(row=18,column=10)
            astLabel = tk.Label(top,text="Assists",font = ("AmericanTypewriter-Bold")).grid(row=18,column=11)
            toLabel = tk.Label(top,text="Fouls",font = ("AmericanTypewriter-Bold")).grid(row=18,column=12)
            flsLabel = tk.Label(top,text="Turnovers",font = ("AmericanTypewriter-Bold")).grid(row=18,column=13)
            pmLabel = tk.Label(top,text="+/-",font = ("AmericanTypewriter-Bold")).grid(row=18,column=14)
            oppScoreLabel = tk.Label(top,text="0").grid(row=10,column=19,sticky="w")
            usScoreLabel = tk.Label(top,text="0").grid(row=11,column=19,sticky="w")
            oppLabel = tk.Label(top, text="Opponent Score:").grid(row=10,column=18,sticky="w")
            usLabel = tk.Label(top,text="Plauge Score:").grid(row=11,column=18,sticky="w")
            canvas = tk.Canvas(top, width = 848, height = 449)
            canvas.grid(row=0,column=0,rowspan=17,columnspan = 17)
            self.img = ImageTk.PhotoImage(Image.open('court.png'))
            iLabel = tk.Label(top,image = self.img)
            canvas.create_image(0,0,image=self.img,anchor="nw")
            var = tk.IntVar()
            half = tk.IntVar()
            half.set(1)
            increment = 0
            def sel():
                print(playerList[var.get()].printInfo())
            for player in playerList:
                b = tk.Radiobutton(top, text=player.printInfo(), value=playerList.index(player),variable=var,command=lambda:sel(),indicatoron=0)
                b.grid(row=19+increment,column=0,columnspan=2,sticky="w")
                increment+=1
            increment = 0
            rebund = 0
            for player in playerList:
                b1 = tk.Label(top, text=player.twoMd,)
                b2 = tk.Label(top, text=player.twoAtt)
                b3 = tk.Label(top, text=player.threeMd)
                b4 = tk.Label(top, text=player.threeAtt)
                b5 = tk.Label(top, text=player.ftMd)
                b6 = tk.Label(top, text=player.ftAtt)
                b7 = tk.Label(top, text=player.reb)
                b8 = tk.Label(top, text=player.stl)
                b9 = tk.Label(top, text=player.blk)
                b10 = tk.Label(top, text=player.ast)
                b11 = tk.Label(top, text=player.to)
                b12 = tk.Label(top, text=player.fls)
                b13 = tk.Label(top, text=player.pm)
                b1.grid(row=19+increment,column=2,columnspan=1,sticky="e")
                b2.grid(row=19+increment,column=3,columnspan=1,sticky="e")
                b3.grid(row=19+increment,column=4,columnspan=1,sticky="e")
                b4.grid(row=19+increment,column=5,columnspan=1,sticky="e")
                b5.grid(row=19+increment,column=6,columnspan=1,sticky="e")
                b6.grid(row=19+increment,column=7,columnspan=1,sticky="e")
                b7.grid(row=19+increment,column=8,columnspan=1,sticky="e")
                b8.grid(row=19+increment,column=9,columnspan=1,sticky="e")
                b9.grid(row=19+increment,column=10,columnspan=1,sticky="e")
                b10.grid(row=19+increment,column=11,columnspan=1,sticky="e")
                b11.grid(row=19+increment,column=12,columnspan=1,sticky="e")
                b12.grid(row=19+increment,column=13,columnspan=1,sticky="e")
                b13.grid(row=19+increment,column=14,sticky="e")
                increment+=1
            #half = 1
            half1 = tk.Radiobutton(top,text="First Half", value = 1,variable=half).grid(row=4,column=18)
            half2 = tk.Radiobutton(top,text="Second Half", value = 2,variable=half).grid(row=5,column=18)
            r=10
            def printcoordsL(event):
                print("LeftClick")
                print (type(event.x))
                if((event.x<=50 and (event.y>40 and event.y<400)) or(math.sqrt((event.x - 50)**2 + (event.y - 220)**2)<170) and event.x<420) or ((event.x>=750 and (event.y>40 and event.y<400)) or (math.sqrt((event.x - 792)**2 + (event.y - 220)**2)<170) and event.x>420):
                    playerList[var.get()].up2Pt()
                    print("Here")
                    print(playerList[var.get()].twoMd)
                    print(playerList[var.get()].twoAtt)
                    tk.Label(top, text=playerList[var.get()].twoMd).grid(row=18+var.get()+1,column=2,sticky="e")
                    tk.Label(top, text=playerList[var.get()].twoAtt).grid(row=18+var.get()+1,column=3,sticky="e")
                    c2.execute("INSERT INTO shots VALUES(?, ?, ?, ?, ?)",(playerList[var.get()].firstName[0:1]+playerList[var.get()].lastName[0:1]+playerList[var.get()].number,event.x,event.y,True,half.get()))
                    conn2.commit()
                    print(half.get())
                else:
                    print("not here")
                    playerList[var.get()].up3Pt()
                    print(playerList[var.get()].threeMd)
                    print(playerList[var.get()].threeAtt)
                    tk.Label(top, text=playerList[var.get()].threeMd).grid(row=18+var.get()+1,column=4,sticky="e")
                    tk.Label(top, text=playerList[var.get()].threeAtt).grid(row=18+var.get()+1,column=5,sticky="e")
                    c2.execute("INSERT INTO shots VALUES(?, ?, ?, ?, ?)",(playerList[var.get()].firstName[0:1]+playerList[var.get()].lastName[0:1]+playerList[var.get()].number,event.x,event.y,True,half.get()))
                    conn2.commit()
                points = 0
                for player in playerList:
                    points+=player.calcPts()
                gameObject.plageScore=points
                scoreLabel = tk.Label(top,text=gameObject.plageScore).grid(row=11,column=19,sticky="w")
                draw.ellipse([event.x-r,event.y-r,event.x+r,event.y+r],fill= 'green')
                draw.text([event.x-r,event.y-r],text=playerList[var.get()].getInitials(),font=ImageFont.load_default())
                make = canvas.create_oval(event.x-r, event.y-r, event.x+r, event.y+r, fill='green')
                canvas.create_text(event.x,event.y,text=playerList[var.get()].getInitials(),font=("Arial",8))
                courtIm.save(gameName+".png")
            def printcoordsR(event):
                print("RightClick")
                print (event.x,event.y)
                if((event.x<=50 and (event.y>40 and event.y<400))or(math.sqrt((event.x - 50)**2 + (event.y - 220)**2)<170) and event.x<420) or ((event.x>=750 and (event.y>40 and event.y<400)) or (math.sqrt((event.x - 792)**2 + (event.y - 220)**2)<170) and event.x>420):
                    playerList[var.get()].up2PtM()
                    tk.Label(top, text=playerList[var.get()].twoMd).grid(row=18+var.get()+1,column=2,sticky="e")
                    tk.Label(top, text=playerList[var.get()].twoAtt).grid(row=18+var.get()+1,column=3,sticky="e")
                    c2.execute("INSERT INTO shots VALUES(?, ?, ?, ?, ?)",(playerList[var.get()].getInitials(),event.x,event.y,False,half.get()))
                    conn2.commit()
                else:
                    playerList[var.get()].up3PtM()
                    tk.Label(top, text=playerList[var.get()].threeMd).grid(row=18+var.get()+1,column=4,sticky="e")
                    tk.Label(top, text=playerList[var.get()].threeAtt).grid(row=18+var.get()+1,column=5,sticky="e")
                    c2.execute("INSERT INTO shots VALUES(?, ?, ?, ?, ?)",(playerList[var.get()].getInitials(),event.x,event.y,False,half.get()))
                    conn2.commit()
                draw.ellipse([event.x-r,event.y-r,event.x+r,event.y+r],fill= 'red')
                draw.text([event.x-r,event.y-r],text=playerList[var.get()].getInitials(),font=ImageFont.load_default())
                miss = canvas.create_oval(event.x-r, event.y-r, event.x+r, event.y+r, fill='red')
                canvas.create_text(event.x,event.y,text=playerList[var.get()].getInitials(),font=("Arial",8))
                courtIm.save(gameName+".png")
            canvas.bind("<Button-1>",printcoordsL)
            canvas.bind("<Button-2>",printcoordsR)
            quitButton.grid(row=3,column=18)
            top.mainloop()
        if(self.tlCount==0):
            top = tk.Toplevel(parent)
            self.tlCount+=1
            ttlCount+=1
            top.title("Create a Game")
            top.minsize(width=300,height=100)
            top.resizable(False,False)
            top.protocol("WM_DELETE_WINDOW", lambda:self.topDestroy(top))
            tk.Label(top, text="Enter Game Name").grid(row=0)
            fN = tk.Entry(top)
            fN.grid(row=0, column=1)
            quitButton = tk.Button(top,text="Quit",command=lambda:self.topDestroy(top))
            quitButton.grid(row = 1,column = 2)
            submitButton = tk.Button(top,text="Submit",command=lambda:addGame(fN.get()))
            submitButton.grid(row=1,column = 1)
            def addGame(gName):
                if(len(gName)==0) or ( os.path.isfile('Games/'+gName+'.db')):
                    print("Cannot leave name empty or file exists")
                else:
                    newGame = Game(gName)
                    gameName=gName
                    print(newGame)
                    conn2=sqlite3.connect('Games/'+gameName+'.db')
                    c2=conn2.cursor()
                    ttlCount=0
                    top.withdraw()
                    createGameWindow(newGame,conn2,c2,gameName)
                    self.tlCount = 0
                    c.close()
            top.mainloop()
        print("return to main")
    def Season(self,parent):
        print ("Loading Data")
        parent.withdraw()
        playerList=[]
        print dbPlayerList
        for i in range(0,len(dbPlayerList)):
            x = Team(dbPlayerList[i][1],dbPlayerList[i][0],dbPlayerList[i][2])
            x.twoAtt=dbPlayerList[i][3]
            x.threeAtt=dbPlayerList[i][4]
            x.ftAtt=dbPlayerList[i][5]
            x.twoMd=dbPlayerList[i][6]
            x.threeMd=dbPlayerList[i][7]
            x.ftMd=dbPlayerList[i][8]
            x.reb=dbPlayerList[i][9]
            x.stl=dbPlayerList[i][10]
            x.blk=dbPlayerList[i][11]
            x.ast=dbPlayerList[i][12]
            x.to=dbPlayerList[i][13]
            x.fls=dbPlayerList[i][14]
            x.pm=dbPlayerList[i][15]
            print(x.printInfo())
            playerList.append(x)
        print(len(playerList))
        if(self.tlCount==0):
            top = tk.Toplevel(parent)
            self.tlCount+=1
            top.resizable(False,False)
            top.title("View The Stats")
            top.protocol("WM_DELETE_WINDOW", lambda:self.topDestroy(top))
            increment = 0
            tk.Label(top,text="Season Stats",font = ("AmericanTypewriter-Bold",45)).grid(row=0,column=0,columnspan=16)
            tk.Label(top,text="Name/Number",font = ("AmericanTypewriter-Bold",15)).grid(row=1,column=0)
            tk.Label(top,text="2Pt Made",font = ("AmericanTypewriter-Bold",15)).grid(row=1,column=1)
            tk.Label(top,text="2pt Attempt",font = ("AmericanTypewriter-Bold",15)).grid(row=1,column=2)
            tk.Label(top,text="3pt Made",font = ("AmericanTypewriter-Bold",15)).grid(row=1,column=3)
            tk.Label(top,text="3pt Attempt",font = ("AmericanTypewriter-Bold",15)).grid(row=1,column=4)
            tk.Label(top,text="FT Made",font = ("AmericanTypewriter-Bold",15)).grid(row=1,column=5)
            tk.Label(top,text="FT Attempt",font = ("AmericanTypewriter-Bold",15)).grid(row=1,column=6)
            tk.Label(top,text="Points",font = ("AmericanTypewriter-Bold",15)).grid(row=1,column=7)
            tk.Label(top,text="Rebounds",font = ("AmericanTypewriter-Bold",15)).grid(row=1,column=8)
            tk.Label(top,text="Steals",font = ("AmericanTypewriter-Bold",15)).grid(row=1,column=9)
            tk.Label(top,text="Assists",font = ("AmericanTypewriter-Bold",15)).grid(row=1,column=10)
            tk.Label(top,text="Blocks",font = ("AmericanTypewriter-Bold",15)).grid(row=1,column=11)
            tk.Label(top,text="Turnovers",font = ("AmericanTypewriter-Bold",15)).grid(row=1,column=12)
            tk.Label(top,text="Fouls",font = ("AmericanTypewriter-Bold",15)).grid(row=1,column=13)
            tk.Label(top,text="+/-",font = ("AmericanTypewriter-Bold",15)).grid(row=1,column=14)
            tk.Label(top,text="FG%",font = ("AmericanTypewriter-Bold",15)).grid(row=1,column=15)
            tk.Label(top,text="FT%",font = ("AmericanTypewriter-Bold",15)).grid(row=1,column=16)
            for player in playerList:
                tk.Label(top,text=player.firstName+" "+player.lastName+" #"+player.number,font = ("AmericanTypewriter",12)).grid(row=2+increment,column=0)
                tk.Label(top,text=player.twoMd,font = ("AmericanTypewriter",12)).grid(row=2+increment,column=1)
                tk.Label(top,text=player.twoAtt,font = ("AmericanTypewriter",12)).grid(row=2+increment,column=2)
                tk.Label(top,text=player.threeMd,font = ("AmericanTypewriter",12)).grid(row=2+increment,column=3)
                tk.Label(top,text=player.threeAtt,font = ("AmericanTypewriter",12)).grid(row=2+increment,column=4)
                tk.Label(top,text=player.ftMd,font = ("AmericanTypewriter",12)).grid(row=2+increment,column=5)
                tk.Label(top,text=player.ftAtt,font = ("AmericanTypewriter",12)).grid(row=2+increment,column=6)
                tk.Label(top,text=player.calcPts(),font = ("AmericanTypewriter",12)).grid(row=2+increment,column=7)
                tk.Label(top,text=player.reb,font = ("AmericanTypewriter",12)).grid(row=2+increment,column=8)
                tk.Label(top,text=player.stl,font = ("AmericanTypewriter",12)).grid(row=2+increment,column=9)
                tk.Label(top,text=player.ast,font = ("AmericanTypewriter",12)).grid(row=2+increment,column=10)
                tk.Label(top,text=player.blk,font = ("AmericanTypewriter",12)).grid(row=2+increment,column=11)
                tk.Label(top,text=player.to,font = ("AmericanTypewriter",12)).grid(row=2+increment,column=12)
                tk.Label(top,text=player.fls,font = ("AmericanTypewriter",12)).grid(row=2+increment,column=13)
                tk.Label(top,text=player.pm,font = ("AmericanTypewriter",12)).grid(row=2+increment,column=14)
                tk.Label(top,text=str(player.calcFG())+""+"%",font = ("AmericanTypewriter",12)).grid(row=2+increment,column=15)
                tk.Label(top,text=str(player.calcFt())+""+"%",font = ("AmericanTypewriter",12)).grid(row=2+increment,column=16)
                increment+=1
            quitButton = tk.Button(top,text="Quit",command=lambda:self.topDestroy(top))
            quitButton.grid(row=increment+3,column=16)
            top.mainloop()
            c.close()
        parent.deiconify()
        print("return to main")
    def Game(self,parent):
        print("Viewing Game")
        gameName = ""
        parent.withdraw()
        playerList = []
        #ttlCount=0
        def createGameWindow(dbPlayerList,gameName):
            print("Enter second here")
            top = tk.Toplevel(parent)
            self.tlCount+=1
            playerList=[]
            top.resizable(False,False)
            for dbPlayer in dbPlayerList:
                pList = list(dbPlayer)
                x = Team(pList[1],pList[0],pList[2])
                x.twoAtt=pList[3]
                x.threeAtt=pList[4]
                x.ftAtt=pList[5]
                x.twoMd=pList[6]
                x.threeMd=pList[7]
                x.ftMd=pList[8]
                x.reb=pList[9]
                x.stl=pList[10]
                x.blk=pList[11]
                x.ast=pList[12]
                x.to=pList[13]
                x.fls=pList[14]
                x.pm=pList[15]
                print(x.printInfo())
                playerList.append(x)
            top.title("View The Stats")
            top.protocol("WM_DELETE_WINDOW", lambda:self.topDestroy(top))
            increment = 0
            tk.Label(top,text=gameName+" Stats",font = ("AmericanTypewriter-Bold",45)).grid(row=0,column=0,columnspan=16)
            tk.Label(top,text="Name/Number",font = ("AmericanTypewriter-Bold",15)).grid(row=1,column=0)
            tk.Label(top,text="2Pt Made",font = ("AmericanTypewriter-Bold",15)).grid(row=1,column=1)
            tk.Label(top,text="2pt Attempt",font = ("AmericanTypewriter-Bold",15)).grid(row=1,column=2)
            tk.Label(top,text="3pt Made",font = ("AmericanTypewriter-Bold",15)).grid(row=1,column=3)
            tk.Label(top,text="3pt Attempt",font = ("AmericanTypewriter-Bold",15)).grid(row=1,column=4)
            tk.Label(top,text="FT Made",font = ("AmericanTypewriter-Bold",15)).grid(row=1,column=5)
            tk.Label(top,text="FT Attempt",font = ("AmericanTypewriter-Bold",15)).grid(row=1,column=6)
            tk.Label(top,text="Points",font = ("AmericanTypewriter-Bold",15)).grid(row=1,column=7)
            tk.Label(top,text="Rebounds",font = ("AmericanTypewriter-Bold",15)).grid(row=1,column=8)
            tk.Label(top,text="Steals",font = ("AmericanTypewriter-Bold",15)).grid(row=1,column=9)
            tk.Label(top,text="Assists",font = ("AmericanTypewriter-Bold",15)).grid(row=1,column=10)
            tk.Label(top,text="Blocks",font = ("AmericanTypewriter-Bold",15)).grid(row=1,column=11)
            tk.Label(top,text="Turnovers",font = ("AmericanTypewriter-Bold",15)).grid(row=1,column=12)
            tk.Label(top,text="Fouls",font = ("AmericanTypewriter-Bold",15)).grid(row=1,column=13)
            tk.Label(top,text="+/-",font = ("AmericanTypewriter-Bold",15)).grid(row=1,column=14)
            tk.Label(top,text="FG%",font = ("AmericanTypewriter-Bold",15)).grid(row=1,column=15)
            tk.Label(top,text="FT%",font = ("AmericanTypewriter-Bold",15)).grid(row=1,column=16)
            for player in playerList:
                tk.Label(top,text=player.firstName+" "+player.lastName+" #"+player.number,font = ("AmericanTypewriter",12)).grid(row=2+increment,column=0)
                tk.Label(top,text=player.twoMd,font = ("AmericanTypewriter",12)).grid(row=2+increment,column=1)
                tk.Label(top,text=player.twoAtt,font = ("AmericanTypewriter",12)).grid(row=2+increment,column=2)
                tk.Label(top,text=player.threeMd,font = ("AmericanTypewriter",12)).grid(row=2+increment,column=3)
                tk.Label(top,text=player.threeAtt,font = ("AmericanTypewriter",12)).grid(row=2+increment,column=4)
                tk.Label(top,text=player.ftMd,font = ("AmericanTypewriter",12)).grid(row=2+increment,column=5)
                tk.Label(top,text=player.ftAtt,font = ("AmericanTypewriter",12)).grid(row=2+increment,column=6)
                tk.Label(top,text=player.calcPts(),font = ("AmericanTypewriter",12)).grid(row=2+increment,column=7)
                tk.Label(top,text=player.reb,font = ("AmericanTypewriter",12)).grid(row=2+increment,column=8)
                tk.Label(top,text=player.stl,font = ("AmericanTypewriter",12)).grid(row=2+increment,column=9)
                tk.Label(top,text=player.ast,font = ("AmericanTypewriter",12)).grid(row=2+increment,column=10)
                tk.Label(top,text=player.blk,font = ("AmericanTypewriter",12)).grid(row=2+increment,column=11)
                tk.Label(top,text=player.to,font = ("AmericanTypewriter",12)).grid(row=2+increment,column=12)
                tk.Label(top,text=player.fls,font = ("AmericanTypewriter",12)).grid(row=2+increment,column=13)
                tk.Label(top,text=player.pm,font = ("AmericanTypewriter",12)).grid(row=2+increment,column=14)
                tk.Label(top,text=str(player.calcFG())+""+"%",font = ("AmericanTypewriter",12)).grid(row=2+increment,column=15)
                tk.Label(top,text=str(player.calcFt())+""+"%",font = ("AmericanTypewriter",12)).grid(row=2+increment,column=16)
                increment+=1
            quitButton = tk.Button(top,text="Quit",command=lambda:self.topDestroy(top))
            gameImage = Image.open(gameName+'.png')
            imageHome = ImageTk.PhotoImage(gameImage)
            backgroundLabel=tk.Label(top,image = imageHome).grid(row=increment+3,column=0,columnspan=16)
            quitButton.grid(row=increment+4,column=16)
            top.mainloop()
        if(self.tlCount==0):
            top = tk.Toplevel(parent)
            self.tlCount+=1
            ttlCount+=1
            top.title("Create a Game")
            top.minsize(width=300,height=100)
            top.resizable(False,False)
            top.protocol("WM_DELETE_WINDOW", lambda:self.topDestroy(top))
            tk.Label(top, text="Enter Game Name").grid(row=0)
            fN = tk.Entry(top)
            fN.grid(row=0, column=1)
            quitButton = tk.Button(top,text="Quit",command=lambda:self.topDestroy(top))
            quitButton.grid(row = 1,column = 2)
            submitButton = tk.Button(top,text="Submit",command=lambda:addGame(fN.get()))
            submitButton.grid(row=1,column = 1)
            def addGame(gName):
                if(len(gName)==0) or (not os.path.isfile('Games/'+gName+'.db')):
                    print("Cannot leave name empty or game does not exist")
                else:
                    ttlCount=0
                    top.withdraw()
                    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
                    db_path = os.path.join(BASE_DIR, "Games/"+gName+".db")
                    conn3=sqlite3.connect(db_path)
                    c3=conn3.cursor()
                    c3.execute("""SELECT * FROM stats""")
                    dbPlayerList = list(c3.fetchall())
                    createGameWindow(dbPlayerList,gName)
                    self.tlCount = 0
                    c3.close()
            top.mainloop()
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
