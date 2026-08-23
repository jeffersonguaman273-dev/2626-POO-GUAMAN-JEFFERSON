from typing import Dict


class Producto:
    """Representa un producto del restaurante con validaciones básicas.

    Atributos:
        codigo: identificador único (str, no vacío)
        nombre: nombre del producto (str, no vacío)
        categoria: categoría del producto (str, no vacío)
        precio: precio unitario (float, >= 0)
    """

    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float) -> None:
        if not codigo or not str(codigo).strip():
            raise ValueError("Código inválido")
        if not nombre or not str(nombre).strip():
            raise ValueError("Nombre inválido")
        if not categoria or not str(categoria).strip():
            raise ValueError("Categoría inválida")
        try:
            precio_val = float(precio)
        except (TypeError, ValueError):
            raise ValueError("Precio inválido")
        if precio_val < 0:
            raise ValueError("Precio no puede ser negativo")

        self.codigo: str = str(codigo).strip()
        self.nombre: str = str(nombre).strip()
        self.categoria: str = str(categoria).strip()
        self.precio: float = precio_val

    def mostrar_informacion(self) -> str:
        return (
            f"Código: {self.codigo} | Nombre: {self.nombre} | "
            f"Categoría: {self.categoria} | Precio: S/ {self.precio:.2f}"
        )

    def to_dict(self) -> Dict[str, object]:
        """Convierte el producto a un diccionario compatible con JSON."""
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
        }
