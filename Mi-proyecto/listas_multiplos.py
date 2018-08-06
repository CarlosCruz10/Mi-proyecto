""""
Crear un programa que guarde e imprima varias listas
con todos los números que estén dentro de una lista proporcionada
por el usuario y sean múltiplos de 2, de 3, de 5 y de 7.
"""

lista_usuario = []
S_o_N = input("¿Quieres agregar un numero a la lista (S/N): ").upper()

while S_o_N == "S":
    numeros_usuario = int(input("Di un número:"))
    lista_usuario.append(numeros_usuario)
    S_o_N = input("¿Quieres agregar un numero a la lista (S/N): ").upper()

lista_dos = []
lista_tres = []
lista_cinco = []
lista_siete = []

for number in lista_usuario:
    if number % 2 == 0:
        lista_dos.append(number)
    elif number % 3 == 0:
        lista_tres.append(number)
    elif number % 5 == 0:
        lista_cinco.append(number)
    elif number % 7 == 0:
        lista_siete.append(number)

print(lista_dos)
print(lista_tres)
print(lista_cinco)
print(lista_siete)