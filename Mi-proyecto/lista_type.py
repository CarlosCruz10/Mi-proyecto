numbers = "0123456789"
letters = "qwertyuiopasdfghjklzxcvbnm"
list_usuario = []
list_str = []
list_int = []
T_N = input("¿Quieres agregar algo a la lista(escribe t=si o f=no)?: ").upper()

#inputs del usuario

while T_N == "T":
    user_element = input("Di lo que quieras agregar a la lista (pueden ser numeros o letras): ")
    list_usuario.append(user_element)
    T_N = input("¿Quieres agregar algo a la lista(escribe t=si o f=no)?: ").upper()

for element in list_usuario:
    if element in numbers:
        list_int.append(element)
    else:
        list_str.append(element)

print(list_int)
print(list_str)