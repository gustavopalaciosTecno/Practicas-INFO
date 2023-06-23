# Ejercicio 7
"""
Ecribir un programa que pida al usuario un carácter y muestre por pantalla si
es una letra mayúscula, una letra minúscula, un número o un carácter especial.
"""

caracter = input("Introduce una caracter: ")

if caracter.islower():
    print("es un valor en letra minuscula")
elif caracter.isupper():
    print("es un valor en letra mayúscula")
elif caracter.isdigit():
    print("es un valor numérico")    
else:
    print("es una cadena")    