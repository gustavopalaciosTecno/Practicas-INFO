class Coche:
    
    color = "rojo"
    marca = "Ferrari"
    modelo = "2015"
    owner = "Gustavo"
    velocidad = 1500
    puertas = 2
    
    
    def acelerar(self):
        self.velocidad +=3
        
    def disminuir(self):
        self.velocidad -= 1
        
        
    def get_velocidad(self):
        return self.velocidad() 



coche = Coche()
print(coche.marca, coche.color)
print(coche.velocidad)
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()

print(coche.velocidad)
              
    