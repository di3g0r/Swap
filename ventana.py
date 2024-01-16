import tkinter as tk
from rgbtohex import _from_rgb

#Initial configuration
window = tk.Tk()
window.title('Swap')
window.geometry('650x400')
bgcolor = _from_rgb((15,114,219))
window.configure(bg = bgcolor)

welcome = tk.Label(window, text= 'SWAP', bg = bgcolor,  justify = 'center',fg = "white", font = ('Arial', 24))
welcome.place(x = 230, y = 40)  
welcome.pack()

window.resizable(True, True) 

window.mainloop()

