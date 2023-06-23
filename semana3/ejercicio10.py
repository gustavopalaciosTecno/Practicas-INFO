# Escribe un programa que pida al usuario una cadena de texto y luego imprima
# la misma cadena pero con todas las vocales en mayúscula.

texto = input("Escribi una frase o cualquier palabra: ")

for letra in texto:
    #print(letra, end="\n")
    if letra.isalpha():
        if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra=="u":
            print(letra.upper())
 
 
cadena = input("Ingrese una cadena de texto: ")
vocales = ['a', 'e', 'i', 'o', 'u']
resultado = ""

for letra in cadena:
    if letra.lower() in vocales:
        resultado += letra.upper()
    else:
        resultado += letra

print("La cadena original es:", cadena)
print("La cadena con vocales en mayúscula es:", resultado)
           