"""
Escribe una función que reciba una lista de números y devuelva otra pero conteniendo solo los números pares.
"""


def dime_los_pares(lista):
    lista_pares = []
    for number in lista:
        if number % 2 == 0:
            lista_pares.append(number)
    return lista_pares


list = []
agregar_numbers = True
while agregar_numbers == True:
    number_ = float(input("Di un número que quieras agregar a la lista: "))
    list.append(number_)
    status = input("¿Quireres agregar más números[s/n]?")
    if status == "s":
        agregar_numbers = True
    else:
        agregar_numbers = False

pairs = dime_los_pares(list)
print("Los numeros pares son: {}".format(pairs))

