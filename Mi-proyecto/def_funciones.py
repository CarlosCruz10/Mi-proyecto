"""
Escribe una función que encuentre el numero más grande entre 3 numeros.
"""


def mayor_enre_tres(primero, segundo, tercero):
    user_values = [primero,segundo, tercero]
    mayor = ""
    if primero > segundo and primero > tercero:
        mayor = primero
    elif segundo > primero and segundo > tercero:
            mayor = segundo
    elif tercero > primero and tercero > segundo:
            mayor = tercero
    return mayor


primero = int(input("Di un número: "))
segundo = int(input("Di otro número: "))
tercero = int(input("Di un número más: "))
mayor = mayor_enre_tres(primero, segundo, tercero)

print("El número más grande fue {}".format(mayor))
