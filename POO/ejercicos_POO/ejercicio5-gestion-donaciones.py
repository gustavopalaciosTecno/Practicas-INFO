# Ejercicio 5: Gestión de Donaciones
# Nos piden que diseñemos un programa para gestionar donaciones de alimentos.
# Los productos tienen los siguientes atributos:
# Nombre
# Cantidad
# Perecedero: tiene un atributo llamado días a caducar.
# No perecedero: tiene un atributo llamado tipo.
# Tendremos una función llamada Calcular, que según cada clase hará una cosa u
# otra, a esta función se le envía la cantidad por producto y entidades a las cuáles
# se entregarán donaciones.
# Debe obtener la cantidad que se enviará a cada entidad, sabiendo que la
# distribución debe ser lo más equitativa posible. En caso que sobren
# productos, se almacenan para el próximo ciclo de donación.
# Además si el producto es perecedero, se informará:
# Si le queda menos de 10 días para caducar, la entrega debe hacerse en el
# día actual.
# Si le queda 1 mes para caducar, la entrega debe hacerse en el plazo de 1
# semana.
# Si fuera No Perecedero, se informa cuántos productos se entregarán por
# entidad y que queda libre la elección de la fecha de entrega siempre que no
# supere el mes.

class Gestion:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad
        
    def perecedero(self, diasCaducar):
        if diasCaducar <= 10:
            return "la entrega debe hacerse en el dia"
        else:
            return "la entrega debe hacerse en una semana"
        
    def Noperecedero(self, tipo):
        if tipo == "No Perecedero":
            return True
        else:
            return False        
        
    def calcular(self):
        self.donacion = int(input("ingrese una cantidad de donación: "))
        self.cantidad * self.donacion       
        