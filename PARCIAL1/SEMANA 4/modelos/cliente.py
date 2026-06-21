# Módulo: cliente.py
# Descripción: Define la clase Cliente que representa los clientes del restaurante

from datetime import datetime

class Cliente:
    """
    Clase que representa un cliente del restaurante.

    Atributos:
        id (int): Identificador único del cliente
        nombre (str): Nombre completo del cliente
        email (str): Correo electrónico del cliente
        telefono (str): Número de teléfono de contacto
        fecha_registro (datetime): Fecha del primer registro del cliente
        numero_pedidos (int): Cantidad de pedidos realizados por el cliente
    """

    def __init__(self, id, nombre, email, telefono):
        """
        Constructor de la clase Cliente.

        Args:
            id (int): Identificador único del cliente
            nombre (str): Nombre del cliente
            email (str): Correo electrónico del cliente
            telefono (str): Número de teléfono del cliente
        """
        self.id = id
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.fecha_registro = datetime.now()
        self.numero_pedidos = 0

    def __str__(self):
        """
        Retorna una representación en texto del cliente.
        Facilita la visualización de la información de forma legible.
        """
        fecha_str = self.fecha_registro.strftime("%d/%m/%Y")
        return f"[{self.id}] {self.nombre} - {self.email} - {self.telefono} (Registrado: {fecha_str})"

    def obtener_informacion(self):
        """
        Retorna información detallada del cliente.
        """
        return {
            'id': self.id,
            'nombre': self.nombre,
            'email': self.email,
            'telefono': self.telefono,
            'fecha_registro': self.fecha_registro.strftime("%d/%m/%Y %H:%M:%S"),
            'numero_pedidos': self.numero_pedidos
        }

    def actualizar_contacto(self, email=None, telefono=None):
        """
        Actualiza la información de contacto del cliente.

        Args:
            email (str): Nuevo correo electrónico (opcional)
            telefono (str): Nuevo número de teléfono (opcional)
        """
        if email:
            self.email = email
        if telefono:
            self.telefono = telefono

    def registrar_pedido(self):
        """
        Incrementa el contador de pedidos del cliente.
        Se llama cuando el cliente realiza un nuevo pedido.
        """
        self.numero_pedidos += 1

    def obtener_dias_cliente(self):
        """
        Calcula y retorna la cantidad de días desde el registro del cliente.
        """
        dias = (datetime.now() - self.fecha_registro).days
        return dias


