#Longitud de funcion

def largo(lista):
    largo= 0
    for item in lista:
       largo += 1
    return largo


mi_lista = [2, 3, 4, 5]

print(largo(mi_lista))

"""
Reverse string
"""


def reverse_string(string_to_reverse):
    string_reversed = ""
    current_index = len(string_to_reverse) - 1
    while current_index >= 0:
        string_reversed += string_to_reverse[current_index]
        current_index -= 1
    return string_reversed


print(reverse_string("Hola"))

