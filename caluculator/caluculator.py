import tkinter as tk
from tkinter import *
from tkinter.ttk import *

root = tk.Tk()
root.title('simple caluculator')
p1 = PhotoImage(file = 'Lovepik_com-400254962-calculator.png')
root.iconphoto(False, p1)
screen = tk.Entry(root,width=28,borderwidth=5,validate='none')
screen.grid(column=0,columnspan=4,row=0)
rem = None
mode = None

def button_click(number):
    current = screen.get()
    screen.delete(0,END)
    screen.insert(0,str(current)+str(number))

def add():
    global rem
    global mode
    mode = 'add'
    rem = screen.get()
    screen.delete(0,END)


def clear():
    screen.delete(0,END)


def sub():
    global rem
    global mode
    mode = 'sub'
    rem = screen.get()
    screen.delete(0,END)

def div():
    global rem
    global mode
    mode = 'div'
    rem = screen.get()
    screen.delete(0,END)
    
def mult():
    global rem
    global mode
    mode = 'mult'
    rem = screen.get()
    screen.delete(0,END)

def equal():
    global nu
    global mode

    if (rem == int()):
        screen.delete(0,END)
        screen.insert(0,'error:input value to be integer')



    if(mode == 'add' ):
        rem2 = screen.get()
        add = int(rem) + int(rem2)
        screen.delete(0,END)
        screen.insert(0,str(add))
        mode = None

    if(mode == 'sub' ):
        rem2 = screen.get()
        sub = int(rem) - int(rem2)
        screen.delete(0, END)
        screen.insert(0, str(sub))
        mode = None

    if (mode == 'div' ):
        rem2 = screen.get()
        div = int(rem) / int(rem2)
        screen.delete(0, END)
        screen.insert(0, str(div))
        mode = None
        
    if (mode == 'mult' ):
        rem2 = screen.get()
        mult = int(rem) * int(rem2)
        screen.delete(0, END)
        screen.insert(0, str(mult))
        mode = None


button_1 = tk.Button(root,text='1',padx=25,pady=20,command=lambda: button_click(1))
button_2 = tk.Button(root,text='2',padx=25,pady=20,command=lambda: button_click(2))
button_3 = tk.Button(root,text='3',padx=25,pady=20,command=lambda: button_click(3))
button_4 = tk.Button(root,text='4',padx=25,pady=20,command=lambda: button_click(4))
button_5 = tk.Button(root,text='5',padx=25,pady=20,command=lambda: button_click(5))
button_6 = tk.Button(root,text='6',padx=25,pady=20,command=lambda: button_click(6))
button_7 = tk.Button(root,text='7',padx=25,pady=20,command=lambda: button_click(7))
button_8 = tk.Button(root,text='8',padx=25,pady=20,command=lambda: button_click(8))
button_9 = tk.Button(root,text='9',padx=25,pady=20,command=lambda: button_click(9))
button_0 = tk.Button(root,text='0',padx=25,pady=20,command=lambda: button_click(0))
button_a = tk.Button(root,text='add',padx=16.5,pady=20,command=lambda: add())
button_e = tk.Button(root,text='equal',padx=11,pady=20,command=lambda: equal())
button_clear = tk.Button(root,text='clear',padx=12,pady=20,command=lambda: clear())
button_sub = tk.Button(root,text='sub',padx=16.5,pady=20,command=lambda: sub())
button_div = tk.Button(root,text='/',padx=26,pady=20,command=lambda: div())
button_mult = tk.Button(root,text='*',padx=26,pady=20,command=lambda: mult())




button_1.grid(column=0, row=3)
button_2.grid(column=1, row=3)
button_3.grid(column=2, row=3)

button_4.grid(column=0, row=2)
button_5.grid(column=1, row=2)
button_6.grid(column=2, row=2)

button_7.grid(column=0, row=1)
button_8.grid(column=1, row=1)
button_9.grid(column=2, row=1)

button_0.grid(column=1, row=4)
button_a.grid(column=3,row=1)
button_e.grid(column=2,row=4)
button_clear.grid(column=0,row=4)
button_sub.grid(column=3,row=2)
button_div.grid(column=3,row=4)
button_mult.grid(column=3,row=3)


root.mainloop()
