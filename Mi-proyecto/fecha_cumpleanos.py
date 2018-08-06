import datetime


def dia_de_la_semana(weekday):
    if weekday == 0:
        weekday = "Lunes"
    elif weekday == 1:
        weekday = "Martes"
    elif weekday == 2:
        weekday = "Miercoles"
    elif weekday == 3:
        weekday = "Jueves"
    elif weekday == 4:
        weekday = "Viernes"
    elif weekday == 5:
        weekday = "Sabado"
    elif weekday == 6:
        weekday = "Domingo"
    return weekday


year = int(input("Di el año de tu siguiente cumpleaños: "))
month = int(input("Di el mes en que naciste: "))
day = int(input("Di el día que naciste: "))

user_birthday = datetime.datetime(year=year, month=month, day=day)

time_remaining = user_birthday - datetime.datetime.now()
wday = user_birthday.weekday()
weekday = dia_de_la_semana(wday)

print("Faltan {} dias y {} horas".format(time_remaining.days, int(time_remaining.seconds/3600)))

print("Ese día es {}".format(weekday))
