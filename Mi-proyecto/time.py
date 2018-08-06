from time import sleep
import datetime

NIGHT_STARTS = 19
DAY_STARTS = 7
HOUR_DURATION = 1


def write_file_and_screen(text, file_name):
    with open(file_name, "a") as hours_file:
        hours_file.write("{}{}".format(text, "\n"))
        print(text)


def main():
    current_time = datetime.datetime.now()
    is_night = False
    alarm = input("¿Quieres programar una alarma[S/N]: ").upper()
    if alarm == "S":
        hora = int(input("¿A qué hora quieres que suene?: "))
        day = input("¿Qué días quieres que suene?: ").upper()
        print("¡Genial!, la alarma sonará a las {} el día {}".format(hora, day))
        if day == "LUNES":
            day = 0
        elif day == "MARTES":
            day = 1
        elif day == "MIERCOLES":
            day = 2
        elif day == "JUEVES":
            day = 3
        elif day == "VIERNES":
            day = 4
        elif day == "SABADO":
            day = 5
        elif day == "DOMINGO":
            day = 6
    else:
        pass
    while True:
        sleep(HOUR_DURATION)
        current_time += datetime.timedelta(hours=1)
        light_changed = False

        if (current_time.hour >= NIGHT_STARTS or current_time.hour <= DAY_STARTS) and not is_night:
            is_night = True
            light_changed = True
        elif (current_time.hour > DAY_STARTS and current_time.hour < NIGHT_STARTS) and is_night:
            is_night = False
            light_changed = True

        if light_changed:
            if is_night:
                write_file_and_screen("Se ha hecho de noche", "horas.txt")
            else:
                write_file_and_screen("Se ha hecho de día", "horas.txt")

        if alarm == "S" and current_time.hour == hora and current_time.weekday() == day:
            print("Suena la alarma")
        weekday = current_time.weekday()
        write_file_and_screen("La hora actual es {}".format(current_time), "horas.txt")


if __name__ == "__main__":
    main()
