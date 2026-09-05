class Venta:
    """Representa la relación de venta entre un usuario y un producto."""

    def __init__(self, usuario_id: str, producto_codigo: str, cantidad: int) -> None:
        if not usuario_id or not str(usuario_id).strip():
            raise ValueError("ID de usuario inválido")
        if not producto_codigo or not str(producto_codigo).strip():
            raise ValueError("Código de producto inválido")
        try:
            cantidad_val = int(cantidad)
        except (TypeError, ValueError):
            raise ValueError("Cantidad inválida")
        if cantidad_val <= 0:
            raise ValueError("La cantidad debe ser mayor que cero")

        self.usuario_id: str = str(usuario_id).strip()
        self.producto_codigo: str = str(producto_codigo).strip()
        self.cantidad: int = cantidad_val

    def to_dict(self) -> dict:
        return {
            "usuario_id": self.usuario_id,
            "producto_codigo": self.producto_codigo,
            "cantidad": self.cantidad,
        }

    @classmethod
    def from_dict(cls, datos: dict) -> "Venta":
        try:
            return cls(datos["usuario_id"], datos["producto_codigo"], datos["cantidad"])
        except KeyError as e:
            raise KeyError(f"Falta la clave {e} en datos de venta")
