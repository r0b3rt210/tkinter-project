import tkinter
screen = tkinter.Tk()
screen.geometry("350x150")
screen.title("tk")
def convertpress():
    kg = int(userweight.get())
    ansgrams = tkinter.Label(screen , text = kg*1000)
    anspounds = tkinter.Label(screen , text = kg*2.20462262)
    ansounce= tkinter.Label(screen , text = kg*35.273962)
    ansgrams.grid(row=3 , column=1)
    anspounds.grid(row=3 , column=2)
    ansounce.grid(row=3 , column=3) 
enter_weight = tkinter.Label(screen , text  = "Enter the weight in kg")
userweight = tkinter.Entry(screen)
convert = tkinter.Button(screen ,  text="convert" , command=convertpress)
grams = tkinter.Label(screen , text = "grams")
pounds = tkinter.Label(screen , text = "pounds")
ounce = tkinter.Label(screen , text = "ounce")



enter_weight.grid(row = 1, column=1)
userweight.grid(row=1,column=2)
convert.grid(row=1 ,column=3)
grams.grid(row=2 , column=1)
pounds.grid(row=2 , column=2)
ounce.grid(row=2 , column=3)

screen.mainloop()