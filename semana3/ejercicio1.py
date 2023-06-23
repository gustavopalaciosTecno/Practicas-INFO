# Ejercicio 1
"""
1-Escribe un programa que pida al usuario una palabra y luego imprima cada
letra de la palabra en una línea separada.
"""
escribePalabra = input("Coloca una palabra acá: ")

for letra in escribePalabra:
    print(letra, end=" - ")
