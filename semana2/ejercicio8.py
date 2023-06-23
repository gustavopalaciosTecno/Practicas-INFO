# Ejercicio 8
"""
Escribir un programa que pida al usuario una cadena de caracteres y muestre
por pantalla si contiene la letra "a".
"""

def controlDePalabra():
    palabra = input("introduce unas palabras: ")

    if "a" in palabra.lower():
        print("tiene la palabra a")
    else:
        print("No tiene la palabra a")
        
controlDePalabra()       
    