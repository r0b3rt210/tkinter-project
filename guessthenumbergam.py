import tkinter
import random
screen = tkinter.Tk()
screen.geometry("500x500")
screen.title("guess the number")
number = random.randint(1 , 100)
def guess1():
    if number >= 50:
        print("the number is above 49")
    if number <=50:
        print("the number is less than 51")
name = tkinter.Label(screen , text = "what is your name?")
entername=tkinter.Entry(screen )
ok = tkinter.Button(screen , text = "Ok")
takeaguess = tkinter.Label(screen , text = "take a guess")
urguess=tkinter.Entry(screen )
guess = tkinter.Button(screen , text = "guess")
name.grid(row=2 , column=1)
entername.grid(row=2 , column=2)
ok.grid(row=2 , column=3)
takeaguess.grid(row=4 , column=1)
urguess.grid(row=4 , column=2)
guess.grid(row=4 , column=3)
screen.mainloop()
