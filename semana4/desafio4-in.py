# # Desafío 4: La inmobiliaria
# # Requisitos técnicos:
# # - Operadores.
# # - Estructuras de datos.
# # - Estructuras de control de flujo.
# # - Funciones
# # Una inmobiliaria de tu ciudad solicita un sistema para automatizar la gestión de sus inmuebles.
# # Se te pide construir un programa que permita:
# #  Agregar, editar y eliminar inmuebles a la lista.
# # Las funciones deben ajustarse al formato de lista y reglas de validación.
# #  Cambiar el estado de un inmueble, sin modificar sus demás datos.
# # Las funciones deben ajustarse al formato de lista y reglas de validación.
# #  Hacer búsqueda de inmuebles en función de un presupuesto dado.
# # La función recibirá como entrada la lista de inmuebles y un precio, 
# # y devolverá otra lista con los inmuebles cuyo precio sea menor o igual que el dado 
# # y el estado sea Disponible o Reservado. 
# # Los inmuebles de la lista que se devuelva deben incorporar un nuevo par a cada diccionario con el precio 
# # del inmueble, donde el precio de un inmueble se calcula con las reglas de precio en función de la zona.

# print("PROGRAMA INMUEBLES")
def inmobiliaria():
    inmuebles = []
    while True:
        print("""
        ELEGÍ UNA DE LAS OPCIONES:
        1. Agregar un nuevo inmueble, colocando nombre y precio
        2. Mostrar el inmueble, colocando nuevo nombre y un nuevo precio
        3. Eliminar un inmueble
        4. Editar un inmueble
        5. Salir de la aplicación si ya no realiza mas operaciones
        """)
        operaciones = input("Elegí una de las opeciones: ")
        
        if operaciones == '1':
            datos = input("coloca nombre: ")
            precio = int(input("Coloca un precio: "))
            estado = input("coloca un estado: puede ser DISPONIBLE O RESERVADO: ")
            #inmuebles.append({"nombre": datos, "precio": precio})
            inmuebles.append(datos)
            inmuebles.append(precio)
            inmuebles.append(estado)
            
        elif operaciones == "2":
            
            print("inmueble cargado por el momento: ",inmuebles[:])
            buscar = input("elegi un nombre del inmueble para buscar: ")
            for buscar in inmuebles:
                print("el valor inmueble encontrado es: ",buscar)
        
            else:
                print("inmueble no encontrado")             
                
        elif operaciones == "3":
            nombre_a_eliminar = input("Ingrese el nombre que desea eliminar de la lista: ")
            if nombre_a_eliminar in inmuebles:
                inmuebles.remove(nombre_a_eliminar)
                print(f"El nombre '{nombre_a_eliminar}' ha sido eliminado de la lista.")
            else:
                print(f"El nombre '{nombre_a_eliminar}' no se encuentra en la lista.")

            print(inmuebles)
        
        elif operaciones == "4":
                           
          indice_a_editar = int(input("Ingrese el índice del valor que desea editar: "))
          nuevo_valor = input("Ingrese el nuevo valor: ")
          if indice_a_editar >= 0 and indice_a_editar < len(inmuebles):
              inmuebles[indice_a_editar] = nuevo_valor
              print(f"El valor ha sido editado exitosamente; {inmuebles[:]}")  
  
          else:
              print("el índice ingresado está fuera del rango válido")
                
         
           
        elif operaciones == "5":
            print("Gracias, fin del programa")
            break   
        
        else:
            print("Operación inválida") 
        
inmobiliaria()            

