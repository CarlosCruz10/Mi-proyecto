lista = []
numero_usuario = input("Di el numero que quieres agergar a la lista(Escribe FIN al terminar): ")

while numero_usuario != "FIN":
    lista.append(numero_usuario)
    numero_usuario = input("Di el número que quieras agregar a la lista(Escribe FIN al terminar): ")

print(lista)
largo = 0

for numero in lista:
    largo += 1

print("El largo de la lista es de {}".format(largo))