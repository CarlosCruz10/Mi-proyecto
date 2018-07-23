puntos = "."
comas = ","
espacios = " "
n_puntos = 0
n_comas = 0
n_espacios = 0
texto_usuario = input("introduce una frase: ")

for letra in texto_usuario:
    if letra in puntos:
        n_puntos += 1
    if letra in comas:
        n_comas += 1
    if letra in espacios:
        n_espacios += 1

print("Los espacios en tu frase son {}".format(n_espacios))
print("Los puntos en tu frase son {}".format(n_puntos))
print("Las comas en tu frase son {}".format(n_comas))