string_usuario = input("Di algo:_")

for a in string_usuario:
    string_usuario = string_usuario.replace("a", "{}")

for A in string_usuario:
    string_usuario = string_usuario.replace("A", "{}")

for clave in string_usuario:
    string_usuario = string_usuario.replace("{}", "VACA")

print(string_usuario)