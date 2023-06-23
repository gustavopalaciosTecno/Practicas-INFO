# Ejercicio 3
"""
Escribir un programa que pida al usuario dos números y muestre por pantalla
cuál de ellos es mayor.
"""
numero1 = int(input("Introducí un primer número: ")) 
numero2 = int(input("Introducí un segundo número: "))

if numero1 > numero2:
    print(f"el número {numero1} es mayor")
elif numero2 > numero1:
    print(f"el número {numero2} es mayor")   
else:
    print("ambos son iguales")
    