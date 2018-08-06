import datetime
import random

from time import sleep

period = 1
#seconds=0
frases_alegres = [1, 2]
#seconds=1
nombres_de_muebles = [2, 3]
#seconds=2
nombres_de_bebidas = [3, 4]
#seconds=3
frases_de_odio = [4, 5]
#seconds=4
nombres_de_comidas = [5, 6]
#seconds=5
frases_absurdas = [6, 7]
#seconds=6
nombres_de_animales = [7, 8]
#seconds=7
frases_motivacionales = [8, 9]
#seconds=8
sonidos_de_animales = [9, 10]
#seconds=9
frases_tristes = [10, 11]



def main():

    while True:
        ran = 0
        time = sleep(period)
        frases = [frases_alegres, nombres_de_muebles, nombres_de_bebidas, frases_de_odio, nombres_de_comidas,
                  frases_absurdas, nombres_de_animales, frases_motivacionales, sonidos_de_animales, frases_tristes]
        phrase = frases[ran][random.randint(0, len(frases[ran]))]
        ran += 1
        print(phrase)


if __name__ == '__main__':
    main()
