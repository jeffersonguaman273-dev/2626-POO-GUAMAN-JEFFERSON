"""
ejemplo_uso.py
Ejemplos de cómo usar el sistema de restaurante sin el menú interactivo.
Útil para entender el API del sistema.
"""

from modelos import Producto, Cliente
from servicios import Restaurante


def ejemplo_1_crear_objetos():
    """Ejemplo 1: Crear objetos usando constructores"""
    print("\n" + "="*60)
    print("EJEMPLO 1: Crear objetos usando constructores")
    print("="*60)
    
    # CREAR OBJETO PRODUCTO
    print("\n1. Creando objeto Producto...")
    try:
        hamburguesa = Producto("Hamburguesa", "Platos Principales", 12.99)
        print(f"✓ Producto creado: {hamburguesa}")
        print(f"  Detalles:\n{hamburguesa.mostrar_informacion()}")
    except ValueError as e:
        print(f"❌ Error: {e}")
    
    # INTENTAR CREAR PRODUCTO CON DATOS INVÁLIDOS
    print("\n2. Intentando crear producto con precio negativo...")
    try:
        producto_invalido = Producto("Pizza", "Platos", -50)
    except ValueError as e:
        print(f"❌ Validación capturada: {e}")
    
    # CREAR OBJETO CLIENTE
    print("\n3. Creando objeto Cliente (@dataclass)...")
    try:
        cliente1 = Cliente("Juan García", "juan@email.com", "CLI001")
        print(f"✓ Cliente creado: {cliente1}")
        print(f"  Detalles:\n{cliente1.mostrar_informacion()}")
    except ValueError as e:
        print(f"❌ Error: {e}")


def ejemplo_2_usar_property_setter():
    """Ejemplo 2: Usar @property y @setter para modificar objetos"""
    print("\n" + "="*60)
    print("EJEMPLO 2: Usar @property y @setter")
    print("="*60)
    
    # Crear producto
    pizza = Producto("Pizza Margherita", "Platos", 14.50)
    print(f"\nProducto inicial: {pizza}")
    print(f"  Precio: ${pizza.precio}")
    print(f"  Disponible: {pizza.disponible}")
    
    # USAR PROPERTY PARA LEER
    print(f"\n1. Leyendo atributos con @property:")
    print(f"   Nombre: {pizza.nombre}")
    print(f"   Categoría: {pizza.categoria}")
    print(f"   Precio: ${pizza.precio:.2f}")
    
    # USAR SETTER PARA ESCRIBIR (con validación)
    print(f"\n2. Modificando precio con @setter:")
    print(f"   Precio anterior: ${pizza.precio}")
    pizza.precio = 16.99
    print(f"   Precio nuevo: ${pizza.precio}")
    
    print(f"\n3. Modificando disponibilidad:")
    print(f"   Disponible antes: {pizza.disponible}")
    pizza.disponible = False
    print(f"   Disponible después: {pizza.disponible}")
    
    print(f"\n4. Intentando asignar precio inválido:")
    try:
        pizza.precio = -10
    except ValueError as e:
        print(f"   ❌ Validación: {e}")


def ejemplo_3_servicio_crud():
    """Ejemplo 3: Usar el servicio Restaurante para CRUD"""
    print("\n" + "="*60)
    print("EJEMPLO 3: Operaciones CRUD en el servicio")
    print("="*60)
    
    # Crear instancia del servicio
    restaurante = Restaurante("Mi Restaurante")
    
    # CREATE: Registrar productos
    print("\n1. CREATE: Registrando productos...")
    productos = [
        Producto("Hamburguesa", "Platos", 12.99),
        Producto("Pizza", "Platos", 14.50),
        Producto("Ensalada", "Ensaladas", 8.99),
        Producto("Café", "Bebidas", 3.50),
    ]
    
    for prod in productos:
        if restaurante.registrar_producto(prod):
            print(f"   ✓ {prod.nombre} registrado")
        else:
            print(f"   ❌ {prod.nombre} ya existe")
    
    # READ: Listar todos
    print(f"\n2. READ: Listando todos los productos:")
    for idx, prod in enumerate(restaurante.listar_productos(), 1):
        print(f"   {idx}. {prod}")
    
    # READ: Buscar específico
    print(f"\n3. READ: Buscando producto específico...")
    pizza = restaurante.buscar_producto_por_nombre("Pizza")
    if pizza:
        print(f"   ✓ Encontrado: {pizza}")
        print(f"      {pizza.mostrar_informacion()}")
    
    # UPDATE: Actualizar
    print(f"\n4. UPDATE: Actualizando precio de Hamburguesa...")
    if restaurante.actualizar_producto("Hamburguesa", precio_nuevo=15.99):
        hamburguesa = restaurante.buscar_producto_por_nombre("Hamburguesa")
        print(f"   ✓ Nuevo precio: ${hamburguesa.precio}")
    
    # DELETE: Eliminar
    print(f"\n5. DELETE: Eliminando Ensalada...")
    if restaurante.eliminar_producto("Ensalada"):
        print(f"   ✓ Ensalada eliminada")
    
    # READ: Verificar cambios
    print(f"\n6. Verificación final - Total de productos: {len(restaurante.listar_productos())}")


def ejemplo_4_busquedas_avanzadas():
    """Ejemplo 4: Búsquedas avanzadas"""
    print("\n" + "="*60)
    print("EJEMPLO 4: Búsquedas avanzadas")
    print("="*60)
    
    restaurante = Restaurante("Restaurante Ejemplo")
    
    # Cargar productos
    productos = [
        Producto("Hamburguesa Clásica", "Platos Principales", 12.99),
        Producto("Hamburguesa Doble", "Platos Principales", 15.99),
        Producto("Ensalada César", "Ensaladas", 8.99),
        Producto("Pasta Alfredo", "Platos Principales", 13.99),
        Producto("Café Espresso", "Bebidas", 3.50),
    ]
    
    for prod in productos:
        restaurante.registrar_producto(prod)
    
    # Búsqueda por categoría
    print("\n1. Búsqueda por categoría 'Platos Principales':")
    platos = restaurante.buscar_productos_por_categoria("Platos Principales")
    for plato in platos:
        print(f"   - {plato} (${plato.precio})")
    
    # Productos disponibles
    print("\n2. Productos disponibles:")
    disponibles = restaurante.obtener_productos_disponibles()
    print(f"   Total: {len(disponibles)}")
    for prod in disponibles:
        print(f"   - {prod}")
    
    # Búsqueda insensible a mayúsculas
    print("\n3. Búsqueda insensible a mayúsculas:")
    busqueda = restaurante.buscar_producto_por_nombre("café espresso")
    if busqueda:
        print(f"   ✓ Encontrado: {busqueda}")


def ejemplo_5_clientes():
    """Ejemplo 5: Trabajar con clientes"""
    print("\n" + "="*60)
    print("EJEMPLO 5: Trabajar con clientes")
    print("="*60)
    
    restaurante = Restaurante("Restaurante Ejemplo")
    
    # Crear clientes
    print("\n1. Creando clientes:")
    clientes = [
        Cliente("Juan García", "juan@email.com", "CLI001"),
        Cliente("María López", "maria@email.com", "CLI002"),
        Cliente("Carlos Martínez", "carlos@email.com", "CLI003"),
    ]
    
    for cliente in clientes:
        if restaurante.registrar_cliente(cliente):
            print(f"   ✓ {cliente.nombre} registrado")
    
    # Listar clientes
    print(f"\n2. Listando todos los clientes:")
    for cliente in restaurante.listar_clientes():
        print(f"   - {cliente}")
    
    # Buscar por ID
    print(f"\n3. Buscar cliente por ID 'CLI001':")
    cliente = restaurante.buscar_cliente_por_id("CLI001")
    if cliente:
        print(f"   ✓ Encontrado:\n{cliente.mostrar_informacion()}")
    
    # Buscar por nombre
    print(f"\n4. Buscar clientes por nombre que contenga 'María':")
    encontrados = restaurante.buscar_cliente_por_nombre("María")
    for cliente in encontrados:
        print(f"   - {cliente}")
    
    # Buscar por correo
    print(f"\n5. Buscar cliente por correo 'carlos@email.com':")
    cliente = restaurante.buscar_cliente_por_correo("carlos@email.com")
    if cliente:
        print(f"   ✓ {cliente.nombre} (ID: {cliente.id_cliente})")


def ejemplo_6_estadisticas():
    """Ejemplo 6: Obtener estadísticas"""
    print("\n" + "="*60)
    print("EJEMPLO 6: Estadísticas del restaurante")
    print("="*60)
    
    restaurante = Restaurante("El Buen Sabor")
    
    # Agregar datos
    productos = [
        Producto("Hamburguesa", "Platos", 12.99),
        Producto("Pizza", "Platos", 14.50),
        Producto("Ensalada", "Ensaladas", 8.99),
        Producto("Café", "Bebidas", 3.50),
        Producto("Postre", "Postres", 7.99),
    ]
    
    for prod in productos:
        restaurante.registrar_producto(prod)
    
    clientes_data = [
        Cliente("Juan", "juan@email.com", "CLI001"),
        Cliente("María", "maria@email.com", "CLI002"),
        Cliente("Carlos", "carlos@email.com", "CLI003"),
    ]
    
    for cliente in clientes_data:
        restaurante.registrar_cliente(cliente)
    
    # Obtener estadísticas
    stats = restaurante.obtener_estadisticas()
    
    print(f"\n📊 ESTADÍSTICAS DE: {stats['nombre']}")
    print(f"   - Total de productos: {stats['total_productos']}")
    print(f"   - Productos disponibles: {stats['productos_disponibles']}")
    print(f"   - Precio promedio: ${stats['precio_promedio']:.2f}")
    print(f"   - Total de clientes: {stats['total_clientes']}")


def ejemplo_7_validaciones():
    """Ejemplo 7: Demostrar validaciones"""
    print("\n" + "="*60)
    print("EJEMPLO 7: Validaciones en acción")
    print("="*60)
    
    print("\n1. Validar nombre no vacío:")
    try:
        Producto("", "Platos", 10.00)
    except ValueError as e:
        print(f"   ❌ {e}")
    
    print("\n2. Validar categoría no vacía:")
    try:
        Producto("Pizza", "", 10.00)
    except ValueError as e:
        print(f"   ❌ {e}")
    
    print("\n3. Validar precio > 0:")
    try:
        Producto("Pizza", "Platos", 0)
    except ValueError as e:
        print(f"   ❌ {e}")
    
    print("\n4. Validar precio es número:")
    try:
        Producto("Pizza", "Platos", "abc")
    except ValueError as e:
        print(f"   ❌ {e}")
    
    print("\n5. Validar cliente completo:")
    try:
        Cliente("", "correo@email.com", "CLI001")
    except ValueError as e:
        print(f"   ❌ {e}")


def main():
    """Ejecuta todos los ejemplos"""
    print("\n" + "🍽️  EJEMPLOS DE USO: SISTEMA DE RESTAURANTE")
    
    ejemplo_1_crear_objetos()
    ejemplo_2_usar_property_setter()
    ejemplo_3_servicio_crud()
    ejemplo_4_busquedas_avanzadas()
    ejemplo_5_clientes()
    ejemplo_6_estadisticas()
    ejemplo_7_validaciones()
    
    print("\n" + "="*60)
    print("✓ Todos los ejemplos ejecutados exitosamente")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
