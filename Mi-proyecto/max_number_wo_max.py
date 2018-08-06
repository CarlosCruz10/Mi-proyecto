lista = []
S_o_N = input("¿quieres seguir agregando cosas (S/N): ").upper()

while S_o_N == "S":
    user_statement = int(input("agrega un numero a la lista: "))
    lista.append(user_statement)
    S_o_N = input("¿quieres seguir agregando cosas (S/N): ").upper()

numero_mayor = lista[0]

for numero in lista:
    if numero > numero_mayor:
        numero_mayor = numero

print("El numero más grande de la lista es {}".format(numero_mayor))