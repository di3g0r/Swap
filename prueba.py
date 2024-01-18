import tkinter as tk
from rgbtohex import _from_rgb


def raise_frame(frame):
    frame.tkraise()
    frame.pack()

root = tk.Tk()
root.geometry('650x400')

bgcolor = _from_rgb((15,114,219))
root.configure(bg = bgcolor)

f1 = tk.Frame(root)
f2 = tk.Frame(root)
f3 = tk.Frame(root)
f4 = tk.Frame(root)


tk.Label(f1, text= 'SWAP', bg = bgcolor, justify = 'center',fg = "white", font = ('Arial', 10)).place(relx = 0.5, rely= 0.3, anchor = 'center')
tk.Button(f1, text='Go to frame 2', command=lambda:raise_frame(f2)).pack()


tk.Label(f2, text='FRAME 2').pack()
tk.Button(f2, text='Go to frame 3', command=lambda:raise_frame(f3)).pack()

tk.Label(f3, text='FRAME 3').pack(side='left')
tk.Button(f3, text='Go to frame 4', command=lambda:raise_frame(f4)).pack(side='left')

tk.Label(f4, text='FRAME 4').pack()
tk.Button(f4, text='Goto to frame 1', command=lambda:raise_frame(f1)).pack()


raise_frame(f1)

root.mainloop()