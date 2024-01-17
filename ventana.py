import tkinter as tk
from rgbtohex import _from_rgb
from enterParticipants import participants

#Initial configuration
window = tk.Tk()
window.title('SWAP')
window.geometry('650x400')

#Main Menu
bgcolor = _from_rgb((15,114,219))
window.configure(bg = bgcolor)

def saludar():
    print("¡Hola, mundo!")

welcome = tk.Label(window, text= 'SWAP', bg = bgcolor, justify = 'center',fg = "white", font = ('Arial', 50)).place(relx = 0.5, rely= 0.3, anchor = 'center')

start = tk.Button(window, text="START", command = participants(window), bg = 'red', justify = 'center',fg = "white", font = ('Arial', 20)).place(relx = 0.5, rely= 0.6, anchor = 'center')


window.resizable(True, True) 

window.mainloop()

