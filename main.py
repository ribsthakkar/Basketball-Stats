import Tkinter as tk
import ttk
from PIL import ImageTk,Image,ImageDraw,ImageColor,ImageFont
from team import *
import sqlite3
import math
from game import *
import os
#creating a connection using sqlite to the roster database
conn = sqlite3.connect('roster.db')
c = conn.cursor()

#creating class for GUI Main Menu
class MainGUI(tk.Frame):
    tlCount = 0 #count number of top level windows to prevent multiple windows from opening
    def __init__(self, parent,*args,**kwargs):
        #Constructor for parent Frame class
        tk.Frame.__init__(self, parent,*args,**kwargs)
        #importing background image for Main Menu
        homeImage = Image.open('homepage.jpg')
        self.imageHome = ImageTk.PhotoImage(homeImage)
        backgroundLabel=tk.Label(parent,image = self.imageHome)
        backgroundLabel.place(x=0,y=0,relwidth = 1,relheight = 1)
        wd = homeImage.width
        hd = homeImage.height
        parent.minsize(width=wd,height=hd)
        parent.resizable(False,False)

        #Title of Main Menu
        titleLabel = tk.Label(parent, text = "BasketStats", font = ("AmericanTypewriter-Bold",80),bd = 0)
        titleLabel.place(x = 80, y= 10)

        #Main Menu Button Items
        teamButton = tk.Button(parent,text="Add to Basketball Roster",command=lambda:self.Roster(parent),bd = 0)
        createButton = tk.Button(parent,text="Create New Basketball Game",command=lambda:self.Create(parent),bd = 0)
        loadButton = tk.Button(parent,text="View Season Stats",command=lambda:self.Season(parent),bd = 0)
        viewButton = tk.Button(parent,text = "View Completed Basketball Games",command = lambda:self.Game(parent),bd = 0)
        teamButton.place(x=240,y=120)
        createButton.place(x = 240, y = 180)
        loadButton.place(x = 230, y = 240)
        viewButton.place(x = 225, y = 300)
        parent.protocol("WM_DELETE_WINDOW", lambda:quit())
    #The following methods are called by selecting the specific menu items to create their respective windows
    #Roster method called when player is to be added to the roster datatabse
    def Roster(self,parent):
        print("Team Created")
        parent.withdraw()
        #checking if no mroe than 1 top level window is open
        if(self.tlCount==0):
            #Constructing toplevel object
            top = tk.Toplevel(parent)
            self.tlCount+=1
            top.title("Create a Team")
            top.minsize(width=300,height=100)
            top.resizable(False,False)
            top.protocol("WM_DELETE_WINDOW", lambda:self.topDestroy(top))
            #Creating entry Labels to input text data
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
            #empty object created in order to get the number of players in the roster to prevent more than 15 Players
            tim = Player(None,None,None)
            if(tim.rosterCount<=15):
                submitButton = tk.Button(top,text="Submit",command=lambda:addPlayer(fN.get(),lN.get(),jN.get()))
                submitButton.grid(row=4,column = 2)
            #AddPlayer method called when submit button is clicked in order to create player object and storing the player info into the Roster Database
            def addPlayer(fName,lName,jNum):
                if(len(fName)==0 or len(lName)==0 or len(jNum)==0):
                    #Chcecking if there is valid input
                    print("There is number(s) in your name, letter(s) in your jersey number slot, or not all of the slots are filled!")
                else:
                    newPlayer = Player(lName,fName,jNum)
                    #Executing sqlite method to create new row in database
                    c.execute("INSERT INTO roster VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",(newPlayer.firstName,newPlayer.lastName,newPlayer.number,0,0,0,0,0,0,0,0,0,0,0,0,0))
                    conn.commit()
                    print(newPlayer.firstName + " " + newPlayer.lastName + " #"+ newPlayer.number)
                    #Destroying Window
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
        #Creating a List of existing players in the database using the list obtained from sqlite fetchall method
        playerList = []
        for dbPlayer in dbPlayerList:
            pList = list(dbPlayer)
            x = Player(pList[1],pList[0],pList[2])
            print(x.printInfo())
            playerList.append(x)
        #importing blank image of basketball court to be edited when creating shot chart
        courtIm = Image.open('court.png')
        draw = ImageDraw.Draw(courtIm)
        #createGameWindow method used to create the window where all fo the statistics are tracked. method is called after name for the game is set
        def createGameWindow(gameObject,conn2,c2,gameName):
            print("Enter second here")
            parent.withdraw()
            top = tk.Toplevel(parent)
            self.tlCount+=1
            top.protocol("WM_DELETE_WINDOW", lambda:self.topDestroy(top))
            top.title("Record Game Stats")
            top.minsize(width=1000,height=750)
            top.resizable(False,False)
            #The following functions are called when their respective buttons are pressed to edit the stats of the players in the game
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
            #Update Stats function is called when submit button is pressed to update the main season stats in the roster database and the game specific database using sqlite commands
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
            #The following buttons are part of the windo GUI in order to call the methods to update each of the statistics
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
            #The following labels are used to understand what each column in the table represents as well as the understanding which team's score we are viewing
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
            #placing the copy of the court above the table of statistics
            canvas = tk.Canvas(top, width = 848, height = 449)
            canvas.grid(row=0,column=0,rowspan=17,columnspan = 17)
            self.img = ImageTk.PhotoImage(Image.open('court.png'))
            iLabel = tk.Label(top,image = self.img)
            canvas.create_image(0,0,image=self.img,anchor="nw")
            #Initializing variables to be used in the radio buttons. Var is used for accessing the list of of players while half is used to define which half the shot occured
            var = tk.IntVar()
            half = tk.IntVar()
            half.set(1)
            increment = 0
            #For loop used to create the radio button list of each of the players on the roster
            for player in playerList:
                b = tk.Radiobutton(top, text=player.printInfo(), value=playerList.index(player),variable=var,indicatoron=0)
                b.grid(row=19+increment,column=0,columnspan=2,sticky="w")
                increment+=1
            increment = 0
            #For loop used to create the labels represeting the player statistics across the board
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
            #Radio buttons used to represent the specific half of the game that is ongoing to be stored in the shots database
            half1 = tk.Radiobutton(top,text="First Half", value = 1,variable=half).grid(row=4,column=18)
            half2 = tk.Radiobutton(top,text="Second Half", value = 2,variable=half).grid(row=5,column=18)
            #initializing the radius of the circles drawn on the shot chart
            r=10
            #printcooordsL method keeps track of a "LeftClick" on the shot chart represting a made shot
            def printcoordsL(event):
                print("LeftClick")
                print (type(event.x))
                #Simple check used to see whether the shot occured within the small rectangular area near the baseline inside 3 point line or if it is beyond the rectangular area that the shot occured within the 3 point line using the distance formula
                if((event.x<=50 and (event.y>40 and event.y<400)) or(math.sqrt((event.x - 50)**2 + (event.y - 220)**2)<170) and event.x<420) or ((event.x>=750 and (event.y>40 and event.y<400)) or (math.sqrt((event.x - 792)**2 + (event.y - 220)**2)<170) and event.x>420):
                    playerList[var.get()].up2Pt()
                    print("Here")
                    print(playerList[var.get()].twoMd)
                    print(playerList[var.get()].twoAtt)
                    tk.Label(top, text=playerList[var.get()].twoMd).grid(row=18+var.get()+1,column=2,sticky="e")
                    tk.Label(top, text=playerList[var.get()].twoAtt).grid(row=18+var.get()+1,column=3,sticky="e")
                    #saving the shot x,y inside the shots database of the game
                    c2.execute("INSERT INTO shots VALUES(?, ?, ?, ?, ?)",(playerList[var.get()].firstName[0:1]+playerList[var.get()].lastName[0:1]+playerList[var.get()].number,event.x,event.y,True,half.get()))
                    conn2.commit()
                    print(half.get())
                else:
                    #if the shot isnt't inside the constraints then its value is a 3pointer and the stats are updated accordingly
                    print("not here")
                    playerList[var.get()].up3Pt()
                    print(playerList[var.get()].threeMd)
                    print(playerList[var.get()].threeAtt)
                    tk.Label(top, text=playerList[var.get()].threeMd).grid(row=18+var.get()+1,column=4,sticky="e")
                    tk.Label(top, text=playerList[var.get()].threeAtt).grid(row=18+var.get()+1,column=5,sticky="e")
                    c2.execute("INSERT INTO shots VALUES(?, ?, ?, ?, ?)",(playerList[var.get()].firstName[0:1]+playerList[var.get()].lastName[0:1]+playerList[var.get()].number,event.x,event.y,True,half.get()))
                    conn2.commit()
                points = 0
                #updating the points in the gameObject for the plague
                for player in playerList:
                    points+=player.calcPts()
                gameObject.plageScore=points
                scoreLabel = tk.Label(top,text=gameObject.plageScore).grid(row=11,column=19,sticky="w")
                #Drawing an ellipse and writing the initials of the player who took the shots inside the ellipse onto the canvas displayed on the GUI and the ImageDraw object
                draw.ellipse([event.x-r,event.y-r,event.x+r,event.y+r],fill= 'green')
                draw.text([event.x-r,event.y-r],text=playerList[var.get()].getInitials(),font=ImageFont.load_default())
                make = canvas.create_oval(event.x-r, event.y-r, event.x+r, event.y+r, fill='green')
                canvas.create_text(event.x,event.y,text=playerList[var.get()].getInitials(),font=("Arial",8))
                #saving the ImageDraw object
                courtIm.save(gameName+".png")
            #printcooordsR method keeps track of a "RightClick" on the shot chart represting a missed shot
            def printcoordsR(event):
                print("RightClick")
                print (event.x,event.y)
                #Simple check used to see whether the shot occured within the small rectangular area near the baseline inside 3 point line or if it is beyond the rectangular area that the shot occured within the 3 point line using the distance formula
                if((event.x<=50 and (event.y>40 and event.y<400))or(math.sqrt((event.x - 50)**2 + (event.y - 220)**2)<170) and event.x<420) or ((event.x>=750 and (event.y>40 and event.y<400)) or (math.sqrt((event.x - 792)**2 + (event.y - 220)**2)<170) and event.x>420):
                    playerList[var.get()].up2PtM()
                    tk.Label(top, text=playerList[var.get()].twoMd).grid(row=18+var.get()+1,column=2,sticky="e")
                    tk.Label(top, text=playerList[var.get()].twoAtt).grid(row=18+var.get()+1,column=3,sticky="e")
                    c2.execute("INSERT INTO shots VALUES(?, ?, ?, ?, ?)",(playerList[var.get()].getInitials(),event.x,event.y,False,half.get()))
                    conn2.commit()
                else:
                    #if the shot isnt't inside the constraints then its value is a 3pointer and the stats are updated accordingly
                    playerList[var.get()].up3PtM()
                    tk.Label(top, text=playerList[var.get()].threeMd).grid(row=18+var.get()+1,column=4,sticky="e")
                    tk.Label(top, text=playerList[var.get()].threeAtt).grid(row=18+var.get()+1,column=5,sticky="e")
                    c2.execute("INSERT INTO shots VALUES(?, ?, ?, ?, ?)",(playerList[var.get()].getInitials(),event.x,event.y,False,half.get()))
                    conn2.commit()
                #Drawing an ellipse and writing the initials of the player who took the shots inside the ellipse onto the canvas displayed on the GUI and the ImageDraw object
                draw.ellipse([event.x-r,event.y-r,event.x+r,event.y+r],fill= 'red')
                draw.text([event.x-r,event.y-r],text=playerList[var.get()].getInitials(),font=ImageFont.load_default())
                miss = canvas.create_oval(event.x-r, event.y-r, event.x+r, event.y+r, fill='red')
                canvas.create_text(event.x,event.y,text=playerList[var.get()].getInitials(),font=("Arial",8))
                #saving the ImageDraw object
                courtIm.save(gameName+".png")
            #binding the left and right clicks to their respective methods
            canvas.bind("<Button-1>",printcoordsL)
            canvas.bind("<Button-2>",printcoordsR)
            quitButton.grid(row=3,column=18)
            top.mainloop()
        #outside of the createGameWindow method, the following is the first window seen by the user to create the game object and determine the name for the game
        if(self.tlCount==0):
            top = tk.Toplevel(parent)
            self.tlCount+=1
            top.title("Create a Game")
            top.minsize(width=300,height=100)
            top.resizable(False,False)
            top.protocol("WM_DELETE_WINDOW", lambda:self.topDestroy(top))
            #Label and entry fields to enter a game name
            tk.Label(top, text="Enter Game Name").grid(row=0)
            fN = tk.Entry(top)
            fN.grid(row=0, column=1)
            quitButton = tk.Button(top,text="Quit",command=lambda:self.topDestroy(top))
            quitButton.grid(row = 1,column = 2)
            submitButton = tk.Button(top,text="Submit",command=lambda:addGame(fN.get()))
            submitButton.grid(row=1,column = 1)
            def addGame(gName):
                #Check if the game exists or the entry is empty to prevent errors
                if(len(gName)==0) or ( os.path.isfile('Games/'+gName+'.db')):
                    print("Cannot leave name empty or file exists")
                else:
                    #Creating a game object to create all of the neccessary tables in the database as well as the instances to keep track of the score
                    newGame = Game(gName)
                    gameName=gName
                    print(newGame)
                    #creating the sqlite3 objects to connect to the database and edit items
                    conn2=sqlite3.connect('Games/'+gameName+'.db')
                    c2=conn2.cursor()
                    #ttlCount=0
                    top.withdraw()
                    #calling the createGameWindow method to display the stats tracking window after the name is all set as well as the database connection objects
                    createGameWindow(newGame,conn2,c2,gameName)
                    self.tlCount = 0
                    c.close()
            top.mainloop()
        print("return to main")
    def Season(self,parent):
        print ("Loading Data")
        parent.withdraw()
        #creating a list of player objects and storing all of the values from the tuples provided in the list from directly accessed from the roster database
        playerList=[]
        print dbPlayerList
        for i in range(0,len(dbPlayerList)):
            #creating a player object and setting all of its instances to add to the player list
            x = Player(dbPlayerList[i][1],dbPlayerList[i][0],dbPlayerList[i][2])
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
        #check if no more than one toplevel window is open
        if(self.tlCount==0):
            top = tk.Toplevel(parent)
            self.tlCount+=1
            top.resizable(False,False)
            top.title("View The Stats")
            top.protocol("WM_DELETE_WINDOW", lambda:self.topDestroy(top))
            increment = 0
            #labels for each statistic opened as the table headers as well as the title of window
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
            #printing each of the player's season statistics under the respective labels
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
        #viewGameWindow function called to view the statistics of a specific game and the shot chart of the specific game
        def viewGameWindow(gameScores,dbPlayerList,gameName):
            print("Enter second here")
            top = tk.Toplevel(parent)
            self.tlCount+=1
            playerList=[]
            top.resizable(False,False)
            #using the playerList directly accessed from game specific database to add player objects into a lsit of players
            for dbPlayer in gameDBPlayerList:
                pList = list(dbPlayer)
                x = Player(pList[1],pList[0],pList[2])
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
            #All of the labels for the stats to be displayed as well as the title of the game
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
            #listing the specific statistics of each of the players in roster for the specified game
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
            tk.Label(top,text="Plague Score:",font = ("AmericanTypewriter-Bold",15)).grid(row=2,column=18)
            tk.Label(top,text="Opponent Score:",font = ("AmericanTypewriter-Bold",15)).grid(row=3,column=18)
            tk.Label(top,text=gameScores[0][0],font = ("AmericanTypewriter",12)).grid(row=2,column=19)
            tk.Label(top,text=gameScores[0][1],font = ("AmericanTypewriter",12)).grid(row=3,column=19)
            quitButton = tk.Button(top,text="Quit",command=lambda:self.topDestroy(top))
            #importing the image of the shot chart of the game to be viewed underneath the statistics
            gameImage = Image.open(gameName+'.png')
            imageHome = ImageTk.PhotoImage(gameImage)
            backgroundLabel=tk.Label(top,image = imageHome).grid(row=increment+3,column=0,columnspan=19)
            quitButton.grid(row=increment+4,column=16)
            top.mainloop()
        #The check to see no more than one top level window is open. the following code is what is run first to query the name of the game to be viewd before the viewGameWindow function is called for that specified game.
        if(self.tlCount==0):
            top = tk.Toplevel(parent)
            self.tlCount+=1
            top.title("View a Game")
            top.minsize(width=300,height=100)
            top.resizable(False,False)
            top.protocol("WM_DELETE_WINDOW", lambda:self.topDestroy(top))
            #The entry option to type the name of the game to be opened for view
            tk.Label(top, text="Enter Game Name").grid(row=0)
            fN = tk.Entry(top)
            fN.grid(row=0, column=1)
            quitButton = tk.Button(top,text="Quit",command=lambda:self.topDestroy(top))
            quitButton.grid(row = 1,column = 2)
            submitButton = tk.Button(top,text="Submit",command=lambda:findGame(fN.get()))
            submitButton.grid(row=1,column = 1)
            #findGame method called when the submit button is pressed in order to access the data for the specified game if it exists
            def findGame(gName):
                #check to see if the game exists or the entry field is left empty
                if(len(gName)==0) or (not os.path.isfile('Games/'+gName+'.db')):
                    print("Cannot leave name empty or game does not exist")
                else:
                    top.withdraw()
                    #accessing the game directory and creating a sqlite conection to the database
                    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
                    db_path = os.path.join(BASE_DIR, "Games/"+gName+".db")
                    conn3=sqlite3.connect(db_path)
                    c3=conn3.cursor()
                    c3.execute("""SELECT * FROM stats""")
                    gameDBPlayerList = list(c3.fetchall())
                    c3.execute("""SELECT * FROM final""")
                    gameScores=list(c3.fetchall())
                    #calling the viewGameWindow method passing the sqlite fetched data and the name of the game
                    viewGameWindow(gameDBPlayerList,gameScores,gName)
                    self.tlCount = 0
                    c3.close()
            top.mainloop()
        print("return to main")
    #the topDestroy method is used to destroy the Toplevel windows and return to the main menu
    def topDestroy(self,top):
        top.destroy()
        self.tlCount=0
        parent = tk.Toplevel()
        parent.title("Home")
        my_gui = MainGUI(parent)
        parent.mainloop()


#main method
if __name__ == '__main__':
    root = tk.Tk()
    root.title("Home")
    #accesing the list of players and season statistics from the roster database to be used by other menu options
    c.execute("SELECT * FROM roster")
    dbPlayerList = list(c.fetchall())
    #creating an instance of the main menu to open in the main method
    my_gui = MainGUI(root)
    root.mainloop()
    print(c.fetchall())
    conn.close()
