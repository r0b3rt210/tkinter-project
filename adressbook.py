import tkinter
import tkinter.messagebox
import tkinter.filedialog
screen = tkinter.Tk()
screen.geometry("450x650")
screen.title("Address Book")


adressbook={}
def openn():
    global adressbook
    openfile = tkinter.filedialog.askopenfile()
    if openfile != None:
        adressbook= eval(openfile.readline())
        updateboxx()
    
def details():
    index = box.curselection()
    value = box.get(index)
    detail=adressbook[value]
    tkinter.messagebox.showinfo("details" , f"Name : {value}\n Adress : {detail[0]} \n Mobile : {detail[1]} \n Email : {detail[2]} \n Birthday : {detail[3]}")


def deletee():
    index = box.curselection()
    value= box.get(index)
    del adressbook[value]
    updateboxx()


def updateaddd():
    namee = nameinp.get()
    adresss = addressinp.get()
    mobilee = mobileinp.get()
    emaill = emailinp.get()
    birthdayy = birthdayinp.get()
    adressbook[namee] = [adresss , mobilee , emaill , birthdayy]
    updateboxx()

def editt():
    index = box.curselection()
    value = box.get(index)
    addres , mobil , emai , birthda = adressbook[value]
    nameinp.insert(0 , value)
    addressinp.insert(0, addres)
    mobileinp.insert(0 , mobil)
    emailinp.insert(0 , emai)
    birthdayinp.insert(0 , birthda)

def updateboxx():
    box.delete(0,tkinter.END)
    for key in adressbook.keys():
        box.insert(tkinter.END , key)
    nameinp.delete(0,tkinter.END)
    addressinp.delete(0,tkinter.END)
    mobileinp.delete(0,tkinter.END)
    emailinp.delete(0,tkinter.END)
    birthdayinp.delete(0,tkinter.END)

def savee():
    savedfile = tkinter.filedialog.asksaveasfile()
    if savedfile != None:
        print(adressbook , file = savedfile)
        


title = tkinter.Label(screen, text = "My Adress Book")
open = tkinter.Button(screen , text = "Open" , command = openn)
box = tkinter.Listbox(screen)
box.bind("<<ListboxSelect>>", details)
name= tkinter.Label(screen, text = "name:")
nameinp = tkinter.Entry(screen )
address= tkinter.Label(screen, text = "address:")
addressinp = tkinter.Entry(screen )
mobile= tkinter.Label(screen, text = "mobile:")
mobileinp = tkinter.Entry(screen )
email= tkinter.Label(screen, text = "email:")
emailinp = tkinter.Entry(screen )
birthday= tkinter.Label(screen, text = "birthday:")
birthdayinp = tkinter.Entry(screen )
edit = tkinter.Button(screen, text = "Edit" , command= editt)
delete = tkinter.Button(screen , text = "Delete" , command= deletee)
updateadd = tkinter.Button(screen , text= "update/add" , command=updateaddd)
save = tkinter.Button(screen , text="             save            " ,command= savee)




title.grid(row=1,column= 2)
open.grid(row=1,column= 3)
box.grid(row=2,column= 1 , rowspan=5, columnspan=2)
name.grid(row=2,column= 3)
nameinp.grid(row=2,column=4)
address.grid(row=3 , column=3)
addressinp.grid(row = 3 , column=4)
mobile.grid(row = 4 , column = 3)
mobileinp.grid(row = 4 , column=4)
email.grid(row = 5 , column = 3)
emailinp.grid(row = 5 , column = 4)
birthday.grid(row = 6 , column = 3)
birthdayinp.grid(row = 6 , column = 4)

edit.grid(row = 7 , column =1)
delete.grid(row = 7 , column = 2)
updateadd.grid(row =7 , column = 4)
save.grid(row =8 , column=1 , columnspan=5)

screen.mainloop()