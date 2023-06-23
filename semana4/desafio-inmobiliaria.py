print("PROPIEDAD INTELECUAL DE PALACIOS MEYER, NÉSTOR GUSTAVO")
print("Se permite la copia y/o distribución de este código bajo las normas de la GPL ")
def mostrar_lista_inmuebles(lista):
    contador=1
    for inmueble in lista:
        print(f"----INMUEBLE {contador}-----")
        print("Año:", inmueble['año'])
        print("Metros cuadrados:", inmueble['metros'])
        print("Número de habitaciones:", inmueble['habitaciones'])
        print("¿Tiene garaje?:", "Sí" if inmueble['garaje'] else "No")
        print("Zona:", inmueble['zona'])
        print("Estado:", inmueble['estado'])
        print("Precio:", calcular_precio(inmueble))
        print("---------")
        contador+=1        



def agregar():
    inmueble = {}

    inmueble['año'] = int(input("Año: "))
    inmueble['metros'] = int(input("Metros cuadrados: "))
    inmueble['habitaciones'] = int(input("Número de habitaciones: "))
    inmueble['garaje'] = input("¿Tiene garaje? (S/N): ").upper() == 'S'
    inmueble['zona'] = input("Zona (A, B o C): ").upper()
    inmueble['estado'] = input("Estado (Disponible, Reservado o Vendido): ").capitalize()

    if validar_inmueble(inmueble):
        print ('Agregado correctamente')
        return inmueble
    else:
        print("El inmueble no cumple con las reglas de validación.")



def editar(lista):
    print("ESTÁ A PUNTO DE MODIFICAR UN ELEMENTO")
    mostrar_lista_inmuebles(lista)
    index = int(input('SELECCIONE EL NÚMERO DEL INMUEBLE QUE QUIERE CAMBIAR: '))
    if index >= 0 and index<= len(lista):
        inmueble = lista[index-1]
        inmueble_guardado={}
        inmueble_guardado.update(inmueble)

        inmueble['año'] = int(input("Nuevo año: "))
        inmueble['metros'] = int(input("Nuevos metros cuadrados: "))
        inmueble['habitaciones'] = int(input("Nuevo número de habitaciones: "))
        inmueble['garaje'] = input("¿Tiene garaje? (S/N): ").upper() == 'S'
        inmueble['zona'] = input("Nueva zona (A, B o C): ").upper()

        if validar_inmueble(inmueble):
            print("Inmueble editado correctamente.")
        else:
            inmueble.clear()
            inmueble.update(inmueble_guardado)
            print("El inmueble no cumple con las reglas de validación, se restablecieron los valores antes del cambio.")
    else:
        print("El índice del inmueble es inválido,se restablecieron los valores antes de la modificacion.")
        inmueble.clear()
        inmueble.update(inmueble_guardado)



def eliminar(lista):
    indice = int(input("Ingrese el índice del inmueble a eliminar: "))
    mostrar_lista_inmuebles(lista)
    if indice >= 0 and indice <= len(lista):
        del lista[indice-1]
        print("Inmueble eliminado.")
    else:
        print("Índice inválido.")



def busqueda(lista, precio):
    inmuebles_encontrados = []

    for inmueble in lista:
        if inmueble['estado'] in ['Disponible', 'Reservado'] and calcular_precio(inmueble) <= precio:
            inmueble['precio'] = calcular_precio(inmueble)
            inmuebles_encontrados.append(inmueble)

    return inmuebles_encontrados




def validar_inmueble(inmueble):
    if inmueble['zona'] not in ['A', 'B', 'C']:
        return False
    if inmueble['estado'] not in ['Disponible', 'Reservado', 'Vendido']:
        return False
    if inmueble['año'] < 2000:
        return False
    if inmueble['metros'] < 60:
        return False
    if inmueble['habitaciones'] < 2:
        return False

    return True

def calcular_precio(inmueble):
    precio_base = (inmueble['metros'] * 100) + (inmueble['habitaciones'] * 500) + (inmueble['garaje'] * 1500)
    antiguedad = 2023 - inmueble['año']

    if inmueble['zona'] == 'A':
        precio = precio_base * (1 - antiguedad / 100)
    elif inmueble['zona'] == 'B':
        precio = precio_base * (1 - antiguedad / 100) * 1.5
    elif inmueble['zona'] == 'C':
        precio = precio_base * (1 - antiguedad / 100) * 2
    return precio


# diccionario dentro de la lista
inmuebles = [{'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
             {'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
             {'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
             {'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
             {'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}]

# Menú principal
while True:
    print("-------- Menú --------")
    print("1. Agregar inmueble")
    print("2. Editar inmueble")
    print("3. Eliminar inmueble")
    print("4. Búsqueda de inmuebles por presupuesto")
    print("5. Mostrar Inmueble")
    print("6. Salir")
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        inmuebles.append(agregar())
    elif opcion == "2":
        editar(inmuebles)
    elif opcion == "3":
        eliminar(inmuebles)
    elif opcion == "4":
        presupuesto = float(input("Ingrese un presupuesto: "))
        resultados = busqueda(inmuebles, presupuesto)
        for inmueble in resultados:
            print(inmueble)
    elif opcion == "5":
        mostrar_lista_inmuebles(inmuebles)
    elif opcion == "6":
        break
    else:
        print("Opción inválida. Intente nuevamente.")

print("¡Hasta luego!")