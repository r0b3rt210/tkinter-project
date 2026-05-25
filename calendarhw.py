import tkinter
import calendar
screen = tkinter.Tk()
screen.geometry("300x300")
screen.title("calendar hw")
def show_calendar():
    year = int(entertext.get())
    calendartext = calendar.calendar(year)
    screen2 = tkinter.Tk()
    screen2.geometry("650x1000")
    screen2.title("calendar")
    text1 = tkinter.Text(screen2  , height=40 )
    text1.insert(tkinter.END , calendartext)
    text1.grid(row = 1 , column=1)
    screen2.mainloop()
def exit():
    screen.destroy()


calendarr = tkinter.Label(screen , text = "Calendar" , background="gray" , fg = "black" , font=("Arial" , 54))
enteryear = tkinter.Label(screen , text = "Enter Year" , background ="green" , fg = "black", font=("Arial" , 20))
showc = tkinter.Button(screen , text = "show calendar" , background="red" , fg = "black", font=("Arial" , 20), command = show_calendar)
exit = tkinter.Button(screen , text = "exit" , background ="red" , fg = "black", font=("Arial" , 20) , command = exit)
entertext = tkinter.Entry(screen , font=("Arial" , 18))
calendarr.grid(row = 1, column=1)
enteryear.grid(row=2,column=1)
entertext.grid(row=3 ,column=1)
showc.grid(row=4 , column=1)
exit.grid(row=5 , column=1)
screen.mainloop()