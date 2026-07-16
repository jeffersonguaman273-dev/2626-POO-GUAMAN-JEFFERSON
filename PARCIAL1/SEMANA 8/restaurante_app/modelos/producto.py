class Producto:
    """Representa un producto general del restaurante.

    Atributos:
        codigo: identificador único del producto
        nombre: nombre del producto
        categoria: categoría o tipo del producto
        precio: precio unitario (float)
    """

    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float) -> None:
        self.codigo: str = codigo.strip()
        self.nombre: str = nombre.strip()
        self.categoria: str = categoria.strip()
        self.precio: float = float(precio)

    def mostrar_informacion(self) -> str:
        """Devuelve una cadena con la información del producto.

        Este método está pensado para ser sobrescrito por subclases,
        pero ofrece una implementación base útil para productos generales.
        """
        return (
            f"Código: {self.codigo} | Nombre: {self.nombre} | "
            f"Categoría: {self.categoria} | Precio: S/ {self.precio:.2f}"
        )

