#Guía telefónica
salida = False
agenda = dict()


while not salida:
    accion = input("¿Que quieres hacer? [Añadir numero [A]]/ Consultar numero[C]] / Salir [S]: ")

    #Accion añadir
    if accion == "A":
        print("Vamos a añadir un número de telefono")
        print("-----------------------------------------------")
        nombre = input("Nombre: ")
        numero = input("Número: ")
        agenda[nombre] = numero

    #Accion consultar
    elif accion == "C":
        print("Consultar numero")
        print("-----------------------------------------------")
        nombre = input("De quien quieres saber el numero: ")
        print(agenda[nombre])

    #Accion salir
    elif accion == "S":
        salida = True


