# Punto de arranque del sistema de gestión de restaurante
# Importamos las clases necesarias desde los módulos

from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def main():
    """Función principal que demuestra el funcionamiento del sistema."""
    
    # Crear una instancia del restaurante
    restaurante = Restaurante(nombre="Delicias del Sabor")
    
    # ============ Crear productos ============
    print("=" * 60)
    print("CREANDO PRODUCTOS DEL RESTAURANTE")
    print("=" * 60)
    
    # Primer producto
    producto_1 = Producto(
        id=1,
        nombre="Ensalada César",
        descripcion="Ensalada fresca con aderezo César casero",
        precio=8.50,
        disponible=True,
        categoria="Ensaladas"
    )
    
    # Segundo producto
    producto_2 = Producto(
        id=2,
        nombre="Filete de Res",
        descripcion="Filete a la parrilla con verduras asadas",
        precio=18.99,
        disponible=True,
        categoria="Platos Principales"
    )
    
    # Tercer producto
    producto_3 = Producto(
        id=3,
        nombre="Jugo Natural de Naranja",
        descripcion="Jugo natural recién exprimido",
        precio=3.50,
        disponible=True,
        categoria="Bebidas"
    )
    
    # Cuarto producto
    producto_4 = Producto(
        id=4,
        nombre="Brownie de Chocolate",
        descripcion="Postre de chocolate casero con nueces",
        precio=5.75,
        disponible=False,
        categoria="Postres"
    )
    
    print(f"\nProducto 1: {producto_1}")
    print(f"Producto 2: {producto_2}")
    print(f"Producto 3: {producto_3}")
    print(f"Producto 4: {producto_4}")
    
    # Agregar productos al restaurante
    restaurante.agregar_producto(producto_1)
    restaurante.agregar_producto(producto_2)
    restaurante.agregar_producto(producto_3)
    restaurante.agregar_producto(producto_4)
    
    # ============ Crear clientes ============
    print("\n" + "=" * 60)
    print("CREANDO CLIENTES DEL RESTAURANTE")
    print("=" * 60)
    
    # Primer cliente
    cliente_1 = Cliente(
        id=101,
        nombre="María López",
        email="maria.lopez@email.com",
        telefono="555-1234",
        es_miembro=True
    )
    
    # Segundo cliente
    cliente_2 = Cliente(
        id=102,
        nombre="Carlos García",
        email="carlos.garcia@email.com",
        telefono="555-5678",
        es_miembro=False
    )
    
    # Tercer cliente
    cliente_3 = Cliente(
        id=103,
        nombre="Ana Martínez",
        email="ana.martinez@email.com",
        telefono="555-9012",
        es_miembro=True
    )
    
    # Cuarto cliente
    cliente_4 = Cliente(
        id=104,
        nombre="Roberto Rodríguez",
        email="roberto.rodriguez@email.com",
        telefono="555-3456",
        es_miembro=False
    )
    
    print(f"\nCliente 1: {cliente_1}")
    print(f"Cliente 2: {cliente_2}")
    print(f"Cliente 3: {cliente_3}")
    print(f"Cliente 4: {cliente_4}")
    
    # Agregar clientes al restaurante
    restaurante.agregar_cliente(cliente_1)
    restaurante.agregar_cliente(cliente_2)
    restaurante.agregar_cliente(cliente_3)
    restaurante.agregar_cliente(cliente_4)
    
    # Registrar algunos pedidos de los clientes
    cliente_1.agregar_pedido("Ensalada César")
    cliente_1.agregar_pedido("Filete de Res")
    cliente_2.agregar_pedido("Jugo Natural de Naranja")
    cliente_3.agregar_pedido("Brownie de Chocolate")
    
    # ============ Mostrar información del restaurante ============
    print("\n" + "=" * 60)
    print("INFORMACIÓN COMPLETA DEL RESTAURANTE")
    print("=" * 60)
    restaurante.mostrar_informacion()


if __name__ == "__main__":
    main()

