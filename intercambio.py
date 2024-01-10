from sendEmail import sendMail

running = True

def imprimirListas():
    for i in range(0,len(lista_de_participantes)):
            print(str(i+1) + ".- Nombre: " + lista_de_participantes[i] + " , Correo: " + lista_de_correos[i])

while running:
    print("Bienvenido a un programa para hacer un intercambio automatico")
    print("Ingresa los nombres de los participantes, cuando no haya mas ingresa X")

    lista_de_participantes = []
    lista_de_correos = []

    #Ingresar nombrs de participantes
    participantes = input("Participante: ")
    while participantes != "X":
        lista_de_participantes.append(participantes)
        participantes = input("Participante: ")


    #Ingresar correos de participantes
    if len(lista_de_participantes) > 2:
        print("Ahora ingresa los correos de los participantes en el mismo orden\nque ingresaste los nombres")
        correo = input("Correo de " + lista_de_participantes[0] + ": ")
        for i in range(1,len(lista_de_participantes)):
            lista_de_correos.append(correo)
            correo = input("Correo de " + lista_de_participantes[i] + ": ")

        lista_de_correos.append(correo)
    else:
        print("No es posible hacer un intercambio con menos de 2 personas")
        break

    print("Comprueba de que los nombres y correos esten bien, si hay alguno mal\nescribe su indice, si todo esta bien escribe 0")

    imprimirListas()

    #Verificacion y posibles cambios
    verificacion = int(input("todo bien? "))
    while verificacion != 0:
        print("Modificar " + lista_de_participantes[verificacion - 1])
        lista_de_participantes[verificacion - 1] = input("Nombre: ")
        lista_de_correos[verificacion - 1] = input("Correo: ")
        print(str(verificacion) + ".- Nombre: " + lista_de_participantes[verificacion - 1] + " , Correo: " + lista_de_correos[verificacion - 1])
        verificacion = int(input("todo bien? "))

        imprimirListas()

    #Eliminacion de algun participante
    print("Quieres eliminar a alguien antes de continuar?, SI o NO")
    eliminar = input("SI o NO")
    while eliminar == "SI":
        if len(lista_de_participantes) - 1 > 2:
            imprimirListas()
            who = int(input("Ingresa su numero: "))
            if who <= len(lista_de_participantes):
                del lista_de_participantes[who - 1]
                del lista_de_correos[who - 1]

            imprimirListas()

            print("Quieres eliminar a alguien antes de continuar?, SI o NO: ")
            eliminar = input("SI o NO")
        else:
            print("Si eliminas a alguien más no es posible realizar el intercambio")
            continuar = input("Quieres continuar? SI o NO: ")
            if continuar == "SI":
                break
            if continuar == "NO":
                print("ok")

    
    running = False

