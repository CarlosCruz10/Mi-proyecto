
numero_elegido = int (input("elige un numero entre 1 y 10 para que el jugador 2 lo adivine(no dejes que lo vea): "))

numero_de_j2 = int (input("elige un numero entre el 1 y 10: "))

while numero_elegido != numero_de_j2:
    print("prueba de nuevo")
    numero_de_j2 = int(input("elige un numero entre el 1 y 10: "))

print("Felicidades, lo has adivinado")