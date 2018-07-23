lista = []
numero_usuario = int(input("Di el numero que quieres agregar a la lista: "))
lista.append(numero_usuario)
suma = 0

status_usuario = input("Quieres seguir introduciendo numeros(s/n): ").upper()
while status_usuario == "S":
    numero_usuario = int(input("Di el número que quieras agregar a la lista: "))
    lista.append(numero_usuario)
    status_usuario = input("Quieres seguir introduciendo numeros(s/n): ").upper()

print(lista)

for numero in lista:
    suma += numero

len(lista)

media = suma / len(lista)
print (media)