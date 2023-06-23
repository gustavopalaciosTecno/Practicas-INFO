import numpy as np
"""
Desafío 2:
Escribe un programa que solicite al usuario su información personal, incluyendo
su nombre completo, edad, estatura, peso, dirección y número de teléfono.
A continuación, el programa deberá imprimir un mensaje con los datos
ingresados por el usuario en el siguiente formato:
La información ingresada es la siguiente:
Nombre completo: [nombre completo]
Edad: [edad]
Estatura: [estatura] cm
Peso: [peso] kg
Dirección: [dirección]
Número de teléfono: [número de teléfono]
"""

print("####### Información Personal #########")
nombre = input("Coloca tu nombre completo acá: ")
edad = int(input("Coloca tu edad: "))
estatura = float(input("Coloca tu estatura: ")) 
peso = float(input("Coloca tu peso: "))
direccion = input("Coloca tu dirección: ")
numeroTelefono = int(input("Coloca tu número de teléfono: "))

print("####### Información Personal #########")
print(f"tu nombre es: [{nombre}]")
print("\n")
print(f"tu edad es de : [{edad}] años")
print("\n")
print(f"tu estarura es de : [{estatura}] cm")
print("\n")
print(f"tu peso es de : {peso} Kg")
print("\n")
print(f"tu direccion es: [{direccion}]")
print("\n")
print(f"tu número de teléfono es: [{numeroTelefono}]")



