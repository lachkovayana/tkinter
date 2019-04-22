from tkinter import*
root=Tk()
canv=Canvas(root, width=400,height=400)
canv.create_oval(100,100,250,250,fill='green')
canv.pack()
mainloop()
