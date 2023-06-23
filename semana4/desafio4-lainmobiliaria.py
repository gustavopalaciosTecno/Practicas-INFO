# Desafío 4: La inmobiliaria
# Requisitos técnicos:
# - Operadores.
# - Estructuras de datos.
# - Estructuras de control de flujo.
# - Funciones
# Una inmobiliaria de tu ciudad solicita un sistema para automatizar la gestión de sus inmuebles.
# Se te pide construir un programa que permita:
#  Agregar, editar y eliminar inmuebles a la lista.
# Las funciones deben ajustarse al formato de lista y reglas de validación.
#  Cambiar el estado de un inmueble, sin modificar sus demás datos.
# Las funciones deben ajustarse al formato de lista y reglas de validación.
#  Hacer búsqueda de inmuebles en función de un presupuesto dado.
# La función recibirá como entrada la lista de inmuebles y un precio, 
# y devolverá otra lista con los inmuebles cuyo precio sea menor o igual que el dado 
# y el estado sea Disponible o Reservado. 
# Los inmuebles de la lista que se devuelva deben incorporar un nuevo par a cada diccionario con el precio 
# del inmueble, donde el precio de un inmueble se calcula con las reglas de precio en función de la zona.

def gestionar_inmuebles(lista, precio):
    while True:
        print("1. Agregar diccionario")
        print("2. Editar diccionario")
        print("3. Eliminar diccionario")
        print("4. Ver productos agregados recientemente")
        print("5. Buscar productos por precio")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            productos = {}
            llave = input("Ingrese la llave: ")
            valor = input("Ingrese el valor: ")
            productos[llave] = {"valor": valor, "precio": precio}
            lista.append(productos)
            print("Producto agregado exitosamente.")
            print()
            
        elif opcion == "2":
            if len(lista) == 0:
                print("No hay productos para editar.")
                print()
                continue
            
            indice = int(input("Ingrese el índice del producto a editar: "))
            
            if indice < 0 or indice >= len(lista):
                print("Índice inválido.")
                print()
                continue
            
            productos = lista[indice]
            llave = input("Ingrese la clave a editar: ")
            
            if llave not in lista:
                print("La clave no existe en el diccionario.")
                print()
                continue
            
            nuevo_valor = input("Ingrese el nuevo valor: ")
            lista[llave]["valor"] = nuevo_valor
            lista[llave]["precio"] = precio
            print("lista editado exitosamente.")
            print()
            
        elif opcion == "3":
            if len(lista) == 0:
                print("No hay productos para eliminar.")
                print()
                continue
            
            indice = int(input("Ingrese el índice de producto a eliminar: "))
            
            if indice < 0 or indice >= len(lista):
                print("Índice inválido.")
                print()
                continue
            
            del lista[indice]
            print("Producto eliminado exitosamente.")
           
            
                
        elif opcion == "4":
            if len(lista) == 0:
                print("No hay diccionarios para buscar.")
                print()
                continue

            llave_buscar = input("Ingrese la llave a buscar: ")
            valor_buscar = input("Ingrese el valor a buscar: ")

            for productos in lista:
                if llave_buscar in productos and productos[llave_buscar] == valor_buscar:
                    print("Producto encontrado:", productos)
                    #break
            else:
                print("Producto no encontrado.")

            print()
        
        elif opcion == "5":
            indice = int(input("Ingrese el índice de producto a buscar:  "))
            print(lista[:])
            continue
        
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción inválida.")
          

# Ejemplo de uso
lista = [{"producto1": 
    {"nombre": "Casa quinta", 
     "precio": 19.000, 
     "estado":"disponible"}
    }, 
    {"producto2": 
    {"nombre": "Quinta", 
     "precio": 95.000,
     "estado":"reservado"
     }},
     {"producto3": 
    {"nombre": "Mojon escrachado", 
     "precio": 25.0000,
     "estado":"reservado"
     }},
    {"producto4": 
    {"nombre": "Casa quinta verde amarella", 
     "precio": 30.000,
     "estado":"disponible"
     }},
    ]
#precio = 99.99
precio = lista

gestionar_inmuebles(lista, precio)

        