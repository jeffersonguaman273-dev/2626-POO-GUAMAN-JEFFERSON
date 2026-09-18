from modelos.producto import Producto
from modelos.usuario import Usuario

class RestauranteServicio:
    def __init__(self, archivo_servicio):
        self.archivo = archivo_servicio
        self.productos = []
        self.usuarios = []
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

    def _persistir_productos(self):
        data = [p.to_dict() for p in self.productos]
        self.archivo.escribir("productos.json", data)

    def validar_acceso(self, username: str, password: str):
        for u in self.usuarios:
            if u.username == username and u.password == password:
                return True
        return False

    def listar_productos(self):
        return self.productos

    def listar_usuarios(self):
        return self.usuarios

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
