# Desafío 2: Analizador de textos
"""
Requisitos técnicos:
Se te pide crear un programa que le pida al usuario que ingresar un texto
cualquiera, por ejemplo, un artículo o una frase.
Luego el programa le va a pedir al usuario que también ingrese 3 letras a su
elección.
Nuestro código va a procesar esa información para realizar los análisis
necesarios para devolverle al usuario la siguiente información:
1- Cantidad de veces que aparece cada una de letras que eligió.
Tip 1: almacenar las letras en una lista para usar algún método de contar un substring en un
string
Tip 2: al buscar las letras puede haber mayúscula y minúsculas. Para asegurar que se
encuentren todas las letras, pasa tanto el texto original como las letras a buscar a
minúscula.
2- Cuantas palabras hay en total en todo el texto.
Tip 3: usa métodos para transformar el texto en lista de palabras y para calcular su longitud.
3- Cual es la primera letra y cuál es la última. (Indexación)
4- Mostrar el texto en orden inverso.
5- Decir si la palabra "python" aparece en el texto.
Tip 4: usa bool para verificar si se encuentra, y un diccionario para asociar el booleano con un
string para mostrar al usuario
"""

texto = input("Ingresa un texto cualquiera \"por ejemplo, un artículo o una frase\": ")
letras = input("ingresa tres letras: \"a tu elección: \"")
letras2 = input("ingresa tres letras: \"a tu elección: \"")
letras3= input("ingresa tres letras: \"a tu elección: \"")

almacenar_letras = []
letras.lower()
almacenar_letras.append(f"se almacenaron las siguiente letras: {letras}")
print(almacenar_letras)

for letra in letras:
       if letra.isalpha():
            print("La letra " + letra + " aparece " + str(letras.count(letra)) + " veces.")

print("el total de letras son: ",len(letras))
print("la lista es la siguiente", letras.split())
primera_letra = letras[0]
ultima_letra = letras[-1]
print(f"La primera letra es:, {primera_letra} y la última letra es {ultima_letra}")
lista_inversa = texto[::-1]
print("la lista inversa es: ",lista_inversa)

mi_diccionario = {"clave1":" ", "clave2":" "}
if "python" in texto.lower():
    print(True)
    mi_diccionario['clave1'] = "Si se encuentra la palabra python"
else:
    print(False)  
    mi_diccionario['clave2'] = "No se encuentra la palabra python"  
 

print(mi_diccionario)


