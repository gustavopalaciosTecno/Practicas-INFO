# Ejercicio 9
"""
9-Escribe un programa que solicite al usuario dos números y luego imprima la
suma, la resta, la multiplicación y la división de los dos números.
"""

def Calcular():
    primer_numero = int(input("Coloca primer valor: "))
    segundo_numero = int(input("Coloca segundo valor: "))
    operacion = input("elegí la opración que queres realizar suma/resta/multiplicacion/division:  ")
    
    if operacion == "suma" or operacion == "SUMA":
        resultado = (primer_numero + segundo_numero)
        return (f"el resultado de la suma entre {primer_numero} y {segundo_numero} es: {resultado}")
    elif operacion == "resta" or operacion == "RESTA":
        resultado = (primer_numero - segundo_numero)
        return (f"el resultado de la resta entre {primer_numero} y {segundo_numero} es: {resultado}")
    elif operacion == "division" or operacion == "DIVISION":
        resultado = (primer_numero / segundo_numero)
        return (f"el resultado de la división entre {primer_numero} y {segundo_numero} es: {resultado}")
    elif operacion == "multiplicacion" or operacion == "MULTIPLICACION":
        resultado = (primer_numero * segundo_numero)
        return (f"el resultado de la mutiplicación entre {primer_numero} y {segundo_numero} es: {resultado}")
    else:
        print("Coloca el nombre de la operación correctamente")
    
    
print(Calcular())    
  