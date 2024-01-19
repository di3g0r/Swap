from sendEmail import sendMail
import random

running = True

def imprimirListas():
    for i in range(0,len(lista_de_participantes)):
            print(str(i+1) + ".- Name: " + lista_de_participantes[i] + " , Email: " + lista_de_correos[i])

def space():
    for i in range(0,30):
        print()

while running:
    random.seed()

    print("Welcome to a program to make a Secret Santa game.")
    print("Enter the names of the participants, when there are no more enter X")

    lista_de_participantes = []
    lista_de_correos = []

    #Ingresar nombrs de participantes
    participantes = input("Participant: ")
    while participantes != "X":
        lista_de_participantes.append(participantes)
        participantes = input("Participant: ")

    space()

    #Ingresar correos de participantes
    if len(lista_de_participantes) > 2:
        print("Now enter the participants' emails in the same order\nthat you entered the names")
        correo = input("Email of " + lista_de_participantes[0] + ": ")
        for i in range(1,len(lista_de_participantes)):
            lista_de_correos.append(correo)
            correo = input("Email of " + lista_de_participantes[i] + ": ")

        lista_de_correos.append(correo)
    else:
        print("It is not possible to make a Secret Santa game with less than 2 people")
        break

    space()

    print("Check that the names and emails are correct, if there are any wrong, write their index, if everything is correct, write 0")

    imprimirListas()

    #Verificacion y posibles cambios
    verificacion = int(input("All good?\n"))
    while verificacion != 0:
        print("Modify " + lista_de_participantes[verificacion - 1])
        lista_de_participantes[verificacion - 1] = input("Name: ")
        lista_de_correos[verificacion - 1] = input("Email: ")
        print(str(verificacion) + ".- Name: " + lista_de_participantes[verificacion - 1] + " ,Email: " + lista_de_correos[verificacion - 1])
        verificacion = int(input("All good?\n"))

        imprimirListas()

    space()

    #Eliminacion de algun participante
    print("Do you want to eliminate someone before continuing? YES or NO: ")
    eliminar = input("YES or NO: ")
    while eliminar == "YES":
        if len(lista_de_participantes) - 1 > 2:
            imprimirListas()
            who = int(input("Enter its number: "))
            if who <= len(lista_de_participantes):
                del lista_de_participantes[who - 1]
                del lista_de_correos[who - 1]

            imprimirListas()

            print("Do you want to eliminate someone before continuing? YES or NO: ")
            eliminar = input("YES or NO: ")
        else:
            print("If you eliminate someone else it is not possible to make the Secret Santa")
            continuar = input("Do you want to continue? YES or NO: ")
            if continuar == "YES":
                break
            if continuar == "NO":
                print("OK")

    space()

    #Realizar Intercambio
    parejas = {}
    def Intercambio():
        lista_desechable = lista_de_participantes.copy()

        while lista_desechable:
            persona_actual = lista_desechable.pop(0)
            posible_destino = [p for p in lista_desechable if p != persona_actual]

            if not posible_destino:
                # Handle the special case when no options are available except gifting yourself
                print("You can't make an exchange without giving yourself away.")
                return

            destino = random.choice(posible_destino)
            lista_desechable.remove(destino)
            parejas[persona_actual] = destino

        

    Intercambio()

    print(parejas)

    #Send Mail
    subject = "Your Secret Santa is..."
    for i in range(0,len(lista_de_participantes)):
        receiver = lista_de_participantes[i]
        receiver_email = lista_de_correos[i]

        gift_receiver = parejas[receiver]

        message = """Hi """ + receiver + """ in this Secret Santa you have to give a gift to... """ + gift_receiver + """!!!"""

       

        sendMail(receiver_email, subject, message)

    print("Done")

    
    running = False

