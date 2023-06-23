import math
# Ejercicio 6.
"""
6-Crea un programa que pida al usuario el radio de un círculo y calcule su área.
La fórmula A = pi * r^2. Luego, muestra en pantalla el resultado.
Supongamos que pi = 3.1416
"""

radio = int(input("Coloca un valor para calcular el área: "))

area = round(math.pi * radio ** 2, 2)
print(f"el valor del área es: {area}")

