# Ejercicio 2
"""
Escribe un programa que pida al usuario un número y calcule la suma de todos
los números naturales del 1 hasta ese número.
"""
numeros = int(input("Coloca un número: "))
suma = 0
for i in range(1, numeros + 1):
          
      suma = suma + i
      print("La suma de los números naturales del 1 hasta", numeros, "es:", suma)
    