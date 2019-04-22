from tkinter import*
from random import*
root=Tk()
canv=Canvas(root, width=400,height=400)
colors=['blue', 'green', 'red', 'yellow']
for i in range(12):
    R=randint(5,50)
    x=randint(R,400-R)
    y=randint(R,400-R)
    color=choice(colors)
    canv.create_oval(x-R,y-R, x+R, y+R, fill=color)
canv.pack()
mainloop()
