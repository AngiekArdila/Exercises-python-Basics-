import datetime
year1=int(input("Ingres el año de tu nacimiento"))
month1=int(input("Ingresa el mes de tu nacimiento"))
day1=int(input("Ingresa el dia de tu nacimiento"))

dia_actual=datetime.datetime.now()
nacimiento=datetime.datetime(year1,month1,day1)

diferencia=(dia_actual.day-nacimiento.day),(dia_actual.month-nacimiento.month),(dia_actual.year-nacimiento.year)

print(str(dia_actual))
print("Esta es tu edad actual en dia,mes,hora", str(diferencia))


