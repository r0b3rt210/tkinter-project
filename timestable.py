import tkinter 
import tkinter.messagebox
import tkinter.ttk

screen = tkinter.Tk()
screen.geometry("400x700")
screen.title("times table")
numbers = [i for i in range(1 , 51)]


title = tkinter.Label(screen , text = "multipliction table")
numberandrange = tkinter.Label(screen , text="enter number and range:")
usernumber = tkinter.ttk.Combobox(screen , values=numbers)

def multiplication():
    numberselected = int(usernumber.get())
    answers = ""
    for i in range(21):
        answers = answers + f"{numberselected} x  {i} = {numberselected*i}\n"#\n inserts a new line
    
    result.config(text = answers)


range10 = tkinter.Radiobutton(screen , text=10)
range20 = tkinter.Radiobutton(screen , text=20)
range30 = tkinter.Radiobutton(screen , text=30)
execute = tkinter.Button(screen , text="generate" , command = multiplication)
result = tkinter.Label(screen , text="")
title.grid(row = 1 , column=2)
numberandrange.grid(row = 3 , column=1)
usernumber.grid(row = 3 , column=2, padx=12)
range10.grid(row = 2 , column=3 , padx=12)
range20.grid(row = 3 , column=3,padx=12)
range30.grid(row = 4 , column=3,padx=12)
execute.grid(row = 5 , column=2,pady=12)
result.grid(row=6 , column=2)
screen.mainloop()


