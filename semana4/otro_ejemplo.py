# class Circulo:
#     def __init__(self, radio):
#         self.radio = radio
        
#     def calcular_area(self):
#         area = 3.14 * self.radio * self.radio
#         return area
        
#     def imprimir_resultado(self, area):
#         return "el resultado del área es: ", area
    
# radio = int(input("Coloca un valor para calcular el área: "))    
# circulo = Circulo(radio)               
# resultado = circulo.calcular_area()
# print(circulo.imprimir_resultado(resultado))

class Calculadora:
    def __init__(self, valor1, valor2, operacion):
        self.valor1 = valor1
        self.valor2 = valor2
        self.operacion = operacion

    def realizar_operacion(self):
        if self.operacion == "s":
            return self.valor1 + self.valor2
        elif self.operacion == "r":
            return self.valor1 - self.valor2
        elif self.operacion == "m":
            return self.valor1 * self.valor2
        elif self.operacion == "d":
            if self.valor2 != 0:
                return self.valor1 / self.valor2
            else:
                return "Error: división entre cero"

    def mostrar_resultado(self, resultado):
        print("El resultado de la operación es:", resultado)


operacion = input("Elija una letra para realizar la operación (s para sumar, r para restar, m para multiplicar, d para dividir): ")
valor1 = int(input("Agregar primer valor: "))
valor2 = int(input("Agregar segundo valor: "))

calculadora = Calculadora(valor1, valor2, operacion)
respuesta = calculadora.realizar_operacion()
calculadora.mostrar_resultado(respuesta)




    
# operacion = input("elija una letra para realizar la operación s(sumar) - r(restar) - m(multiplicar) y d(dividir):  ")
# valor1 = int(input("agregar primer valor: "))
# valor2 = int(input("agregar segundo valor: "))
# calculadora = Calculadora(valor1=0, valor2=0, operacion=0)
# respuesta = calculadora.realizar_operacion()
# calculadora.mostrar_resultado(respuesta)



   
        