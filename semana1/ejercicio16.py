# Ejercicio 16
"""
16-Escribe un programa que solicite al usuario su peso y su altura, y luego calcule
e imprima su índice de masa corporal (IMC).
La fórmula para calcular el IMC es: IMC = peso / (altura ** 2).
"""
peso = int(input("Coloca tu peso: "))
altura = float(input("Coloca tu altura: "))

print(f"tu peso es de {peso}kg")
print(f"tu altura es de {altura}m")
imc = round(peso / (altura ** 2),2)
print(f"tu índice de masa corporal es: {imc}")


