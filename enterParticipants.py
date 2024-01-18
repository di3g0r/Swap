import tkinter as tk
import time
from rgbtohex import _from_rgb

def participants(root):
    root.destroy()

    window = tk.Tk()
    window.title('SWAP')
    window.geometry('650x400')

    # Main Menu
    bgcolor = _from_rgb((15, 114, 219))
    window.configure(bg=bgcolor)

    def take_input():
        while True:
            try:
                input_text = answer.get(1.0, "end-1c")
                input_number = int(input_text)
                return input_number
            except ValueError:
                window.update()

    def num():
        print(take_input())

    ptc = tk.Label(window, text='How Many Participants ?', bg=bgcolor, justify='center', fg="white",
                   font=('Arial', 38)).place(relx=0.5, rely=0.1, anchor='center')
    
    only_nums = tk.Label(window, text='Please enter numbers only!!!', bg=bgcolor, justify='center', fg="white",
                   font=('Arial', 15)).place(relx=0.5, rely=0.2, anchor='center')

    answer = tk.Text(window, height=1, width=2, bg='white', font=('Arial', 20))
    answer.place(relx=0.5, rely=0.4, anchor='center')

    enter = tk.Button(window, text="ENTER", command=num, justify='center', fg="black", font=('Arial', 20))
    enter.place(relx=0.5, rely=0.6, anchor='center')

    window.resizable(True, True)

    window.mainloop()



    
