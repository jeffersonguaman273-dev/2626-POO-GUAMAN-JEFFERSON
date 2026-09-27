class Venta:
    def __init__(self, id: int, username: str, producto_id: int, fecha: str):
        self.id = id
        self.username = username
        self.producto_id = producto_id
        self.fecha = fecha

    def __repr__(self):
        return f"Venta(id={self.id}, usuario='{self.username}', producto_id={self.producto_id}, fecha='{self.fecha}')"

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "producto_id": self.producto_id,
            "fecha": self.fecha,
        }