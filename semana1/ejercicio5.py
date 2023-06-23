# Ejercicio 4
"""
5-Crea un programa que pida al usuario dos números enteros y muestre en
pantalla su cociente y su resto.
"""
numero1 = int(input("coloca primer número: "))
numero2 = int(input("coloca segundo número: "))

cociente = numero1 // numero2
resto = numero1 % numero2
print(f"su cociente es: {cociente} y su resto es: {resto}")