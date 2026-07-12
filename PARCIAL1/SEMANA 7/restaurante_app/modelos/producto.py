"""
Módulo: producto.py
Descripción: Define la clase Producto con atributos controlados mediante
decoradores @property y @setter para validación.
"""


class Producto:
    """
    Clase que representa un producto del restaurante.
    
    Utiliza constructor tradicional __init__ y decoradores @property/@setter
    para controlar el acceso y modificación de atributos con validaciones.
    """
    
    def __init__(self, nombre, categoria, precio, disponible=True):
        """
        Constructor de la clase Producto.
        
        Args:
            nombre (str): Nombre del producto (no puede estar vacío)
            categoria (str): Categoría del producto (no puede estar vacía)
            precio (float): Precio del producto (debe ser mayor que 0)
            disponible (bool): Estado de disponibilidad (por defecto True)
        """
        # Usar los setters para validar los datos al inicializar
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.disponible = disponible
    
    # ========== PROPIEDADES Y SETTERS PARA NOMBRE ==========
    @property
    def nombre(self):
        """Obtiene el nombre del producto."""
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor):
        """
        Establece el nombre del producto con validación.
        
        Raises:
            ValueError: Si el nombre está vacío
        """
        if not valor or not isinstance(valor, str) or valor.strip() == "":
            raise ValueError("❌ El nombre del producto no puede estar vacío")
        self._nombre = valor.strip()
    
    # ========== PROPIEDADES Y SETTERS PARA CATEGORÍA ==========
    @property
    def categoria(self):
        """Obtiene la categoría del producto."""
        return self._categoria
    
    @categoria.setter
    def categoria(self, valor):
        """
        Establece la categoría del producto con validación.
        
        Raises:
            ValueError: Si la categoría está vacía
        """
        if not valor or not isinstance(valor, str) or valor.strip() == "":
            raise ValueError("❌ La categoría del producto no puede estar vacía")
        self._categoria = valor.strip()
    
    # ========== PROPIEDADES Y SETTERS PARA PRECIO ==========
    @property
    def precio(self):
        """Obtiene el precio del producto."""
        return self._precio
    
    @precio.setter
    def precio(self, valor):
        """
        Establece el precio del producto con validación.
        
        Raises:
            ValueError: Si el precio no es válido o es menor/igual a 0
        """
        try:
            precio_float = float(valor)
            if precio_float <= 0:
                raise ValueError("❌ El precio debe ser mayor que cero")
            self._precio = precio_float
        except (TypeError, ValueError):
            raise ValueError("❌ El precio debe ser un número válido mayor que cero")
    
    # ========== PROPIEDADES Y SETTERS PARA DISPONIBILIDAD ==========
    @property
    def disponible(self):
        """Obtiene el estado de disponibilidad del producto."""
        return self._disponible
    
    @disponible.setter
    def disponible(self, valor):
        """Establece el estado de disponibilidad del producto."""
        if not isinstance(valor, bool):
            raise ValueError("❌ La disponibilidad debe ser True o False")
        self._disponible = valor
    
    # ========== MÉTODOS DE UTILIDAD ==========
    def mostrar_informacion(self):
        """Retorna una representación legible de la información del producto."""
        estado = "✓ Disponible" if self.disponible else "✗ No disponible"
        return (
            f"Producto: {self.nombre}\n"
            f"Categoría: {self.categoria}\n"
            f"Precio: ${self.precio:.2f}\n"
            f"Estado: {estado}"
        )
    
    def __repr__(self):
        """Representación en string del objeto Producto."""
        return f"Producto('{self.nombre}', '{self.categoria}', ${self.precio})"
    
    def __str__(self):
        """String amigable para mostrar el producto."""
        return f"{self.nombre} - ${self.precio:.2f}"
