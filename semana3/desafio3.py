# Desafío 3: Adivina el número
"""
Requisitos técnicos:
Operadores lógicos.
Operadores de comparación.
Control de flujo - Condicionales.
Control de Flujo - Repetitivas.

Vamos a crear un juego completamente funcional.
Para ello el programa debe:
Pedir al usuario que ingrese su nombre.
# Informarle que el número a adivinar está entre 1 y 100, y que tiene 8 intentos
# para adivinarlo.
# Generar aleatoriamente un número entero entre 1 y 100.

# tip 1: importar de la biblioteca random la función randint (Tu profe te explicará en
# clase cómo hacerlo).
Informarle al usuario cuántos intentos le quedan y solicitarle que ingrese un
número.
El "número" ingresado por el usuario puede:
No ser un número, en éste caso avisar al usuario que no es un número entero
el que ingresó.

tip 2: con el método isdigit() puedes saber si es posible convertir a entero.
Ser menor al que tiene que adivinar, en éste caso informarle que el número a
adivinar es mayor.
Ser mayor al que tiene que adivinar, en éste caso informarle que el número a
adivinar es menor.
Igual al que tiene que adivinar, en éste caso informarle que ha ganado y
decirle en cuál intento lo adivinó.
Si el usuario no ingresa un número entero debes descontarle un intento, en
los demás casos no debes descontarle un intento.
En cada intento debes informarle al usuario los intentos que le quedan
disponibles y solicitarle que ingrese otro número.
Si el usuario no acierta en los 8 intentos, debes informarle que se agotaron los
intentos y cuál era el número que tenía que adivinar.
"""

import random
aleatorio = random.randint(1,100)
contador = 1
parametro = 7
print("####### el número a adivinar está entre 1 y 100 y tiene 8 intentos #####")
nombre = input("Ingresa tu nombre: ")
print(f"Hola {nombre} vamos a jugar a adivinar el número ")
while contador <= parametro:

    numero = int(input("digita un número: "))
    contador+= 1   
    if numero > aleatorio:
        #if numero.isdigit() > aleatorio:
        print("Colocá un número menor")
        print(f"ya sumas {contador} intentos")
    elif numero < aleatorio:
        print("Colocá un número mayor")  
        print(f"ya sumas {contador} intentos")
    elif numero == aleatorio:
        print(f"Felicitaciones, adivinaste es el número {numero}")
        print(f"la cantidad de intentos es {contador}")  
        break  
    else:
        print(f"Tenes que colocar valores numéricos, se te descuenta un intento {contador -1}")  
         
else:
    print(f"No lograste adivinar usuario: '{nombre}' el número en {contador} intentos")
    print(f"el número que tenias que adivinar era el {aleatorio}")
   
