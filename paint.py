import tkinter
from tkinter.colorchooser import askcolor
screen = tkinter.Tk()
screen.geometry("800x650")
screen.title("paint")
colour = "black"
size = 5
py = None 
px = None
eraseron = False
penon= True
def penselected():
    global penon ,eraseron
    penon=True
    eraseron=False
def spraycanselected():
    pass
def colorselected():
    global colour
    colour=askcolor()[1]
def eraserselected():
    global penon
    global eraseron
    eraseron=True
    penon = False
    
def paint(event):
    global px , py 
    size=scale.get()
    if eraseron==True:
        pencolor = "white"
    if penon==True:
        pencolor = colour
    if py and px :    
        canvas.create_line(px,py,event.x,event.y , width=size ,fill=pencolor, capstyle=tkinter.ROUND)
    py=event.y
    px = event.x
pen = tkinter.Button(screen , text="Pen")
spraycan= tkinter.Button(screen ,text="spray can")
color = tkinter.Button(screen , text="Color" ,command=colorselected)
eraser = tkinter.Button(screen , text="Eraser", command=eraserselected)
scale  = tkinter.Scale(screen, from_= 1,to=100)
canvas = tkinter.Canvas(screen , height=500 , width = 800, background="white")
canvas.bind("<B1-Motion>", paint)
pen.grid(row = 1, column=1 )
spraycan.grid(row = 1, column =2)
color.grid(row =1 , column =3)
eraser.grid(row =1 , column =4)
scale.grid(row =1 , column =5)
canvas.grid(row =2 , column =1 ,columnspan=5)
screen.mainloop()