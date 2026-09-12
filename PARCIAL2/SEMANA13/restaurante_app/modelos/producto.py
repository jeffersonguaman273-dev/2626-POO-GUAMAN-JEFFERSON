class Producto:
    def __init__(self, id: int, nombre: str, precio: float, cantidad: int):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __repr__(self):
        return f"Producto(id={self.id}, nombre='{self.nombre}', precio={self.precio}, cantidad={self.cantidad})"

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "precio": self.precio,
            "cantidad": self.cantidad,
        }