from .producto import Producto

class Platillo(Producto):
    """Clase que representa un platillo del restaurante."""

    def __init__(self, nombre: str, precio: float, calorias: int, tipo: str, tiempo_preparacion: int, disponible: bool = True):
        super().__init__(nombre, precio, disponible)
        self.calorias = calorias
        self.tipo = tipo  # e.g., 'entrada', 'principal', 'postre'
        self.tiempo_preparacion = tiempo_preparacion  # en minutos

    # sobrescribir mostrar_informacion para demostrar polimorfismo
    def mostrar_informacion(self) -> str:
        base = super().mostrar_informacion()
        return (f"{base} | Tipo: {self.tipo} | Calorías: {self.calorias} kcal | "
                f"Tiempo preparación: {self.tiempo_preparacion} min")
