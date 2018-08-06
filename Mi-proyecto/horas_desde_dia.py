import datetime

year = int(input("Di el año: "))
month = int(input("Di el mes: "))
day = int(input("Di el día: "))

user_date = datetime.datetime(year=year, month=month, day=day)
time_passed = datetime.datetime.now() - user_date

print("Han pasado {} horas desde entonces".format(int(time_passed.total_seconds()/3600)))
