vocales = ("a", "e", "i", "o", "u")
vocales_usadas = []
frase_usuario = input("introduce un texto: ")

for letra in frase_usuario:
    if letra in vocales:
        if letra == "a":
            vocales_usadas += "a"
        elif letra == "e":
            vocales_usadas += "e"
        elif letra == "o":
            vocales_usadas += "o"
        elif letra == "u":
            vocales_usadas += "u"
        elif letra == "i":
            vocales_usadas += "i"


print("{}".format(vocales_usadas))