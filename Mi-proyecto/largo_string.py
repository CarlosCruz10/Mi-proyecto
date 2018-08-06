lista_strings = []
lista_len_str = []
input_usuario = input("Di el nombre de lo que quieres agregar a la lista (escribe FIN para terminar): ")

while input_usuario != "FIN":
    lista_strings.append(input_usuario)
    input_usuario = input("Di el nombre de lo que quieres agregar a la lista(Escribe FIN para terminar): ")

for input in lista_strings:
    lista_len_str.append(len(input))

print(lista_len_str)