import datetime
import random

AVERAGE_LIFESPAN = 80
SMOKER_PENALIZATION = 7
DRINKER_PENALIZATION = 7
SEDENTARY_PENALIZATION = 5
CANCER_RISK = random.randint(1, 15)
DIABETES = random.randint(1, 15)
SLEEP_TIME = random.randint(1, 5)


def print_with_underscores(message):
    print(message)
    print(len(message) * "-")


def sometimes(message):
    response = None
    while response != "S" and response != "N" and response != "A":
        response = input(message + "[S/N/A]")
    return response


def day_of_the_week(weekday):
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


def yes_or_not(message):
    response = None
    while response != "S" and response != "N":
        response = input(message + "[S/N]")
        return response == "S"


print_with_underscores("¡Averigua cuanto te queda de vida!")
print("Completa esta encuesta para saber cuanto tiempo de vida te queda")

birth_date = input("¿Cuál es tu fecha de nacimiento (formato: dd/mm/yyyy)?: ")

birth_date = datetime.datetime.strptime(birth_date, "%d/%m/%Y")
years_lost = 0


if sometimes("¿Fumas?"):
    years_lost += SMOKER_PENALIZATION

if sometimes("¿Bebes?"):
    years_lost += DRINKER_PENALIZATION

Jogger = sometimes("¿Haces deporte?")
if Jogger == "N":
    years_lost += SEDENTARY_PENALIZATION
elif Jogger == "S":
    pass
elif Jogger == "T":
    years_lost += SEDENTARY_PENALIZATION/2
if yes_or_not("¿Alguien en tu familia ha tenido cancer?"):
    years_lost += CANCER_RISK
if yes_or_not("¿Alguien ha tenido diabetes en tu familia?"):
    years_lost += DIABETES
sleep = sometimes("¿Duermes 8 horas diario?")
if sleep == "S":
    pass
elif sleep == "N":
    years_lost -= SLEEP_TIME
elif sleep == "A":
    years_lost -= SLEEP_TIME/2


base_lifespan = random.randint(AVERAGE_LIFESPAN/2, AVERAGE_LIFESPAN)

lifespan = AVERAGE_LIFESPAN - years_lost
death_date = birth_date + datetime.timedelta(days=lifespan*365)
days_to_death = death_date - datetime.datetime.now()
wday = death_date.weekday()
weekday = day_of_the_week(wday)

print("Fecha de muerte: {}, te quedan días para morir: {}".format(death_date.strftime("%d/%m/%Y"), days_to_death.days))
print("Ese día será {}".format(weekday))