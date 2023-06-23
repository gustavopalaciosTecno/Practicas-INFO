# Ejercicio 1
"""
Escribir un programa que pida al usuario su edad y muestre por pantalla si es
mayor de edad (18 años o más) o no.
"""
edad = int(input("Introducí una edad: "))
"""
if edad >= 18:
    print(f"sos mayor de edad, tenes {edad} años de edad")
else:
    print("sos menor de edad")      
"""                 
if edad >= 18 and edad <= 100:
    print(f"sos mayor de edad, tenes {edad} años de edad")
elif edad < 18:
    print("sos menor de edad") 
elif edad >100:
    print("año no contemplado")     
    