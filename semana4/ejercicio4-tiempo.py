# Ejercicio 4: Tiempo
# Crear una clase Tiempo, con atributos hora, minuto y segundo, que pueda ser
# instanciada indicando: los tres atributos, sólo la hora y minuto, o sólo la hora.
# Crear además los métodos necesarios para modificar la hora en cualquier
# momento de forma manual. Mantenga la integridad de los datos en todo
# momento definiendo de tipo “private”. Crear una clase prueba_tiempo que
# prueba una hora concreta y la modifique a su gusto mostrándola por pantalla.

class Tiempo:
    def __init__(self, hora, minuto=0, segundo=0):
        self.__hora = hora
        self.__minuto = minuto
        self.__segundo = segundo
        
    def __str__(self):
        return f"Es la hora: {self.__hora}\n"\
               f"con {self.__minuto} minutos:\n"\
               f"y {self.__segundo} segundos: \n"\
        
     
    def set_hora(self, hora):
        self.__hora = hora
        
    def set_minuto(self, minuto):
        self.__minuto = minuto
        
    def set_segundo(self, segundo):
        self.segundo = segundo  
        
class prueba_tiempo:
    tiempo = Tiempo(
        hora=int(input("ingresa la hora: ")),
        minuto=int(input("ingresa los minutos: ")),
        segundo=int(input("ingresa los segundos: ")))
    print(tiempo)
    # tiempo.set_hora(14)
    # tiempo.set_minuto(15)
    # tiempo.set_segundo(30)
    # print(tiempo)
    
        
                
        
    
        