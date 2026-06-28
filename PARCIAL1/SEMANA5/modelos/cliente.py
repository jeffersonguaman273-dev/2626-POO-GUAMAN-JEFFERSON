# Clase Cliente: Representa un cliente registrado en el restaurante
# Atributos: id, nombre, email, teléfono, membresía y historial de pedidos


class Cliente:
    """
    Clase que representa un cliente del restaurante.

    Atributos:
        id (int): Identificador único del cliente
        nombre (str): Nombre completo del cliente
        email (str): Dirección de correo electrónico del cliente
        telefono (str): Número de teléfono del cliente
        es_miembro (bool): Indica si el cliente es miembro del programa de lealtad
        historial_pedidos (list): Lista de pedidos realizados por el cliente
    """

    def __init__(self, id: int, nombre: str, email: str, telefono: str,
                 es_miembro: bool):
        """
        Constructor que inicializa los atributos del cliente.

        Args:
            id: Identificador único del cliente
            nombre: Nombre completo y descriptivo del cliente
            email: Correo electrónico del cliente
            telefono: Número de contacto del cliente
            es_miembro: Estado de membresía del cliente
        """
        self.id: int = id
        self.nombre: str = nombre
        self.email: str = email
        self.telefono: str = telefono
        self.es_miembro: bool = es_miembro
        self.historial_pedidos: list = []  # Lista para almacenar pedidos

    def __str__(self) -> str:
        """
        Retorna una representación textual del cliente.

        Returns:
            str: Información resumida del cliente
        """
        estado_miembro = "Miembro" if self.es_miembro else "No miembro"
        total_pedidos = len(self.historial_pedidos)
        return (f"[ID: {self.id}] {self.nombre} - {self.email} "
                f"({estado_miembro}) - {total_pedidos} pedidos")

    def obtener_detalles(self) -> str:
        """
        Proporciona información detallada del cliente.

        Returns:
            str: Detalles completos del cliente
        """
        estado_miembro = "Sí" if self.es_miembro else "No"
        detalles = (f"Cliente: {self.nombre}\n"
                   f"  ID: {self.id}\n"
                   f"  Email: {self.email}\n"
                   f"  Teléfono: {self.telefono}\n"
                   f"  Miembro: {estado_miembro}\n"
                   f"  Total de pedidos: {len(self.historial_pedidos)}")

        if self.historial_pedidos:
            detalles += "\n  Historial de pedidos:"
            for i, pedido in enumerate(self.historial_pedidos, 1):
                detalles += f"\n    {i}. {pedido}"

        return detalles

    def agregar_pedido(self, nombre_producto: str) -> None:
        """
        Registra un nuevo pedido en el historial del cliente.

        Args:
            nombre_producto: Nombre del producto pedido
        """
        self.historial_pedidos.append(nombre_producto)

    def obtener_total_pedidos(self) -> int:
        """
        Retorna la cantidad total de pedidos del cliente.

        Returns:
            int: Número de pedidos realizados
        """
        return len(self.historial_pedidos)

    def suscribir_a_membresia(self) -> None:
        """
        Suscribe al cliente al programa de membresía."""
        self.es_miembro = True

    def cancelar_membresia(self) -> None:
        """
        Cancela la membresía del cliente."""
        self.es_miembro = False

    def actualizar_contacto(self, nuevo_email: str, nuevo_telefono: str) -> None:
        """
        Actualiza la información de contacto del cliente.

        Args:
            nuevo_email: Nuevo correo electrónico
            nuevo_telefono: Nuevo número de teléfono
        """
        self.email = nuevo_email
        self.telefono = nuevo_telefono

