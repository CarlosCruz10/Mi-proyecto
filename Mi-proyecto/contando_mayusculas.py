mayusculas = "QWERTYUIOPASDFGHJKLÑZXCVBNM"
n_mayusculas = 0
frase_usuario = input("Escribe lo que quieras: ")

for letra in frase_usuario:
        if letra in mayusculas:
            n_mayusculas += 1

print("el numero de mayusculas es de {}".format(n_mayusculas))
