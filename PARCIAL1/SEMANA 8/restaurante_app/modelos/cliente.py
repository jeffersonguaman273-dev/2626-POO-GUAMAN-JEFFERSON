class Cliente:
    """Representa un cliente registrado en el sistema."""

    def __init__(self, identificacion: str, nombre: str, correo: str) -> None:
        self.identificacion: str = identificacion.strip()
        self.nombre: str = nombre.strip()
        self.correo: str = correo.strip()

    def mostrar_informacion(self) -> str:
        return (
            f"ID cliente: {self.identificacion} | Nombre: {self.nombre} | "
            f"Correo: {self.correo}"
        )

