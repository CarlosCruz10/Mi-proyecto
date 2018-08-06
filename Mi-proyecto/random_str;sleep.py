import random
from time import sleep
import datetime
strs = ["dar antes de recibir", "decae el patriarcado", "ganar es para perder", "ostentas el título",
        "oportunamente este código exite", "ñoño le dicen a los capaces", "kimono es lo que usa Mitsuha",
        "defensa es una posicion del futbol", "hola cara de bola", "zapato negro", "abrete sesamo",
        "Walter Gaitan fue Tigre", "solo, es mejor", "falsamente despedido", "estas bien", "¿que es eso?",
        "¿Cuanto es eso?", "sad", "Wow", "defiendete"]
period = 3



def main():
    current_time = datetime.datetime.now()
    while True:
        r_number = random.randint(0, len(strs)-1)
        r_text = strs[r_number]
        sleep(period)
        print(r_text)


if __name__ == '__main__':
    main()