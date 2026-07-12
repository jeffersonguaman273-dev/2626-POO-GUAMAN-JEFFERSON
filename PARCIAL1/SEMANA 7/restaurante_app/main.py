"""
Sistema de Gestión de Restaurante - SEMANA 7
Programa principal: menú interactivo para administrar productos y clientes.

Conceptos OOP demostrados:
- Constructores (__init__)
- Decoradores (@property, @setter)
- Decorador @dataclass
- Arquitectura modular (modelos, servicios)
- Encapsulación y validación
"""

from modelos import Producto, Cliente
from servicios import Restaurante


# ========== FUNCIONES DE UTILIDAD ==========

def limpiar_pantalla():
    """Limpia la pantalla de la consola."""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def mostrar_encabezado():
    """Muestra el encabezado principal del sistema."""
    print("=" * 50)
    print("        SISTEMA DE GESTIÓN DE RESTAURANTE")
    print("=" * 50)


def mostrar_menu_principal():
    """Muestra el menú principal interactivo."""
    print("\n" + "=" * 50)
    print("              MENÚ PRINCIPAL")
    print("=" * 50)
    print("\n🍽️  PRODUCTOS:")
    print("  1. Registrar producto")
    print("  2. Listar productos")
    print("  3. Buscar producto")
    print("  4. Ver productos disponibles")
    print("  5. Eliminar producto")
    
    print("\n👥 CLIENTES:")
    print("  6. Registrar cliente")
    print("  7. Listar clientes")
    print("  8. Buscar cliente")
    print("  9. Eliminar cliente")
    
    print("\n📊 INFORMACIÓN:")
    print("  10. Ver estadísticas del restaurante")
    
    print("\n" + "-" * 50)
    print("  0. Salir")
    print("=" * 50)


def obtener_opcion_valida(minimo=0, maximo=10):
    """
    Solicita una opción válida al usuario.
    
    Args:
        minimo (int): Valor mínimo permitido
        maximo (int): Valor máximo permitido
        
    Returns:
        int: Opción seleccionada
    """
    while True:
        try:
            opcion = int(input(f"\nSelecciona una opción [{minimo}-{maximo}]: "))
            if minimo <= opcion <= maximo:
                return opcion
            else:
                print(f"❌ Debes ingresar un número entre {minimo} y {maximo}")
        except ValueError:
            print("❌ Entrada inválida. Por favor, ingresa un número entero")


def pausar():
    """Pausa la ejecución hasta que el usuario presione Enter."""
    input("\n✓ Presiona Enter para continuar...")


# ========== FUNCIONES PARA PRODUCTOS ==========

def registrar_producto_interactivo(restaurante):
    """
    Interfaz interactiva para registrar un nuevo producto.
    Demuestra cómo datos de entrada se transforman en un objeto.
    """
    print("\n" + "-" * 50)
    print("📝 REGISTRAR NUEVO PRODUCTO")
    print("-" * 50)
    
    try:
        nombre = input("Nombre del producto: ").strip()
        categoria = input("Categoría (ej: Bebida, Plato Principal, Postre): ").strip()
        
        while True:
            try:
                precio = float(input("Precio ($): "))
                break
            except ValueError:
                print("❌ El precio debe ser un número válido")
        
        # CREAR OBJETO MEDIANTE CONSTRUCTOR
        nuevo_producto = Producto(nombre, categoria, precio)
        
        # REGISTRAR EN EL SERVICIO
        if restaurante.registrar_producto(nuevo_producto):
            print(f"\n✓ Producto registrado exitosamente!")
            print(f"  {nuevo_producto.mostrar_informacion()}")
        else:
            print(f"❌ El producto '{nombre}' ya existe en el sistema")
            
    except ValueError as e:
        print(f"❌ Error: {e}")
    
    pausar()


def listar_productos(restaurante):
    """Muestra la lista completa de productos."""
    print("\n" + "-" * 50)
    print("📋 LISTA DE PRODUCTOS")
    print("-" * 50)
    
    productos = restaurante.listar_productos()
    
    if not productos:
        print("⚠️  No hay productos registrados aún")
    else:
        for idx, producto in enumerate(productos, 1):
            print(f"\n{idx}. {producto}")
            print(f"   Categoría: {producto.categoria} | Disponible: {'✓' if producto.disponible else '✗'}")
    
    pausar()


def buscar_producto(restaurante):
    """Búsqueda interactiva de productos."""
    print("\n" + "-" * 50)
    print("🔍 BUSCAR PRODUCTO")
    print("-" * 50)
    
    nombre = input("Ingresa el nombre del producto a buscar: ").strip()
    producto = restaurante.buscar_producto_por_nombre(nombre)
    
    if producto:
        print(f"\n✓ Producto encontrado:")
        print(f"\n{producto.mostrar_informacion()}")
    else:
        print(f"\n❌ No se encontró el producto '{nombre}'")
    
    pausar()


def ver_productos_disponibles(restaurante):
    """Muestra solo los productos disponibles."""
    print("\n" + "-" * 50)
    print("✓ PRODUCTOS DISPONIBLES")
    print("-" * 50)
    
    disponibles = restaurante.obtener_productos_disponibles()
    
    if not disponibles:
        print("⚠️  No hay productos disponibles en este momento")
    else:
        for idx, producto in enumerate(disponibles, 1):
            print(f"\n{idx}. {producto}")
            print(f"   Categoría: {producto.categoria}")
    
    pausar()


def eliminar_producto(restaurante):
    """Elimina un producto del sistema."""
    print("\n" + "-" * 50)
    print("🗑️  ELIMINAR PRODUCTO")
    print("-" * 50)
    
    nombre = input("Nombre del producto a eliminar: ").strip()
    
    if restaurante.eliminar_producto(nombre):
        print(f"\n✓ Producto '{nombre}' eliminado exitosamente")
    else:
        print(f"\n❌ No se encontró el producto '{nombre}'")
    
    pausar()


# ========== FUNCIONES PARA CLIENTES ==========

def registrar_cliente_interactivo(restaurante):
    """
    Interfaz interactiva para registrar un nuevo cliente.
    Utiliza @dataclass para crear el objeto.
    """
    print("\n" + "-" * 50)
    print("👤 REGISTRAR NUEVO CLIENTE")
    print("-" * 50)
    
    try:
        nombre = input("Nombre completo: ").strip()
        correo = input("Correo electrónico: ").strip()
        id_cliente = input("ID único del cliente (ej: CLI001): ").strip()
        
        # CREAR OBJETO MEDIANTE @dataclass
        nuevo_cliente = Cliente(nombre, correo, id_cliente)
        
        # REGISTRAR EN EL SERVICIO
        if restaurante.registrar_cliente(nuevo_cliente):
            print(f"\n✓ Cliente registrado exitosamente!")
            print(f"  {nuevo_cliente.mostrar_informacion()}")
        else:
            print(f"❌ El ID '{id_cliente}' ya existe en el sistema")
            
    except ValueError as e:
        print(f"❌ Error: {e}")
    
    pausar()


def listar_clientes(restaurante):
    """Muestra la lista completa de clientes."""
    print("\n" + "-" * 50)
    print("📋 LISTA DE CLIENTES")
    print("-" * 50)
    
    clientes = restaurante.listar_clientes()
    
    if not clientes:
        print("⚠️  No hay clientes registrados aún")
    else:
        for idx, cliente in enumerate(clientes, 1):
            print(f"\n{idx}. {cliente}")
    
    pausar()


def buscar_cliente(restaurante):
    """Búsqueda interactiva de clientes."""
    print("\n" + "-" * 50)
    print("🔍 BUSCAR CLIENTE")
    print("-" * 50)
    print("\nOpciones de búsqueda:")
    print("  1. Por ID")
    print("  2. Por nombre")
    print("  3. Por correo")
    
    opcion = obtener_opcion_valida(1, 3)
    
    if opcion == 1:
        id_cliente = input("Ingresa el ID: ").strip()
        cliente = restaurante.buscar_cliente_por_id(id_cliente)
        if cliente:
            print(f"\n✓ Cliente encontrado:")
            print(f"\n{cliente.mostrar_informacion()}")
        else:
            print(f"\n❌ No se encontró cliente con ID '{id_cliente}'")
            
    elif opcion == 2:
        nombre = input("Ingresa el nombre: ").strip()
        clientes = restaurante.buscar_cliente_por_nombre(nombre)
        if clientes:
            print(f"\n✓ Se encontraron {len(clientes)} cliente(s):")
            for cliente in clientes:
                print(f"  - {cliente}")
        else:
            print(f"\n❌ No se encontraron clientes con nombre '{nombre}'")
            
    elif opcion == 3:
        correo = input("Ingresa el correo: ").strip()
        cliente = restaurante.buscar_cliente_por_correo(correo)
        if cliente:
            print(f"\n✓ Cliente encontrado:")
            print(f"\n{cliente.mostrar_informacion()}")
        else:
            print(f"\n❌ No se encontró cliente con correo '{correo}'")
    
    pausar()


def eliminar_cliente(restaurante):
    """Elimina un cliente del sistema."""
    print("\n" + "-" * 50)
    print("🗑️  ELIMINAR CLIENTE")
    print("-" * 50)
    
    id_cliente = input("ID del cliente a eliminar: ").strip()
    
    if restaurante.eliminar_cliente(id_cliente):
        print(f"\n✓ Cliente con ID '{id_cliente}' eliminado exitosamente")
    else:
        print(f"\n❌ No se encontró cliente con ID '{id_cliente}'")
    
    pausar()


def mostrar_estadisticas(restaurante):
    """Muestra estadísticas del restaurante."""
    print("\n" + "-" * 50)
    print("📊 ESTADÍSTICAS DEL RESTAURANTE")
    print("-" * 50)
    
    stats = restaurante.obtener_estadisticas()
    
    print(f"\n🏪 Nombre: {stats['nombre']}")
    print(f"📦 Total de productos: {stats['total_productos']}")
    print(f"✓ Productos disponibles: {stats['productos_disponibles']}")
    print(f"💰 Precio promedio: ${stats['precio_promedio']:.2f}")
    print(f"👥 Total de clientes: {stats['total_clientes']}")
    
    pausar()


# ========== INICIALIZACIÓN CON DATOS DE EJEMPLO ==========

def cargar_datos_ejemplo(restaurante):
    """
    Carga datos de ejemplo al restaurante para propósitos didácticos.
    Demuestra cómo el sistema funciona con datos previos.
    """
    print("\n📦 Cargando datos de ejemplo...")
    
    # Productos de ejemplo
    productos_ejemplo = [
        Producto("Hamburguesa Clásica", "Platos Principales", 12.99),
        Producto("Pizza Margherita", "Platos Principales", 14.50),
        Producto("Ensalada César", "Ensaladas", 8.99),
        Producto("Pasta Alfredo", "Platos Principales", 13.99),
        Producto("Café Espresso", "Bebidas", 3.50),
        Producto("Jugo Natural", "Bebidas", 5.99),
        Producto("Postre de Chocolate", "Postres", 7.99),
        Producto("Helado de Vainilla", "Postres", 4.99),
    ]
    
    for producto in productos_ejemplo:
        restaurante.registrar_producto(producto)
    
    # Clientes de ejemplo
    clientes_ejemplo = [
        Cliente("Juan García", "juan.garcia@email.com", "CLI001"),
        Cliente("María López", "maria.lopez@email.com", "CLI002"),
        Cliente("Carlos Martínez", "carlos.martinez@email.com", "CLI003"),
        Cliente("Ana Rodríguez", "ana.rodriguez@email.com", "CLI004"),
    ]
    
    for cliente in clientes_ejemplo:
        restaurante.registrar_cliente(cliente)
    
    print("✓ Datos de ejemplo cargados exitosamente")


# ========== PROGRAMA PRINCIPAL ==========

def main():
    """Función principal que ejecuta el programa."""
    
    # Crear instancia del restaurante (SERVICIO PRINCIPAL)
    restaurante = Restaurante("El Buen Sabor")
    
    # Cargar datos de ejemplo
    cargar_datos_ejemplo(restaurante)
    
    while True:
        limpiar_pantalla()
        mostrar_encabezado()
        
        # Mostrar estadísticas rápidas
        stats = restaurante.obtener_estadisticas()
        print(f"\n📊 {stats['total_productos']} productos | 👥 {stats['total_clientes']} clientes")
        
        mostrar_menu_principal()
        opcion = obtener_opcion_valida(0, 10)
        
        if opcion == 0:
            print("\n👋 ¡Gracias por usar el Sistema de Restaurante!")
            print("Desarrollado con POO y Python - SEMANA 7\n")
            break
        
        # PRODUCTOS
        elif opcion == 1:
            registrar_producto_interactivo(restaurante)
        elif opcion == 2:
            listar_productos(restaurante)
        elif opcion == 3:
            buscar_producto(restaurante)
        elif opcion == 4:
            ver_productos_disponibles(restaurante)
        elif opcion == 5:
            eliminar_producto(restaurante)
        
        # CLIENTES
        elif opcion == 6:
            registrar_cliente_interactivo(restaurante)
        elif opcion == 7:
            listar_clientes(restaurante)
        elif opcion == 8:
            buscar_cliente(restaurante)
        elif opcion == 9:
            eliminar_cliente(restaurante)
        
        # INFORMACIÓN
        elif opcion == 10:
            mostrar_estadisticas(restaurante)


if __name__ == "__main__":
    main()
