class Usuario:
    def __init__(self, username: str, password: str, nombre: str = ""):
        self.username = username
        self.password = password
        self.nombre = nombre

    def __repr__(self):
        return f"Usuario(username='{self.username}', nombre='{self.nombre}')"

    def to_dict(self):
        return {"username": self.username, "password": self.password, "nombre": self.nombre}