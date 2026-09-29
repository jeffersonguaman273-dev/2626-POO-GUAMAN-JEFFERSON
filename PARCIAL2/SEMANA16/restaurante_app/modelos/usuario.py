class Usuario:
    def __init__(self, username: str, password: str, nombre: str = "", rol: str = "Cliente", id: int = None):
        self.id = id
        self.username = username
        self.password = password
        self.nombre = nombre
        self.rol = rol if rol else "Cliente"

    def __repr__(self):
        return f"Usuario(id={self.id}, username='{self.username}', nombre='{self.nombre}', rol='{self.rol}')"

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "nombre": self.nombre,
            "rol": self.rol,
        }