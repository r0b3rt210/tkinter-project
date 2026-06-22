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
    run = True
    secondselected= int(second.get())
    minuteselected= int(minute.get())
    hourselected= int(hour.get())
    while run == True:
        if secondselected==0:
            if minuteselected==0:
            
            
                if hourselected==0:
                    run= False
                    tkinter.messagebox.showinfo( "timer" ,"times up")
                else:
                    hourselected = hourselected-1
                    minuteselected = minuteselected+59
                    secondselected = secondselected+60
            else:
                 minuteselected= minuteselected - 1
                 secondselected = secondselected + 60        
        
        secondselected = secondselected-1
        time.sleep(1) 
        h.set(hourselected)
        m.set(minuteselected)
        s.set(secondselected)
        screen.update()
        

hour = tkinter.Entry(screen,width=5 ,font=("arial",20) , textvariable=h)
minute = tkinter.Entry(screen,width=5,font=("arial",20), textvariable=m)
second = tkinter.Entry(screen,width=5,font=("arial",20), textvariable=s)
start = tkinter.Button(screen , text = "start" , font=("arial" , 20) , fg="red" , command=go)
hour.grid(row=1 , column=1 , padx=15)
minute.grid(row=1 , column=2, padx=15)
second.grid(row=1 , column=3, padx=15)
start.grid(row=2 , column=2, pady = 20)
tkinter.mainloop()

