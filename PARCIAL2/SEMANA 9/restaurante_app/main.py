from typing import Callable, Dict, Tuple

from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.usuario import Usuario


# Tupla que representa las opciones de menú estables del sistema
MENU_OPCIONES: Tuple[str, ...] = (
    "1. Registrar producto",
    "2. Buscar producto",
    "3. Actualizar producto",
    "4. Eliminar producto",
    "5. Listar productos",
    "6. Registrar usuario",
    "7. Listar usuarios",
    "8. Mostrar categorías",
    "9. Salir",
)


def solicitar_input(prompt: str) -> str:
    return input(prompt).strip()


# --- Funciones que interactúan con el servicio (no tocan colecciones internas) ---

def opcion_registrar_producto(servicio: Restaurante) -> None:
    print("\nRegistrar producto")
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


def opcion_buscar_producto(servicio: Restaurante) -> None:
    codigo = solicitar_input("Código del producto a buscar: ")
    producto = servicio.buscar_producto(codigo)
    if producto is None:
        print("Producto no encontrado.")
    else:
        print("Producto encontrado:")
        print(producto.mostrar_informacion())


def opcion_actualizar_producto(servicio: Restaurante) -> None:
    codigo = solicitar_input("Código del producto a actualizar: ")
    if not servicio.producto_existe(codigo):
        print("Producto no encontrado.")
        return
    print("Dejar un campo vacío para no modificarlo.")
    nombre = solicitar_input("Nuevo nombre: ")
    categoria = solicitar_input("Nueva categoría: ")
    precio_str = solicitar_input("Nuevo precio: ")
    precio = None
    if precio_str:
        try:
            precio = float(precio_str)
        except ValueError:
            print("Precio inválido. Actualización cancelada.")
            return
    nombre = nombre if nombre else None
    categoria = categoria if categoria else None
    if servicio.actualizar_producto(codigo, nombre=nombre, categoria=categoria, precio=precio):
        print("Producto actualizado.")
    else:
        print("No se pudo actualizar el producto.")


def opcion_eliminar_producto(servicio: Restaurante) -> None:
    codigo = solicitar_input("Código del producto a eliminar: ")
    confirmar = solicitar_input("Confirma eliminación? (s/N): ")
    if confirmar.lower() != "s":
        print("Eliminación cancelada.")
        return
    if servicio.eliminar_producto(codigo):
        print("Producto eliminado.")
    else:
        print("Producto no encontrado.")


def opcion_listar_productos(servicio: Restaurante) -> None:
    print("\nListado de productos:")
    productos = servicio.listar_productos()
    if not productos:
        print("(No hay productos registrados)")
        return
    for info in productos:
        print(" - ", info)


def opcion_registrar_usuario(servicio: Restaurante) -> None:
    print("\nRegistrar usuario")
    identificacion = solicitar_input("Identificación: ")
    if servicio.usuario_existe(identificacion):
        print("Error: ya existe un usuario con esa identificación.")
        return
    nombre = solicitar_input("Nombre: ")
    correo = solicitar_input("Correo: ")
    usuario = Usuario(identificacion, nombre, correo)
    if servicio.registrar_usuario(usuario):
        print("Usuario registrado correctamente.")
    else:
        print("No se pudo registrar el usuario.")


def opcion_listar_usuarios(servicio: Restaurante) -> None:
    print("\nListado de usuarios:")
    usuarios = servicio.listar_usuarios()
    if not usuarios:
        print("(No hay usuarios registrados)")
        return
    for info in usuarios:
        print(" - ", info)


def opcion_mostrar_categorias(servicio: Restaurante) -> None:
    categorias = servicio.obtener_categorias()
    if not categorias:
        print("(No hay categorías registradas)")
        return
    print("Categorías únicas de productos:")
    for cat in sorted(categorias):
        print(" - ", cat)


def main() -> None:
    servicio = Restaurante()

    # Diccionario que relaciona la opción (clave) con la función que la ejecuta (valor)
    acciones: Dict[str, Callable[[Restaurante], None]] = {
        "1": opcion_registrar_producto,
        "2": opcion_buscar_producto,
        "3": opcion_actualizar_producto,
        "4": opcion_eliminar_producto,
        "5": opcion_listar_productos,
        "6": opcion_registrar_usuario,
        "7": opcion_listar_usuarios,
        "8": opcion_mostrar_categorias,
    }

    while True:
        print("\n========================================")
        print("        SISTEMA DE RESTAURANTE")
        print("========================================")
        for linea in MENU_OPCIONES:
            print(linea)

        opcion = solicitar_input("Seleccione una opción: ")
        if opcion == "9":
            print("Guardando datos y saliendo...")
            servicio.guardar_datos()
            break
        accion = acciones.get(opcion)
        if accion is None:
            print("Opción inválida. Intente de nuevo.")
            continue
        try:
            accion(servicio)
        except Exception as e:
            print("Ocurrió un error al procesar la operación:", e)


if __name__ == "__main__":
    main()
