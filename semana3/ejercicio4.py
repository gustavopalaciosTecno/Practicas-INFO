# Ejercicio 4
"""
Escribe un programa que imprima los números pares del 1 al 100.
"""
numerosPares = int(input("Coloca un número: "))
for i in range(1,100):
    if i % 2 == 0:
        print(i)
