#Nombres y años de nacimiento de la gente
salida = False
agenda = dict()


while not salida:
    action = input("¿Que quieres hacer? [Añadir año de nacimiento [A]]/ Consultar año de nacimiento [C] / Salir [S]]: ")

    #Accion añadir
    if action == "A":
        print("Vamos a añadir un año de nacimiento")
        print("-----------------------------------------------")
        nombre = input("Nombre: ")
        ano_de_nacimiento = input("Año: ")
        agenda[nombre] = ano_de_nacimiento

    #Accion consultar
    elif action == "C":
        print("Consultar año de nacimiento")
        print("-----------------------------------------------")
        nombre = input("De quien quieres saber el numero: ")
        print(agenda[nombre])

    #Accion salir
    elif action == "S":
        salida = True


