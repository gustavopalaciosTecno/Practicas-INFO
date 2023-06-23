import random
aleatorio = random.randint(1,100)
contador = 1
parametro = 7
print("####### el número a adivinar está entre 1 y 100 y tiene 8 intentos #####")
nombre = input("Ingresa tu nombre: ")
print(f"Hola {nombre} vamos a jugar a adivinar el número ")
while contador <= parametro:

    numero = input("digita un número: ")
    contador+= 1   
    if numero.isdigit() > aleatorio:
        print("Colocá un número menor")
        print(f"ya sumas {contador} intentos")
    elif numero.isdigit() < aleatorio:
        print("Colocá un número mayor")  
        print(f"ya sumas {contador} intentos")
    else:
        print(f"Felicitaciones, adivinaste es el número {numero}")
        print(f"la cantidad de intentos es {contador}")  
        break  

else:
    print(f"No lograste adivinar '{nombre}' el número en {contador} intentos")
    print(f"el número que tenias que adivinar era el {aleatorio}")
# try:
#     nota = int(input("el profe Lucas Rios te colocará una nota: ")) 
#     if nota >= 6 and nota < 10:
#             print(f"estas aprobado con {nota}")
#     elif nota <= 5:    
#             print(f"estas desaprobado con {nota}")
#     elif nota > 10:
#             print("fuera del rango de la nota")    
# except Exception as e:            
#     print("Coloca una nota numérica", e) 
# finally:
#     print("Fin del programa")    
           