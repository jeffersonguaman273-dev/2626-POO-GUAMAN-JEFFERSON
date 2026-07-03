from .producto import Producto

class Bebida(Producto):
    """Clase que representa una bebida del restaurante."""

    def __init__(self, nombre: str, precio: float, volumen_ml: int, tamano: str, tipo_bebida: str, disponible: bool = True):
        super().__init__(nombre, precio, disponible)
        self.volumen_ml = volumen_ml
        self.tamano = tamano  # e.g., 'pequeña', 'mediana', 'grande'
        self.tipo_bebida = tipo_bebida  # e.g., 'gaseosa', 'jugo', 'alcohólica'

    # sobrescribir mostrar_informacion
    def mostrar_informacion(self) -> str:
        base = super().mostrar_informacion()
        return (f"{base} | Tipo bebida: {self.tipo_bebida} | Volumen: {self.volumen_ml} ml | "
                f"Tamaño: {self.tamano}")
