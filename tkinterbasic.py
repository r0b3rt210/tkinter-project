import tkinter
screen = tkinter.Tk()
screen.geometry("750x750")
screen.title("tkinter basics")
label1 = tkinter.Label(screen ,  text="hello" , bg="red", fg = "white") #label dispays text on screen #read only text
entry1 = tkinter.Entry(screen )   #input from user
button1 = tkinter.Button(screen , text= "press me" ) #self explanatory   #]
label1.pack() #  pack is to put  it into  your screen
entry1.pack( )
button1.pack()
screen.mainloop()
