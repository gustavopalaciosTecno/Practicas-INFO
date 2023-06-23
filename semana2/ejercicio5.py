#Ejercicio 5
"""
Escribir un programa que pida al usuario un número entero y muestre por
pantalla si es par o impar.
"""

numero = int(input("Introducí un valor numérico: "))

if numero %2 == 0:
    print("ES PAR")
elif numero %2 == 1:
    print("ES IMPAR")    