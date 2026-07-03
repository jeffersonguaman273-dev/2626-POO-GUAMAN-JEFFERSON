class Producto:
    """Clase padre que representa un producto general del restaurante."""

    def __init__(self, nombre: str, precio: float, disponible: bool = True):
        self.nombre = nombre
        # atributo encapsulado: precio privado
        self.__precio = 0.0
        self.cambiar_precio(precio)
        self.disponible = disponible

    # método de acceso
    def obtener_precio(self) -> float:
        return self.__precio

    # método modificador con validación
    def cambiar_precio(self, nuevo_precio: float) -> bool:
        if not isinstance(nuevo_precio, (int, float)):
            raise TypeError('El precio debe ser numérico')
        if nuevo_precio <= 0:
            # no se permite precio cero o negativo
            return False
        self.__precio = float(nuevo_precio)
        return True

    def mostrar_informacion(self) -> str:
        estado = 'Disponible' if self.disponible else 'No disponible'
        return f"Producto: {self.nombre} | Precio: ${self.__precio:.2f} | {estado}"
