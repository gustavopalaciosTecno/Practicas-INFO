# Desafio entregable
# CTRL + K + C para comentar, CTRL + K + U para descomentar
# CTRL + llave de cierre para comentar
# Se te pide crear un programa que le pida al usuario que ingrese un texto
# cualquiera, por ejemplo, un artículo o una frase.

texto = input("Ingrese un articulo o frase: ")

# Luego el programa le va a pedir al usuario que también ingrese 3 letras a su
# elección.

# letra1, letra2, letra3 = input("Ingrese la letra 1 a eleccion"), input("Ingrese la letra 2 a eleccion"), input("Ingrese la letra 3 a eleccion")

# letras = []
# letras.append(input("Ingrese la letra 1 a eleccion"))
# letras.append(input("Ingrese la letra 2 a eleccion"))
# letras.append(input("Ingrese la letra 3 a eleccion"))

letra1 = input("Ingrese la letra 1 a eleccion: ")
letra2 = input("Ingrese la letra 2 a eleccion: ")
letra3 = input("Ingrese la letra 3 a eleccion: ")



# 1- Cantidad de veces que aparece cada una de letras que eligió.
# Tip 1: almacenar las letras en una lista para usar algún método de contar un substring en un
# string
# Tip 2: al buscar las letras puede haber mayúscula y minúsculas. Para asegurar que se
# encuentren todas las letras, pasa tanto el texto original como las letras a buscar a
# minúscula.
texto = texto.lower() # paso a minusculas el texto, upper() paso a mayusculas el texto
letras = [letra1.lower(), letra2.lower(), letra3.lower()] # guardo en lista las letras y las pongo en minuscula

for letra in letras:
    print(f'La letra {letra} aparecio {texto.count(letra)} veces')

# 2- Cuantas palabras hay en total en todo el texto.
# Tip 3: usa métodos para transformar el texto en lista de palabras y para calcular su longitud.

palabras = texto.replace('.', '')
palabras = palabras.replace(':', '')
palabras = palabras.replace(';', '')
palabras_sep = palabras.split(' ')
print("Palabras sin caracteres de puntuacion", palabras)

cant_palabras = len(palabras_sep)
print("Cantidad de palabras en el texto", cant_palabras)

# 3- Cual es la primera letra y cuál es la última. (Indexación)
print("Primera letra:", palabras[0], "Ultima letra:", palabras[-1])


# 4 - Mostrar el texto en orden inverso.
texto_reversa = palabras[::-1] # 'hola como estas'
print("Texto en forma inversa:", texto_reversa)

palabras_reversa = palabras_sep[::-1] # ['hola', 'como', 'estas']
print("Palabras en forma inversa:", palabras_reversa)

texto_palabras_reversa = " ".join(palabras_reversa)
print("Palabras en forma inversa como string:", texto_palabras_reversa)

# 5- Decir si la palabra "python" aparece en el texto.
# Tip 4: usa bool para verificar si se encuentra, y un diccionario para asociar el booleano con un
# string para mostrar al usuario

# if("python" in texto):
#     print("Existe python en el texto")
# else:
#     print("No existe python en el texto")

opciones = {True: "existe" , False: "no existe"} # True, False son llaves, clave, key... Existe, No existe son valores, values 
existe_python = "python" in texto # True o False
print("La palabra python", opciones[existe_python])
