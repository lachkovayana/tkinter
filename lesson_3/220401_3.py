from tkinter import*
from random import*
root=Tk()
canv=Canvas(root, width=400,height=400)
for i in range(10):
    R=randint(5,50)
    x=randint(R,400-R)
    y=randint(R,400-R)
    canv.create_oval(x-R,y-R, x+R, y+R, fill='blue')
canv.pack()
mainloop()
