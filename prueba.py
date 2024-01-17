from tkinter import *
from rgbtohex import _from_rgb


def raise_frame(frame):
    frame.tkraise()

root = Tk()
root.geometry('650x400')

bgcolor = _from_rgb((15,114,219))
root.configure(bg = bgcolor)

f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)
f4 = Frame(root)

for frame in (f1, f2, f3, f4):
    frame.grid(row=0, column=0, sticky='news')

Label(f1, text= 'SWAP', bg = bgcolor, justify = 'center',fg = "white", font = ('Arial', 10)).place(relx = 0.5, rely= 0.3, anchor = 'center')
Button(f1, text='Go to frame 2', command=lambda:raise_frame(f2))


Label(f2, text='FRAME 2').pack()
Button(f2, text='Go to frame 3', command=lambda:raise_frame(f3)).pack()

Label(f3, text='FRAME 3').pack(side='left')
Button(f3, text='Go to frame 4', command=lambda:raise_frame(f4)).pack(side='left')

Label(f4, text='FRAME 4').pack()
Button(f4, text='Goto to frame 1', command=lambda:raise_frame(f1)).pack()

raise_frame(f1)
root.mainloop()