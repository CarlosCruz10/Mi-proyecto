#muestra las talas en ordendescendiente
multiplo = int(input("De que numero quieres la tabla de multiplicar: "))

for numero in range (-10, 0):
    print("{} x {} = {}".format(multiplo, -1 * numero, multiplo * (-1 * numero)))