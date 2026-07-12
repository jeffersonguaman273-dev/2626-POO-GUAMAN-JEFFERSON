"""
Módulo: restaurante.py
Descripción: Define la clase Restaurante que actúa como servicio para
administrar productos y clientes del restaurante.
"""


class Restaurante:
    """
    Clase de servicio encargada de administrar listas de productos y clientes.
    
    Implementa métodos para registrar, listar y buscar productos y clientes
    dentro del sistema del restaurante.
    """
    
    def __init__(self, nombre_restaurante="Mi Restaurante"):
        """
        Constructor del servicio Restaurante.
        
        Args:
            nombre_restaurante (str): Nombre del restaurante
        """
        self.nombre_restaurante = nombre_restaurante
        self.productos = []  # Lista de objetos Producto
        self.clientes = []   # Lista de objetos Cliente
    
    # ========== MÉTODOS PARA PRODUCTOS ==========
    
    def registrar_producto(self, producto):
        """
        Registra un nuevo producto en el restaurante.
        
        Args:
            producto (Producto): Objeto producto a registrar
            
        Returns:
            bool: True si se registró exitosamente, False si ya existe
        """
        # Evitar duplicados por nombre
        if any(p.nombre.lower() == producto.nombre.lower() for p in self.productos):
            return False
        self.productos.append(producto)
        return True
    
    def listar_productos(self):
        """
        Retorna la lista de todos los productos registrados.
        
        Returns:
            list: Lista de objetos Producto
        """
        return self.productos
    
    def obtener_productos_disponibles(self):
        """
        Retorna solo los productos que están disponibles.
        
        Returns:
            list: Lista de productos disponibles
        """
        return [p for p in self.productos if p.disponible]
    
    def buscar_producto_por_nombre(self, nombre):
        """
        Busca un producto por nombre (búsqueda insensible a mayúsculas).
        
        Args:
            nombre (str): Nombre del producto a buscar
            
        Returns:
            Producto: El producto encontrado, o None si no existe
        """
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                return producto
        return None
    
    def buscar_productos_por_categoria(self, categoria):
        """
        Busca todos los productos de una categoría específica.
        
        Args:
            categoria (str): Categoría a buscar
            
        Returns:
            list: Lista de productos en esa categoría
        """
        return [p for p in self.productos 
                if p.categoria.lower() == categoria.lower()]
    
    def actualizar_producto(self, nombre_antiguo, nombre_nuevo=None, 
                           categoria_nueva=None, precio_nuevo=None):
        """
        Actualiza los datos de un producto existente.
        
        Args:
            nombre_antiguo (str): Nombre actual del producto
            nombre_nuevo (str, optional): Nuevo nombre
            categoria_nueva (str, optional): Nueva categoría
            precio_nuevo (float, optional): Nuevo precio
            
        Returns:
            bool: True si se actualizó, False si no existe el producto
        """
        producto = self.buscar_producto_por_nombre(nombre_antiguo)
        if producto is None:
            return False
        
        if nombre_nuevo:
            producto.nombre = nombre_nuevo
        if categoria_nueva:
            producto.categoria = categoria_nueva
        if precio_nuevo is not None:
            producto.precio = precio_nuevo
        
        return True
    
    def eliminar_producto(self, nombre):
        """
        Elimina un producto del restaurante.
        
        Args:
            nombre (str): Nombre del producto a eliminar
            
        Returns:
            bool: True si se eliminó, False si no existe
        """
        producto = self.buscar_producto_por_nombre(nombre)
        if producto:
            self.productos.remove(producto)
            return True
        return False
    
    # ========== MÉTODOS PARA CLIENTES ==========
    
    def registrar_cliente(self, cliente):
        """
        Registra un nuevo cliente en el restaurante.
        
        Args:
            cliente (Cliente): Objeto cliente a registrar
            
        Returns:
            bool: True si se registró exitosamente, False si ya existe
        """
        # Evitar duplicados por ID
        if any(c.id_cliente == cliente.id_cliente for c in self.clientes):
            return False
        self.clientes.append(cliente)
        return True
    
    def listar_clientes(self):
        """
        Retorna la lista de todos los clientes registrados.
        
        Returns:
            list: Lista de objetos Cliente
        """
        return self.clientes
    
    def buscar_cliente_por_id(self, id_cliente):
        """
        Busca un cliente por su ID.
        
        Args:
            id_cliente (str): ID del cliente a buscar
            
        Returns:
            Cliente: El cliente encontrado, o None si no existe
        """
        for cliente in self.clientes:
            if cliente.id_cliente == id_cliente:
                return cliente
        return None
    
    def buscar_cliente_por_nombre(self, nombre):
        """
        Busca clientes por nombre (búsqueda insensible a mayúsculas).
        
        Args:
            nombre (str): Nombre del cliente a buscar
            
        Returns:
            list: Lista de clientes que coinciden con el nombre
        """
        return [c for c in self.clientes 
                if nombre.lower() in c.nombre.lower()]
    
    def buscar_cliente_por_correo(self, correo):
        """
        Busca un cliente por correo electrónico.
        
        Args:
            correo (str): Correo del cliente a buscar
            
        Returns:
            Cliente: El cliente encontrado, o None si no existe
        """
        for cliente in self.clientes:
            if cliente.correo.lower() == correo.lower():
                return cliente
        return None
    
    def eliminar_cliente(self, id_cliente):
        """
        Elimina un cliente del restaurante.
        
        Args:
            id_cliente (str): ID del cliente a eliminar
            
        Returns:
            bool: True si se eliminó, False si no existe
        """
        cliente = self.buscar_cliente_por_id(id_cliente)
        if cliente:
            self.clientes.remove(cliente)
            return True
        return False
    
    # ========== MÉTODOS DE INFORMACIÓN ==========
    
    def obtener_estadisticas(self):
        """
        Retorna estadísticas del restaurante.
        
        Returns:
            dict: Diccionario con información del restaurante
        """
        total_productos = len(self.productos)
        productos_disponibles = len(self.obtener_productos_disponibles())
        
        return {
            "nombre": self.nombre_restaurante,
            "total_productos": total_productos,
            "productos_disponibles": productos_disponibles,
            "total_clientes": len(self.clientes),
            "precio_promedio": (
                sum(p.precio for p in self.productos) / total_productos 
                if total_productos > 0 else 0
            )
        }
