from datetime import datetime

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class RestauranteServicio:
    ROLES_PERMITIDOS = ["Administrador", "Empleado", "Cliente"]

    def __init__(self, archivo_servicio):
        self.archivo = archivo_servicio
        self.productos = []
        self.usuarios = []
        self.ventas = []
        self.cargar()

    def cargar(self):
        try:
            productos_data = self.archivo.leer("productos.json")
            self.productos = [Producto(**p) for p in productos_data]
        except Exception:
            self.productos = []

        try:
            usuarios_data = self.archivo.leer("usuarios.json")
            self.usuarios = [Usuario(**u) for u in usuarios_data]
        except Exception:
            self.usuarios = []

        try:
            ventas_data = self.archivo.leer("ventas.json")
            self.ventas = [Venta(**v) for v in ventas_data]
        except Exception:
            self.ventas = []

    def _persistir_productos(self):
        data = [p.to_dict() for p in self.productos]
        self.archivo.escribir("productos.json", data)

    def _persistir_usuarios(self):
        data = [u.to_dict() for u in self.usuarios]
        self.archivo.escribir("usuarios.json", data)

    def _persistir_ventas(self):
        data = [v.to_dict() for v in self.ventas]
        self.archivo.escribir("ventas.json", data)

    def validar_acceso(self, username: str, password: str):
        usuario = self.obtener_usuario_por_username(username)
        if usuario is None:
            return False
        return usuario.password == password

    def obtener_usuario_por_username(self, username: str):
        if username is None:
            return None
        for u in self.usuarios:
            if u.username == username:
                return u
        return None

    def listar_productos(self):
        return self.productos

    def listar_usuarios(self):
        return sorted(self.usuarios, key=lambda u: (u.id is None, u.id or 0))

    def listar_ventas(self):
        return self.ventas

    def cantidad_producto(self, producto_id):
        for p in self.productos:
            if p.id == producto_id:
                return p.cantidad
        return None

    def agregar_producto(self, nombre: str, precio: float, cantidad: int):
        if not nombre:
            raise ValueError("El nombre es requerido")
        try:
            precio = float(precio)
            cantidad = int(cantidad)
        except Exception:
            raise ValueError("Precio o cantidad inválidos")
        next_id = 1
        if self.productos:
            next_id = max(p.id for p in self.productos) + 1
        nuevo = Producto(next_id, nombre, precio, cantidad)
        self.productos.append(nuevo)
        self._persistir_productos()
        return nuevo

    def obtener_producto(self, producto_id):
        try:
            producto_id = int(producto_id)
        except Exception:
            return None
        for p in self.productos:
            if p.id == producto_id:
                return p
        return None

    def actualizar_producto(self, producto_id, nombre=None, precio=None, cantidad=None):
        p = self.obtener_producto(producto_id)
        if not p:
            raise ValueError("Producto no encontrado")
        if nombre is not None and nombre != "":
            p.nombre = nombre
        if precio is not None and precio != "":
            p.precio = float(precio)
        if cantidad is not None and cantidad != "":
            p.cantidad = int(cantidad)
        self._persistir_productos()
        return p

    def eliminar_producto(self, producto_id):
        p = self.obtener_producto(producto_id)
        if not p:
            raise ValueError("Producto no encontrado")
        self.productos = [x for x in self.productos if x.id != p.id]
        self._persistir_productos()
        return True

    def obtener_usuario(self, usuario_id):
        try:
            usuario_id = int(usuario_id)
        except Exception:
            return None
        for u in self.usuarios:
            if u.id == usuario_id:
                return u
        return None

    def registrar_usuario(self, username: str, password: str, nombre: str, rol: str):
        username = (username or "").strip()
        password = (password or "").strip()
        nombre = (nombre or "").strip()
        rol = (rol or "Cliente").strip()

        if not username:
            raise ValueError("El nombre de usuario es requerido")
        if not password:
            raise ValueError("La contraseña es requerida")
        if not nombre:
            raise ValueError("El nombre completo es requerido")
        if rol not in self.ROLES_PERMITIDOS:
            raise ValueError("El rol no es válido")
        if self.obtener_usuario_por_username(username):
            raise ValueError("El nombre de usuario ya existe")

        next_id = 1
        if self.usuarios:
            next_id = max(u.id for u in self.usuarios if u.id is not None) + 1

        usuario = Usuario(id=next_id, username=username, password=password, nombre=nombre, rol=rol)
        self.usuarios.append(usuario)
        self._persistir_usuarios()
        return usuario

    def actualizar_usuario(self, usuario_id, username=None, password=None, nombre=None, rol=None):
        usuario = self.obtener_usuario(usuario_id)
        if not usuario:
            raise ValueError("Usuario no encontrado")

        nuevo_username = (username or "").strip()
        nueva_password = (password or "").strip()
        nuevo_nombre = (nombre or "").strip()
        nuevo_rol = (rol or usuario.rol).strip()

        if nuevo_username:
            existente = self.obtener_usuario_por_username(nuevo_username)
            if existente and existente.id != usuario.id:
                raise ValueError("El nombre de usuario ya existe")
            usuario.username = nuevo_username
        if nueva_password:
            usuario.password = nueva_password
        if nuevo_nombre:
            usuario.nombre = nuevo_nombre
        if nuevo_rol in self.ROLES_PERMITIDOS:
            usuario.rol = nuevo_rol
        self._persistir_usuarios()
        return usuario

    def eliminar_usuario(self, usuario_id, usuario_actual=None):
        usuario = self.obtener_usuario(usuario_id)
        if not usuario:
            raise ValueError("Usuario no encontrado")
        if usuario_actual and usuario.id == usuario_actual.id:
            raise ValueError("No puede eliminar la cuenta administradora activa")
        self.usuarios = [u for u in self.usuarios if u.id != usuario.id]
        self._persistir_usuarios()
        return True

    def registrar_venta(self, username: str, producto_id):
        usuario = self.obtener_usuario_por_username(username)
        if not usuario:
            raise ValueError("Usuario no encontrado")

        producto = self.obtener_producto(producto_id)
        if not producto:
            raise ValueError("Producto no encontrado")

        next_id = 1
        if self.ventas:
            next_id = max(v.id for v in self.ventas) + 1
        fecha = datetime.now().isoformat()
        venta = Venta(next_id, username, producto.id, fecha)
        self.ventas.append(venta)
        self._persistir_ventas()
        return venta
