def agregar_inmueble(lista, inmueble):
    if validar_inmueble(inmueble):
        lista.append(inmueble)

def editar_inmueble(lista, indice, inmueble):
    if validar_inmueble(inmueble):
        lista[indice] = inmueble

def eliminar_inmueble(lista, indice):
    del lista[indice]

def cambiar_estado(lista, indice, nuevo_estado):
    if nuevo_estado in ['Disponible', 'Reservado', 'Vendido']:
        lista[indice]['estado'] = nuevo_estado

def buscar_por_presupuesto(lista, presupuesto):
    return [
        {**inmueble, 'precio': calcular_precio(inmueble)}
        for inmueble in lista
        if inmueble['estado'] in ['Disponible', 'Reservado']
        and calcular_precio(inmueble) <= presupuesto
    ]

def validar_inmueble(inmueble):
    return (
        inmueble['zona'] in ['A', 'B', 'C'] and
        inmueble['estado'] in ['Disponible', 'Reservado', 'Vendido'] and
        inmueble['año'] >= 2000 and
        inmueble['metros'] >= 60 and
        inmueble['habitaciones'] >= 2
    )

def calcular_precio(inmueble):
    antiguedad = 2023 - inmueble['año']
    factor_zona = {'A': 1, 'B': 1.5, 'C': 2}
    return (inmueble['metros'] * 100 + inmueble['habitaciones'] * 500 + inmueble['garaje'] * 1500) * (1 - antiguedad / 100) * factor_zona[inmueble['zona']]

