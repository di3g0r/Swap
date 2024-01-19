import tkinter as tk
from rgbtohex import _from_rgb
import time
import random
from PIL import ImageTk, Image
from sendEmail import sendMail
from email.message import EmailMessage

random.seed()

names_list = []
email_list = []

cont_names = 0

pairs = {}

def saludar():
    print("¡Hola, mundo!")


def MainMenu():
    #Initial configuration
    window = tk.Tk()
    window.title('SWAP')
    window.geometry('650x400')

    #Main Menu
    bgcolor = _from_rgb((15,114,219))
    window.configure(bg = bgcolor)

    welcome = tk.Label(window, text= 'SWAP', bg = bgcolor, justify = 'center',fg = "white", font = ('Arial', 50)).place(relx = 0.5, rely= 0.3, anchor = 'center')

    start = tk.Button(window, text="START", command = lambda:participants(window), justify = 'center',fg = "black", font = ('Arial', 20)).place(relx = 0.5, rely= 0.6, anchor = 'center')


    window.resizable(True, True) 

    window.mainloop()

def participants(root):
    root.destroy()

    window = tk.Tk()
    window.title('SWAP')
    window.geometry('650x400')
    bgcolor = _from_rgb((15, 114, 219))
    window.configure(bg=bgcolor)

    def take_input():
        while True:
            try:
                input_text = answer.get(1.0, "end-1c")
                input_number = int(input_text)
                if input_number < 3:
                    answer.delete(1.0, tk.END)
                else:
                    return True, input_number
            except ValueError:
                window.update()

    def num():
        print(take_input())

    def next():
        x, input_number = take_input()
        if x == True:
            confirmation(window, input_number)

    ptc = tk.Label(window, text='How Many Participants ?', bg=bgcolor, justify='center', fg="white",
                   font=('Arial', 38)).place(relx=0.5, rely=0.1, anchor='center')
    
    only_nums = tk.Label(window, text='Please enter numbers only!!!', bg=bgcolor, justify='center', fg="white",
                   font=('Arial', 15)).place(relx=0.5, rely=0.2, anchor='center')

    answer = tk.Text(window, height=1, width=2, bg='white', font=('Arial', 20))
    answer.place(relx=0.5, rely=0.4, anchor='center')

    enter = tk.Button(window, text="ENTER", command=lambda:next(), justify='center', fg="black", font=('Arial', 20))
    enter.place(relx=0.5, rely=0.6, anchor='center')

    window.resizable(True, True)

    window.mainloop()

def confirmation(root, numParticipants):
    root.destroy()

    window = tk.Tk()
    window.title('SWAP')
    window.geometry('650x400')
    bgcolor = _from_rgb((15, 114, 219))
    window.configure(bg=bgcolor)

    ptc = tk.Label(window, text='Is ' + str(numParticipants) + ' the number of participants?', bg=bgcolor, justify='center', fg="white",
                   font=('Arial', 28)).place(relx=0.5, rely=0.1, anchor='center')
    
    no = tk.Button(window, text="NO",height= 1, width=3, command=lambda:participants(window), justify='center', fg="black", font=('Arial', 20))
    no.place(relx=0.3, rely=0.6, anchor='center')

    yes = tk.Button(window, text="YES", height= 1, width=3,command=lambda:enterParticipants(window, numParticipants), justify='center', fg="black", font=('Arial', 20))
    yes.place(relx=0.6, rely=0.6, anchor='center')
    
    window.resizable(True, True)

    window.mainloop()

def enterParticipants(root, numParticipants):
    root.destroy()

    window = tk.Tk()
    window.title('SWAP')
    window.geometry('650x400')
    bgcolor = _from_rgb((15, 114, 219))
    window.configure(bg=bgcolor)

    def add_Names_and_Emails():
        new_name = name_box.get(1.0, "end-1c")
        new_email = email_box.get(1.0, "end-1c")
        names_list.append(new_name)
        email_list.append(new_email)

        name_box.delete(1.0, tk.END)
        email_box.delete(1.0,tk.END)

        global cont_names

        cont_names += 1

        if cont_names == numParticipants:
            swapTime()
            x = sendMails()
            if x == True:
                finish(window)

    nameEmail = tk.Label(window, text='Enter Name and Email', bg=bgcolor, justify='center', fg="white",
                   font=('Arial', 28)).place(relx=0.5, rely=0.1, anchor='center')
    
    name = tk.Label(window, text='Name:', bg=bgcolor, justify='center', fg="white",
                   font=('Arial', 20)).place(relx=0.1, rely=0.3, anchor='center')
    
    email = tk.Label(window, text='Email:', bg=bgcolor, justify='center', fg="white",
                   font=('Arial', 20)).place(relx=0.1, rely=0.5, anchor='center')
    
    name_box = tk.Text(window, height=1, width=25, bg='white', font=('Arial', 20))
    name_box.place(relx=0.5, rely=0.3, anchor='center')

    email_box = tk.Text(window, height=1, width=25, bg='white', font=('Arial', 20))
    email_box.place(relx=0.5, rely=0.5, anchor='center')

    enter = tk.Button(window, text="ENTER", command=lambda:add_Names_and_Emails(), justify='center', fg="black", font=('Arial', 20))
    enter.place(relx=0.5, rely=0.7, anchor='center')

    window.resizable(True, True)

    window.mainloop()

"""def makingSwap(root):
    root.destroy()

    window = tk.Tk()
    window.title('SWAP')
    window.geometry('650x400')
    bgcolor = _from_rgb((15, 114, 219))
    window.configure(bg=bgcolor)

    wait_screen = tk.Label(window, text='We are making the SWAP hang tight!!!', bg=bgcolor, justify='center', fg="white",
                   font=('Arial', 28)).place(relx=0.5, rely=0.1, anchor='center')
    
    image = Image.open("Swap/SandClock.png")
    resize_image = image.resize((300,300))
    img = ImageTk.PhotoImage(resize_image)

    load_image = tk.Label(window, image = img)
    load_image.image = img
    load_image.place(relx=0.5, rely=0.6, anchor='center')

    window.resizable(True, True)

    window.mainloop()"""


def swapTime():
    global pairs

    sender_list = names_list.copy()
    receiver_list = names_list.copy()

    while sender_list:
        actual_person = sender_list.pop(0)
        posible_destiny = [p for p in receiver_list if p != actual_person]

        if not posible_destiny:
            return
        
        destiny = random.choice(posible_destiny)
        receiver_list.remove(destiny)
        pairs[actual_person] = destiny


def sendMails():
    subject = "Your Secret Santa is..."

    for i in range(0,len(names_list)):
        receiver = names_list[i]
        receiver_email = email_list[i]

        gift_receiver = pairs[receiver]

        message = """Hi """ + receiver + """ in this Secret Santa you have to give a gift to... """ + gift_receiver + """!!!"""

        sendMail(receiver_email, subject, message)

    return True

def finish(root):
    root.destroy()

    window = tk.Tk()
    window.title('SWAP')
    window.geometry('650x400')
    bgcolor = _from_rgb((15, 114, 219))
    window.configure(bg=bgcolor)

    done = tk.Label(window, text='Your SWAP has been made', bg=bgcolor, justify='center', fg="white",
                   font=('Arial', 28)).place(relx=0.5, rely=0.1, anchor='center')
    
    thank_you = tk.Label(window, text='Thank You for using my program. Enjoy your gifts!!!', bg=bgcolor, justify='center', fg="white",
                   font=('Arial', 15)).place(relx=0.5, rely=0.2, anchor='center')
    
    image = Image.open("Swap/Heart.jpg")
    resize_image = image.resize((250,250))
    img = ImageTk.PhotoImage(resize_image)

    load_image = tk.Label(window, image = img)
    load_image.image = img
    load_image.place(relx=0.5, rely=0.6, anchor='center')

    window.resizable(True, True)

    window.mainloop()


MainMenu()

