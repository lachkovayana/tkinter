from tkinter import*
from random import*
root=Tk()
canv=Canvas(root, width=400,height=400)
R=randint(5,200)
x=randint(R,400-R)
y=randint(R,400-R)
canv.create_oval(x-R,y-R, x+R, y+R, fill='blue')
canv.pack()
mainloop()
