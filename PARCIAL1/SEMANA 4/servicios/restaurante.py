# Módulo: restaurante.py
# Descripción: Define la clase Restaurante que gestiona productos y clientes

class Restaurante:
    """
    Clase que representa y gestiona el restaurante.
    Administra la lista de productos y clientes registrados en el sistema.
    
    Atributos:
        nombre (str): Nombre del restaurante
        ubicacion (str): Ubicación del restaurante
        productos (list): Lista de objetos Producto disponibles
        clientes (list): Lista de objetos Cliente registrados
    """
    
    def __init__(self, nombre, ubicacion):
        """
        Constructor de la clase Restaurante.
        
        Args:
            nombre (str): Nombre del restaurante
            ubicacion (str): Ubicación o dirección del restaurante
        """
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.productos = []
        self.clientes = []
    
    def __str__(self):
        """
        Retorna una representación en texto del restaurante.
        """
        return f"Restaurante: {self.nombre}\nUbicación: {self.ubicacion}\nProductos: {len(self.productos)} | Clientes: {len(self.clientes)}"
    
    # ======================== GESTIÓN DE PRODUCTOS ========================
    
    def agregar_producto(self, producto):
        """
        Agrega un nuevo producto al restaurante.
        Verifica que el producto no esté duplicado por ID.
        
        Args:
            producto (Producto): Objeto de la clase Producto a agregar
            
        Returns:
            bool: True si se agregó exitosamente, False si ya existe
        """
        # Verificar que el producto no esté duplicado
        for prod in self.productos:
            if prod.id == producto.id:
                print(f"Error: El producto con ID {producto.id} ya existe.")
                return False
        
        self.productos.append(producto)
        print(f"✓ Producto '{producto.nombre}' agregado exitosamente.")
        return True
    
    def eliminar_producto(self, id_producto):
        """
        Elimina un producto del restaurante por su ID.
        
        Args:
            id_producto (int): ID del producto a eliminar
            
        Returns:
            bool: True si se eliminó, False si no existe
        """
        for i, producto in enumerate(self.productos):
            if producto.id == id_producto:
                nombre = producto.nombre
                self.productos.pop(i)
                print(f"✓ Producto '{nombre}' eliminado exitosamente.")
                return True
        
        print(f"Error: Producto con ID {id_producto} no encontrado.")
        return False
    
    def obtener_producto(self, id_producto):
        """
        Busca y retorna un producto por su ID.
        
        Args:
            id_producto (int): ID del producto a buscar
            
        Returns:
            Producto: Objeto del producto si existe, None en caso contrario
        """
        for producto in self.productos:
            if producto.id == id_producto:
                return producto
        return None
    
    def listar_productos(self):
        """
        Muestra todos los productos registrados en el restaurante.
        """
        if not self.productos:
            print("\nNo hay productos registrados.")
            return
        
        print("\n" + "="*60)
        print("CATÁLOGO DE PRODUCTOS".center(60))
        print("="*60)
        for producto in self.productos:
            print(str(producto))
        print("="*60)
    
    def listar_productos_por_tipo(self, tipo):
        """
        Muestra los productos filtrados por tipo.
        
        Args:
            tipo (str): Tipo de producto a filtrar
        """
        productos_filtrados = [p for p in self.productos if p.tipo_producto == tipo]
        
        if not productos_filtrados:
            print(f"\nNo hay productos del tipo '{tipo}'.")
            return
        
        print(f"\n--- Productos: {tipo} ---")
        for producto in productos_filtrados:
            print(str(producto))
    
    # ======================== GESTIÓN DE CLIENTES ========================
    
    def agregar_cliente(self, cliente):
        """
        Agrega un nuevo cliente al restaurante.
        Verifica que el cliente no esté duplicado por ID.
        
        Args:
            cliente (Cliente): Objeto de la clase Cliente a agregar
            
        Returns:
            bool: True si se agregó exitosamente, False si ya existe
        """
        # Verificar que el cliente no esté duplicado
        for cli in self.clientes:
            if cli.id == cliente.id:
                print(f"Error: El cliente con ID {cliente.id} ya existe.")
                return False
        
        self.clientes.append(cliente)
        print(f"✓ Cliente '{cliente.nombre}' registrado exitosamente.")
        return True
    
    def eliminar_cliente(self, id_cliente):
        """
        Elimina un cliente del restaurante por su ID.
        
        Args:
            id_cliente (int): ID del cliente a eliminar
            
        Returns:
            bool: True si se eliminó, False si no existe
        """
        for i, cliente in enumerate(self.clientes):
            if cliente.id == id_cliente:
                nombre = cliente.nombre
                self.clientes.pop(i)
                print(f"✓ Cliente '{nombre}' eliminado del sistema.")
                return True
        
        print(f"Error: Cliente con ID {id_cliente} no encontrado.")
        return False
    
    def obtener_cliente(self, id_cliente):
        """
        Busca y retorna un cliente por su ID.
        
        Args:
            id_cliente (int): ID del cliente a buscar
            
        Returns:
            Cliente: Objeto del cliente si existe, None en caso contrario
        """
        for cliente in self.clientes:
            if cliente.id == id_cliente:
                return cliente
        return None
    
    def listar_clientes(self):
        """
        Muestra todos los clientes registrados en el restaurante.
        """
        if not self.clientes:
            print("\nNo hay clientes registrados.")
            return
        
        print("\n" + "="*70)
        print("BASE DE CLIENTES".center(70))
        print("="*70)
        for cliente in self.clientes:
            print(str(cliente))
        print("="*70)
    
    def registrar_pedido_cliente(self, id_cliente):
        """
        Registra un nuevo pedido para un cliente.
        
        Args:
            id_cliente (int): ID del cliente que realiza el pedido
            
        Returns:
            bool: True si se registró exitosamente, False si el cliente no existe
        """
        cliente = self.obtener_cliente(id_cliente)
        if cliente:
            cliente.registrar_pedido()
            print(f"✓ Pedido registrado para {cliente.nombre}. Total de pedidos: {cliente.numero_pedidos}")
            return True
        else:
            print(f"Error: Cliente con ID {id_cliente} no encontrado.")
            return False
    
    # ======================== ESTADÍSTICAS ========================
    
    def obtener_estadisticas(self):
        """
        Genera y muestra estadísticas generales del restaurante.
        """
        print("\n" + "="*60)
        print("ESTADÍSTICAS DEL RESTAURANTE".center(60))
        print("="*60)
        print(f"Total de productos: {len(self.productos)}")
        print(f"Total de clientes: {len(self.clientes)}")
        
        if self.clientes:
            total_pedidos = sum(cliente.numero_pedidos for cliente in self.clientes)
            print(f"Total de pedidos registrados: {total_pedidos}")
            if total_pedidos > 0:
                promedio_pedidos = total_pedidos / len(self.clientes)
                print(f"Promedio de pedidos por cliente: {promedio_pedidos:.2f}")
        
        productos_disponibles = sum(1 for p in self.productos if p.disponibilidad)
        print(f"Productos disponibles: {productos_disponibles}/{len(self.productos)}")
        
        if self.productos:
            precio_promedio = sum(p.precio for p in self.productos) / len(self.productos)
            print(f"Precio promedio de productos: ${precio_promedio:.2f}")
        
        print("="*60)


