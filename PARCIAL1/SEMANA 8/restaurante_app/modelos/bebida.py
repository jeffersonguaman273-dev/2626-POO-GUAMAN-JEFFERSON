from .producto import Producto


class Bebida(Producto):
    """Representa una bebida del restaurante.

    Hereda de Producto e incorpora atributos específicos como tamano y envase.
    """

    def __init__(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float,
        tamano: str,
        envase: str,
    ) -> None:
        super().__init__(codigo, nombre, categoria, precio)
        self.tamano: str = tamano.strip()
        self.envase: str = envase.strip()

    def mostrar_informacion(self) -> str:
        """Sobrescribe la información para incluir atributos de bebida."""
        base_info = super().mostrar_informacion()
        return f"{base_info} | Tamaño: {self.tamano} | Envase: {self.envase}"

