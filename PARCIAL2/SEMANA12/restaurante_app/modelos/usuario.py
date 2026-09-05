from typing import Dict


class Usuario:
    """Representa un usuario general del sistema (cliente, empleado, etc.)."""

    def __init__(self, identificacion: str, nombre: str, correo: str) -> None:
        if not identificacion or not str(identificacion).strip():
            raise ValueError("Identificación inválida")
        if not nombre or not str(nombre).strip():
            raise ValueError("Nombre inválido")
        if not correo or not str(correo).strip():
            raise ValueError("Correo inválido")
        self.identificacion: str = str(identificacion).strip()
        self.nombre: str = str(nombre).strip()
        self.correo: str = str(correo).strip()

    def mostrar_informacion(self) -> str:
        return (
            f"ID: {self.identificacion} | Nombre: {self.nombre} | Correo: {self.correo}"
        )

    def to_dict(self) -> Dict[str, str]:
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "correo": self.correo,
        }

    @classmethod
    def from_dict(cls, datos: Dict[str, str]) -> "Usuario":
        try:
            return cls(datos["identificacion"], datos["nombre"], datos["correo"])
        except KeyError as e:
            raise KeyError(f"Falta la clave {e} en datos de usuario")
