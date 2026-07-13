import tkinter
import tkinter.messagebox
import tkinter.filedialog
screen = tkinter.Tk()
screen.geometry("450x650")
screen.title("Notes")

def openn():
    openfile = tkinter.filedialog.askopenfile()
    if openfile != None:
        data = openfile.readlines()
        for item in data:
            box.insert(tkinter.END , item)
def deletee():
    index=box.curselection()
    box.delete(index)

def savee():
     savedfile = tkinter.filedialog.asksaveasfile()
     if savedfile != None:
        items = box.get(0,tkinter.END)
        for item in items:
            print( item ,  file= savedfile)
def addd():

    usernote = enternote.get()
    if usernote!="":
        box.insert(tkinter.END, usernote)
        enternote.delete(0,tkinter.END)
    
    
open = tkinter.Button(screen , text = "OPEN" , font=("robot" , 20 , "bold"), command= openn )
delete = tkinter.Button(screen , text = "DELETE" , font=("robot" , 20 , "bold") , command=deletee)
save = tkinter.Button(screen , text = "SAVE" , font=("robot" , 20 , "bold") , command=savee)
add = tkinter.Button(screen , text = "ADD" , font=("robot" , 20 , "bold" ), command=addd)#
box = tkinter.Listbox(screen , font=("robot" , 20 , "bold"))
enternote = tkinter.Entry(screen  , width=20  , font=("robot" , 20 , "bold"))
open.grid(row = 1 , column=1)
delete.grid(row = 1 , column=2)
save.grid(row = 1 , column=3 , padx=15)
enternote.grid(row = 2 , column=1, columnspan= 2)
add.grid(row = 2 , column=3 ,pady=10)
box.grid(row = 3 , column =1 , columnspan = 3 , pady=20)
screen.mainloop()
