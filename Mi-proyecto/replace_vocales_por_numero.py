string_usuario = input("Di algo:_")
vocales = "aeiou"
number = 1

for letter in string_usuario:
    if letter in vocales:
        string_usuario = string_usuario.replace(letter, str(number))
        number += 1

print(string_usuario)