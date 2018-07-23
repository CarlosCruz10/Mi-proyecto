numeros_usuario = []
numero_usuario = ""

while len(numeros_usuario) < 6:
    while not numero_usuario.isdigit():
        numero_usuario = input("Di un numero: ")
    numeros_usuario.append(numero_usuario)
    numero_usuario = ""
    print("¡Número añadido!")

print(numeros_usuario)

numero_pequeno = numeros_usuario[0]

for numero in numeros_usuario:
    if numero < numero_pequeno:
        numero_pequeno = numero

print("El número más pequeño es {}".format(numero_pequeno))