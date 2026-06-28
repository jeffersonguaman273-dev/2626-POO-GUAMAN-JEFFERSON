# Clase Restaurante: Centro administrador de productos y clientes
# Responsable de gestionar listas de productos y clientes del restaurante


from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    """
    Clase que gestiona el sistema del restaurante.

    Administra listas de productos y clientes, permitiendo operaciones
    de búsqueda, registro y visualización de información.

    Atributos:
        nombre (str): Nombre del restaurante
        productos (list): Lista de productos disponibles en el restaurante
        clientes (list): Lista de clientes registrados en el restaurante
    """

    def __init__(self, nombre: str):
        """
        Constructor que inicializa el restaurante.

        Args:
            nombre: Nombre descriptivo del restaurante
        """
        self.nombre: str = nombre
        self.productos: list = []  # Lista para almacenar productos
        self.clientes: list = []   # Lista para almacenar clientes

    def agregar_producto(self, producto: Producto) -> None:
        """
        Agrega un nuevo producto al catálogo del restaurante.

        Args:
            producto: Objeto de tipo Producto a agregar
        """
        self.productos.append(producto)
        print(f"✓ Producto agregado: {producto.nombre}")

    def agregar_cliente(self, cliente: Cliente) -> None:
        """
        Registra un nuevo cliente en el sistema del restaurante.

        Args:
            cliente: Objeto de tipo Cliente a registrar
        """
        self.clientes.append(cliente)
        print(f"✓ Cliente registrado: {cliente.nombre}")

    def buscar_producto_por_id(self, id_producto: int) -> Producto or None:
        """
        Busca un producto por su identificador.

        Args:
            id_producto: Identificador del producto a buscar

        Returns:
            Producto encontrado o None si no existe
        """
        for producto in self.productos:
            if producto.id == id_producto:
                return producto
        return None

    def buscar_cliente_por_id(self, id_cliente: int) -> Cliente or None:
        """
        Busca un cliente por su identificador.

        Args:
            id_cliente: Identificador del cliente a buscar

        Returns:
            Cliente encontrado o None si no existe
        """
        for cliente in self.clientes:
            if cliente.id == id_cliente:
                return cliente
        return None

    def buscar_productos_por_categoria(self, categoria: str) -> list:
        """
        Busca todos los productos de una categoría específica.

        Args:
            categoria: Nombre de la categoría a buscar

        Returns:
            Lista de productos que pertenecen a la categoría
        """
        productos_filtrados = [p for p in self.productos if p.categoria == categoria]
        return productos_filtrados

    def obtener_productos_disponibles(self) -> list:
        """
        Obtiene todos los productos disponibles para la venta.

        Returns:
            Lista de productos disponibles
        """
        productos_disponibles = [p for p in self.productos if p.disponible]
        return productos_disponibles

    def obtener_clientes_miembros(self) -> list:
        """
        Obtiene todos los clientes que son miembros del programa de lealtad.

        Returns:
            Lista de clientes miembros
        """
        clientes_miembros = [c for c in self.clientes if c.es_miembro]
        return clientes_miembros

    def calcular_promedio_precios(self) -> float:
        """
        Calcula el precio promedio de todos los productos.

        Returns:
            Promedio de precios en formato decimal
        """
        if not self.productos:
            return 0.0

        suma_precios = sum(p.precio for p in self.productos)
        promedio = suma_precios / len(self.productos)
        return round(promedio, 2)

    def mostrar_informacion(self) -> None:
        """
        Muestra toda la información registrada en el restaurante
        de forma organizada en la consola.
        """
        print("\n" + "=" * 70)
        print(f"RESTAURANTE: {self.nombre.upper()}")
        print("=" * 70)

        # Mostrar información de productos
        print(f"\n📋 PRODUCTOS ({len(self.productos)} total)")
        print("-" * 70)
        if self.productos:
            for producto in self.productos:
                print(f"  {producto}")

            print(f"\n  Promedio de precios: ${self.calcular_promedio_precios():.2f}")

            # Mostrar productos por categoría
            categorias = set(p.categoria for p in self.productos)
            print(f"\n  Categorías disponibles:")
            for categoria in categorias:
                productos_cat = self.buscar_productos_por_categoria(categoria)
                print(f"    • {categoria}: {len(productos_cat)} producto(s)")
        else:
            print("  No hay productos registrados")

        # Mostrar información de clientes
        print(f"\n👥 CLIENTES ({len(self.clientes)} total)")
        print("-" * 70)
        if self.clientes:
            for cliente in self.clientes:
                print(f"  {cliente}")

            # Mostrar estadísticas de clientes
            miembros = self.obtener_clientes_miembros()
            cliente_mas_activo = max(self.clientes, key=lambda c: c.obtener_total_pedidos())

            print(f"\n  Clientes miembros: {len(miembros)}")
            print(f"  Cliente con más pedidos: {cliente_mas_activo.nombre} "
                  f"({cliente_mas_activo.obtener_total_pedidos()} pedidos)")
        else:
            print("  No hay clientes registrados")

        print("\n" + "=" * 70)

    def mostrar_detalles_completos(self) -> None:
        """
        Muestra información detallada de todos los productos y clientes.
        """
        print("\n" + "=" * 70)
        print(f"DETALLES COMPLETOS - {self.nombre.upper()}")
        print("=" * 70)

        # Detalles de productos
        print("\n📦 DETALLES DE PRODUCTOS")
        print("-" * 70)
        if self.productos:
            for producto in self.productos:
                print(f"\n{producto.obtener_detalles()}")
        else:
            print("No hay productos registrados")

        # Detalles de clientes
        print("\n\n👤 DETALLES DE CLIENTES")
        print("-" * 70)
        if self.clientes:
            for cliente in self.clientes:
                print(f"\n{cliente.obtener_detalles()}")
        else:
            print("No hay clientes registrados")

        print("\n" + "=" * 70)

