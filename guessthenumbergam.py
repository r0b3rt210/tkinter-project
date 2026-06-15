import tkinter
import random
import tkinter.messagebox
screen = tkinter.Tk()
screen.geometry("500x500")
screen.title("guess the number")
number = random.randint(1 , 100)
playername = ""
def guess1():
    playerguess = int(urguess.get())
    if number > playerguess:
        tkinter.messagebox.showwarning("guess" , "your number is lower")
  
    elif number < playerguess:
        tkinter.messagebox.showwarning("guess" , "your number is higher")
    elif number == playerguess:
        tkinter.messagebox.showinfo("guess" , "your guess is correct ")

def namee():
    playername = entername.get()
    tkinter.messagebox.showinfo("greeting" , f"hello {playername}, guess the number between 1-100")
name = tkinter.Label(screen , text = "what is your name?")
entername=tkinter.Entry(screen )
ok = tkinter.Button(screen , text = "Ok" , command=namee)
takeaguess = tkinter.Label(screen , text = f"take a guess,{playername}")
urguess=tkinter.Entry(screen )
guess = tkinter.Button(screen , text = "guess" , command=guess1)
name.grid(row=2 , column=1)
entername.grid(row=2 , column=2)
ok.grid(row=2 , column=3)
takeaguess.grid(row=4 , column=1)
urguess.grid(row=4 , column=2)
guess.grid(row=4 , column=3)
screen.mainloop()
