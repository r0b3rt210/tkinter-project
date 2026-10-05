import tkinter
import tkinter.messagebox 
import random
screen = tkinter.Tk()
screen.geometry("400x500")
screen.title("tictactoe")

#buttons 
topleft = tkinter.Button(screen , width=5 , height=3,font = ("Andalus" , 20) ,  command = lambda:playerchoice(topleft))
topmid = tkinter.Button(screen, width=5 , height=3,font =("Andalus" , 20), command = lambda:playerchoice(topmid))
topright = tkinter.Button(screen, width=5 , height=3, font =("Andalus" , 20),command = lambda:playerchoice(topright))
midleft = tkinter.Button(screen, width=5 , height=3, font =("Andalus" , 20),command = lambda:playerchoice(midleft))
midmid = tkinter.Button(screen, width=5 , height=3 , font =("Andalus" , 20),command = lambda:playerchoice(midmid))
midright = tkinter.Button(screen, width=5 , height=3 ,font= ("Andalus" , 20),  command = lambda:playerchoice(midright))
bottomleft = tkinter.Button(screen, width=5 , height=3 ,font=("Andalus" , 20), command=lambda:playerchoice(bottomleft))
bottommid = tkinter.Button(screen, width=5 , height=3 ,font =("Andalus" , 20), command = lambda:playerchoice(bottommid))
bottomright = tkinter.Button(screen, width=5 , height=3 , font= ("Andalus" , 20) ,  command = lambda:playerchoice(bottomright))

choices = [topleft , topmid , topright , midleft , midmid , midright , bottomleft , bottommid , bottomright]
def playerchoice(b_selected):
    if b_selected in choices:
        b_selected.config(text="X")
        choices.remove(b_selected)
        opp()

   # x = tkinter.Label(screen , text = "X")

def opp():
    choice = random.choice(choices)
    choices.remove(choice)
    choice.config(text = "O")
#def empty():
  #  if 


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

#list all combos in tuple if the combo hgas the same x or o 