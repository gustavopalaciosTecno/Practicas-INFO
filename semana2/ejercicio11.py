# Ejercicio 11
"""
Escribir un programa que pida al usuario dos números y muestre por pantalla
la suma de ellos solo si ambos son pares.
"""
numero1 = int(input("Introduce primer valor: "))
numero2 = int(input("Introduce segundo valor: "))

if numero1 % 2 == 0 and numero2 % 2 == 0:
    resultado = numero1 + numero2
    print(f" el {numero1} y el {numero2} son pares y la suma de ambos es {resultado}")
else:
    print("uno de ellos no es par o ambos no son pares")    



