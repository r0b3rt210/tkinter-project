import tkinter
screen = tkinter.Tk()
screen.geometry("200x100")
screen.title("login")
def login():
    username1 = username.get()
    password1 = password.get()
    if username1 == "robert" and password1 == "robert123":
        print("correct")
    else:
        print("username or password may be incorrect")
label1 = tkinter.Label(screen ,  text="username")
label2 = tkinter.Label(screen ,  text="password")
username = tkinter.Entry(screen )
password = tkinter.Entry(screen )
login = tkinter.Button(screen , text= "login" , bg = "green" ,command = login) 
cancel = tkinter.Button(screen , text= "cancel" , bg = "red" ) 
label1.grid(row=1 , column=1)
label2.grid(row=2 , column=1)
username.grid(row=1, column=2)
password.grid(row=2, column=2)
login.grid(row=3, column=1)
cancel.grid(row=3, column=2)
screen.mainloop()