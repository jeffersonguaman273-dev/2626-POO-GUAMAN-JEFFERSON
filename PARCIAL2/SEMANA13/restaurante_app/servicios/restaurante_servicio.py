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
