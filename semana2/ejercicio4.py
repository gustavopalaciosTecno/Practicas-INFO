# Ejercicio 4
"""
Escribir un programa que pida al usuario una nota del 0 al 10 y muestre por
pantalla si está aprobado (5 o más) o no.
"""

nota1 = int(input("introducí una nota: "))
if nota1 >=6 and nota1 <=10:
    print("APROBADO")
elif nota1 >10:
    print("NOTA FUERA DE RANGO")
else:
    print("DESAPROBADO")
    