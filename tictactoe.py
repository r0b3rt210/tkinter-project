import tkinter
import tkinter.messagebox 
screen = tkinter.Tk()
screen.geometry("300x300")
screen.title("tictactoe")

#buttons 
topleft = tkinter.Button(screen , width=5 , height=3, command = lambda:playerchoice(topleft))
topmid = tkinter.Button(screen, width=5 , height=3, command = lambda:playerchoice(topmid))
topright = tkinter.Button(screen, width=5 , height=3, command = lambda:playerchoice(topright))
midleft = tkinter.Button(screen, width=5 , height=3, command = lambda:playerchoice(midleft))
midmid = tkinter.Button(screen, width=5 , height=3 , command = lambda:playerchoice(midmid))
midright = tkinter.Button(screen, width=5 , height=3 , command = lambda:playerchoice(midright))
bottomleft = tkinter.Button(screen, width=5 , height=3 , command=lambda:playerchoice(bottomleft))
bottommid = tkinter.Button(screen, width=5 , height=3 , command = lambda:playerchoice(bottommid))
bottomright = tkinter.Button(screen, width=5 , height=3 , command = lambda:playerchoice(bottomright))


def playerchoice(b_selected):
    b_selected.config(text="X")
   # x = tkinter.Label(screen , text = "X")


#turn
#turn = tkinter.Label(screen , text = f"d {} turn")

#
topleft.grid(row=1 , column=1 ,columnspan=1 , padx= 5 , pady=5)
topmid.grid(row = 1 , column= 2 , columnspan=1 , padx=5 , pady=5)
topright.grid(row = 1 , column= 3 , columnspan=1 , padx = 5 , pady=5)
midleft.grid(row =2 , column = 1 , columnspan=1 , padx=5 , pady=5)
midmid.grid(row = 2 , column=2 ,columnspan=1 , padx=5 , pady=5)
midright.grid(row = 2 , column=3 , columnspan=1 ,padx=5 , pady=5)
bottomleft.grid(row=3 , column=1 , columnspan=1, padx=5 , pady=5)
bottommid.grid(row = 3 , column= 2 ,  columnspan=1 , padx=5 , pady=5)
bottomright.grid(row = 3 , column = 3 , columnspan=1, padx=5 , pady=5)
screen.mainloop()

# make it so that u cant change the value or the bot  , try to make  the bot have its own chocie