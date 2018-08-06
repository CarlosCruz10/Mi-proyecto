lista_numeros = [1, ]
user_number = None
si_o_no = input("¿Quieres agreagra un numero a la lista(S/N): ").upper()

while si_o_no == "S":
    user_number = int(input("Di un número que quieras agregar a la lista: "))
    lista_numeros.append(user_number)
    si_o_no = input("¿Quieres agreagra un numero a la lista(S/N): ").upper()

numberx = 0

for number in lista_numeros:
    