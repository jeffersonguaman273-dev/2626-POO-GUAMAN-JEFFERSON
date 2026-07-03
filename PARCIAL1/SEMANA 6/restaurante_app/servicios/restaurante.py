from typing import List

class Restaurante:
    """Clase de servicio que administra una lista de productos."""

    def __init__(self, nombre: str):
        self.nombre = nombre
        self.productos: List[object] = []  # lista heterogénea de productos

    def agregar_producto(self, producto: object) -> None:
        # se asume que producto implementa mostrar_informacion()
        self.productos.append(producto)

    def mostrar_productos(self) -> None:
        print(f"--- Productos en {self.nombre} ---")
        if not self.productos:
            print("No hay productos registrados.")
            return
        for idx, p in enumerate(self.productos, start=1):
            # demostración de polimorfismo: cada objeto resuelve su propio método
            info = p.mostrar_informacion()
            print(f"{idx}. {info}")

    def buscar_por_nombre(self, nombre: str):
        return [p for p in self.productos if getattr(p, 'nombre', '').lower() == nombre.lower()]
