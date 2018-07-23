multiplo = int(input("De que numero quieres la tabla de multiplicar: "))

for numero in range (1, 11):
    if (multiplo * numero) % 2 == 0:
        print("{} x {} = {}".format(multiplo, numero, multiplo * numero))



