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


today = datetime.datetime.now()

_days_ago = datetime.timedelta(days=5)

date_was = today - _days_ago

weekday = date_was.weekday()
wday = dia_de_la_semana(weekday)

print("Hace 5 días fue {}".format(date_was.strftime("%d del %m de %Y")))
print("Ese día fue {}".format(wday))