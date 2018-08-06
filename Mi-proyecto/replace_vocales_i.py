string_usuario = input("Di algo:_")
vocales = "aeou"

for letter in string_usuario:
    if letter in vocales:
        string_usuario = string_usuario.replace(letter, "i")

print(string_usuario)