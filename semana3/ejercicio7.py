# Ejercicio 7
"""
7-Escribe un programa que pida al usuario una palabra y determine si es un
palíndromo (es decir, si se lee igual de izquierda a derecha que de derecha a
izquierda).
"""
escribirPalabra = input("Escribí una palabra: ")
alreves = escribirPalabra
if alreves == escribirPalabra[::-1]:
    print(f"la palabra {alreves} es un palíndromo")
else:
    print("No es un palíndromo")


