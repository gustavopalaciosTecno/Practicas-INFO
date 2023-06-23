class Usuario:
    def __init__(self, id, nombre, apellido, telefono, username, email, contrasenia, fecha_registro, avatar, estado, online):
        self._id = id
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.username = username
        self.email = email
        self.contrasenia = contrasenia
        self.fecha_registro = fecha_registro
        self.avatar = avatar
        self.estado = estado
        self.online = online
    #gg    
    print("Registrar usuario")   
    def registrar(self):
        return f"Identificador: {self._id}\n" \
               f"Nombre: {self.nombre}\n" \
               f"Apellido: {self.apellido}\n" \
               f"Celular: {self.telefono}\n" \
               f"Usuario: {self.username}\n" \
               f"Correo: {self.email}\n" \
               f"Password: {self.contrasenia}\n" \
               f"Fecha de registro: {self.fecha_registro}\n" \
               f"Imagen: {self.avatar}\n" \
               f"Estado: {self.estado}\n" \
               f"Online: {self.online}"

    # def login(self, username='anonimo', contrasenia='123'):
    #     return f"El usuario es: {self.username}\n" \
    #            f"La contraseña es: {self.contrasenia}"
               
    print("Loguearse")             
    def iniciar_sesion(self, usuario, contrasenia):
        # Lista de usuarios y contraseñas válidos
        usuarios_validos = [
            {"usuario": "usuario1", "contrasenia": "123"},
            {"usuario": "usuario2", "contrasenia": "1015"},
            {"usuario": "usuario3", "contrasenia": "pass3"}
        ]
        
        for u in usuarios_validos:
            if u["usuario"] == usuario and u["contrasenia"] == contrasenia:
                self.online = True
                return "Inicio de sesión exitoso!"
            # return "Usuario o contraseña incorrectos   
            return "Usuario o contraseña incorrectos"         
               
               


class Publico(Usuario):
    def __init__(self, id, nombre, apellido, telefono, username, email, contrasenia, fecha_registro, avatar, estado,
                 online, es_publico):
        super().__init__(id, nombre, apellido, telefono, username, email, contrasenia, fecha_registro, avatar, estado,
                         online)
        self.es_publico = es_publico

    def comentar(self, id_articulo, contenido):
        self.id_articulo = id_articulo
        self.contenido = contenido
        return f"El usuario {self.nombre} {self.apellido} deja el siguiente comentario sobre el artículo {self.id_articulo}: {self.contenido}"


class Colaborador(Usuario):
    def __init__(self, id, nombre, apellido, telefono, username, email, contrasenia, fecha_registro, avatar, estado,
                 online, es_colaborador):
        super().__init__(id, nombre, apellido, telefono, username, email, contrasenia, fecha_registro, avatar, estado,
                         online)
        self.es_colaborador = es_colaborador

    def publicar(self, titulo, resumen, contenido, imagen=False):
        self.titulo = titulo
        self.resumen = resumen
        self.contenido = contenido
        self.imagen = imagen
        return f"El usuario {self.nombre} {self.apellido} publica {self.titulo} con el siguiente resumen: {self.resumen}"


class Articulo:
    def __init__(self, id, id_usuario, titulo, resumen, contenido, fecha_publicacion, imagen, estado):
        self.id = id
        self.id_usuario = id_usuario
        self.titulo = titulo
        self.resumen = resumen
        self.contenido = contenido
        self.fecha_publicacion = fecha_publicacion
        self.imagen = imagen
        self.estado = estado
    def mostrar_articulos(self):
        return(f"Id del artículo:, {self.id}, N° de usuario: {self.id_usuario}, Título: {self.titulo}, Resumen: {self.resumen}, Contenido: {self.contenido}, Fecha de publicación: {self.fecha_publicacion}, 'Avatar': {self.imagen}, Estado: {self.estado}")

class Comentario:
    def __init__(self, id=1, id_articulo=1, id_usuario=1, contenido="", fecha_hora="", estado=""):
        self.id = id
        self.id_articulo = id_articulo
        self.id_usuario = id_usuario
        self.contenido = contenido
        self.fecha_hora = fecha_hora
        self.estado = estado
    def mostar_comentario(self):
        return f" N° Identificador: {self.id}  N°artículo {self.id_articulo} Usuario: {self.id_usuario} Contenido: {self.contenido} Fecha y Hora: {self.fecha_hora} Estado: {self.estado}"
    
    

 
usuario = Usuario(id=0, 
                  nombre=input("agrega un nombre: "), 
                  apellido=input("agregar apellido: "), 
                  telefono=int(input("agregar teléfono: ")), 
                  username=input("agregar usuario: "), 
                  email=input("agregar email: "), 
                  contrasenia=input("agregar contraseña"), 
                  fecha_registro=input("agregar fecha: "), 
                  avatar="😂", 
                  estado=input("agregar estado: "), 
                  online=input("agregar si esta online: "))
print(usuario.registrar())  
  

usuario.iniciar_sesion(usuario=input("agregar usuario: "), contrasenia=input("agregar contraseña: "))


usuario2 = Publico(2, 
                   "Paco", 
                   "Rabal", 
                   "455455", 
                   "admin", 
                   "mailito@mail.com", 
                   "45111gg", "05-06-2023", 
                   "-", "activo", 
                   "si", 
                   "es publico")
print(usuario2.comentar(2, "un buen momento para comenzar a estudiar programación"))
usuario3 = Comentario(
                      #id_usuario=int("agregar un identificador para el usuario: "),  
                      estado=input("agregar estado: "), 
                      contenido=input("agregar contenido: "),
                      fecha_hora=input("agregar fecha: "), 
                      )
print(usuario3.mostar_comentario())
usuario4 = Articulo(1, 
                    10, 
                    "Ovnis en Resistencia", 
                    "emergencia nacional comienza hoy",
                    "este contenido está a punto de autodestruirse",
                    "19/06/2023",
                    "- ",
                    "activo"
                    )

print(usuario.login())