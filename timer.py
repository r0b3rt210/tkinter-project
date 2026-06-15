import tkinter 
import tkinter.messagebox
import time
screen = tkinter.Tk()
screen.geometry("350x250")
screen.title("timer")
h=tkinter.StringVar()
m=tkinter.StringVar()
s=tkinter.StringVar()
h.set("00")
m.set("00")
s.set("00")
def go():
    secondselected= int(second.get())
    minuteselected= int(minute.get())
    hourselected= int(hour.get())


hour = tkinter.Entry(screen,width=5 ,font=("arial",20) , textvariable=h)
minute = tkinter.Entry(screen,width=5,font=("arial",20), textvariable=m)
second = tkinter.Entry(screen,width=5,font=("arial",20), textvariable=s)
start = tkinter.Button(screen , text = "start" , font=("arial" , 20) , fg="red")
hour.grid(row=1 , column=1 , padx=15)
minute.grid(row=1 , column=2, padx=15)
second.grid(row=1 , column=3, padx=15)
start.grid(row=2 , column=2, pady = 20)
tkinter.mainloop()

