multiplo = int(input("De que numero quieres la tabla de multiplicar: "))

for numero in range (5, 16):
    print("{} x {} = {}".format(multiplo, numero, multiplo * numero))

