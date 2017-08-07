import sqlite3
import math
conn = sqlite3.connect('roster.db')
c = conn.cursor()
#c.execute("""CREATE TABLE roster (
#        first text,
#        last text,
#        num text,
#        att2 integer,
#        att3 integer,
#        attf integer,
#        md2 integer,
#        md3 integer,
#        mdf integer,
#        reb integer,
#        stl integer,
#        blk integer,
#        ast integer,
#        tov integer,
#        fls integer,
#        pms integer
#        )  """)
c.execute("select * from roster")
conn.commit()
results = c.fetchall()
class Team:
    rosterCount = len(results)
    print(rosterCount)
    def __init__(self,lastName,firstName,number):
        #conn = sqlite3.connect('roster.db')
        #c = conn.cursor()
        self.firstName=firstName
        self.lastName=lastName
        self.number = number
        self.twoAtt = 0
        self.threeAtt = 0
        self.ftAtt = 0
        self.twoMd = 0
        self.threeMd = 0
        self.ftMd = 0
        self.reb = 0
        self.stl = 0
        self.blk = 0
        self.ast = 0
        self.to = 0
        self.fls = 0
        self.pm = 0
        self.rosterCount+=1
        self.plusminus=[]
    def calcPM(self,newItem):
        self.plusminus.append(newItem)
        if(len(self.plusminus)%2==0):
            self.pm+=(self.plusminus[1]-self.plusminus[0])
            del self.plusminus[:]
            """i=0
            while i<len(self.plusminus)-1:
                self.pm+=(self.plusminus[i+1]-self.plusminus[i])
                i+=2"""
    def getInitials(self):
        return self.firstName[0:1]+self.lastName[0:1]+self.number
    def calcPts(self):
        return 2*self.twoMd + 3*self.threeMd + self.ftMd
    def calc3Per(self):
        if(self.threeAtt>0):
            return round(((float(self.threeMd)/float(self.threeAtt)))*100,1)
        else:
            return 0
    def calcFG(self):
        if(self.threeAtt+self.twoAtt>0):
            return round((float(self.threeMd+self.twoMd)/float(self.threeAtt+self.twoAtt))*100,1)
        else:
            return 0
    def calcFt(self):
        if(self.ftAtt>0):
            return round((float(self.ftMd)/float(self.ftAtt))*100,1)
        else:
            return 0
    def upReb(self):
        self.reb+=1
    def downReb(self):
        if(not (self.reb==0)):
            self.reb-=1
    def upStl(self):
        self.stl+=1
    def downStl(self):
        if(not(self.stl==0)):
            self.stl-=1
    def upBlk(self):
        self.blk+=1
    def downBlk(self):
        if(not(self.blk==0)):
            self.blk-=1
    def upAst(self):
        self.ast+=1
    def downAst(self):
        if(not(self.ast==0)):
            self.ast-=1
    def upFls(self):
        self.fls+=1
    def downFls(self):
        if(not(self.fls==0)):
            self.fls-=1
    def upTo(self):
        self.to+=1
    def downTo(self):
        if(not(self.to==0)):
            self.to-=1
    def upFT(self):
        self.ftAtt+=1
        self.ftMd+=1
    def downFT(self):
        if(not(self.ftAtt==0)):
            self.ftAtt-=1
            self.ftMd-=1
    def upFTM(self):
        self.ftAtt+=1
    def downFTM(self):
        if(not(self.ftAtt==0)):
            self.ftAtt-=1
    def up2Pt(self):
        self.twoAtt+=1
        self.twoMd+=1
    def down2Pt(self):
        if(not(self.twAtt==0)):
            self.twoAtt-=1
            self.twoMd-=1
    def up2PtM(self):
        self.twoAtt+=1
    def down2PtM(self):
        if(not(self.twoAtt==0)):
            self.twoAtt-=1
    def up3Pt(self):
        self.threeAtt+=1
        self.threeMd+=1
    def down3Pt(self):
        if(not(self.threeAtt==0)):
            self.threeAtt-=1
            self.threeMd-=1
    def up3PtM(self):
        self.threeAtt+=1
    def down3PtM(self):
        if(not(self.threeAtt==0)):
            self.threeAtt-=1
    def printInfo(self):
        return "Name & Jersey Number: "+ self.firstName+" "+ self.lastName+" #"+self.number
