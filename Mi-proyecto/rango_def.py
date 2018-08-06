"""
Escribe una funcion que dado un numero y un rango (otros dos numeros), compruebe que ese numero está entre los dos (dentro del rango).
"""


def is_in_the_range(guess, min, max):

    rango = range(min, max)
    val = False
    if guess in rango:
        val = True
    else:
        val = False
    return val


min = int(input("Di el número minimo de tu rango: "))
max = int(input("Di el numero maximo de tu rango: "))
guess = int(input("Di el número que buscas en el rango"))


print(is_in_the_range(guess, min, max))