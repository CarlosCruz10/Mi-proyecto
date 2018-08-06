import datetime

year = int(input("Di el año: "))
month = int(input("Di el mes: "))
day = int(input("Di el día: "))

user_date = datetime.datetime(year=year, month=month, day=day)

time_remaining = user_date - datetime.datetime.now()

print("Faltan {} dias y {} horas".format(time_remaining.days, int(time_remaining.seconds/3600)))

print("Ese día es {}".format(user_date.strftime("%d del %m de %Y")))
