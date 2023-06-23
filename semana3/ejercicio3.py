# Ejercicio 3
"""
Escribe un programa que pida al usuario un número y luego imprima la tabla de
multiplicar correspondiente a ese número del 1 al 10.
"""
numeroTabla = int(input("Coloca un número para crear la tabla: "))
print(f"elegiste la tabla del {numeroTabla}")

for i in range(1,10):
    print(f"{numeroTabla} x {i} = {numeroTabla*i}")
