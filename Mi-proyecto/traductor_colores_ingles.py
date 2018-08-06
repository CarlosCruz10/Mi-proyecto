#Traductor colores a ingles
colors = {"rojo": "red",
          "azul": "blue",
          "amarillo": "yellow",
          "gris": "grey",
          "blanco": "white",
          "negro": "black",
          "verde": "green",
          "naranja": "orange"}

salida = False

while not salida:
    status = input("¿Qué quieres hacer? [Traducir[T]/Salir[S]]")
    if status == "T":
        print("Vamos a traducir un color")
        color = input("¿Qué color quieres traducir?: ")
        print(colors[color])

    elif status == "S":
        salida = True



