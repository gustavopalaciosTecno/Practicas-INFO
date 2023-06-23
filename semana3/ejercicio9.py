# Ejercicio 9
# Escribe un programa que pida al usuario un número y luego imprima la
# secuencia de Fibonacci correspondiente a ese número.

valor = int(input("Introducí un número entero positivo: "))

antes, despues = 0,1

for i in range(valor):
    #antes, despues = despues, antes + despues
    fib = antes + despues
    despues = antes
    antes = fib
    print(fib, end="\n")


