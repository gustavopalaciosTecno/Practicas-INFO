# Ejercicio 9
"""
9-Escribir un programa que pida al usuario tres números y muestre por pantalla
el mayor de ellos.
"""
primer_valor = int(input("introduce primer valor: "))
segundo_valor = int(input("introduce segundo valor: "))
tercer_valor = int(input("introduce tercer valor: "))

if primer_valor > segundo_valor and primer_valor > tercer_valor:
    print(f"el primer valor {primer_valor} es mayor")
elif segundo_valor > primer_valor and segundo_valor > tercer_valor:
    print(f"el segundo valor {segundo_valor} es mayor") 
elif tercer_valor > primer_valor and tercer_valor > segundo_valor:
    print(f"el tercer valor {tercer_valor} es mayor") 
else:
    print("Los tres valores son iguales")