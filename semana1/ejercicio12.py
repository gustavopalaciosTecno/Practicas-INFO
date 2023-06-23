import datetime
# Ejercicio 12
"""
12-Escribe un programa que solicite al usuario su fecha de nacimiento en formato
dd/mm/aaaa y luego imprima su edad en años.
Utiliza la función .split()
"""

fecha_nac = input("coloca la fecha de nacimiento en formato dd/mm/aa (dia/mes/año) :  ")

dia, mes, anio = map(int, fecha_nac.split('/'))
fecha_nac = datetime.date(anio, mes, dia)
fecha_actual = datetime.date.today()
edad = fecha_actual.year - fecha_nac.year
print(f"tu edad es de: {edad} años")











