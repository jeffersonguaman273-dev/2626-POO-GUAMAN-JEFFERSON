from typing import List

from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    """Servicio que administra productos y clientes del restaurante."""

    def __init__(self) -> None:
        # Colección única de productos (Producto y sus subclases)
        self._productos: List[Producto] = []
        # Colección de clientes
        self._clientes: List[Cliente] = []

    # ---------- PRODUCTOS ----------
    def producto_existe(self, codigo: str) -> bool:
        codigo = codigo.strip()
        return any(p.codigo == codigo for p in self._productos)

    def registrar_producto(self, producto: Producto) -> bool:
        """Registra un producto si su código no existe. Devuelve True si se agregó."""
        if self.producto_existe(producto.codigo):
            return False
        self._productos.append(producto)
        return True

    def listar_productos(self) -> List[str]:
        """Devuelve una lista de cadenas con la información de cada producto.

        Aplica polimorfismo usando el método mostrar_informacion() de cada objeto.
        """
        return [p.mostrar_informacion() for p in self._productos]

    # ---------- CLIENTES ----------
    def cliente_existe(self, identificacion: str) -> bool:
        identificacion = identificacion.strip()
        return any(c.identificacion == identificacion for c in self._clientes)

    def registrar_cliente(self, cliente: Cliente) -> bool:
        """Registra un cliente si su identificación no existe. Devuelve True si se agregó."""
        if self.cliente_existe(cliente.identificacion):
            return False
        self._clientes.append(cliente)
        return True

    def listar_clientes(self) -> List[str]:
        return [c.mostrar_informacion() for c in self._clientes]

