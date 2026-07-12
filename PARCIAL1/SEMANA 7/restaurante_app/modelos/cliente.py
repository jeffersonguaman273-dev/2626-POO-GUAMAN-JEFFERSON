"""
Módulo: cliente.py
Descripción: Define la clase Cliente utilizando el decorador @dataclass
para una definición concisa y automática de métodos especiales.
"""

from dataclasses import dataclass


@dataclass
class Cliente:
    """
    Clase que representa un cliente del restaurante.
    
    Utiliza el decorador @dataclass para generar automáticamente
    __init__, __repr__ y otros métodos especiales.
    
    Atributos:
        nombre (str): Nombre completo del cliente
        correo (str): Dirección de correo electrónico del cliente
        id_cliente (str): Identificador único del cliente
    """
    nombre: str
    correo: str
    id_cliente: str
    
    def __post_init__(self):
        """
        Validaciones adicionales después de la inicialización.
        Se ejecuta automáticamente después de __init__.
        """
        if not self.nombre or self.nombre.strip() == "":
            raise ValueError("❌ El nombre del cliente no puede estar vacío")
        if not self.correo or self.correo.strip() == "":
            raise ValueError("❌ El correo del cliente no puede estar vacío")
        if not self.id_cliente or self.id_cliente.strip() == "":
            raise ValueError("❌ El ID del cliente no puede estar vacío")
        
        # Normalizar strings
        self.nombre = self.nombre.strip()
        self.correo = self.correo.strip()
        self.id_cliente = self.id_cliente.strip()
    
    def mostrar_informacion(self):
        """Retorna una representación legible de la información del cliente."""
        return (
            f"Cliente: {self.nombre}\n"
            f"Correo: {self.correo}\n"
            f"ID: {self.id_cliente}"
        )
    
    def __str__(self):
        """String amigable para mostrar el cliente."""
        return f"{self.nombre} ({self.id_cliente}) - {self.correo}"
