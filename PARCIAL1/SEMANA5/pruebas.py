# Script de prueba: Demuestra funcionalidades avanzadas del sistema

from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def prueba_funcionalidades():
    """Ejecuta pruebas de funcionalidades avanzadas del sistema."""

    # Crear restaurante
    restaurante = Restaurante(nombre="La Buena Mesa")

    # Crear productos
    pizza = Producto(
        id=1, nombre="Pizza Margarita", descripcion="Pizza tradicional con queso y tomate",
        precio=12.99, disponible=True, categoria="Pizzas"
    )

    burguesa = Producto(
        id=2, nombre="Hamburguesa Premium", descripcion="Hamburguesa con carne de calidad",
        precio=9.99, disponible=True, categoria="Sándwiches"
    )

    pasta = Producto(
        id=3, nombre="Pasta Alfredo", descripcion="Pasta cremosa con salsa Alfredo",
        precio=11.50, disponible=False, categoria="Platos Principales"
    )

    refresco = Producto(
        id=4, nombre="Refresco Cola", descripcion="Bebida refrescante",
        precio=2.50, disponible=True, categoria="Bebidas"
    )

    restaurante.agregar_producto(pizza)
    restaurante.agregar_producto(burguesa)
    restaurante.agregar_producto(pasta)
    restaurante.agregar_producto(refresco)

    # Crear clientes
    cliente_vip = Cliente(
        id=201, nombre="Juan Pérez", email="juan@email.com",
        telefono="555-0001", es_miembro=True
    )

    cliente_regular = Cliente(
        id=202, nombre="Laura Sánchez", email="laura@email.com",
        telefono="555-0002", es_miembro=False
    )

    restaurante.agregar_cliente(cliente_vip)
    restaurante.agregar_cliente(cliente_regular)

    # Pruebas de funcionalidades
    print("\n" + "=" * 70)
    print("PRUEBAS DE FUNCIONALIDADES AVANZADAS")
    print("=" * 70)

    # Prueba 1: Búsqueda de producto por ID
    print("\n1️⃣ BUSCAR PRODUCTO POR ID")
    print("-" * 70)
    producto_encontrado = restaurante.buscar_producto_por_id(1)
    if producto_encontrado:
        print(f"Producto encontrado: {producto_encontrado}\n")
        print(f"Detalles:\n{producto_encontrado.obtener_detalles()}")
    else:
        print("Producto no encontrado")

    # Prueba 2: Productos disponibles
    print("\n\n2️⃣ PRODUCTOS DISPONIBLES")
    print("-" * 70)
    disponibles = restaurante.obtener_productos_disponibles()
    print(f"Total de productos disponibles: {len(disponibles)}")
    for prod in disponibles:
        print(f"  • {prod}")

    # Prueba 3: Productos por categoría
    print("\n\n3️⃣ BÚSQUEDA POR CATEGORÍA")
    print("-" * 70)
    categoria_buscar = "Platos Principales"
    productos_categoria = restaurante.buscar_productos_por_categoria(categoria_buscar)
    print(f"Productos en '{categoria_buscar}':")
    if productos_categoria:
        for prod in productos_categoria:
            print(f"  • {prod}")
    else:
        print(f"  No hay productos en esta categoría")

    # Prueba 4: Cálculo de descuentos
    print("\n\n4️⃣ APLICAR DESCUENTOS")
    print("-" * 70)
    print(f"Pizza Margarita - Precio original: ${pizza.precio:.2f}")
    precio_con_descuento = pizza.aplicar_descuento(15)
    print(f"Pizza Margarita - Precio con 15% descuento: ${precio_con_descuento:.2f}")
    ahorro = pizza.precio - precio_con_descuento
    print(f"Ahorro: ${ahorro:.2f}")

    # Prueba 5: Clientes y sus pedidos
    print("\n\n5️⃣ GESTIÓN DE PEDIDOS DE CLIENTES")
    print("-" * 70)
    cliente_vip.agregar_pedido("Pizza Margarita")
    cliente_vip.agregar_pedido("Refresco Cola")
    cliente_regular.agregar_pedido("Hamburguesa Premium")

    print(f"\nDetalles de {cliente_vip.nombre}:")
    print(cliente_vip.obtener_detalles())

    print(f"\nDetalles de {cliente_regular.nombre}:")
    print(cliente_regular.obtener_detalles())

    # Prueba 6: Clientes miembros
    print("\n\n6️⃣ CLIENTES MIEMBROS")
    print("-" * 70)
    miembros = restaurante.obtener_clientes_miembros()
    print(f"Total de clientes miembros: {len(miembros)}")
    for cliente in miembros:
        print(f"  • {cliente}")

    # Prueba 7: Disponibilidad de productos
    print("\n\n7️⃣ CAMBIAR DISPONIBILIDAD DE PRODUCTOS")
    print("-" * 70)
    print(f"Estado anterior: {pasta.nombre} - {'Disponible' if pasta.disponible else 'No disponible'}")
    pasta.cambiar_disponibilidad(True)
    print(f"Estado posterior: {pasta.nombre} - {'Disponible' if pasta.disponible else 'No disponible'}")

    # Prueba 8: Actualizar contacto de cliente
    print("\n\n8️⃣ ACTUALIZAR CONTACTO DE CLIENTE")
    print("-" * 70)
    print(f"Contacto anterior:")
    print(f"  Email: {cliente_regular.email}")
    print(f"  Teléfono: {cliente_regular.telefono}")

    cliente_regular.actualizar_contacto("laura.new@email.com", "555-9999")

    print(f"\nContacto actualizado:")
    print(f"  Email: {cliente_regular.email}")
    print(f"  Teléfono: {cliente_regular.telefono}")

    # Prueba 9: Membresía
    print("\n\n9️⃣ GESTIÓN DE MEMBRESÍA")
    print("-" * 70)
    print(f"Estado de membresía de {cliente_regular.nombre}: {'Miembro' if cliente_regular.es_miembro else 'No miembro'}")
    cliente_regular.suscribir_a_membresia()
    print(f"Después de suscribirse: {'Miembro' if cliente_regular.es_miembro else 'No miembro'}")

    # Prueba 10: Información completa del restaurante
    print("\n\n🔟 INFORMACIÓN COMPLETA DEL RESTAURANTE")
    print("-" * 70)
    restaurante.mostrar_informacion()

    print("\n✅ TODAS LAS PRUEBAS COMPLETADAS EXITOSAMENTE")
    print("=" * 70)


if __name__ == "__main__":
    prueba_funcionalidades()

