from tkinter import*
import math
root=Tk()
root.title('Калькулятор')

text1=Entry(root, width=38, justify='right')
text1.grid(row=0, column=0, columnspan=5)
def number_button(num):
    text1.insert(END,str(num))
    
def clear():
    text1.delete(0,END)

def clear2():
    n=text1.get()
    text1.delete(len(n)-1)
    
def factorial():
    s=int(text1.get())
    f=1
    for i in range(1,s+1):
        f*=1
    clear()
    text1.insert(0,f)
    
def sqrt():
    s=int(text1.get())
    f=math.sqrt(s)
    clear()
    text1.insert(0,f)

def iquel()

btn1=Button(root, text='MC', width=4, height=1)
btn1.grid(row=1, column=0, padx=5, pady=5)
btn2=Button(root, text='MR', width=4, height=1)
btn2.grid(row=1, column=1, padx=5)
btn3=Button(root, text='MS', width=4, height=1)
btn3.grid(row=1, column=2, padx=5)
btn4=Button(root, text='M+', width=4, height=1)
btn4.grid(row=1, column=3, padx=5)
btn5=Button(root, text='M-', width=4, height=1)
btn5.grid(row=1, column=4, padx=5)

btn6=Button(root, text='^', width=4, height=1, command=lambda:number_button('**'))
btn6.grid(row=2, column=0, padx=5, pady=3)
btn7=Button(root, text='CE', width=4, height=1, command=clear)
btn7.grid(row=2, column=1, padx=5)
btn8=Button(root, text='C', width=4, height=1, command=clear2)
btn8.grid(row=2, column=2, padx=5)
btn9=Button(root, text='n!', width=4, height=1, command=factorial)
btn9.grid(row=2, column=3, padx=5)
btn9=Button(root, text='sqrt', width=4, height=1, command=sqrt)
btn9.grid(row=2, column=4, padx=5)

btn10=Button(root, text='7', width=4, height=1, command=lambda : number_button(7))
btn10.grid(row=3, column=0, padx=5)
btn11=Button(root, text='8', width=4, height=1, command=lambda : number_button(8))
btn11.grid(row=3, column=1, padx=5, pady=3)
btn12=Button(root, text='9', width=4, height=1, command=lambda : number_button(9))
btn12.grid(row=3, column=2, padx=5)
btn13=Button(root, text='/', width=4, height=1)
btn13.grid(row=3, column=3, padx=5)
btn14=Button(root, text='(', width=4, height=1)
btn14.grid(row=3, column=4, padx=5)

btn15=Button(root, text='4', width=4, height=1, command=lambda : number_button(4))
btn15.grid(row=4, column=0, padx=5)
btn16=Button(root, text='5', width=4, height=1, command=lambda : number_button(5))
btn16.grid(row=4, column=1, padx=5, pady=3)
btn17=Button(root, text='6', width=4, height=1, command=lambda : number_button(6))
btn17.grid(row=4, column=2, padx=5)
btn18=Button(root, text='*', width=4, height=1)
btn18.grid(row=4, column=3, padx=5)
btn19=Button(root, text=')', width=4, height=1)
btn19.grid(row=4, column=4, padx=5)

btn20=Button(root, text='1', width=4, height=1, command=lambda : number_button(1))
btn20.grid(row=5, column=0, padx=5)
btn21=Button(root, text='2', width=4, height=1, command=lambda : number_button(2))
btn21.grid(row=5, column=1, padx=5, pady=3)
btn22=Button(root, text='3', width=4, height=1, command=lambda : number_button(3))
btn22.grid(row=5, column=2, padx=5)
btn23=Button(root, text='-', width=4, height=1)
btn23.grid(row=5, column=3, padx=5)
btn24=Button(root, text='=', width=4, height=3)
btn24.grid( rowspan=2, row=5, column=4, padx=5)

btn25=Button(root, text='0', height=1, width=12)
btn25.grid(row=6, column=0, padx=5, columnspan=2)
btn26=Button(root, text='.', width=4, height=1, command=lambda:number_button('.'))
btn26.grid(row=6, column=2, padx=5, pady=3)
btn27=Button(root, text='+', width=4, height=1, command=lambda:number_button('+'))
btn27.grid(row=6, column=3, padx=5)

root.mainloop()
