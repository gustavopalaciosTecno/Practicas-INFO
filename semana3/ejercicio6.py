# Ejercicio 6
"""
Escribe un programa que pida al usuario una palabra y luego imprima la misma
palabra pero con las letras en orden inverso.

"""
palabra = input("Escribe una palabra: ")

palabra_inversa = palabra[::-1] # se encarga de invertir el orden en las letras de la palabra
print(palabra_inversa)
