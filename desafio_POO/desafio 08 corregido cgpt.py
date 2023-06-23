import time
from datetime import datetime

class Usuario:
    def __init__(self, id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar, estado, online):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.username = username
        self.email = email
        self.contraseña = contraseña
        self.fecha_registro = fecha_registro
        self.avatar = avatar
        self.estado = estado
        self.online = online

    def login(self, username, contraseña):
        if self.username == username and self.contraseña == contraseña:
            self.online = True
            print("Inicio de sesión exitoso.")
        else:
            print("Contraseña incorrecta.")

    def registrar(self):
        self.id += 1
        self.fecha_registro = time.strftime("%x") # función para obtener la fecha actual
        self.nombre = input("Ingrese su nombre: ")
        self.apellido = input("Ingrese su apellido: ")
        self.telefono = input("Ingrese su telefono: ")
        self.username = input("Ingrese su nombre de usuario: ")
        self.email = input("Ingrese su email: ")
        self.contraseña = input("Ingrese su contraseña: ")
        self.avatar = input("Suba su imagen de perfil:")
        self.estado = "activo"
        self.online = True
        return self

    def __str__(self):
        return f"Usuario: {self.nombre} {self.apellido}\nID: {self.id}\nEstado: {'Conectado' if self.online else 'Desconectado'}"


class Publico(Usuario):
    def __init__(self, id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar, estado, online, es_publico):
        super().__init__(id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar, estado, online)
        self.es_publico = True

    def registrar(self):
        super().registrar()

    def comentar(self, comentario):
        nuevo_comentario = Comentario(
            id=comentario.id,
            id_articulo=comentario.id_articulo,
            contenido=comentario.contenido,
            fecha_hora=datetime.now(),
            estado="publicado"
        )


class Colaborador(Usuario):
    def __init__(self, id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar, estado, online, es_colaborador):
        super().__init__(id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar, estado, online)
        self.es_colaborador = True

    def registrar(self):
        super().registrar()

    def publicar(self, articulo):
        nuevo_articulo = Articulo(
            id=articulo.id,
            id_usuario=self.id,
            titulo=articulo.titulo,
            resumen=articulo.resumen,
            contenido=articulo.contenido,
            fecha_publicacion=datetime.now(),
            imagen=None,
            estado='publicado'
        )

        nuevo_articulo.mostrar_contenido()


class Articulo:
    def __init__(self, id, id_usuario, titulo, resumen, contenido, fecha_publicacion, imagen, estado):
        self.id = id
        self.contenido = contenido
        self.id_usuario = id_usuario
        self.titulo = titulo
        self.resumen = resumen
        self.fecha_publicacion = fecha_publicacion
        self.imagen = imagen
        self.estado = estado

    def mostrar_contenido(self):
        print("Título:", self.titulo)
        print("Contenido:", self.contenido)

    @staticmethod
    def crear_articulo(usuario):
        id = 0  # Considera una estrategia adecuada para asignar identificadores únicos
        titulo = input("Ingrese título: ")
        contenido = input("Ingrese el contenido: ")
        id_usuario = usuario.id
        resumen = input("Ingrese el resumen: ")
        fecha_publicacion = datetime.now()
        imagen = None
        estado = 'publicado'
        nuevo_articulo = Articulo(id, id_usuario, titulo, resumen, contenido, fecha_publicacion, imagen, estado)
        return nuevo_articulo


class Comentario:
    def __init__(self, id, id_articulo, contenido, fecha_hora, estado):
        self.id = id
        self.contenido = contenido
        self.fecha_hora = fecha_hora
        self.estado = estado

    def mostrar_contenido(self):
        print("Fecha:", self.fecha_hora)
        print("Contenido:", self.contenido)


# Código para login o registro
u1 = Usuario(1, "John", "Doe", "123456789", "pe3", "johndoe@example.com", "1234", "2021-01-01", "avatar.jpg", "activo", True)
u2 = Usuario(2, "John", "Doe", "123456789", "pe3", "johndoe@example.com", "1234", "2021-01-01", "avatar.jpg", "activo", True)
u3 = Colaborador(2, "pepito", "colab", "123456789", "cola", "johndoe@example.com", "borador", "2021-01-01", "avatar.jpg", "activo", True, True)

op = input("Ingrese opción 1 (registro) o 2 (login) o 3 (colaborador): ")

if op == "1":
    print("Registro")
    print(u2.registrar())

elif op == "2":
    print("Login")
    username = input("Ingresa tu nombre de usuario: ")
    contraseña = input("Ingresa tu contraseña: ")
    u1.login(username, contraseña)

elif op == "3":
    print(f"Bienvenido {u3.nombre}")
    if u3.es_colaborador:
        art = Articulo.crear_articulo(u3)
        u3.publicar(art)

else:
    print("Opción no válida")
 