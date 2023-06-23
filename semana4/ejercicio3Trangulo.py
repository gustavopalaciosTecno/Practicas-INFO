class Triangulo:
    
    def __init__(self, lado1, lado2, lado3):
        self.lados = [lado1, lado2, lado3]
    
    def obtener_tipo_triangulo(self):
        lados_iguales = len(set(self.lados)) == 1
        lados_dos_iguales = len(set(self.lados)) == 2
        if lados_iguales:
            return "Equilatero"
        elif lados_dos_iguales:
            return "Isosceles"
        else:
            return "Escaleno"
    
    def encontrar_lado_mayor(self):
        return max(self.lados)
    
    def imprimir_datos(self):
        print("Lado mayor:", self.encontrar_lado_mayor())
        print("Tipo de triángulo:", self.obtener_tipo_triangulo())
    
    
triangulo = Triangulo(
    lado1=int(input("agregá primer valor: ")),
    lado2=int(input("agregá segundo valor: ")),
    lado3=int(input("agregá tercer valor: "))
)

triangulo.imprimir_datos()



