# Ejercicio 13
"""
13-Escribe un programa que solicite al usuario su nombre y su edad, y luego
imprima un mensaje que indique cuántos años tendrá el usuario en 10 años más.
"""

nombre = input("Coloca tu nombre: ")
edad = int(input("Coloca tu edad: "))
dentro_de_varios_years = 10
futuro = edad + dentro_de_varios_years
print(f"tu nombre es {nombre} y vas a tener dentro de 10 años unos: {futuro} años de edad")

