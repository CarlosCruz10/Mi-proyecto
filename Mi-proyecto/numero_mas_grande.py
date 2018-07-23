numeros_usuario = []
numero_del_usuario = ""

while len(numeros_usuario) < 10:
    while not numero_del_usuario.isdigit():
        numero_del_usuario = input("Dime un número: ")
    numeros_usuario.append(numero_del_usuario)
    numero_del_usuario = ""
    print("¡Número añadido!")

print(numeros_usuario)

numero_grande = numeros_usuario[0]

for numero in numeros_usuario:
    if numero > numero_grande:
        numero_grande = numero

print("El número más grande es {}".format(numero_grande))
