from tkinter import*
from random import*
root=Tk()
canv=Canvas(root, width=600,height=600)
colors=['blue', 'green', 'red', 'yellow']
count=0
for i in range(20):
    R=randint(5,50)
    x=randint(R,600-R)
    y=randint(R,600-R)
    color=choice(colors)
    canv.create_oval(x-R,y-R, x+R, y+R, fill=color)
    if color =='red':
        count+=1
print(count)
canv.pack()
mainloop()
