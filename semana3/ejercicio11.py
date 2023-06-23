# Ejercicio 11

# Escribe un programa que pida al usuario un número y calcule su factorial.
# Un factorial es el producto que resulta de multiplicar un número entero positivo
# dado por todos los enteros inferiores a él hasta el uno. Por ejemplo, el factorial
# de 4 es 4! = 4 × 3 × 2 × 1 = 24.

numero = int(input("Introducí un número: "))

if numero == 0:
    print(1)
else:
    factorial = 1
    for i in range(factorial, numero + 1):
        factorial = factorial * i
        print(factorial)
    
    