# Ejercicio 17
"""
Crear un set/conjunto con los números impares del 1 al 10 y mostrar el número
de elementos en el conjunto.
"""
conjunto_impares = set(range(1,11))
for i in conjunto_impares:
    if i %2 == 1:
        print(f"es impar: {i}")
        
print("\n")  
      
conjunto_impares = set(range(int(input("Coloca un número y vas a ver sus impares: "))))
for i in conjunto_impares:
    if i %2 == 1:
        print(f"es impar: {i}")    