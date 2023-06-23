import math
# Ejercicio 8
"""
8-Crea un programa que pida al usuario el radio de un círculo y muestre su
diámetro, su circunferencia y su área.
Supón que pi es aproximadamente 3.14159.
"""
radio= int(input("Coloca un valor para calcular el área del círculo: "))

area = round(math.pi * radio **2,2)
diametro = 2 * radio
circunferencia = 2 * math.pi * radio
print(f"el valor del área es: {area}, del diámetro: {diametro} y de la circunferencia: {circunferencia}")