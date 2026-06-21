# Módulo: producto.py
# Descripción: Define la clase Producto que representa los artículos disponibles en el restaurante

class Producto:
    """
    Clase que representa un producto del restaurante.

    Atributos:
        id (int): Identificador único del producto
        nombre (str): Nombre del producto (ej: Pizza Margarita, Refresco, Postre)
        precio (float): Precio del producto en unidades monetarias
        descripcion (str): Descripción breve del producto
        tipo_producto (str): Categoría del producto (plato_principal, bebida, postre, entrada)
        disponibilidad (bool): Indica si el producto está disponible para venta
    """

    def __init__(self, id, nombre, precio, descripcion, tipo_producto, disponibilidad=True):
        """
        Constructor de la clase Producto.

        Args:
            id (int): Identificador único del producto
            nombre (str): Nombre del producto
            precio (float): Precio del producto
            descripcion (str): Descripción del producto
            tipo_producto (str): Tipo o categoría del producto
            disponibilidad (bool): Estado de disponibilidad (por defecto True)
        """
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.tipo_producto = tipo_producto
        self.disponibilidad = disponibilidad

    def __str__(self):
        """
        Retorna una representación en texto del producto.
        Facilita la visualización de la información de forma legible.
        """
        estado = "Disponible" if self.disponibilidad else "No disponible"
        return f"[{self.id}] {self.nombre} - ${self.precio:.2f} ({self.tipo_producto}) - {estado}"

    def obtener_informacion(self):
        """
        Retorna información detallada del producto.
        """
        return {
            'id': self.id,
            'nombre': self.nombre,
            'precio': self.precio,
            'descripcion': self.descripcion,
            'tipo': self.tipo_producto,
            'disponible': self.disponibilidad
        }

    def cambiar_disponibilidad(self, disponible):
        """
        Cambia el estado de disponibilidad del producto.

        Args:
            disponible (bool): Nuevo estado de disponibilidad
        """
        self.disponibilidad = disponible

    def actualizar_precio(self, nuevo_precio):
        """
        Actualiza el precio del producto.

        Args:
            nuevo_precio (float): Nuevo precio del producto
        """
        if nuevo_precio > 0:
            self.precio = nuevo_precio
        else:
            print("Error: El precio debe ser mayor a 0")


