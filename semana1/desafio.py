"""
Desafío 1:
Trabajas en una empresa X donde sus vendedores cobran comisiones del 6% de
sus ventas totales y el departamento comercial te solicita que ayudes a los
vendedores a calcular sus comisiones creando un programa que les pregunte su
nombre y cuánto han vendido en éste mes.
Tu programa le va a responder con una frase que incluya su nombre y el monto
que le corresponde por las comisiones

"""

nombreVendedor = input("Coloca tu nombre acá: ")
ventasMes = float(input("Coloca el monto vendido del mes: "))

comision = 0.06
resultado = (comision * ventasMes)
total = resultado + ventasMes
print(f"sos el vendedor {nombreVendedor} y tu comision con el 6% de tus ventas totales son: {total}")

"""
nombre = input("Ingresa tu nombre: ")
ventas = float(input("Ingresa el monto de ventas del mes: "))

comision = ventas * 0.06
total = comision + ventas
print(nombre + ", tu comisión del mes es de $", "{:.2f}".format(total))
"""