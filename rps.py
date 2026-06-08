import tkinter
import random
screen = tkinter.Tk()
screen.geometry("500x500")
screen.title("rock paper scissors")
def selection_S():
    selection = "scissors"
    yourselection = tkinter.Label(screen , text= "you selected: Scissors")
    yourselection.grid(row=6, column=1)
    Winner(selection)
def selection_r():
    selection = "rock"
    yourselection = tkinter.Label(screen , text= "you selected: Rock")
    yourselection.grid(row=6 , column=1)
    Winner(selection)
def selection_p():
    selection = "paper"
    yourselection = tkinter.Label(screen , text= "you selected: Paper")
    yourselection.grid(row=6 , column=1)
    Winner(selection)    
def Winner(selection):
    global winner
    cselection = [ "rock " , " paper " , "scissors "]
    cchoice = cselection[random.randint(0,2)]
    computersselection.config(text=f"computer selected: {cchoice}")
    winner = "h"

    if selection == "rock" and cchoice=="paper":
        winner = "computer"
        winnerlabel.config(text = winner )
    if selection=="paper" and cchoice=="paper":
        winner = "tie"
        winnerlabel.config(text = winner )
    if selection=="scissors" and cchoice=="paper":
        winner = "player"
        winnerlabel.config(text = winner )
    if selection=="rock" and cchoice=="scissors":
        winner = "computer"
        winnerlabel.config(text = winner )
    if selection=="paper" and cchoice=="scissors":
        winner = "computer"
        winnerlabel.config(text = winner )
    if selection=="scissors" and cchoice=="scissors":
        winner = "tie"
        winnerlabel.config(text = winner )
    if selection=="rock" and cchoice=="rock":
        winner = "tie"
        winnerlabel.config(text = winner )
    if selection=="paper" and cchoice=="rock":
        winner = "player"
        winnerlabel.config(text = winner )
    if selection=="scissors" and cchoice=="rock":
        winner = "computer"
        winnerlabel.config(text = winner )

   



rockpaperscissors = tkinter.Label(screen , text="rock paper scissors" )
winnerlabel = tkinter.Label(screen , text = "winner is ")

options = tkinter.Label(screen , text = "options:")
rock = tkinter.Button(screen , text = "rock", bg="pink", command=selection_r)
paper = tkinter.Button(screen , text = "paper", bg="gray", command=selection_p)
scissors = tkinter.Button(screen , text = "scissors" , bg="cyan" , command=selection_S)
#score = tkinter.Label(screen , text = "score:")

computersselection = tkinter.Label(screen , text="")

rockpaperscissors.grid(row=1 , column=2)

options.grid(row=3 , column=1)
rock.grid(row=4 , column=1)
paper.grid(row=4 , column=2)
scissors.grid(row=4 , column=3)
winnerlabel.grid(row=8 , column=2)
#score.grid(row=5 , column=1)

computersselection.grid(row=7 , column=1)
screen.mainloop()
