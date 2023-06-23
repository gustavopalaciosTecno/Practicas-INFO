# Ejercicio 10
"""
10-Crea un programa que pida al usuario una cantidad en dólares y la convierta a
euros.
Supón que el tipo de cambio es de 0.84 euros por dólar.
"""
cantidad_dolares = float(input("Coloca un valor: "))

tipo_cambio = float(0.84)
resultado = cantidad_dolares * tipo_cambio
print("su valor en euros es", resultado)