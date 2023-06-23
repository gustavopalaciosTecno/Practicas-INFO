# Ejercicio 19
"""
Escribe un programa que pida al usuario un número y luego imprima si ese
número es un número perfecto o no. Un número perfecto es aquel que es igual a
la suma de sus divisores propios (excluyendo el propio número).
Los números perfectos son aquellos iguales a la suma de sus divisores: 6 se
puede dividir por 1, 2 y 3, y cuando sumas esos números, el resultado es 6
"""

num = int(input("Ingresa un número: "))
divisores = []

for i in range(1, num):
    if num % i == 0:
        divisores.append(i)

if sum(divisores) == num:
    print(num, "es un número perfecto")
else:
    print(num, "no es un número perfecto")

# print("Hola1", "que", sep="-", end="") # por default sep=" " end="\n"
# print("Hola2") # \n salto de linea
# print("Hola3")

# Como hago mas proligo mi codigo? Modularizacion
# Que tengo que usar cuando se repiten cosas? Modularizacion
# Que formas de modularizar existen? funciones y procedimientos
# Que hace una funcion? Realiza N acciones -> devuelve un valor. f(x). f(3)->5
# Que hace un procedimiento? Realiza N acciones

# def nombre_funcion(param1, param2, param3):
#     pass

# def funcion(x, y, z):
#     pass

# def derivada(x, y):
#     pass

# Escribe un programa que pida al usuario un número y luego imprima si ese
# número es un número perfecto o no. Un número perfecto es aquel que es igual a
# la suma de sus divisores propios (excluyendo el propio número).
# Los números perfectos son aquellos iguales a la suma de sus divisores: 6 se
# puede dividir por 1, 2 y 3, y cuando sumas esos números, el resultado es 6

def perfecto(numero): # 6. 1, 2, 3
    divisores = []
    for num in range(1,numero):
        if(numero % num == 0):
            divisores.append(num)    
    
    if(numero==suma(divisores)):
        print("Es perfecto.")
    else:
        print("No es perfecto.")

def suma(numeros_lista):
    suma_lista = 0
    for num in numeros_lista:
        suma_lista += num 
    
    return suma_lista

perfecto(int(input("Ingrese su numero: ")))    
    

  