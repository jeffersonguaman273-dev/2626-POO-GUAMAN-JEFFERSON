# Clase Producto: Representa un producto disponible en el restaurante
# Atributos: id, nombre, descripción, precio, disponibilidad y categoría


class Producto:
    """
    Clase que representa un producto del restaurante.

    Atributos:
        id (int): Identificador único del producto
        nombre (str): Nombre del producto
        descripcion (str): Descripción detallada del producto
        precio (float): Precio del producto en pesos
        disponible (bool): Indica si el producto está disponible
        categoria (str): Categoría a la que pertenece el producto
    """

    def __init__(self, id: int, nombre: str, descripcion: str, precio: float,
                 disponible: bool, categoria: str):
        """
        Constructor que inicializa los atributos del producto.

        Args:
            id: Identificador único del producto
            nombre: Nombre descriptivo del producto
            descripcion: Descripción de las características del producto
            precio: Precio en formato decimal
            disponible: Estado de disponibilidad del producto
            categoria: Clasificación del producto
        """
        self.id: int = id
        self.nombre: str = nombre
        self.descripcion: str = descripcion
        self.precio: float = precio
        self.disponible: bool = disponible
        self.categoria: str = categoria

    def __str__(self) -> str:
        """
        Retorna una representación textual del producto.

        Returns:
            str: Información formateada del producto
        """
        estado = "✓ Disponible" if self.disponible else "✗ No disponible"
        return (f"[ID: {self.id}] {self.nombre} (${self.precio:.2f}) - "
                f"{self.categoria} - {estado}")

    def obtener_detalles(self) -> str:
        """
        Proporciona información detallada del producto.

        Returns:
            str: Detalles completos incluyendo descripción
        """
        return (f"Producto: {self.nombre}\n"
                f"  Descripción: {self.descripcion}\n"
                f"  Precio: ${self.precio:.2f}\n"
                f"  Categoría: {self.categoria}\n"
                f"  Estado: {'Disponible' if self.disponible else 'No disponible'}")

    def cambiar_disponibilidad(self, nuevo_estado: bool) -> None:
        """
        Modifica el estado de disponibilidad del producto.

        Args:
            nuevo_estado: Nuevo valor de disponibilidad
        """
        self.disponible = nuevo_estado

    def aplicar_descuento(self, porcentaje_descuento: float) -> float:
        """
        Calcula el precio con descuento aplicado.

        Args:
            porcentaje_descuento: Porcentaje de descuento a aplicar

        Returns:
            float: Precio final después del descuento
        """
        descuento = self.precio * (porcentaje_descuento / 100)
        precio_con_descuento = self.precio - descuento
        return round(precio_con_descuento, 2)

