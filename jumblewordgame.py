import tkinter
import tkinter.messagebox
screen = tkinter.Tk()
screen.geometry("400x400")
screen.title("jumbled word game")
#words=[] 
jumbledword = "ym mena si terbor"
titlee = tkinter.Label(screen , text=  "jumbled word game")
jumbledword = tkinter.Label(screen , text = jumbledword )
useranswer = tkinter.Entry(screen)

titlee.grid(row=1 ,column=1)
jumbledword.grid(row = 2 , column=1)
useranswer.grid(row = 3  , column=1)





screen.mainloop()