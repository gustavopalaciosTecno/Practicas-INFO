class Usuario:
    
    def __init__(self, 
                 id, 
                 nombre, 
                 apellido,
                 telefono, 
                 username, 
                 email, 
                 contrasenia,
                 fecha_registro,
                 avatar,
                 estado,
                 online
                 ) :
        self.id = id
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
        
    def registrar(self):
            
                    
            return (f"identificador: {self.id}, \n"
                    f"nombre: {self.nombre}, \n"
                    f"apellido: {self.apellido}, \n"
                    f"celular: {self.telefono}, \n"
                    f"usuario: {self.username}, \n"
                    f"correo: {self.email}, \n"
                    f"password: {self.contrasenia}, \n"
                    f"fecha de registro: {self.fecha_registro}, \n"
                    f"imagen: {self.avatar}, \n"
                    f"estado: {self.estado}, \n"
                    f"online?: {self.online}"
        )
                   
    def login(self, username='anonimo', contrasenia='123'):
        return (f"el usuario es: {self.username}, \n"
                f"el password es: {self.contrasenia}"
                )
               
        
    
class Publico(Usuario):
    
    def __init__(self, id, nombre, apellido, telefono, username, email, contrasenia, fecha_registro, avatar, estado, online, es_publico):
         super().__init__(id, nombre, apellido, telefono, username, email, contrasenia, fecha_registro, avatar, estado, online)
         self.es_publico = es_publico

         
    def comentar(self, id_articulo, contenido):
        self.id_articulo = id_articulo
        self.contenido = contenido
        return f"el usuario {self.nombre}, {self.apellido} deja el siguiente comentario sobre el artículo: {self.id_articulo} - {self.contenido} "  
         
class Colaborador(Usuario):
    def __init__(self, id, nombre, apellido, telefono, username, email, contrasenia, fecha_registro, avatar, estado, online, es_colaborador):
         super().__init__(id, nombre, apellido, telefono, username, email, contrasenia, fecha_registro, avatar, estado, online)    
         self.es_colaborador = es_colaborador
         
    def publicar(self, titulo, resumen, contenido, imagen = False): # no sabía si es así pero lo puse en false para que no me de problemas
        self.titulo = titulo
        self.resumen = resumen
        self.contenido = contenido
        self.imagen = imagen
        return f"el usuario {self.nombre} - {self.apellido} publica {self.titulo} del contenido: {self.contenido} con el siguiente resumen: {self.resumen}"
                  
class Articulo:
    def __init__(self, id, id_usuario, titulo, resumen, contenido, fecha_publicacion, imagen, estado):
        self.id = id
        self.id_usuario = id_usuario
        self.titulo = titulo
        self.titulo = titulo
        self.resumen = resumen
        self.contenido = contenido
        self.fechapublicacion = fecha_publicacion
        self.imagen = imagen
        self.estado = estado
            
class Comentario:
    def __init__(self, id, id_articulo, id_usuario, contenido, fecha_hora, estado):
        self.id = id
        self.id_articulo = id_articulo
        self.id_usuario = id_usuario
        self.contenido = contenido
        self.fecha_hora = fecha_hora
        self.estado = estado
        
        
        
                  
usuario = Usuario(2, "Fabian", "Yrala", "455455", "admin", "mailito@mail.com", "45111gg", "05-06-2023", "-", "activo", "si")
print(usuario.registrar())    
print(usuario.login())
usuario2 = Publico(2, "Fabian", "Yrala", "455455", "admin", "mailito@mail.com", "45111gg", "05-06-2023", "-", "activo", "si", "es publico")
print(usuario2.comentar(2, "mi amiga Yamila F. no quiere pagarse el asado"))





                    
               
              
          
                    
                
                    
                  
        