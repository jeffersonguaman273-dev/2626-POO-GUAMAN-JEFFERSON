from typing import Dict


class Producto:
    """Representa un producto del restaurante con stock y validaciones básicas."""

    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float, stock: int = 0) -> None:
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
        try:
            stock_val = int(stock)
        except (TypeError, ValueError):
            raise ValueError("Stock inválido")
        if stock_val < 0:
            raise ValueError("Stock no puede ser negativo")

        self.codigo: str = str(codigo).strip()
        self.nombre: str = str(nombre).strip()
        self.categoria: str = str(categoria).strip()
        self.precio: float = precio_val
        self.stock: int = stock_val

    def mostrar_informacion(self) -> str:
        return (
            f"Código: {self.codigo} | Nombre: {self.nombre} | "
            f"Categoría: {self.categoria} | Precio: S/ {self.precio:.2f} | Stock: {self.stock}"
        )

    def to_dict(self) -> Dict[str, object]:
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "stock": self.stock,
        }

    def vender(self, cantidad: int) -> None:
        try:
            cantidad_val = int(cantidad)
        except (TypeError, ValueError):
            raise ValueError("Cantidad inválida para venta")
        if cantidad_val <= 0:
            raise ValueError("La cantidad a vender debe ser mayor que cero")
        if cantidad_val > self.stock:
            raise ValueError("Stock insuficiente")
        self.stock -= cantidad_val
