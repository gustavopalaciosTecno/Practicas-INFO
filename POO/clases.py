class Usuario:
    def __init__(self, id=None, nombre=None, apellido=None, telefono=None, username=None, email=None, contrasenia=None, fecha_de_registro=None, avatar=None, estado=None, online=None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.username = username
        self.email = email
        self.contrasenia = contrasenia
        self.fecha_de_registro = fecha_de_registro
        self.avatar = avatar
        self.estado = estado
        self.online = online
    
    def login(self):
        if (input("Ingrese su username: ") == self.username and input("Ingrese su contraseña: ") == self.contrasenia):
            print("Bienvenido", self.username)
            self.estado = "logueado"
            self.online = True
        else:
            print("Usuario o contraseña invalido")
    
    def registrar(self):
        self.nombre = input(f'Ingrese su nombre: ')
        self.apellido = input(f'Ingrese su apellido: ')
        self.telefono = input(f'Ingrese su telefono: ')
        self.username = input(f'Ingrese su username: ')
        self.email = input(f'Ingrese su email: ')
        self.contrasenia = input(f'Ingrese su contrasenia: ')
    
    def get_username(self):
        return self.username
    
    def get_estado(self):
        return self.estado
    
    def get_online(self):
        return self.online

persona = Usuario()
persona.registrar()
usr = persona.get_username()
print('Usuario', usr) 
        