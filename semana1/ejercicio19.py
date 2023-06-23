# Ejercicio 19
"""
Escribe un programa que solicite al usuario un número decimal y luego
imprima la parte entera y decimal por separado.
"""

numero = float(input("Ingresa un número: "))

parte_entera = int(numero)
parte_decimal = round(numero - parte_entera,2)
print(f"la parte entera es: {parte_entera}")
print(f"la parte decimal es: {parte_decimal}")