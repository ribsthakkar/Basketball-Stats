import Tkinter as tk
import ttk
from PIL import ImageTk,Image

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
            quitButton = tk.Button(top,text="Quit",command=lambda:self.topDestroy(top))
            quitButton.place(x=10,y=10)
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
