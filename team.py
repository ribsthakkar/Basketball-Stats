import sqlite3


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

class Team:
    rosterCount = 0
    def __init__(self,lastName,firstName,number):
        #conn = sqlite3.connect('roster.db')
        #c = conn.cursor()
        self.firstName=firstName
        self.lastName=lastName
        self.number = number
        twoAtt = 0
        threeAtt = 0
        ftAtt = 0
        twoMd = 0
        threeMd = 0
        ftMd = 0
        reb = 0
        stl = 0
        blk = 0
        ast = 0
        to = 0
        fls = 0
        pm = 0

        #conn.commit()
        #conn.close()
    def calcPts(self):
        return 2*self.twoMd + 3*self.threeMd + self.ftMd
    def calc3Per(self):
        if(self.threeAtt>0):
            return self.threeMd/self.threeAtt
        else:
            return 0
    def calcFG(self):
        if(self.threeAtt+self.twoAtt>0):
            return (self.threeMd+self.twoMd)/(self.threeAtt+self.twoAtt)
        else:
            return 0
    def calcFt(self):
        if(self.ftAtt>0):
            return ftMd/ftAtt
        else:
            return 0
    def printInfo(self):
        return "Name & Jersey Number: "+ self.firstName+" "+ self.lastName+" #"+self.number
