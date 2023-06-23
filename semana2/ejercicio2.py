# Ejercicio 2
"""
Escribir un programa que pida al usuario un número entero y muestre por
pantalla si es positivo, negativo o cero.
"""
numero = int(input("Introducí un número: "))

if numero > 0:
    print(f"el número {numero} es positivo")
elif numero < 0:
    print(f"el número {numero} es negativo")
else:
    print(f"el número {numero} es igual a cero")