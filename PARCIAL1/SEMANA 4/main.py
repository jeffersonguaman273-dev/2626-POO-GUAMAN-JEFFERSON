# =====================================================================
# SISTEMA DE GESTIÓN DE RESTAURANTE
# =====================================================================
# Punto de entrada principal del programa
# Demuestra el uso completo del sistema de gestión del restaurante
# =====================================================================

# Importaciones: traer las clases desde los módulos
from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def main():
    """
    Función principal que ejecuta la demostración del sistema.
    Crea instancias de objetos y muestra el funcionamiento del sistema.
    """

    print("\n" + "="*70)
    print("BIENVENIDO AL SISTEMA DE GESTIÓN DEL RESTAURANTE".center(70))
    print("="*70)

    # ====== PASO 1: Crear instancia del Restaurante ======
    print("\n[1] Creando el restaurante...")
    restaurante = Restaurante("La Delicia Epicúrea", "Calle Principal #123, Centro")
    print(f"✓ Restaurante creado: {restaurante.nombre}")
    print(f"  Ubicación: {restaurante.ubicacion}")

    # ====== PASO 2: Crear Productos ======
    print("\n[2] Agregando productos al catálogo...")

    # Crear instancias de Producto
    producto1 = Producto(1, "Pizza Margarita", 12.50, "Pizza tradicional con tomate, mozzarella y albahaca", "plato_principal")
    producto2 = Producto(2, "Hamburguesa Premium", 14.99, "Hamburguesa con carne de res, queso y vegetales", "plato_principal")
    producto3 = Producto(3, "Ensalada César", 9.99, "Ensalada fresca con aderezo César y crutones", "entrada")
    producto4 = Producto(4, "Refresco de Cola", 2.50, "Bebida refrescante en botella de 350ml", "bebida")
    producto5 = Producto(5, "Agua Mineral", 1.99, "Agua mineral sin gas", "bebida")
    producto6 = Producto(6, "Pastel de Chocolate", 6.99, "Delicioso pastel de chocolate casero", "postre", disponibilidad=True)
    producto7 = Producto(7, "Flan Tradicional", 5.50, "Flan casero con salsa de caramelo", "postre")

    # Agregar productos al restaurante
    productos = [producto1, producto2, producto3, producto4, producto5, producto6, producto7]
    for prod in productos:
        restaurante.agregar_producto(prod)

    # ====== PASO 3: Crear Clientes ======
    print("\n[3] Registrando clientes en el sistema...")

    # Crear instancias de Cliente
    cliente1 = Cliente(1, "Juan Pérez", "juan.perez@email.com", "0987654321")
    cliente2 = Cliente(2, "María García", "maria.garcia@email.com", "0912345678")
    cliente3 = Cliente(3, "Carlos López", "carlos.lopez@email.com", "0998765432")
    cliente4 = Cliente(4, "Ana Martínez", "ana.martinez@email.com", "0923456789")

    # Agregar clientes al restaurante
    clientes = [cliente1, cliente2, cliente3, cliente4]
    for cli in clientes:
        restaurante.agregar_cliente(cli)

    # ====== PASO 4: Demostrar funcionalidades ======
    print("\n[4] Demostrando funcionalidades del sistema...")

    # Listar productos
    restaurante.listar_productos()

    # Listar clientes
    restaurante.listar_clientes()

    # ====== PASO 5: Simular actividad de clientes ======
    print("\n[5] Registrando pedidos de clientes...")
    restaurante.registrar_pedido_cliente(1)
    restaurante.registrar_pedido_cliente(1)
    restaurante.registrar_pedido_cliente(2)
    restaurante.registrar_pedido_cliente(3)
    restaurante.registrar_pedido_cliente(3)
    restaurante.registrar_pedido_cliente(3)
    restaurante.registrar_pedido_cliente(4)

    # ====== PASO 6: Actualizar información ======
    print("\n[6] Actualizando información...")

    # Actualizar contacto de un cliente
    cliente = restaurante.obtener_cliente(1)
    if cliente:
        print(f"\nAntes: {cliente}")
        cliente.actualizar_contacto(email="juanperez.new@email.com", telefono="0999999999")
        print(f"Después: {cliente}")

    # Cambiar disponibilidad de un producto
    producto = restaurante.obtener_producto(6)
    if producto:
        print(f"\nProducto antes: {producto}")
        producto.cambiar_disponibilidad(False)
        print(f"Producto después: {producto}")

    # Actualizar precio de un producto
    producto = restaurante.obtener_producto(2)
    if producto:
        print(f"\nPrecio anterior de '{producto.nombre}': ${producto.precio:.2f}")
        producto.actualizar_precio(15.99)
        print(f"Precio nuevo de '{producto.nombre}': ${producto.precio:.2f}")

    # ====== PASO 7: Mostrar productos por categoría ======
    print("\n[7] Filtrando productos por categoría...")
    restaurante.listar_productos_por_tipo("plato_principal")
    restaurante.listar_productos_por_tipo("bebida")
    restaurante.listar_productos_por_tipo("postre")

    # ====== PASO 8: Mostrar información detallada ======
    print("\n[8] Información detallada de objetos...")

    print("\nInformación del primer cliente:")
    cliente_info = restaurante.obtener_cliente(1)
    if cliente_info:
        info_dict = cliente_info.obtener_informacion()
        for clave, valor in info_dict.items():
            print(f"  {clave}: {valor}")

    print("\nInformación del primer producto:")
    prod_info = restaurante.obtener_producto(1)
    if prod_info:
        info_dict = prod_info.obtener_informacion()
        for clave, valor in info_dict.items():
            print(f"  {clave}: {valor}")

    # ====== PASO 9: Mostrar estadísticas ======
    restaurante.obtener_estadisticas()

    # ====== PASO 10: Información final del restaurante ======
    print("\n[10] Resumen final del sistema:")
    print(f"\n{restaurante}")

    print("\n" + "="*70)
    print("FIN DE LA DEMOSTRACIÓN DEL SISTEMA".center(70))
    print("="*70 + "\n")


# Punto de entrada del programa
if __name__ == "__main__":
    main()


