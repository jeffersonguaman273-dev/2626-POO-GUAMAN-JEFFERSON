"""Punto de entrada del sistema restaurante.

Presenta un menú interactivo para registrar/listar productos, bebidas y clientes.
"""
from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente


def solicitar_input(prompt: str) -> str:
    return input(prompt).strip()


def registrar_producto(servicio: Restaurante) -> None:
    print("Registrar producto")
    codigo = solicitar_input("Código: ")
    if servicio.producto_existe(codigo):
        print("Error: ya existe un producto con ese código.")
        return
    nombre = solicitar_input("Nombre: ")
    categoria = solicitar_input("Categoría: ")
    try:
        precio = float(solicitar_input("Precio: "))
    except ValueError:
        print("Precio inválido. Registro cancelado.")
        return
    producto = Producto(codigo, nombre, categoria, precio)
    if servicio.registrar_producto(producto):
        print("Producto registrado correctamente.")
    else:
        print("No se pudo registrar el producto.")


def registrar_bebida(servicio: Restaurante) -> None:
    print("Registrar bebida")
    codigo = solicitar_input("Código: ")
    if servicio.producto_existe(codigo):
        print("Error: ya existe un producto con ese código.")
        return
    nombre = solicitar_input("Nombre: ")
    categoria = solicitar_input("Categoría: ")
    try:
        precio = float(solicitar_input("Precio: "))
    except ValueError:
        print("Precio inválido. Registro cancelado.")
        return
    tamano = solicitar_input("Tamaño (p. ej. 500ml, 1L): ")
    envase = solicitar_input("Envase (p. ej. botella, lata): ")
    bebida = Bebida(codigo, nombre, categoria, precio, tamano, envase)
    if servicio.registrar_producto(bebida):
        print("Bebida registrada correctamente.")
    else:
        print("No se pudo registrar la bebida.")


def registrar_cliente(servicio: Restaurante) -> None:
    print("Registrar cliente")
    identificacion = solicitar_input("Identificación: ")
    if servicio.cliente_existe(identificacion):
        print("Error: ya existe un cliente con esa identificación.")
        return
    nombre = solicitar_input("Nombre: ")
    correo = solicitar_input("Correo: ")
    cliente = Cliente(identificacion, nombre, correo)
    if servicio.registrar_cliente(cliente):
        print("Cliente registrado correctamente.")
    else:
        print("No se pudo registrar el cliente.")


def listar_productos(servicio: Restaurante) -> None:
    print("Listado de productos:")
    productos = servicio.listar_productos()
    if not productos:
        print("(No hay productos registrados)")
        return
    for info in productos:
        print(" - ", info)


def listar_clientes(servicio: Restaurante) -> None:
    print("Listado de clientes:")
    clientes = servicio.listar_clientes()
    if not clientes:
        print("(No hay clientes registrados)")
        return
    for info in clientes:
        print(" - ", info)


def main() -> None:
    servicio = Restaurante()

    while True:
        print("\n========================================")
        print("        SISTEMA DE RESTAURANTE")
        print("========================================")
        print("1. Registrar producto")
        print("2. Registrar bebida")
        print("3. Registrar cliente")
        print("----------------------------------------")
        print("4. Listar productos")
        print("5. Listar clientes")
        print("----------------------------------------")
        print("6. Salir")

        opcion = solicitar_input("Seleccione una opción: ")
        if opcion == "1":
            registrar_producto(servicio)
        elif opcion == "2":
            registrar_bebida(servicio)
        elif opcion == "3":
            registrar_cliente(servicio)
        elif opcion == "4":
            listar_productos(servicio)
        elif opcion == "5":
            listar_clientes(servicio)
        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()

