# CREATE TABLE colaborador(
#     dni INT,
#     nombre CHAR(20),
#     apellido CHAR(20),
#     estado CHAR(8) CHECK (estado = 'activo' OR estado = 'inactivo'),
#     fecha_reg DATETIME DEFAULT CURRENT_TIMESTAMP,
#     email CHAR(25) NOT NULL,
#     telefono INT,
#     avatar CHAR(255),
#     contrasenia CHAR(30),
#     PRIMARY KEY(dni)
# );

# class Colaborador(models.Models):
#     def __init__(self, dni, nombre, apellido, estado, fecha_reg, email, telefono, avatar, contrasenia): # __ se llama dunder
#         self.dni = dni
#         self.nombre = nombre
#         self.apellido = apellido
#         self.estado = estado
#         self.fecha_reg = fecha_reg
#         self.email = email
#         self.telefono = telefono
#         self.avatar = avatar
#         self.contrasenia = contrasenia
    
#     def get_dni(dni):
#         pass

#     def set_dni(dni_old, dni_new):
#         pass

#     def delete_row_dni(dni):
#         pass

#     def suma():
#         pass

# Clase Usuario
# -atributos: id, nombre, apellido, teléfono, username, email, contraseña, fecha de 
# registro, avatar, estado, online
# -métodos: login(), registrar()

# Clase Publico(Usuario)
# -atributo: es_publico
# -métodos: registrar(), comentar()

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

# persona = Usuario()
# persona.registrar()
# usr = persona.get_username()
# print('Usuario', usr)

# persona.login()
# estado_persona = persona.get_estado()
# online_persona = persona.get_online()
# print(f'Estado {estado_persona}, Online {online_persona}')


class Publico(Usuario):
    es_publico = True

    def __init__(self, id=None, nombre=None, apellido=None, telefono=None, username=None, email=None, contrasenia=None, fecha_de_registro=None, avatar=None, estado=None, online=None):
        super().__init__(id, nombre, apellido, telefono, username, email, contrasenia, fecha_de_registro, avatar, estado, online)
    
    def get_es_publico(self):
        return self.es_publico

obj_publico = Publico()
obj_publico.registrar()
var_pub = obj_publico.get_es_publico()
print(f'Mediante metodo: {var_pub}, mediante acceso al atrib {obj_publico.es_publico}')
print(f'Obtener username {obj_publico.get_username()}')